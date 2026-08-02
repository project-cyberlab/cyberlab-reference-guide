<!-- generated-by: scripts/generate_pages.py -->
# frida-ps

| | |
|---|---|
| **Kit** | REMnux |
| **Capability** | Emulate or instrument execution |
| **Version** | 17.16.3 |
| **Captured from** | `cyberlab-aio` via `--help` on 2026-08-02 — [raw help output](../../capture/cyberlab-aio/help/frida-ps.help.txt) |
| **Documentation** | <https://frida.re> |

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Trace the execution of a process to analyze its behavior.

## Synopsis

```
frida-ps [options]
```

## Options

All 28 options parsed from the captured help text. The final column is filled in by review.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-h` | — | show this help message and exit |  |
| `--help` | — | show this help message and exit |  |
| `-D` | ID | connect to device with the given ID |  |
| `--device` | ID | connect to device with the given ID |  |
| `-U` | — | connect to USB device |  |
| `--usb` | — | connect to USB device |  |
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
