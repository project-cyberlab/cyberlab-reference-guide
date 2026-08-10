<!-- generated-by: scripts/generate_pages.py -->
# evtxexport

| | |
|---|---|
| **Kit** | SIFT Workstation (libyal) |
| **Capability** | Parse Windows event logs |
| **Captured from** | `cyberlab-aio` via `--help` on 2026-08-10 — [raw help output](../../capture/cyberlab-aio/help/evtxexport.help.txt) |

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Use evtxexport to export items stored in a Windows XML Event Viewer

## When you'd reach for this

An analyst reaches for evtxexport when exporting event records from an XML Event Log (.evtx) file, often after mounting a volume or image to access logs, as it supports exporting full event messages requiring SYSTEM and SOFTWARE registry files; they may use it after mounting a QEMU VM image and before analyzing event data in text or XML format, preferring it over similar tools for its ability to handle multi-language resources and full message exports.

**Sources:** <https://github.com/libyal/libevtx/wiki/Tools>

## Synopsis

```
evtxexport [ -c codepage ] [ -f format ] [ -l log_file ]
[ -m mode ] [ -p resource_files_path ]
[ -r registy_files_path ] [ -s system_file ]
[ -S software_file ] [ -t event_log_type ]
[ -hTvV ] source
```

## Common invocations

```
# Export Windows event log entries for analysis
evtxexport -p c/ -r c/Windows/System32/config/ c/Windows/System32/winevt/Logs/Apllication.Evtx
# Export event logs to XML format from file
evtxexport -f xml p1/Windows/System32/winevt/Logs/Application.evtx
# Extract Windows event logs from mounted volume
evtxexport -p p1/ -r p1/Windows/System32/config/ p1/Windows/System32/winevt/Logs/System.evtx
```

## Options

All 13 options parsed from the captured help text; 7 reviewed with usage guidance.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-c` | — | codepage of ASCII strings, options: ascii, windows-874, windows-932, windows-936, windows-949, windows-950, windows-1250, windows-1251, windows-1252 (default), windows-1253, windows-1254, windows-1255 |  |
| `-f` | — | output format, options: xml, text (default) | An analyst would use the -f flag when exporting event records from an EVTX file in a specific format, such as XML, to ensure the data is structured for analysis or integration with other tools. |
| `-h` | — | shows this help |  |
| `-l` | — | logs information about the exported items | An analyst would use the -l flag when specifying the path to a particular EVTX log file to be processed by evtxexport. |
| `-m` | — | export mode, option: all, items (default), recovered 'all' exports the (allocated) items and recovered items, 'items' exports the (allocated) items and 'recovered' exports the recovered items |  |
| `-p` | — | search PATH for the resource files | An analyst would use the -p flag when specifying the path to a mounted file system or volume containing Windows event logs and registry files for extraction. |
| `-r` | — | name of the directory containing the SOFTWARE and SYSTEM (Windows) Registry file | An analyst would use the -r flag when specifying the directory containing the SYSTEM and SOFTWARE registry files to properly parse event log data from a mounted Windows volume. |
| `-s` | — | filename of the SYSTEM (Windows) Registry file. This option overrides the path provided by -r | An analyst would use the -s flag when specifying the path to the SYSTEM registry file to export event log data that requires registry information for proper interpretation. |
| `-S` | — | filename of the SOFTWARE (Windows) Registry file. This option overrides the path provided by -r | An analyst would use the -S flag when exporting event logs from a mounted volume and needing to include the SOFTWARE registry file to resolve software-specific information referenced in the event data. |
| `-t` | — | event log type, options: application, security, system if not specified the event log type is determined based on the filename. |  |
| `-T` | — | use event template definitions to parse the event record data |  |
| `-v` | — | verbose output to stderr | An analyst would use the -v flag when they need detailed error, verbose, or debug output printed to stderr during the processing of EVTX files to troubleshoot issues or understand the tool's operation. |
| `-V` | — | print version |  |

## Gotchas

_TODO: operational traps._

## See also

[`evtxinfo`](../windows-artifacts/evtxinfo.md), [`EvtxECmd`](../windows-artifacts/EvtxECmd.md), [`chainsaw`](../windows-artifacts/chainsaw.md), [`hayabusa`](../windows-artifacts/hayabusa.md)
