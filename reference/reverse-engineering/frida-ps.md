<!-- generated-by: scripts/generate_pages.py -->
# frida-ps

| | |
|---|---|
| **Kit** | REMnux |
| **Capability** | Emulate or instrument execution |
| **Version** | 17.16.3 |
| **Captured from** | `cyberlab-aio` via `--help` on 2026-08-07 — [raw help output](../../capture/cyberlab-aio/help/frida-ps.help.txt) |
| **Documentation** | <https://frida.re> |

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Trace the execution of a process to analyze its behavior.

## When you'd reach for this

An analyst reaches for frida-ps when they need to list processes on a remote device, such as after connecting via USB or identifying a specific device ID using frida-ls-devices, to inspect running or installed applications. They may run it before attaching to a target process for further analysis or scripting. They choose it over similar tools because it is explicitly designed for listing processes, a foundational step when interacting with remote systems, as highlighted in the documentation.

**Sources:** <https://frida.re/docs/frida-ps/> · <https://www.vaadata.com/en/blog/frida-the-tool-dedicated-to-mobile-application-security/>

## Synopsis

```
frida-ps [options]
```

## Options

All 28 options parsed from the captured help text; 2 reviewed with usage guidance.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-h` | — | show this help message and exit |  |
| `--help` | — | show this help message and exit |  |
| `-D` | ID | connect to device with the given ID | An analyst would use the -D flag when they need to list processes on a specific device by its ID, such as when targeting a particular connected device during a mobile pentest. |
| `--device` | ID | connect to device with the given ID | An analyst would use the -D flag when they need to list processes on a specific device by its ID, such as when targeting a particular connected device during a mobile pentest. |
| `-U` | — | connect to USB device | An analyst would use the -U flag when connecting to a device via USB to list its running processes or installed applications during a mobile forensic investigation. |
| `--usb` | — | connect to USB device | An analyst would use the -U flag when connecting to a device via USB to list its running processes or installed applications during a mobile forensic investigation. |
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
| `-O` | FILE | text file containing additional command line options |  |
| `--options-file` | FILE | text file containing additional command line options |  |
| `--version` | — | show program's version number and exit |  |
| `-a` | — | list only applications |  |
| `--applications` | — | list only applications |  |
| `-i` | — | include all installed applications |  |
| `--installed` | — | include all installed applications |  |
| `-j` | — | output results as JSON |  |
| `--json` | — | output results as JSON |  |
| `-e` | — | exclude icons in output |  |
| `--exclude-icons` | — | exclude icons in output |  |

## Gotchas

_TODO: operational traps._

## See also

[`frida`](../reverse-engineering/frida.md), [`frida-trace`](../reverse-engineering/frida-trace.md), [`frida-discover`](../reverse-engineering/frida-discover.md), [`frida-kill`](../reverse-engineering/frida-kill.md), [`frida-ls-devices`](../reverse-engineering/frida-ls-devices.md)
