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

EOF
