<!-- generated-by: scripts/generate_pages.py -->
# regipy-plugins-run

**Kit:** SIFT Workstation (regipy)  **Capability:** Parse registry hives
**Captured:** `cyberlab-aio` via `--help` on 2026-08-01  [raw](../../capture/cyberlab-aio/help/regipy-plugins-run.help.txt)

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

identified for some reason

## Synopsis

```
regipy-plugins-run [OPTIONS] HIVE_PATH
```

## Common invocations

_TODO: up to 8 task-titled invocations._

## Options

All 11 options parsed from the captured help text. The final column is filled in by review.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-o` | FILE | Output path for plugins result [required] |  |
| `-p` | TEXT | A plugin or list of plugins to execute command separated |  |
| `--plugins` | TEXT | A plugin or list of plugins to execute command separated |  |
| `-t` | TEXT | Specify a hive type, if it could not be identified for some reason |  |
| `--hive-type` | TEXT | Specify a hive type, if it could not be identified for some reason |  |
| `-r` | TEXT | The path from which the partial hive actually starts, for example: -t ntuser -r "/Software" would mean this is actually a HKCU hive, starting from HKCU/Software |  |
| `--partial_hive_path` | TEXT | The path from which the partial hive actually starts, for example: -t ntuser -r "/Software" would mean this is actually a HKCU hive, starting from HKCU/Software |  |
| `-v` | — | Verbosity |  |
| `--verbose` | — | Verbosity |  |
| `--include-unvalidated` | — | Include plugins that don't have validation test cases. These plugins may return incomplete or inaccurate data. Use at your own risk. |  |
| `--help` | — | Show this message and exit. |  |

## Gotchas

_TODO: operational traps._

## See also

[`rip.pl`](../windows-artifacts/rip.pl.md), [`regripper`](../windows-artifacts/regripper.md), [`hivexsh`](../windows-artifacts/hivexsh.md), [`regfexport`](../windows-artifacts/regfexport.md), [`regfinfo`](../windows-artifacts/regfinfo.md), [`regfmount`](../windows-artifacts/regfmount.md), [`regipy-dump`](../windows-artifacts/regipy-dump.md), [`regipy-parse-header`](../windows-artifacts/regipy-parse-header.md)
