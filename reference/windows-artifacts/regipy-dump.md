<!-- generated-by: scripts/generate_pages.py -->
# regipy-dump

| | |
|---|---|
| **Kit** | SIFT Workstation (regipy) |
| **Capability** | Parse registry hives |
| **Captured from** | `cyberlab-aio` via `--help` on 2026-08-07 — [raw help output](../../capture/cyberlab-aio/help/regipy-dump.help.txt) |

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Dump a registry hive to JSON with regipy, so the contents can be searched, diffed or fed into other tooling rather than read key by key.

## Synopsis

```
regipy-dump [OPTIONS] HIVE_PATH
```

## Options

All 18 options parsed from the captured help text; 1 reviewed with usage guidance.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-o` | FILE | — |  |
| `-p` | TEXT | A registry path to start iterating from |  |
| `--registry-path` | TEXT | A registry path to start iterating from |  |
| `-t` | — | Create a CSV timeline instead | An analyst would use the -t flag when they need to output a timeline of the registry hive data instead of a JSON file. |
| `--timeline` | — | Create a CSV timeline instead | An analyst would use the -t flag when they need to output a timeline of the registry hive data instead of a JSON file. |
| `-l` | TEXT | Specify a hive type, if it could not be identified for some reason |  |
| `--hive-type` | TEXT | Specify a hive type, if it could not be identified for some reason |  |
| `-r` | TEXT | The path from which the partial hive actually starts, for example: -t ntuser -r "/Software" would mean this is actually a HKCU hive, starting from HKCU/Software |  |
| `--partial_hive_path` | TEXT | The path from which the partial hive actually starts, for example: -t ntuser -r "/Software" would mean this is actually a HKCU hive, starting from HKCU/Software |  |
| `-v` | — | Verbosity |  |
| `--verbose` | — | Verbosity |  |
| `-d` | — | Not fetching the values for each subkey makes the iteration way faster. Values count will still be returned |  |
| `--do-not-fetch-values` | — | Not fetching the values for each subkey makes the iteration way faster. Values count will still be returned |  |
| `-s` | TEXT | If "-s" was specified, fetch only values for subkeys starting this timestamp in isoformat |  |
| `--start-date` | TEXT | If "-s" was specified, fetch only values for subkeys starting this timestamp in isoformat |  |
| `-e` | TEXT | If "-e" was specified, fetch only values for subkeys until this timestamp in isoformat |  |
| `--end-date` | TEXT | If "-e" was specified, fetch only values for subkeys until this timestamp in isoformat |  |
| `--help` | — | Show this message and exit. |  |

## Gotchas

_TODO: operational traps._

## See also

[`rip.pl`](../windows-artifacts/rip.pl.md), [`regripper`](../windows-artifacts/regripper.md), [`hivexsh`](../windows-artifacts/hivexsh.md), [`regfexport`](../windows-artifacts/regfexport.md), [`regfinfo`](../windows-artifacts/regfinfo.md), [`regfmount`](../windows-artifacts/regfmount.md), [`regipy-parse-header`](../windows-artifacts/regipy-parse-header.md), [`regipy-plugins-run`](../windows-artifacts/regipy-plugins-run.md)
