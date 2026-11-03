#!/usr/bin/env python3
# ipc_generate.py: WebKit's generated IPC code for any ref, no build.
#
#   $ ipc_generate.py <webkit-checkout> <ref> <outdir> [--verbose]
#   $ ipc_generate.py ~/WebKit WebKit-7621.2.5.11.8 out_ipc_gen
#     (--verbose also logs every file the generator writes)
#
# Runs WebKit's own generator, generate-message-receiver.py, on every
# interface listed in Source/WebKit/DerivedSources.make, as the build does.
# Writes to <outdir>/DerivedSources/WebKit/, the layout of a build dir:
#   <Interface>Messages.h            one C++ type per message, for senders
#   <Interface>MessageReceiver.cpp   dispatch: decodes, calls the handler
#   MessageNames.h                   enums numbering interfaces, messages
#   MessageNames.cpp                 each message's name and dispatch flags
#   MessageArgumentDescriptions.cpp  argument names and types, per message
#
# The checkout is not touched: <ref> is read with git into a temp dir.
# Interfaces whose .messages.in is generated at build time (LogStream on
# newer trees) are skipped with a warning. The *.serialization.in code is
# not generated: its generator needs WebCore's build-time headers.
import argparse
import io
import re
import subprocess
import sys
import tarfile
import tempfile
from pathlib import Path

def git(repo, *args):
    return subprocess.run(["git", "-C", str(repo), *args], check=True, capture_output=True).stdout

# Copy what the generator needs at <ref> into dest: its scripts, the
# makefile that lists the interfaces, and every *.messages.in.
def export_sources(repo, ref, dest):
    tree = git(repo, "ls-tree", "-r", "--name-only", ref, "--", "Source/WebKit").decode().splitlines()
    wanted = [path for path in tree
              if path.endswith(".messages.in")
              or path.startswith("Source/WebKit/Scripts/")
              or path == "Source/WebKit/DerivedSources.make"]
    archive = git(repo, "archive", "--format=tar", ref, "--", *wanted)

    with tarfile.open(fileobj=io.BytesIO(archive)) as tar:
        tar.extractall(dest, filter="data")

# MESSAGE_RECEIVERS from DerivedSources.make, relative to Source/WebKit.
# Some are bare names (e.g. LogStream) that make finds through VPATH; we
# resolve each one to its single matching *.messages.in file.
def message_receivers(source):
    makefile = (source / "DerivedSources.make").read_text().replace("\\\n", " ")
    listed = re.search(r"^MESSAGE_RECEIVERS\s*=\s*(.*)$", makefile, re.MULTILINE).group(1).split()
    names = [name for name in listed if not name.startswith(("$", "#"))]
    by_basename = {}

    for path in source.rglob("*.messages.in"):
        # skip the generator's own test fixtures
        if "Scripts/webkit/tests" not in path.as_posix():
            relative = path.relative_to(source).as_posix().removesuffix(".messages.in")
            by_basename.setdefault(path.name.removesuffix(".messages.in"), []).append(relative)

    receivers, skipped = [], []

    for name in names:
        candidates = by_basename.get(Path(name).name, [])
        if (source / f"{name}.messages.in").exists():
            receivers.append(name)
        elif len(candidates) == 1:
            receivers.append(candidates[0])
        else:
            skipped.append(name)

    return receivers, skipped

def log_written_files(out, before):
    for path in sorted(out.iterdir()):
        if before.get(path.name) != path.stat().st_mtime_ns:
            print(f"\t\t[+] Wrote {path.name}")

def main():
    parser = argparse.ArgumentParser(
        description="Generate WebKit's IPC message code for a ref, without a build.")
    parser.add_argument("repo", type=Path, help="WebKit git checkout")
    parser.add_argument("ref", help="tag, branch or commit to generate for")
    parser.add_argument("outdir", type=Path, help="output; the files go to <outdir>/DerivedSources/WebKit/")
    parser.add_argument("--verbose", action="store_true", help="also log every file the generator writes")
    args = parser.parse_args()
    # keep log order with stderr
    sys.stdout.reconfigure(line_buffering=True)

    try:
        git(args.repo, "rev-parse", "--verify", "--quiet", f"{args.ref}^{{commit}}")
    except subprocess.CalledProcessError:
        sys.exit(f"[-] {args.ref} is not a commit in {args.repo}")

    out = args.outdir / "DerivedSources" / "WebKit"
    out.mkdir(parents=True, exist_ok=True)

    print(f"[*] Generating WebKit's IPC code for {args.ref}")

    with tempfile.TemporaryDirectory(prefix="ipc_generate.") as tmp:
        print(f"\t[*] Reading the sources at {args.ref} with git")
        export_sources(args.repo, args.ref, tmp)
        source = Path(tmp) / "Source" / "WebKit"
        receivers, skipped = message_receivers(source)
        print(f"\t[+] {len(receivers)} interfaces listed in DerivedSources.make")

        for name in skipped:
            print(f"\t[-] Skipping {name}: its .messages.in is generated at build time on this ref", file=sys.stderr)

        print("\t[*] Running generate-message-receiver.py")
        generator = source / "Scripts" / "generate-message-receiver.py"
        before = {p.name: p.stat().st_mtime_ns for p in out.iterdir()}
        subprocess.run([sys.executable, str(generator), str(source), *receivers], cwd=out, check=True)

        if args.verbose:
            log_written_files(out, before)

    print(f"[+] Generated the code of {len(receivers)} interfaces in {out}")

if __name__ == "__main__":
    main()

# EOF
