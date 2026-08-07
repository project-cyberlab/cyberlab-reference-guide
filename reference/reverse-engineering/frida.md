<!-- generated-by: scripts/generate_pages.py -->
# frida

| | |
|---|---|
| **Kit** | REMnux |
| **Capability** | Emulate or instrument execution |
| **Version** | 17.16.3 |
| **Captured from** | `cyberlab-aio` via `--help` on 2026-08-07 — [raw help output](../../capture/cyberlab-aio/help/frida.help.txt) |
| **Documentation** | <https://frida.re> |

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Trace the execution of a process to analyze its behavior.

## When you'd reach for this

An analyst reaches for Frida when dynamically modifying a running mobile application's behavior, such as bypassing SSL pinning or decrypting obfuscated data, often running commands like `frida -U -f` or `frida -U -p` before injecting scripts; they choose it over similar tools because it allows real-time interaction and modification of processes without requiring source code access.

**Sources:** <https://www.vaadata.com/en/blog/frida-the-tool-dedicated-to-mobile-application-security/>

## Synopsis

```
frida [options] target
```

## Options

All 66 options parsed from the captured help text; 5 reviewed with usage guidance.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-h` | — | show this help message and exit |  |
| `--help` | — | show this help message and exit |  |
| `-D` | ID | connect to device with the given ID |  |
| `--device` | ID | connect to device with the given ID |  |
| `-U` | — | connect to USB device | When an analyst needs to attach Frida to a target application running on a connected Android device via USB to intercept logs, decrypt data, or hook methods during dynamic instrumentation. |
| `--usb` | — | connect to USB device | When an analyst needs to attach Frida to a target application running on a connected Android device via USB to intercept logs, decrypt data, or hook methods during dynamic instrumentation. |
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
| `-f` | TARGET | spawn FILE | An analyst would use the -f flag when needing to inject a script at the start of a target process to bypass security mechanisms like SSL pinning or anti-root protection as the application launches. |
| `--file` | TARGET | spawn FILE | When an analyst needs to specify the executable file for Frida to monitor and unpack during runtime analysis. |
| `-F` | — | attach to frontmost application |  |
| `--attach-frontmost` | — | attach to frontmost application |  |
| `-n` | NAME | attach to NAME |  |
| `--attach-name` | NAME | attach to NAME |  |
| `-N` | IDENTIFIER | attach to IDENTIFIER | When an analyst needs to inject a script into a specific Android application to modify its behavior, such as bypassing validation or decrypting a flag, they would use the -N flag to target the application by name. |
| `--attach-identifier` | IDENTIFIER | attach to IDENTIFIER | When an analyst needs to inject a script into a specific Android application to modify its behavior, such as bypassing validation or decrypting a flag, they would use the -N flag to target the application by name. |
| `-p` | PID | attach to PID |  |
| `--attach-pid` | PID | attach to PID |  |
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
| `-O` | FILE | text file containing additional command line options |  |
| `--options-file` | FILE | text file containing additional command line options |  |
| `--version` | — | show program's version number and exit |  |
| `-l` | SCRIPT | load SCRIPT | An analyst would use the -l flag when injecting a JavaScript script to modify an application's behavior, such as decrypting obfuscated strings or bypassing security mechanisms like SSL pinning. |
| `--load` | SCRIPT | load SCRIPT | An analyst would use the -l flag when injecting a JavaScript script to modify an application's behavior, such as decrypting obfuscated strings or bypassing security mechanisms like SSL pinning. |
| `-P` | PARAMETERS_JSON | parameters as JSON, same as Gadget |  |
| `--parameters` | PARAMETERS_JSON | parameters as JSON, same as Gadget |  |
| `-C` | USER_CMODULE | load CMODULE |  |
| `--cmodule` | USER_CMODULE | load CMODULE |  |
| `--toolchain` | any,internal,external | CModule toolchain to use when compiling from source code |  |
| `-c` | CODESHARE_URI | load CODESHARE_URI |  |
| `--codeshare` | CODESHARE_URI | load CODESHARE_URI |  |
| `-e` | CODE | evaluate CODE |  |
| `--eval` | CODE | evaluate CODE |  |
| `-q` | — | quiet mode (no prompt) and quit after -l and -e |  |
| `-t` | TIMEOUT | seconds to wait before terminating in quiet mode (or 'inf' to run forever) |  |
| `--timeout` | TIMEOUT | seconds to wait before terminating in quiet mode (or 'inf' to run forever) |  |
| `--pause` | — | leave main thread paused after spawning program |  |
| `-o` | LOGFILE | output to log file |  |
| `--output` | LOGFILE | output to log file |  |
| `--eternalize` | — | eternalize the script before exit |  |
| `--exit-on-error` | — | exit with code 1 after encountering any exception in the SCRIPT |  |
| `--kill-on-exit` | — | kill the spawned program when Frida exits |  |
| `--auto-perform` | — | wrap entered code with Java.perform |  |
| `--auto-reload` | — | Enable auto reload of provided scripts and c module (on by default, will be required in the future) |  |
| `--no-auto-reload` | — | Disable auto reload of provided scripts and c module |  |

## Gotchas

_TODO: operational traps._

## See also

[`frida-trace`](../reverse-engineering/frida-trace.md), [`frida-ps`](../reverse-engineering/frida-ps.md), [`frida-discover`](../reverse-engineering/frida-discover.md), [`frida-kill`](../reverse-engineering/frida-kill.md), [`frida-ls-devices`](../reverse-engineering/frida-ls-devices.md)
