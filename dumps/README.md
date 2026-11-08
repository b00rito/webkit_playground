# dumps

Output of the tools in `ipc_tools/`. One directory per tool and WebKit
version, named `<tool>_<tag>`, for example `ipc_map_WebKit-7621.2.5.11.8`.

## File overview

| File | What it is |
|---|---|
| `ipc_summary.md` | Interfaces and messages per direction |
| `ipc_full_table.md` | Every interface, grouped by direction |
| `ipc_all_messages_<ref>.md` | Every message of every interface |
| `ipc_all_signatures_<ref>.md` | Every message with its arguments and reply |
| `ipc_map.json` | All of it, machine-readable |
| `ipc_raw.json` | The parsed `*.messages.in` files, before the directions are resolved |
| `send_sites.txt` | Every `Messages::<Interface>::<Message>` in the source, as `git grep` found it |

To create dumps:

```sh
ipc_tools/ipc_map.py ~/WebKit <ref> dumps/ipc_map_<ref>
```

## Which origin/main a dump used

The interfaces, messages and signatures in a dump always come from its tag.
Only the direction of an interface that the tag doesn't annotate, from
which process to which, is borrowed from the same interface on WebKit's
`origin/main`. `origin/main` moves with every `git fetch`, so a dump comes
out exactly the same again only with the same `origin/main` commit.
`ipc_map.py` prints the commit it used, and each dump here records it:

| Dump | WebKit version | `origin/main` at |
|---|---|---|
| `ipc_map_WebKit-7621.2.5.11.8` | macOS Safari 18.5 | `9c83f601b16c`, 14 October 2026 |

`ipc_map.py` always reads `origin/main`. To reproduce a dump, point it at
the recorded commit first, for example
`git -C ~/WebKit update-ref refs/remotes/origin/main 9c83f601b16c`; the
next `git fetch` moves it back.

EOF
