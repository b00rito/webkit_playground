#!/usr/bin/env python3
# Show everything about one WebKit IPC message or one interface.
#
#   $ ipc_find.py PixelStorei
#   $ ipc_find.py RemoteGraphicsContextGL::PixelStorei
#   $ ipc_find.py RemoteGraphicsContextGL    # the interface's messages
#   $ ipc_find.py --repo ~/WebKit --ref WebKit-7621.2.5.11.8 \
#         --build-dir out_ipc_gen PixelStorei
#
# For a message it prints
#   1. its declaration: the *.messages.in file and line
#   2. the interface's direction (DispatchedFrom/To) and flags (Stream)
#   3. the handler the generated receiver calls (needs --build-dir) and
#      where it is defined
#   4. every place in Source/WebKit that sends it, grouped by process
# Reads the source at --ref with git only; the checkout is not touched.
import argparse, os, re, subprocess, sys, collections

PROC = [
    ("Source/WebKit/UIProcess/", "UI"),
    ("Source/WebKit/WebProcess/", "WebContent"),
    ("Source/WebKit/GPUProcess/", "GPU"),
    ("Source/WebKit/NetworkProcess/", "Networking"),
    ("Source/WebKit/ModelProcess/", "Model"),
    ("Source/WebKit/webpushd/", "webpushd"),
    ("Source/WebKit/Shared/", "Shared code"),
    ("Source/WebKit/Platform/", "Platform code"),
]

# The IPC declarations without the generator tests
MSG_FILES = [
    "Source/WebKit/*.messages.in",
    ":(exclude)Source/WebKit/Scripts/webkit/tests",
]

# The C++ that defines handlers and sends messages
CODE_FILES = [
    "Source/WebKit/*.cpp",
    "Source/WebKit/*.mm",
    "Source/WebKit/*.h"
]

# A message line, with optional attributes and "void", e.g.
# [EnabledBy=X] void PixelStorei(uint32_t pname, int32_t param)
MSG_LINE = r"^\s*(\[[^]]*\]\s*)*(void\s+)?{name}\s*\("


def proc_of(path):
    return next((p for d, p in PROC if path.startswith(d)), "other")


def git(repo, *args):
    r = subprocess.run(["git", "-C", repo, *args], capture_output=True, text=True)

    return r.stdout


# Lines that contain the plain string `fixed` and match the regex `rx`:
# git grep -E is POSIX ERE, which lacks \s, \w and \b, so git finds the
# candidates and Python's re confirms them.
def grep(repo, ref, fixed, rx, *paths):
    out = git(repo, "grep", "-n", "-F", fixed, ref, "--", *paths)
    rx = re.compile(rx)
    hits = []

    for line in out.splitlines():
        parts = line.split(":", 3)          # ref:path:line:text

        if len(parts) == 4 and rx.search(parts[3]):
            hits.append((parts[1], int(parts[2]), parts[3]))

    return hits


# The interface's line, with an optional namespace, e.g.
#   messages -> RemoteGraphicsContextGL Stream {
#   messages -> WebPushD::PushClientConnection NotUsingIPCConnection {
def find_interfaces(repo, ref, name):
    rx = rf"messages\s*->\s*(\w+::)?{re.escape(name)}\b"

    return grep(repo, ref, name, rx, *MSG_FILES)


# The message's line: void PixelStorei(uint32_t pname, int32_t param)
def find_declarations(repo, ref, msg):
    rx = MSG_LINE.format(name=re.escape(msg))

    return grep(repo, ref, msg, rx, *MSG_FILES)


# Where the method is defined or declared, not called:
# void RemoteGraphicsContextGL::pixelStorei(...)   out of the class
# void pixelStorei(uint32_t pname, int32_t param)  in the class
def find_definitions(repo, ref, method):
    m = re.escape(method)
    rx = rf"::{m}\s*\(|^\s*(void|auto|bool|[A-Z]\w*[ *&<>,:\w]*)\s+{m}\s*\("
    hits = grep(repo, ref, method + "(", rx, *CODE_FILES)

    # Comments and send(...) calls can still look like definitions
    return [h for h in hits
            if not h[2].strip().startswith(("//", "send", "return send"))]


# The message's type, as senders build it:
# send(Messages::RemoteGraphicsContextGL::PixelStorei(pname, param))
def find_senders(repo, ref, receiver, msg):
    name = f"Messages::{receiver}::{msg}"

    return grep(repo, ref, name, rf"{re.escape(name)}\b", *CODE_FILES)


# "Synchronous" in the attributes; a reply follows "->"; else neither
def message_kind(line):
    if re.search(r"\bSynchronous\b", line):
        return "sync"

    return "async+reply" if "->" in line else "async"


def interface_info(repo, ref, path):
    text = git(repo, "show", f"{ref}:{path}")
    info = {
        "receiver": "?",
        "from": ["(not annotated)"],
        "to": ["(not annotated)"],
        "stream": False,
        "messages": [],
    }

    # A receiver without DispatchedFrom may say why in a comment, e.g.
    # // Currently DispatchedFrom both the UI and Network Process
    comment = re.search(r"//\s*Currently (Dispatched\w+[^\n]*)", text)

    if comment:
        info["from"] = [f"(exception: {comment.group(1)})"]

    # The interface's line; a namespace is not part of the name
    m = re.search(r"messages\s*->\s*(?:\w+::)?(\w+)([^{]*)\{", text)

    if not m:
        return info

    # Its attributes: the [...] just above that line and the words after
    # the name, e.g. [DispatchedFrom=WebContent, DispatchedTo=GPU] Stream
    head = text[:m.start()].rstrip() + "\n"
    attrs = " ".join(re.findall(r"\[([^\]]*)\]\s*$", head, re.S))
    attrs += " " + m.group(2)

    info["receiver"] = m.group(1)
    info["from"] = re.findall(r"DispatchedFrom=(\w+)", attrs) or info["from"]
    info["to"] = re.findall(r"DispatchedTo=(\w+)", attrs) or info["to"]
    info["stream"] = bool(re.search(r"\bStream\b", attrs))

    # Every message line inside the { ... }
    msg_line = re.compile(MSG_LINE.format(name=r"(?P<name>[A-Za-z_]\w*)"))

    for line in text[m.end():].splitlines():
        mm = msg_line.match(line)

        if mm and not line.strip().startswith(("#", "//")):
            info["messages"].append((mm.group("name"), message_kind(line)))

    return info


def handler_from_build(build_dir, receiver, message):
    if not build_dir:
        return None

    f = os.path.join(build_dir, "DerivedSources", "WebKit", f"{receiver}MessageReceiver.cpp")

    if not os.path.exists(f):
        return None

    # The binding: handleMessage<Messages::X::Msg>(..., &X::msg)
    pat = re.compile(rf"Messages::{receiver}::{message}>\([^;]*?&(\w+)::(\w+)\)")

    for line in open(f, errors="replace"):
        m = pat.search(line)

        if m:
            return f"{m.group(1)}::{m.group(2)}", f

    return None


def main():
    ap = argparse.ArgumentParser(
        description="Everything about one WebKit IPC message, or one interface.")
    ap.add_argument("query", help="Message, Receiver::Message, or Receiver")
    ap.add_argument("--repo", default=".", help="WebKit checkout (default: current directory)")
    ap.add_argument("--ref", default="HEAD", help="git ref to read (default: HEAD)")
    ap.add_argument("--build-dir", help="products dir with DerivedSources, e.g. WebKitBuild/Debug (optional)")
    a = ap.parse_args()
    receiver_q, _, msg = a.query.rpartition("::")
    receiver_q = receiver_q or None

    # Whole-interface query when the name matches a receiver
    if receiver_q is None:
        iface = find_interfaces(a.repo, a.ref, msg)

        for path, _, _ in iface:
            info = interface_info(a.repo, a.ref, path)
            stream = "  [stream]" if info["stream"] else ""
            print(f"interface {info['receiver']}  ({path})")
            print(f"    direction: {', '.join(info['from'])} -> {', '.join(info['to'])}{stream}")
            count = len(info["messages"])
            print(f"    {count} message{'' if count == 1 else 's'}:")

            for n, kind in info["messages"]:
                print(f"        {n}  ({kind})")

        if iface:
            return

    decl = find_declarations(a.repo, a.ref, msg)

    if receiver_q:
        decl = [h for h in decl if interface_info(a.repo, a.ref, h[0])["receiver"] == receiver_q]

    if not decl:
        sys.exit(f"[-] No IPC message named {a.query!r} at {a.ref}")

    for path, line, text in decl:
        info = interface_info(a.repo, a.ref, path)
        rec = info["receiver"]
        stream = "   [stream interface]" if info["stream"] else ""
        print(f"== {rec}::{msg}")
        print(f"declared:   {path}:{line}\n            {text.strip()}")
        print(f"direction:  {', '.join(info['from'])} -> {', '.join(info['to'])}{stream}")

        h = handler_from_build(a.build_dir, rec, msg)
        method = h[0].split("::")[1] if h else msg[0].lower() + msg[1:]

        if h:
            print(f"handler:    {h[0]}   (bound in {os.path.relpath(h[1])})")
        else:
            print(f"handler:    probably {rec}::{method}   (guessed from the naming convention; pass --build-dir to confirm)")

        # Prefer definitions in the receiver's own files
        defs = find_definitions(a.repo, a.ref, method)
        rec_files = [d for d in defs
                     if rec.replace("Proxy", "") in os.path.basename(d[0])
                     or rec in os.path.basename(d[0])]

        for d in (rec_files or defs)[:6]:
            print(f"            {d[0]}:{d[1]}: {d[2].strip()[:110]}")

        by = collections.defaultdict(list)

        for p, l, t in find_senders(a.repo, a.ref, rec, msg):
            by[proc_of(p)].append((p, l, t.strip()))

        print(f"sent from:  {sum(len(v) for v in by.values())} site(s)")

        for proc in sorted(by):
            print(f"    [{proc}]")

            for p, l, t in by[proc][:8]:
                print(f"        {p}:{l}: {t[:100]}")

        print()


if __name__ == "__main__":
    main()

# EOF
