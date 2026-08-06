<!-- generated-by: scripts/generate_pages.py -->
# evtxinfo

| | |
|---|---|
| **Kit** | SIFT Workstation (libyal) |
| **Capability** | Parse Windows event logs |
| **Captured from** | `cyberlab-aio` via `--help` on 2026-08-06 — [raw help output](../../capture/cyberlab-aio/help/evtxinfo.help.txt) |

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Use evtxinfo to determine information about a Windows XML Event Viewer

## When you'd reach for this

An analyst reaches for evtxinfo after extracting EVTX files from memory dumps using tools like volatility's dumpfiles, running it to inspect file headers and chunk metadata before using evtxdump to parse event data, as it provides structural insights without full log parsing.

**Sources:** <https://manpages.debian.org/unstable/libevtx-utils/evtxexport.1.en.html> · <https://www.rocheston.com/fire/> · <https://www.tophertimzen.com/resources/cs407/slides/week04_02-EventLogs.html>

## Synopsis

```
evtxinfo [ -c codepage ] [ -hvV ] source
```

## Options

All 4 options parsed from the captured help text; 1 reviewed with usage guidance.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-c` | — | codepage of ASCII strings, options: ascii, windows-874, windows-932, windows-936, windows-949, windows-950, windows-1250, windows-1251, windows-1252 (default), windows-1253, windows-1254, windows-1255 | An analyst would use the -c flag when the ASCII strings in the EVTX file are encoded using a codepage different from the default (windows-1252). |
| `-h` | — | shows this help |  |
| `-v` | — | verbose output to stderr |  |
| `-V` | — | print version |  |

## Gotchas

_TODO: operational traps._

## See also

[`evtxexport`](../windows-artifacts/evtxexport.md), [`EvtxECmd`](../windows-artifacts/EvtxECmd.md), [`chainsaw`](../windows-artifacts/chainsaw.md), [`hayabusa`](../windows-artifacts/hayabusa.md)
