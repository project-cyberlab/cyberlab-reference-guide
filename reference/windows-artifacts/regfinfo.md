<!-- generated-by: scripts/generate_pages.py -->
# regfinfo

| | |
|---|---|
| **Kit** | SIFT Workstation (libyal) |
| **Capability** | Parse registry hives |
| **Captured from** | `cyberlab-aio` via `--help` on 2026-08-09 — [raw help output](../../capture/cyberlab-aio/help/regfinfo.help.txt) |

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Use regfinfo to determine information about a Windows NT

## When you'd reach for this

An analyst reaches for regfinfo when examining Windows NT Registry Files (REGF), such as NTUSER.DAT, to retrieve information about the registry's structure and contents. They might run it after extracting the registry file from a disk image or before using other tools that require the key and value hierarchy, as it provides structured output options like bodyfile and verbose diagnostics.

**Sources:** <https://manpages.debian.org/unstable/libregf-utils/regfinfo.1.en.html>

## Synopsis

```
regfinfo [ -B bodyfile ] [ -c codepage ] [ -hHvV ] source
```

## Options

All 6 options parsed from the captured help text; 4 reviewed with usage guidance.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-B` | — | output key and value hierarchy as a bodyfile | An analyst would use the -B flag when they need to output the key and value hierarchy of a REGF file as a bodyfile for further processing or analysis. |
| `-c` | — | codepage of ASCII strings, options: ascii, windows-874, windows-932, windows-936, windows-949, windows-950, windows-1250, windows-1251, windows-1252 (default), windows-1253, windows-1254, windows-1255 | An analyst would use the -c flag when the ASCII strings in the REGF file are encoded using a specific codepage other than the default (windows-1252). |
| `-h` | — | shows this help |  |
| `-H` | — | shows the key and value hierarchy | An analyst would use the -H flag when examining a Windows NT Registry File to display its key and value hierarchy for forensic analysis. |
| `-v` | — | verbose output to stderr | An analyst would use the -v flag when they need detailed error or debug information printed to stderr during the analysis of a Windows NT Registry File. |
| `-V` | — | print version |  |

## Gotchas

_TODO: operational traps._

## See also

[`rip.pl`](../windows-artifacts/rip.pl.md), [`regripper`](../windows-artifacts/regripper.md), [`hivexsh`](../windows-artifacts/hivexsh.md), [`regfexport`](../windows-artifacts/regfexport.md), [`regfmount`](../windows-artifacts/regfmount.md), [`regipy-dump`](../windows-artifacts/regipy-dump.md), [`regipy-parse-header`](../windows-artifacts/regipy-parse-header.md), [`regipy-plugins-run`](../windows-artifacts/regipy-plugins-run.md)
