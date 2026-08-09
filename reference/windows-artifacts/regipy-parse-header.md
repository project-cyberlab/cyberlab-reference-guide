<!-- generated-by: scripts/generate_pages.py -->
# regipy-parse-header

| | |
|---|---|
| **Kit** | SIFT Workstation (regipy) |
| **Capability** | Parse registry hives |
| **Captured from** | `cyberlab-aio` via `--help` on 2026-08-09 — [raw help output](../../capture/cyberlab-aio/help/regipy-parse-header.help.txt) |

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Print a hive's header — sequence numbers, timestamp and whether it was cleanly unmounted. A dirty hive means transaction logs still hold recent changes, so this is the check that tells you whether you are reading the whole story.

## When you'd reach for this

An analyst reaches for regipy-parse-header when examining the header of a registry hive file to quickly retrieve metadata such as sequence numbers and modification times, often running it before deeper analysis of the hive's contents. They may choose it because the Rust backend significantly reduces parsing time compared to the default Python parser, though the Python version remains the default if the Rust backend is not installed.

**Sources:** <https://github.com/mkorman90/regipy>

## Synopsis

```
regipy-parse-header [OPTIONS] HIVE_PATH
```

## Options

All 3 options parsed from the captured help text. The final column is filled in by review.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-v` | — | Verbosity |  |
| `--verbose` | — | Verbosity |  |
| `--help` | — | Show this message and exit. |  |

## Gotchas

_TODO: operational traps._

## See also

[`rip.pl`](../windows-artifacts/rip.pl.md), [`regripper`](../windows-artifacts/regripper.md), [`hivexsh`](../windows-artifacts/hivexsh.md), [`regfexport`](../windows-artifacts/regfexport.md), [`regfinfo`](../windows-artifacts/regfinfo.md), [`regfmount`](../windows-artifacts/regfmount.md), [`regipy-dump`](../windows-artifacts/regipy-dump.md), [`regipy-plugins-run`](../windows-artifacts/regipy-plugins-run.md)
