# webkit_playground

Supporting repo for the blog series *WebKit, Inside Out*: the tools,
scripts and how-tos the posts use, so that their commands and results can
be reproduced.

The posts:
- https://b00rito.github.io/posts/f1_inside_webkit_the_map/
- https://b00rito.github.io/posts/f2_rce_and_sbx/

The tools work on a WebKit checkout (https://github.com/WebKit/WebKit) and
read it with git only, so its working tree is never changed.

For the time being, unless noted otherwise, everything is tested on macOS
against the Safari 18.5 tag, `WebKit-7621.2.5.11.8`.

## Contents

### ipc_tools/

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

EOF
