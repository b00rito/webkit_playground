#!/usr/bin/env python3
# Build the final WebKit IPC map, as JSON and markdown.
#
#   $ build_ipc_tables.py <webkit-checkout> <ref> <ipc_raw.json> \
#         <send_sites.txt> <outdir>
#   $ build_ipc_tables.py ~/WebKit WebKit-7621.2.5.11.8 \
#         out_ipc_map/ipc_raw.json out_ipc_map/send_sites.txt out_ipc_map
#     (ipc_map.py runs it, rarely run standalone)
#
# Merges the interfaces found by extract_ipc.py with the places that send
# their messages, the exception comments in the files and a few manual
# resolutions, and drops the generator's test fixtures. Writes to
# <outdir>:
#   ipc_map.json                   every interface, machine-readable
#   ipc_summary.md                 interfaces and messages per direction
#   ipc_full_table.md              every interface, grouped by direction
#   ipc_all_messages_<ref>.md      every message of every interface
#   ipc_all_signatures_<ref>.md    every message with arguments and reply
#
# The checkout is not touched, since <ref> is read with git.
import argparse
import collections
import json
import re
import subprocess

# The process that owns a file, from its directory
PROC = [
    ("Source/WebKit/UIProcess/", "UI"),
    ("Source/WebKit/WebProcess/", "WebContent"),
    ("Source/WebKit/GPUProcess/", "GPU"),
    ("Source/WebKit/NetworkProcess/", "Networking"),
    ("Source/WebKit/ModelProcess/", "Model"),
    ("Source/WebKit/webpushd/", "webpushd"),
]

# Processes an exception comment can name, e.g.
# // Currently DispatchedFrom both the UI and Network Process
COMMENT_PROCS = [
    "UI",
    "WebContent",
    "GPU",
    "Networking",
    "Model",
]
EXCEPTION_COMMENT = re.compile(r"//\s*Currently DispatchedFrom ([^\n]+)")

# Files of the non-Apple ports, and the IPC testing interfaces
NON_APPLE = re.compile(r"/(glib|gtk|wpe|soup|dmabuf|wc|win|playstation|libwpe|gstreamer)/")
TEST_ONLY = [
    "IPCTester",
    "IPCTesterReceiver",
    "IPCConnectionTester",
    "IPCStreamTester",
    "IPCStreamTesterProxy",
]

# The code generator's own test inputs, not real IPC
FIXTURES = "Source/WebKit/Scripts/webkit/tests/"

# Manual resolutions for interfaces in shared code, checked against the
# send sites and object creation in this tree: (from, to, why)
OVERRIDES = {
    "AuxiliaryProcess": (
        ["UI"], ["WebContent", "GPU", "Networking", "Model"],
        "manual: received by every auxiliary process; sent only from UIProcess/"),
    "NotificationManagerMessageHandler": (
        ["WebContent"], ["UI", "Networking"],
        "manual: sent from WebProcess/; handled in UI and Networking (ExceptionForDispatchedTo on main)"),
    "RemoteObjectRegistry": (
        ["UI", "WebContent"], ["WebContent", "UI"],
        "manual: bidirectional UI <-> WebContent (injected-bundle remote objects)"),
    "WebPaymentCoordinatorProxy": (
        ["WebContent"], ["UI"],
        "manual: DispatchedFrom=WebContent; To=UI, or Networking when APPLE_PAY_REMOTE_UI (comment on main)"),
    "LogStream": (
        ["WebContent"], ["UI"],
        "manual: created in UIProcess/Cocoa/WebProcessProxyCocoa.mm; WebContent logs through it when logd is blocked"),
}

for name in TEST_ONLY:
    OVERRIDES[name] = (["test harness"], ["any process"], "manual: IPC testing API only")

# The order of the directions in every table
ORDER = [
    "WebContent",
    "UI",
    "GPU",
    "Networking",
    "Model",
    "webpushd",
    "test harness",
    "any process",
    "?",
]


def proc_of(path):
    return next((p for d, p in PROC if path.startswith(d)), None)


def git_show(repo, ref, path):
    r = subprocess.run(["git", "-C", repo, "show", f"{ref}:{path}"], capture_output=True, text=True)

    return r.stdout


def write(path, text):
    with open(path, "w", encoding="ascii") as out:
        out.write(text)


# How often each process sends to each interface, from lines like
#   <ref>:Source/WebKit/<path>:Messages::LogStream::LogOnBehalfOfWebContent
def read_senders(path):
    senders = collections.defaultdict(collections.Counter)

    for line in open(path):
        _, file, symbol = line.rstrip("\n").split(":", 2)
        proc = proc_of(file)

        if proc:
            senders[symbol.split("::")[1]][proc] += 1

    return senders


# One interface's row: its direction, from the annotations, an exception
# comment or the observed senders, plus its tags and message counts
def make_row(repo, ref, r, senders):
    comment = EXCEPTION_COMMENT.search(git_show(repo, ref, r["file"]))
    dest = r["to"][0] if r["to"] else None
    observed = {p: n for p, n in senders.get(r["receiver"], {}).items() if p != dest}
    src, how = r["from"], r["direction_source"]

    if comment:
        named = [p for p in COMMENT_PROCS if p.lower() in comment.group(1).lower()]
        src = named or src
        how = "annotated (exception comment)"

    if not src and observed:
        src = sorted(observed, key=lambda p: -observed[p])
        how = "observed send sites"

    if not dest:
        dest = proc_of(r["file"]) or "?"
        how += " + destination from directory"

    tags = []

    if NON_APPLE.search(r["file"]):
        tags.append("non-Apple ports")

    if r["receiver"] in TEST_ONLY:
        tags.append("testing only")

    if "Stream" in r["flags"]:
        tags.append("stream")

    return {
        "receiver": r["receiver"],
        "from": src or ["?"],
        "to": [dest],
        "file": r["file"].replace("Source/WebKit/", ""),
        "n": len(r["messages"]),
        "sync": sum(1 for m in r["messages"] if m["kind"] == "sync"),
        "tags": tags,
        "how": how,
        "observed": observed,
        "messages": r["messages"],
    }


def apply_overrides(rows):
    for x in rows:
        if x["receiver"] in OVERRIDES:
            x["from"], x["to"], x["how"] = OVERRIDES[x["receiver"]]


def order_key(src, dest):
    def rank(p):
        return ORDER.index(p) if p in ORDER else 9

    return rank(src), rank(dest)


# Every (source, destination) pair with its interfaces, in table order
def direction_pairs(rows):
    pairs = collections.defaultdict(list)

    for x in rows:
        for src in x["from"]:
            for dest in x["to"]:
                if src != dest:
                    pairs[(src, dest)].append(x)

    return {k: pairs[k] for k in sorted(pairs, key=lambda k: order_key(*k))}


def in_appendix_order(rows):
    return sorted(rows, key=lambda x: (order_key(x["from"][0], x["to"][0]), x["receiver"]))


def summary_table(pairs):
    lines = ["| Source -> Destination | Interfaces | Messages |\n|---|---|---|"]

    for (src, dest), xs in pairs.items():
        lines.append(f"| {src} -> {dest} | {len(xs)} | {sum(x['n'] for x in xs)} |")

    return "\n".join(lines) + "\n"


# The Notes column: tags, how the direction was found when it isn't a plain
# annotation, and the other ends of multi-process interfaces
def notes(x, src, dest):
    plain = x["how"].startswith("annotated") and "directory" not in x["how"]
    parts = x["tags"] + ([] if plain else [x["how"]])

    if len(x["from"]) > 1:
        parts.append("also from " + ", ".join(s for s in x["from"] if s != src))

    if len(x["to"]) > 1:
        parts.append("also to " + ", ".join(d for d in x["to"] if d != dest))

    return ", ".join(parts)


def full_table(pairs):
    lines = []

    for (src, dest), xs in pairs.items():
        total = sum(x["n"] for x in xs)
        lines.append(f"<details>\n<summary><b>{src} -> {dest}</b>: {len(xs)} interfaces, {total} messages</summary>\n")
        lines.append("| Source | IPC interface (receiver) | Destination | Messages (sync) | Notes | Defined in |\n"
                     "|---|---|---|---|---|---|")

        for x in sorted(xs, key=lambda x: x["receiver"]):
            lines.append(f"| {src} | `{x['receiver']}` | {dest} | {x['n']} ({x['sync']}) "
                         f"| {notes(x, src, dest)} | `{x['file']}` |")

        lines.append("\n</details>\n")

    return "\n".join(lines) + "\n"


def heading(x):
    return f"## `{x['receiver']}` - {', '.join(x['from'])} -> {', '.join(x['to'])}\n\n`{x['file']}`"


def all_messages(rows, ref):
    lines = [
        f"# WebKit IPC messages - {ref}\n",
        "Generated from every `*.messages.in` in `Source/WebKit` (code-generator test fixtures "
        "excluded). Messages marked (sync) are synchronous: the sender blocks until the reply "
        "arrives.\n",
    ]

    for x in in_appendix_order(rows):
        tags = f" - {', '.join(x['tags'])}" if x["tags"] else ""
        lines.append(f"{heading(x)}{tags} - direction: {x['how']}\n")
        lines.append(", ".join(f"`{m['name']}`" + (" (sync)" if m["kind"] == "sync" else "")
                               for m in x["messages"]) + "\n")

    return "\n".join(lines)


def param_list(ps):
    return ", ".join(f"{p['type']} {p['name']}" for p in ps)


# One message as a list item, e.g.
#   - `Name(type a, type b) -> (type r)` (sync, if ENABLE(X))
def signature(m):
    if "parameters" not in m:
        return f"- `{m['name']}(?)`"

    s = f"{m['name']}({param_list(m['parameters'])})"

    if m["reply"] is not None:
        s += f" -> ({param_list(m['reply'])})"

    extra = [a for a in m["attributes"] if a != "Synchronous"]
    extra += ["sync"] if m["kind"] == "sync" else []
    extra += [f"if {m['condition']}"] if m["condition"] else []

    return f"- `{s}`" + (f" ({', '.join(extra)})" if extra else "")


def all_signatures(rows, ref):
    lines = [
        f"# WebKit IPC message signatures - {ref}\n",
        "Every message of every interface with its arguments and, after `->`, its reply. "
        "Generated from every `*.messages.in` in `Source/WebKit` with WebKit's own parser "
        "(code-generator test fixtures excluded).\n",
    ]

    for x in in_appendix_order(rows):
        lines.append(f"{heading(x)}\n")
        lines.append("\n".join(signature(m) for m in x["messages"]) + "\n")

    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser(
        description="The final WebKit IPC map, as JSON and markdown.")
    ap.add_argument("repo", help="WebKit git checkout")
    ap.add_argument("ref", help="tag, branch or commit the map is for")
    ap.add_argument("raw", help="ipc_raw.json, from extract_ipc.py")
    ap.add_argument("sites", help="send_sites.txt, from git grep")
    ap.add_argument("outdir", help="output directory")
    a = ap.parse_args()

    senders = read_senders(a.sites)
    rows = [make_row(a.repo, a.ref, r, senders)
            for r in json.load(open(a.raw))
            if not r["file"].startswith(FIXTURES)]
    apply_overrides(rows)
    pairs = direction_pairs(rows)
    name = a.ref.replace("/", "_")

    with open(f"{a.outdir}/ipc_map.json", "w", encoding="ascii") as out:
        json.dump(rows, out, indent=4)

    write(f"{a.outdir}/ipc_summary.md", summary_table(pairs))
    write(f"{a.outdir}/ipc_full_table.md", full_table(pairs))
    write(f"{a.outdir}/ipc_all_messages_{name}.md", all_messages(rows, a.ref))
    write(f"{a.outdir}/ipc_all_signatures_{name}.md", all_signatures(rows, a.ref))

    # Sub-steps of the caller's "Building" step: two tabs deep
    total = sum(x["n"] for x in rows)
    sync = sum(x["sync"] for x in rows)
    print(f"\t\t[+] {len(rows)} interfaces, {total} messages, {sync} synchronous")

    unresolved = [x["receiver"] for x in rows if x["from"] == ["?"]]

    if unresolved:
        print(f"\t\t[-] No sending process found for: {', '.join(unresolved)}")


if __name__ == "__main__":
    main()

# EOF
