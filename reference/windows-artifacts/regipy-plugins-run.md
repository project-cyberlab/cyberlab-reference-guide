<!-- generated-by: scripts/generate_pages.py -->
# regipy-plugins-run

| | |
|---|---|
| **Kit** | SIFT Workstation (regipy) |
| **Capability** | Parse registry hives |
| **Captured from** | `cyberlab-aio` via `--help` on 2026-08-11 — [raw help output](../../capture/cyberlab-aio/help/regipy-plugins-run.help.txt) |

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Run regipy's plugins over a hive and emit structured results. The Python counterpart to RegRipper, and the easier one to embed in a pipeline because the output is JSON rather than formatted text.

## When you'd reach for this

An analyst reaches for regipy-plugins-run after dumping a registry hive to disk, as it automatically detects the hive type and executes relevant plugins for analysis, offering efficiency over manual plugin selection or alternative tools that lack automatic hive-type detection.

**Sources:** <https://github.com/mkorman90/regipy>

## Synopsis

```
regipy-plugins-run [OPTIONS] HIVE_PATH
```

## Common invocations

```
# Analyze SYSTEM hive using plugins to extract relevant data
regipy-plugins-run ~/Documents/TestEvidence/Registry/SYSTEM -o /tmp/plugins_output.json
```

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
