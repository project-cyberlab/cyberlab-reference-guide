<!-- generated-by: scripts/generate_pages.py -->
# regipy-diff

| | |
|---|---|
| **Kit** | SIFT Workstation (regipy) |
| **Capability** | Parse registry hives |
| **Captured from** | `cyberlab-aio` via `--help` on 2026-08-03 — [raw help output](../../capture/cyberlab-aio/help/regipy-diff.help.txt) |

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Diff two registry hives and report what changed between them. The artifact-level version of a before-and-after detonation: snapshot, run the sample, snapshot again, and read the delta.

## Synopsis

```
regipy-diff [OPTIONS] FIRST_HIVE_PATH SECOND_HIVE_PATH
```

## Options

All 4 options parsed from the captured help text. The final column is filled in by review.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-o` | FILE | — |  |
| `-v` | — | Verbosity |  |
| `--verbose` | — | Verbosity |  |
| `--help` | — | Show this message and exit. |  |

## Gotchas

_TODO: operational traps._

## See also

[`rip.pl`](../windows-artifacts/rip.pl.md), [`regripper`](../windows-artifacts/regripper.md), [`hivexsh`](../windows-artifacts/hivexsh.md), [`regfexport`](../windows-artifacts/regfexport.md), [`regfinfo`](../windows-artifacts/regfinfo.md), [`regfmount`](../windows-artifacts/regfmount.md), [`regipy-dump`](../windows-artifacts/regipy-dump.md), [`regipy-parse-header`](../windows-artifacts/regipy-parse-header.md)
