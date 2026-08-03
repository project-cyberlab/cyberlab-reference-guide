<!-- generated-by: scripts/generate_pages.py -->
# evtxexport

| | |
|---|---|
| **Kit** | SIFT Workstation (libyal) |
| **Capability** | Parse Windows event logs |
| **Captured from** | `cyberlab-aio` via `--help` on 2026-08-03 — [raw help output](../../capture/cyberlab-aio/help/evtxexport.help.txt) |

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Use evtxexport to export items stored in a Windows XML Event Viewer

## When you'd reach for this

An analyst reaches for evtxexport when they need to extract and resolve Windows Event Log (EVTX) records into human-readable formats, particularly after acquiring EVTX files and before analyzing event details in tools like Event Viewer, as it reconstructs fully-formatted event messages using registry data and resource files, offering more accurate and context-rich output than basic parsers or raw XML extraction.

**Sources:** <https://deepwiki.com/libyal/libevtx/5.2-evtxexport>

## Synopsis

```
evtxexport [ -c codepage ] [ -f format ] [ -l log_file ]
[ -m mode ] [ -p resource_files_path ]
[ -r registy_files_path ] [ -s system_file ]
[ -S software_file ] [ -t event_log_type ]
[ -hTvV ] source
```

## Options

All 13 options parsed from the captured help text. The final column is filled in by review.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-c` | — | codepage of ASCII strings, options: ascii, windows-874, windows-932, windows-936, windows-949, windows-950, windows-1250, windows-1251, windows-1252 (default), windows-1253, windows-1254, windows-1255 |  |
| `-f` | — | output format, options: xml, text (default) |  |
| `-h` | — | shows this help |  |
| `-l` | — | logs information about the exported items |  |
| `-m` | — | export mode, option: all, items (default), recovered 'all' exports the (allocated) items and recovered items, 'items' exports the (allocated) items and 'recovered' exports the recovered items |  |
| `-p` | — | search PATH for the resource files |  |
| `-r` | — | name of the directory containing the SOFTWARE and SYSTEM (Windows) Registry file |  |
| `-s` | — | filename of the SYSTEM (Windows) Registry file. This option overrides the path provided by -r |  |
| `-S` | — | filename of the SOFTWARE (Windows) Registry file. This option overrides the path provided by -r |  |
| `-t` | — | event log type, options: application, security, system if not specified the event log type is determined based on the filename. |  |
| `-T` | — | use event template definitions to parse the event record data |  |
| `-v` | — | verbose output to stderr |  |
| `-V` | — | print version |  |

## Gotchas

_TODO: operational traps._

## See also

[`evtxinfo`](../windows-artifacts/evtxinfo.md), [`EvtxECmd`](../windows-artifacts/EvtxECmd.md), [`chainsaw`](../windows-artifacts/chainsaw.md), [`hayabusa`](../windows-artifacts/hayabusa.md)
