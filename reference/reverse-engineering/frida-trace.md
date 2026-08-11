<!-- generated-by: scripts/generate_pages.py -->
# frida-trace

| | |
|---|---|
| **Kit** | REMnux |
| **Capability** | Emulate or instrument execution |
| **Version** | 17.16.3 |
| **Captured from** | `cyberlab-aio` via `--help` on 2026-08-11 — [raw help output](../../capture/cyberlab-aio/help/frida-trace.help.txt) |
| **Documentation** | <https://frida.re> |

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Trace the execution of a process to analyze its behavior.

## When you'd reach for this

An analyst reaches for frida-trace when tracing and modifying application behavior dynamically, such as during reverse engineering or security testing, often after copying frida-server to a remote device and before interacting with the target app's methods. They may choose it over similar tools because it allows real-time modification of method outputs and provides detailed tracing capabilities, as demonstrated by altering return values or inspecting method parameters during execution.

**Sources:** <https://frida.re/docs/frida-trace/> · <https://www.vaadata.com/en/blog/frida-the-tool-dedicated-to-mobile-application-security/>

## Synopsis

```
frida-trace [options] target
```

## Options

All 82 options parsed from the captured help text; 11 reviewed with usage guidance.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-h` | — | show this help message and exit |  |
| `--help` | — | show this help message and exit |  |
| `-D` | ID | connect to device with the given ID |  |
| `--device` | ID | connect to device with the given ID |  |
| `-U` | — | connect to USB device | An analyst would use the -U flag when tracing an application running on a remote Android device connected via USB from their host machine. |
| `--usb` | — | connect to USB device | An analyst would use the -U flag when tracing an application running on a remote Android device connected via USB from their host machine. |
| `-R` | — | connect to remote frida-server |  |
| `--remote` | — | connect to remote frida-server |  |
| `-H` | HOST | connect to remote frida-server on HOST |  |
| `--host` | HOST | connect to remote frida-server on HOST |  |
| `--certificate` | CERTIFICATE | speak TLS with HOST, expecting CERTIFICATE |  |
| `--origin` | ORIGIN | connect to remote server with “Origin” header set to ORIGIN |  |
| `--token` | TOKEN | authenticate with HOST using TOKEN |  |
| `--keepalive-interval` | INTERVAL | set keepalive interval in seconds, or 0 to disable (defaults to -1 to auto-select based on transport) |  |
| `--device-option` | option | override a backend-specific option, such as “control- endpoint=(string)localabstract:/my-frida-server” (supported types are: string, bool, int) |  |
| `--p2p` | — | establish a peer-to-peer connection with target |  |
| `--stun-server` | ADDRESS | set STUN server ADDRESS to use with --p2p |  |
| `-f` | TARGET | spawn FILE | An analyst would use the -f flag when launching a specific application on a mobile device to trace its API calls, such as monitoring crypto functions in Snapchat or Java methods in YouTube. |
| `--file` | TARGET | spawn FILE | An analyst would use the -f flag when launching a specific application on a mobile device to trace its API calls, such as monitoring crypto functions in Snapchat or Java methods in YouTube. |
| `-F` | — | attach to frontmost application |  |
| `--attach-frontmost` | — | attach to frontmost application |  |
| `-n` | NAME | attach to NAME |  |
| `--attach-name` | NAME | attach to NAME |  |
| `-N` | IDENTIFIER | attach to IDENTIFIER | When the target application is already running and the analyst needs to trace functions using its identifier. |
| `--attach-identifier` | IDENTIFIER | attach to IDENTIFIER | When the target application is already running and the analyst needs to trace functions using its identifier. |
| `-p` | PID | attach to PID | An analyst would use the -p flag when tracing functions in a specific process by its process ID, such as monitoring a Windows application's memory-related calls in msvcrt.dll. |
| `--attach-pid` | PID | attach to PID | An analyst would use the -p flag when tracing functions in a specific process by its process ID, such as monitoring a Windows application's memory-related calls in msvcrt.dll. |
| `-W` | PATTERN | await spawn matching PATTERN |  |
| `--await` | PATTERN | await spawn matching PATTERN |  |
| `--stdio` | inherit,pipe | stdio behavior when spawning (defaults to “inherit”) |  |
| `--aux` | option | set aux option when spawning, such as “uid=(int)42” (supported types are: string, bool, int) |  |
| `--realm` | native,emulated | realm to attach in |  |
| `--exceptor` | full,handler-only,off | configure the exception handling mode |  |
| `--disable-unwind-broker` | — | disable the unwind broker |  |
| `--disable-exit-monitor` | — | disable the exit monitor |  |
| `--disable-thread-suspend-monitor` | — | disable the thread suspend monitor |  |
| `--linker-notifier-offset` | OFFSET | add a linker notifier OFFSET (may be specified multiple times) |  |
| `--runtime` | qjs,v8 | script runtime to use |  |
| `--debug` | — | enable the Node.js compatible script debugger |  |
| `--squelch-crash` | — | if enabled, will not dump crash report to console |  |
| `-O` | FILE | text file containing additional command line options | An analyst would use the -O flag when dealing with a large number of command line options that exceed the operating system's maximum command line length, allowing them to pass options via text files. |
| `--options-file` | FILE | text file containing additional command line options | An analyst would use the -O flag when dealing with a large number of command line options that exceed the operating system's maximum command line length, allowing them to pass options via text files. |
| `--version` | — | show program's version number and exit |  |
| `-I` | MODULE | include MODULE | An analyst would use the -I flag when they need to trace all functions within a specific module, such as to broadly monitor activity in a particular library without specifying individual functions. |
| `--include-module` | MODULE | include MODULE | An analyst would use the -I flag when they need to trace all functions within a specific module, such as to broadly monitor activity in a particular library without specifying individual functions. |
| `-X` | MODULE | exclude MODULE |  |
| `--exclude-module` | MODULE | exclude MODULE |  |
| `-i` | FUNCTION | include [MODULE!]FUNCTION | An analyst would use the -i flag when they need to trace specific functions or modules, such as monitoring particular API calls or methods in a target process. |
| `--include` | FUNCTION | include [MODULE!]FUNCTION | An analyst would use the -i flag when they need to trace specific functions or modules, such as monitoring particular API calls or methods in a target process. |
| `-x` | FUNCTION | exclude [MODULE!]FUNCTION | An analyst would use the -x flag when they need to exclude specific functions from being traced after including an entire module or a set of functions matching a pattern. |
| `--exclude` | FUNCTION | exclude [MODULE!]FUNCTION | An analyst would use the -x flag when they need to exclude specific functions from being traced after including an entire module or a set of functions matching a pattern. |
| `-T` | INCLUDE_IMPORTS | include program's imports |  |
| `--include-imports` | INCLUDE_IMPORTS | include program's imports |  |
| `-t` | MODULE | include MODULE imports |  |
| `--include-module-imports` | MODULE | include MODULE imports |  |
| `-m` | OBJC_METHOD | include OBJC_METHOD |  |
| `--include-objc-method` | OBJC_METHOD | include OBJC_METHOD |  |
| `-M` | OBJC_METHOD | exclude OBJC_METHOD |  |
| `--exclude-objc-method` | OBJC_METHOD | exclude OBJC_METHOD |  |
| `-y` | SWIFT_FUNC | include SWIFT_FUNC |  |
| `--include-swift-func` | SWIFT_FUNC | include SWIFT_FUNC |  |
| `-Y` | SWIFT_FUNC | exclude SWIFT_FUNC |  |
| `--exclude-swift-func` | SWIFT_FUNC | exclude SWIFT_FUNC |  |
| `-j` | JAVA_METHOD | include JAVA_METHOD |  |
| `--include-java-method` | JAVA_METHOD | include JAVA_METHOD |  |
| `-J` | JAVA_METHOD | exclude JAVA_METHOD |  |
| `--exclude-java-method` | JAVA_METHOD | exclude JAVA_METHOD |  |
| `-s` | DEBUG_SYMBOL | include DEBUG_SYMBOL |  |
| `--include-debug-symbol` | DEBUG_SYMBOL | include DEBUG_SYMBOL |  |
| `-q` | — | do not format output messages |  |
| `--quiet` | — | do not format output messages |  |
| `-d` | — | add module name to generated onEnter log statement | An analyst would use the --decorate flag when tracing functions that exist in multiple modules to distinguish their logs by adding the module name to the trace output. |
| `--decorate` | — | add module name to generated onEnter log statement | An analyst would use the --decorate flag when tracing functions that exist in multiple modules to distinguish their logs by adding the module name to the trace output. |
| `-S` | PATH | path to JavaScript file used to initialize the session | An analyst would use the -S flag when they need to initialize a frida-trace session by executing custom JavaScript code files to set up the environment, share functions, or add data to the global "state" object before tracing begins. |
| `--init-session` | PATH | path to JavaScript file used to initialize the session | An analyst would use the -S flag when they need to initialize a frida-trace session by executing custom JavaScript code files to set up the environment, share functions, or add data to the global "state" object before tracing begins. |
| `-P` | PARAMETERS_JSON | parameters as JSON, exposed as a global named 'parameters' | An analyst would use the `-P` flag when tracing multiple functions and needing to dynamically control handler behavior, such as conditionally printing the process ID based on a JSON parameter passed via the command line. |
| `--parameters` | PARAMETERS_JSON | parameters as JSON, exposed as a global named 'parameters' | An analyst would use the `-P` flag when tracing multiple functions and needing to dynamically control handler behavior, such as conditionally printing the process ID based on a JSON parameter passed via the command line. |
| `-o` | OUTPUT | dump messages to file |  |
| `--output` | OUTPUT | dump messages to file |  |
| `--ui-host` | UI_HOST | the host to serve the UI on (default localhost) |  |
| `--ui-port` | UI_PORT | the TCP port to serve the UI on |  |
| `--ui-allow-origin` | ORIGIN | allow browser requests from ORIGIN; may be specified multiple times |  |

## Gotchas

_TODO: operational traps._

## See also

[`frida`](../reverse-engineering/frida.md), [`frida-ps`](../reverse-engineering/frida-ps.md), [`frida-discover`](../reverse-engineering/frida-discover.md), [`frida-kill`](../reverse-engineering/frida-kill.md), [`frida-ls-devices`](../reverse-engineering/frida-ls-devices.md)
