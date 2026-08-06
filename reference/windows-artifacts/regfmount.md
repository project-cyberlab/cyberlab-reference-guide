<!-- generated-by: scripts/generate_pages.py -->
# regfmount

| | |
|---|---|
| **Kit** | SIFT Workstation (libyal) |
| **Capability** | Parse registry hives |
| **Captured from** | `cyberlab-aio` via `--help` on 2026-08-06 — [raw help output](../../capture/cyberlab-aio/help/regfmount.help.txt) |

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Use regfmount to mount a Windows NT Registry File (REGF)

## When you'd reach for this

An analyst reaches for regfmount when examining Windows registry hive files to explore their structure and contents, often after extracting the hive from a disk image or virtual machine; they may run commands like `ls` and `cat` on the mounted directory to inspect keys and values, preferring it over similar tools for its ability to present registry data as a navigable file system with editable text files.

**Sources:** <https://miloserdov.org/?p=5448>

## Synopsis

```
regfmount [ -c codepage ] [ -X extended_options ] [ -hvV ] file
mount_point
```

## Options

All 5 options parsed from the captured help text. The final column is filled in by review.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-c` | — | codepage of ASCII strings, options: ascii, windows-874, windows-932, windows-936, windows-949, windows-950, windows-1250, windows-1251, windows-1252 (default), windows-1253, windows-1254, windows-1255 |  |
| `-h` | — | shows this help |  |
| `-v` | — | verbose output to stderr, while regfmount will remain running in the foreground |  |
| `-V` | — | print version |  |
| `-X` | — | extended options to pass to sub system |  |

## Gotchas

_TODO: operational traps._

## See also

[`rip.pl`](../windows-artifacts/rip.pl.md), [`regripper`](../windows-artifacts/regripper.md), [`hivexsh`](../windows-artifacts/hivexsh.md), [`regfexport`](../windows-artifacts/regfexport.md), [`regfinfo`](../windows-artifacts/regfinfo.md), [`regipy-dump`](../windows-artifacts/regipy-dump.md), [`regipy-parse-header`](../windows-artifacts/regipy-parse-header.md), [`regipy-plugins-run`](../windows-artifacts/regipy-plugins-run.md)
