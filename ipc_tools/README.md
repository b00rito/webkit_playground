# ipc_tools

Tools to follow WebKit's IPC messages in the source code. They work on a
WebKit checkout, read it with git only and need Python 3.

- `ipc_generate.py` produces the generated IPC code without a WebKit build
- `ipc_find.py` follows one message or lists one interface
- `ipc_map.py` maps every interface and message of a WebKit version

## ipc_generate.py

`ipc_generate.py` produces WebKit's generated IPC code for any tag or
commit, without building WebKit. It runs WebKit's own generator,
`generate-message-receiver.py`, on every interface as the build would do
and writes the files a build would write:

- `<Interface>Messages.h`: one C++ type per message, used by senders
- `<Interface>MessageReceiver.cpp`: dispatch code that decodes a message
  and calls its handler
- `MessageNames.h`, `MessageNames.cpp`, `MessageArgumentDescriptions.cpp`:
  shared by all interfaces

```sh
$ ipc_tools/ipc_generate.py ~/WebKit WebKit-7621.2.5.11.8 out_ipc_gen
# -> out_ipc_gen/DerivedSources/WebKit/
```

It needs Python 3 and a WebKit checkout. The output has the layout of a
build directory, `DerivedSources/WebKit/`. The `*.serialization.in`
serializers are not generated currently. Their generator needs WebCore's
build-time headers.

## ipc_find.py

`ipc_find.py` follows one IPC message from its declaration to its handler
and to every place that sends it. Given an interface name instead, it lists
the interface's messages. For a message it prints:

- its declaration: the `*.messages.in` file and line
- the interface's direction (`DispatchedFrom`, `DispatchedTo`) and whether
  it is a stream interface
- the handler that the generated receiver calls and where it is defined
- every place in `Source/WebKit` that sends it, grouped by process

```sh
$ ipc_tools/ipc_find.py --repo ~/WebKit --ref WebKit-7621.2.5.11.8 --build-dir out_ipc_gen CookiesForDOM
== NetworkConnectionToWebProcess::CookiesForDOM
declared:   Source/WebKit/NetworkProcess/NetworkConnectionToWebProcess.messages.in:45
            CookiesForDOM(URL firstParty, struct WebCore::SameSiteInfo sameSiteInfo, ...)
direction:  WebContent -> Networking
handler:    NetworkConnectionToWebProcess::cookiesForDOM   (bound in out_ipc_gen/...)
            Source/WebKit/NetworkProcess/NetworkConnectionToWebProcess.cpp:787: ...
            Source/WebKit/NetworkProcess/NetworkConnectionToWebProcess.h:305: ...
sent from:  1 site(s)
    [WebContent]
        Source/WebKit/WebProcess/WebPage/WebCookieJar.cpp:164: ...

$ ipc_tools/ipc_find.py --repo ~/WebKit --ref WebKit-7621.2.5.11.8 LogStream
interface LogStream  (Source/WebKit/Shared/LogStream.messages.in)
    direction: (not annotated) -> (not annotated)  [stream]
    1 message:
        LogOnBehalfOfWebContent  (async)
```

The handler is read from the generated receiver code in `--build-dir`. It
should be the output directory of `ipc_generate.py` or a WebKit build's
products directory such as `WebKitBuild/Debug`. Without `--build-dir`, the
handler is guessed from WebKit's naming convention and the output says so.

## ipc_map.py

`ipc_map.py` maps every IPC interface and message of a tag or commit,
with the direction of each interface. It runs two helpers that must sit
next to it. `extract_ipc.py` parses every `*.messages.in` and
`build_ipc_tables.py` merges the result with the places that send each
message. It writes:

- `ipc_summary.md`: interfaces and messages per direction
- `ipc_full_table.md`: every interface, grouped by direction
- `ipc_all_messages_<ref>.md`: every message of every interface
- `ipc_all_signatures_<ref>.md`: every message with its arguments and reply
- `ipc_map.json`: all of it, machine-readable

```sh
$ ipc_tools/ipc_map.py ~/WebKit WebKit-7621.2.5.11.8 out_ipc_map
[*] Mapping WebKit IPC at WebKit-7621.2.5.11.8
    [*] Collecting send sites
        [+] 4561 send sites
    [*] Parsing *.messages.in (annotation fallback: origin/main at 9c83f601b16c)
        [+] Parsed 241 files, 3513 messages (the generator's test fixtures included)
        [*] Directions: 173 annotated, 45 inferred-from-directory, 23 annotated-on-main
    [*] Building the tables
        [+] 216 interfaces, 3413 messages, 262 synchronous
[+] Done: out_ipc_map/ipc_summary.md, ipc_full_table.md, ipc_all_messages_*.md, ipc_all_signatures_*.md, ipc_map.json
```

The interfaces, messages and signatures always come from the given ref,
read with WebKit's own `*.messages.in` parser at that ref. An interface's
direction comes from its `DispatchedFrom` and `DispatchedTo` annotations.
When the ref lacks them, it comes from the same interface on `origin/main`,
then from the processes that send its messages and for a few shared
interfaces from a table checked by hand for Safari 18.5. The log names the
`origin/main` commit it used.

EOF
