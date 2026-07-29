<!-- generated-by: scripts/generate_pages.py -->
# EvtxECmd

**Kit:** FLARE-VM / SIFT (Eric Zimmerman tools)  **Capability:** Parse Windows event logs  **Version:** 2026.5.0+bfc7f47ccbf65ffc9a3777cde5498db2fdd94664
**Captured:** `cyberlab-aio` via `--help` on 2026-07-29  [raw](../../capture/cyberlab-aio/help/EvtxECmd.help.txt)

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Description:

## Synopsis

```
EvtxECmd [options]
```

## Common invocations

_TODO: up to 8 task-titled invocations._

## Options

All 26 options parsed from the captured help text. The final column is filled in by review.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-f` | f | File to process. Either this or -d is required |  |
| `-d` | d | Directory to recursively process. Either this or -f is required |  |
| `--csv` | csv | Directory to save CSV formatted results to. Be sure to include the full path in double quotes |  |
| `--csvf` | csvf | File name to save CSV formatted results to. When present, overrides default name |  |
| `--json` | json | Directory to save JSON formatted results to. Be sure to include the full path in double quotes |  |
| `--jsonf` | jsonf | File name to save JSON formatted results to. When present, overrides default name |  |
| `--xml` | xml | Directory to save XML formatted results to |  |
| `--xmlf` | xmlf | File name to save XML formatted results to. When present, overrides default name |  |
| `--dt` | dt | The custom date/time format to use when displaying time stamps. See https://goo.gl/CNVq0k for options [default: yyyy-MM-dd HH:mm:ss.fffffff] |  |
| `--inc` | inc | List of Event IDs to process. All others are ignored. Overrides --exc Format is 4624,4625,5410,5500-5600 |  |
| `--exc` | exc | List of Event IDs to IGNORE. All others are included. Format is 4624,4625,5410,5500-5600 |  |
| `--sd` | sd | Start date for including events (UTC). Anything OLDER than this is dropped. Format should match --dt |  |
| `--ed` | ed | End date for including events (UTC). Anything NEWER than this is dropped. Format should match --dt |  |
| `--fj` | — | When true, export all available data when using --json |  |
| `--tdt` | tdt | The number of seconds to use for time discrepancy detection. Default is 1 [default: 1] |  |
| `--met` | — | When true, show metrics about processed event log. Default is true |  |
| `--maps` | maps | The path where event maps are located. Defaults to 'Maps' folder where program was executed [default: /opt/eztools/EvtxECmd/Maps] |  |
| `--vss` | — | Process all Volume Shadow Copies that exist on drive specified by -f or -d |  |
| `--dedupe` | — | Deduplicate -f or -d & VSCs based on SHA-1. First file found wins |  |
| `--sync` | — | If true, the latest maps from https://github.com/EricZimmerman/evtx/tree/master/evtx/Maps are downloaded and local maps updated |  |
| `--debug` | — | Show debug information during processing |  |
| `--trace` | — | Show trace information during processing |  |
| `-?` | — | Show help and usage information |  |
| `-h` | — | Show help and usage information |  |
| `--help` | — | Show help and usage information |  |
| `--version` | — | Show version information |  |

## Gotchas

_TODO: operational traps._

## See also

[`evtxexport`](../windows-artifacts/evtxexport.md), [`evtxinfo`](../windows-artifacts/evtxinfo.md), [`chainsaw`](../windows-artifacts/chainsaw.md), [`hayabusa`](../windows-artifacts/hayabusa.md)
