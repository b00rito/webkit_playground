#!/usr/bin/env python3
# Extract every WebKit IPC interface and message of a ref as JSON.
#
#   $ extract_ipc.py <webkit-checkout> <ref> <fallback-ref> <out.json>
#   $ extract_ipc.py ~/WebKit WebKit-7621.2.5.11.8 origin/main \
#         out_ipc_map/ipc_raw.json
#     (ipc_map.py runs it, rarely run standalone)
#
# Parses every *.messages.in at <ref>, with WebKit's own parser for the
# message signatures. For each interface it records the attributes and
# the direction and for each message its kind, arguments, reply and #if
# condition. An interface without DispatchedFrom and DispatchedTo borrows
# them from the same interface at <fallback-ref> or else gets its
# destination from the directory of its file.
#
# The checkout is not touched, since both refs are read with git. The
# generator's test fixtures are kept here and dropped by
# build_ipc_tables.py.
import argparse
import collections
import importlib
import io
import json
import os
import re
import subprocess
import sys
import tempfile

# The destination process of an interface, from its file's directory
DIRMAP = [
    ("Source/WebKit/GPUProcess/", "GPU"),
    ("Source/WebKit/NetworkProcess/", "Networking"),
    ("Source/WebKit/ModelProcess/", "Model"),
    ("Source/WebKit/UIProcess/", "UI"),
    ("Source/WebKit/WebProcess/", "WebContent"),
    ("Source/WebKit/webpushd/", "webpushd"),
]

# Interface attributes worth keeping
FLAGS = [
    "Stream",
    "LegacyReceiver",
    "WantsDispatchMessage",
    "WantsAsyncDispatchMessage",
    "NotRefCounted",
]

# The interface's line, with an optional namespace that is not part of
# the name, e.g.
#   messages -> RemoteGraphicsContextGL Stream {
#   messages -> WebPushD::PushClientConnection NotUsingIPCConnection {
HEADER = re.compile(r"messages\s*->\s*(?:\w+::)?(\w+)([^{]*)\{")

# A message line, with optional attributes and "void", e.g.
# [EnabledBy=X] void PixelStorei(uint32_t pname, int32_t param)
MSG_LINE = re.compile(r"(?:\[[^\]]*\]\s*)*(?:void\s+)?([A-Za-z_]\w*)\s*\(")


def git(repo, *args):
    r = subprocess.run(["git", "-C", repo, *args], capture_output=True, text=True)

    return r.stdout


def messages_in_files(repo, ref):
    tree = git(repo, "ls-tree", "-r", "--name-only", ref, "--", "Source/WebKit")

    return [f for f in tree.split("\n") if f.endswith(".messages.in")]


# WebKit's own *.messages.in parser at that ref, as the build uses it
def load_webkit_parser(repo, ref):
    tmp = tempfile.mkdtemp(prefix="extract_ipc.")
    os.mkdir(f"{tmp}/webkit")

    for f in ("__init__.py", "parser.py", "model.py"):
        with open(f"{tmp}/webkit/{f}", "w") as out:
            out.write(git(repo, "show", f"{ref}:Source/WebKit/Scripts/webkit/{f}"))

    sys.path.insert(0, tmp)

    return importlib.import_module("webkit.parser")


# None: the message has no reply; []: an empty reply, "-> ()"
def params(ps):
    if ps is None:
        return None

    return [{"type": p.type, "name": p.name} for p in ps]


# Arguments, reply, attributes and #if condition of every message
def signatures(parser, text):
    try:
        receiver = parser.parse(io.StringIO(text))
    except Exception as e:
        print(f"\t\t[-] WebKit's parser failed: {e}")
        return None

    return [{
        "name": m.name,
        "parameters": params(m.parameters),
        "reply": params(m.reply_parameters),
        "attributes": sorted(m.attributes or []),
        "condition": m.condition,
    } for m in receiver.messages]


# "Synchronous" in the attributes; a reply follows "->"; else neither
def message_kind(line):
    if re.search(r"\bSynchronous\b", line):
        return "sync"

    return "async-reply" if "->" in line else "async"


# The interface's attributes: the [...] blocks right before
# "messages ->" plus the words after the interface name
def interface_attributes(text, header):
    before = text[:header.start()].rstrip() + "\n"
    attrs = " ".join(re.findall(r"\[([^\]]*)\]\s*$", before, re.S))
    attrs += " " + header.group(2)

    return re.sub(r"\s+", " ", attrs)


def parse(text, parser=None):
    header = HEADER.search(text)

    if not header:
        return None

    attrs = interface_attributes(text, header)
    msgs = []

    for line in text[header.end():].split("\n"):
        s = line.strip()
        m = MSG_LINE.match(s)

        if m and not s.startswith("#"):
            msgs.append({"name": m.group(1), "kind": message_kind(s)})

    # Add the signatures only when both parsers see the same messages
    sigs = signatures(parser, text) if parser else None

    if sigs is not None and [x["name"] for x in sigs] == [x["name"] for x in msgs]:
        for x, sig in zip(msgs, sigs):
            x.update(sig)
    elif parser:
        print(f"\t\t[-] {header.group(1)}: messages without arguments, the parsers disagree")

    return {
        "receiver": header.group(1),
        "from": re.findall(r"DispatchedFrom=(\w+)", attrs),
        "to": re.findall(r"DispatchedTo=(\w+)", attrs),
        "flags": [w for w in FLAGS if re.search(rf"\b{w}\b", attrs)],
        "messages": msgs,
    }


# Every interface at ref, keyed by file.
# Some names exist once per port (cocoa/, glib/)
def collect(repo, ref, parser=None):
    interfaces = {}

    for f in messages_in_files(repo, ref):
        p = parse(git(repo, "show", f"{ref}:{f}"), parser)

        if p:
            p["file"] = f
            interfaces[f] = p

    return interfaces


# Annotated at ref; else annotated at the fallback; else the destination
# from the file's directory
def resolve_direction(r, fallback):
    other = fallback.get(r["receiver"])

    if r["from"] and r["to"]:
        r["direction_source"] = "annotated"
    elif other and other["from"]:
        r["from"] = r["from"] or other["from"]
        r["to"] = r["to"] or other["to"]
        r["direction_source"] = "annotated-on-main"
    else:
        r["to"] = r["to"] or [p for d, p in DIRMAP if r["file"].startswith(d)][:1]
        r["direction_source"] = "inferred-from-directory"


def main():
    ap = argparse.ArgumentParser(
        description="Every WebKit IPC interface and message of a ref, as JSON.")
    ap.add_argument("repo", help="WebKit git checkout")
    ap.add_argument("ref", help="tag, branch or commit to read")
    ap.add_argument("fallback", help="ref that lends directions, e.g. origin/main")
    ap.add_argument("out", help="output JSON file")
    a = ap.parse_args()

    # Signatures only for the ref; the fallback only lends directions
    fallback = {r["receiver"]: r for r in collect(a.repo, a.fallback).values()}
    current = collect(a.repo, a.ref, load_webkit_parser(a.repo, a.ref))

    for r in current.values():
        resolve_direction(r, fallback)

    with open(a.out, "w", encoding="ascii") as out:
        json.dump(sorted(current.values(), key=lambda r: r["receiver"]), out, indent=4)

    # Sub-steps of the caller's "Parsing" step: two tabs deep
    total = sum(len(r["messages"]) for r in current.values())
    print(f"\t\t[+] Parsed {len(current)} files, {total} messages "
          "(the generator's test fixtures included)")

    how = collections.Counter(r["direction_source"] for r in current.values())
    print("\t\t[*] Directions: " + ", ".join(f"{n} {k}" for k, n in how.most_common()))


if __name__ == "__main__":
    main()

# EOF
