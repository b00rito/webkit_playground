#!/usr/bin/env python3
# Map the whole WebKit IPC of any ref without a build.
#
#   $ ipc_map.py <webkit-checkout> <ref> <outdir>
#   $ ipc_map.py ~/WebKit WebKit-7621.2.5.11.8 out_ipc_map
#     (all three are optional; the defaults are ., HEAD and out_ipc_map)
#
# Runs extract_ipc.py and build_ipc_tables.py, which must sit next to it,
# on every *.messages.in at <ref> and on every place that sends a message.
# Writes to <outdir>:
#   ipc_summary.md                 interfaces and messages per direction
#   ipc_full_table.md              every interface, grouped by direction
#   ipc_all_messages_<ref>.md      every message of every interface
#   ipc_all_signatures_<ref>.md    every message with arguments and reply
#   ipc_map.json                   the same, machine-readable
#   ipc_raw.json, send_sites.txt   the intermediate results
#
# The checkout is not touched, since <ref> is read with git. An
# interface's direction comes from its DispatchedFrom and DispatchedTo
# annotations, else from the same interface on origin/main, else from the
# processes that send it or the directory of its file.
import argparse
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent

# Every use of a message type in the C++, e.g.
#   send(Messages::RemoteGraphicsContextGL::PixelStorei(pname, param))
SEND_SITE = r"Messages::[A-Za-z0-9_]+::[A-Za-z0-9_]+"
CODE_FILES = [
    "Source/WebKit/*.cpp",
    "Source/WebKit/*.mm",
    "Source/WebKit/*.h",
]


def git(repo, *args, ok=(0,)):
    r = subprocess.run(["git", "-C", str(repo), *args], capture_output=True, text=True)

    if r.returncode not in ok:
        sys.exit(f"[-] git {args[0]} failed: {r.stderr.strip()}")

    return r.stdout


# The ref that lends directions to unannotated interfaces: origin/main or
# the ref itself when the checkout has no origin/main
def annotation_fallback(repo, ref):
    found = git(repo, "rev-parse", "--verify", "-q", "origin/main", ok=(0, 1))

    return "origin/main" if found else ref


# One line per send site, as git grep -o prints it: ref:path:symbol.
# Exit status 1 means no match, which is not an error.
def collect_send_sites(repo, ref, out):
    sites = git(repo, "grep", "-o", "-E", SEND_SITE, ref, "--", *CODE_FILES, ok=(0, 1))
    out.write_text(sites)

    return sites.count("\n")


# Run one of the helper scripts next to this one
def run_step(script, *args):
    subprocess.run([sys.executable, "-I", str(HERE / script), *map(str, args)], check=True)


def main():
    parser = argparse.ArgumentParser(
        description="Map every WebKit IPC interface and message at a ref.")
    parser.add_argument("repo", nargs="?", type=Path, default=Path("."),
                        help="WebKit git checkout (default: .)")
    parser.add_argument("ref", nargs="?", default="HEAD",
                        help="tag, branch or commit to map (default: HEAD)")
    parser.add_argument("outdir", nargs="?", type=Path, default=Path("out_ipc_map"),
                        help="output dir (default: out_ipc_map)")
    args = parser.parse_args()

    # The steps print too; keep our lines and theirs in order
    sys.stdout.reconfigure(line_buffering=True)
    fallback = annotation_fallback(args.repo, args.ref)
    raw = args.outdir / "ipc_raw.json"
    sites = args.outdir / "send_sites.txt"
    args.outdir.mkdir(parents=True, exist_ok=True)

    print(f"[*] Mapping WebKit IPC at {args.ref}")
    print("\t[*] Collecting send sites")

    count = collect_send_sites(args.repo, args.ref, sites)

    print(f"\t\t[+] {count} send sites")

    commit = git(args.repo, "rev-parse", "--short=12", fallback).strip()

    print(f"\t[*] Parsing *.messages.in (annotation fallback: {fallback} at {commit})")

    run_step("extract_ipc.py", args.repo, args.ref, fallback, raw)

    print("\t[*] Building the tables")

    run_step("build_ipc_tables.py", args.repo, args.ref, raw, sites, args.outdir)

    print(f"[+] Done: {args.outdir}/ipc_summary.md, ipc_full_table.md, "
          "ipc_all_messages_*.md, ipc_all_signatures_*.md, ipc_map.json")


if __name__ == "__main__":
    main()

# EOF
