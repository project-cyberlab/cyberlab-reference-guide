<!-- generated-by: scripts/generate_pages.py -->
# EvtxECmd

| | |
|---|---|
| **Kit** | FLARE-VM / SIFT (Eric Zimmerman tools) |
| **Capability** | Parse Windows event logs |
| **Version** | 2026.5.0 |
| **Captured from** | `cyberlab-aio` via `--help` on 2026-08-05 — [raw help output](../../capture/cyberlab-aio/help/EvtxECmd.help.txt) |

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Parse Windows event logs into a normalised, filterable CSV, mapping the useful fields out of the XML payload.

## When you'd reach for this

An analyst reaches for EvtxECmd during the "PARSE" phase of the DFIR workflow to convert event logs into standardized CSV, XML, or JSON formats, often after collecting logs with KAPE and before analyzing them in Timeline Explorer, as it supports custom maps, locked file handling, and produces structured output essential for correlation and triage.

**Sources:** <https://ericzimmerman.github.io/> · <https://ridgelinecyber.com/resources/kape-ez-tools/>

## Synopsis

```
EvtxECmd [options]
```

## Options

All 26 options parsed from the captured help text; 20 reviewed with usage guidance.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-f` | f | File to process. Either this or -d is required | A single log, when you already know which one matters. |
| `-d` | d | Directory to recursively process. Either this or -f is required | Recurse a directory of .evtx files — the usual mode when working from a collected `winevt\Logs`. |
| `--csv` | csv | Directory to save CSV formatted results to. Be sure to include the full path in double quotes | Write CSV to a directory. The normal output, and the form the rest of a timeline workflow expects. |
| `--csvf` | csvf | File name to save CSV formatted results to. When present, overrides default name | Override the generated CSV filename. |
| `--json` | json | Directory to save JSON formatted results to. Be sure to include the full path in double quotes | JSON output, for feeding another tool. |
| `--jsonf` | jsonf | File name to save JSON formatted results to. When present, overrides default name | Override the generated JSON filename. |
| `--xml` | xml | Directory to save XML formatted results to | XML output. |
| `--xmlf` | xmlf | File name to save XML formatted results to. When present, overrides default name | Override the generated XML filename. |
| `--dt` | dt | The custom date/time format to use when displaying time stamps. See https://goo.gl/CNVq0k for options [default: yyyy-MM-dd HH:mm:ss.fffffff] | Custom timestamp format for the output. |
| `--inc` | inc | List of Event IDs to process. All others are ignored. Overrides --exc Format is 4624,4625,5410,5500-5600 | Process only these Event IDs. The fastest way to cut a multi-gigabyte log down to the question being asked — ranges are allowed (`4624,4625,5410-5500`). |
| `--exc` | exc | List of Event IDs to IGNORE. All others are included. Format is 4624,4625,5410,5500-5600 | Process everything except these Event IDs. `--inc` wins if both are given. |
| `--sd` | sd | Start date for including events (UTC). Anything OLDER than this is dropped. Format should match --dt | Drop events older than this date (UTC). |
| `--ed` | ed | End date for including events (UTC). Anything NEWER than this is dropped. Format should match --dt | Drop events newer than this date (UTC). With `--sd`, scopes the parse to the incident window instead of all history. |
| `--fj` | — | When true, export all available data when using --json | Export all available data in JSON rather than the mapped subset. |
| `--tdt` | tdt | The number of seconds to use for time discrepancy detection. Default is 1 [default: 1] | Seconds of tolerance for time-discrepancy detection — flags records whose timestamps disagree, a clock-tampering signal. |
| `--met` | — | When true, show metrics about processed event log. Default is true | Show per-log metrics about what was processed. |
| `--maps` | maps | The path where event maps are located. Defaults to 'Maps' folder where program was executed [default: /opt/eztools/EvtxECmd/Maps] | Where the event maps live. The maps are what turn raw XML into named columns; without the right ones, useful fields stay buried in the payload. |
| `--vss` | — | Process all Volume Shadow Copies that exist on drive specified by -f or -d | Also parse every Volume Shadow Copy on the drive, which is where cleared or rotated logs may survive. |
| `--dedupe` | — | Deduplicate -f or -d & VSCs based on SHA-1. First file found wins | Drop duplicates by SHA-1 across the source and shadow copies. Use it whenever `--vss` is on. |
| `--sync` | — | If true, the latest maps from https://github.com/EricZimmerman/evtx/tree/master/evtx/Maps are downloaded and local maps updated | Pull the latest maps from upstream. Worth doing before a big parse — map coverage improves continuously. |
| `--debug` | — | Show debug information during processing |  |
| `--trace` | — | Show trace information during processing |  |
| `-?` | — | Show help and usage information |  |
| `-h` | — | Show help and usage information |  |
| `--help` | — | Show help and usage information |  |
| `--version` | — | Show version information |  |

## Gotchas

- Without a map for an Event ID, the interesting values stay inside the XML payload rather than becoming columns. If an expected field is missing, the map is usually the reason, not the log.
- A cleared log is itself the finding: Security 1102 and System 104 record the clearing. Include them explicitly when hunting anti-forensics.
- Event log timestamps are recorded in UTC but `--sd`/`--ed` are only as good as your assumption about the host's clock. Corroborate before building a timeline on them.

## See also

[`evtxexport`](../windows-artifacts/evtxexport.md), [`evtxinfo`](../windows-artifacts/evtxinfo.md), [`chainsaw`](../windows-artifacts/chainsaw.md), [`hayabusa`](../windows-artifacts/hayabusa.md)
