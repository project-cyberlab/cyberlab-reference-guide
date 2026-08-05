<!-- generated-by: scripts/generate_pages.py -->
# regfexport

| | |
|---|---|
| **Kit** | SIFT Workstation (libyal) |
| **Capability** | Parse registry hives |
| **Captured from** | `cyberlab-aio` via `--help` on 2026-08-05 — [raw help output](../../capture/cyberlab-aio/help/regfexport.help.txt) |

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Use regfexport to export information from a Windows NT

## Synopsis

```
regfexport [ -c codepage ] [ -K key_path ] [ -l logfile ]
[ -hvV ] source
```

## Options

All 6 options parsed from the captured help text. The final column is filled in by review.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-c` | — | codepage of ASCII strings, options: ascii, windows-874, windows-932, windows-936, windows-949, windows-950, windows-1250, windows-1251, windows-1252 (default), windows-1253, windows-1254, windows-1255 |  |
| `-h` | — | shows this help |  |
| `-K` | — | show information about a specific key path. |  |
| `-l` | — | logs information about the exported items |  |
| `-v` | — | verbose output to stderr |  |
| `-V` | — | print version |  |

## Gotchas

_TODO: operational traps._

## See also

[`rip.pl`](../windows-artifacts/rip.pl.md), [`regripper`](../windows-artifacts/regripper.md), [`hivexsh`](../windows-artifacts/hivexsh.md), [`regfinfo`](../windows-artifacts/regfinfo.md), [`regfmount`](../windows-artifacts/regfmount.md), [`regipy-dump`](../windows-artifacts/regipy-dump.md), [`regipy-parse-header`](../windows-artifacts/regipy-parse-header.md), [`regipy-plugins-run`](../windows-artifacts/regipy-plugins-run.md)
