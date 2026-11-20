# jsc_examples

Small tests for the `jsc` shell, JavaScriptCore without a browser around
it, that make the engine show its work.

| File | Run it with | Shows |
|---|---|---|
| `tiers.js` | `$JSC --useConcurrentJIT=false --reportCompileTimes=true tiers.js` | One function climbing the Baseline, DFG and FTL tiers, then recompiled after new types arrive |
| `tiers.js` | `$JSC --useConcurrentJIT=false --printEachOSRExit=true tiers.js` | The OSR exit when a speculation fails |
| `shapes.js` | `$JSC shapes.js` | Objects sharing, or not sharing, a Structure |

`$JSC --options` lists every engine option with its default.

## Building jsc

From a WebKit checkout (https://github.com/WebKit/WebKit), on macOS with
Xcode installed:

```sh
cd ~/WebKit
git checkout WebKit-7621.2.5.11.8
env -u SDKROOT DEVELOPER_DIR=/Applications/Xcode.app/Contents/Developer \
    Tools/Scripts/build-jsc --debug
```

- `DEVELOPER_DIR` points the build at Xcode. It is needed when
  `xcode-select -p` prints `/Library/Developer/CommandLineTools`, which
  has no `xcodebuild`. `sudo xcode-select -s /Applications/Xcode.app`
  does the same permanently.
- `env -u SDKROOT` avoids "Couldn't determine platform name from Xcode
  SDK" when the shell exports `SDKROOT`.
- When the Mac runs an older macOS than Xcode's SDK, the binaries won't
  start. Build for the Mac's own version instead, for example with
  `ARGS=MACOSX_DEPLOYMENT_TARGET=14.7` at the end of the `build-jsc`
  command. On the 18.5 tag that also needs a one-line fix in libpas
  first, or the build fails with "'os_unfair_lock_lock_with_flags' is
  only available on macOS 15.0 or newer":

  ```sh
  sed -i '' 's/(PAS_PLATFORM(MAC) \&\& __MAC_OS_X_VERSION_MAX_ALLOWED >= 150000)/(PAS_PLATFORM(MAC) \&\& __MAC_OS_X_VERSION_MIN_REQUIRED >= 150000)/' \
      Source/bmalloc/libpas/src/libpas/pas_lock.h
  ```

## Running

```sh
export DYLD_FRAMEWORK_PATH=~/WebKit/WebKitBuild/Debug
JSC=~/WebKit/WebKitBuild/Debug/jsc
$JSC --useConcurrentJIT=false --reportCompileTimes=true tiers.js
```

`DYLD_FRAMEWORK_PATH` makes `jsc` load the freshly built
`JavaScriptCore.framework` instead of the one in macOS.

Tested with a Debug `jsc` from `WebKit-7621.2.5.11.8` on macOS 14.7.1 with
Xcode 16.2. Option names and output formats change between releases.

EOF
