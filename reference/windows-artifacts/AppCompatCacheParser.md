<!-- generated-by: scripts/generate_pages.py -->
# AppCompatCacheParser

| | |
|---|---|
| **Kit** | FLARE-VM / SIFT (Eric Zimmerman tools) |
| **Capability** | Parse execution and persistence artifacts |
| **Version** | 2026.5.0 |
| **Captured from** | `cyberlab-aio` via `--help` on 2026-08-04 — [raw help output](../../capture/cyberlab-aio/help/AppCompatCacheParser.help.txt) |

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Parse the Application Compatibility Cache (Shimcache) out of the SYSTEM registry hive. Windows records an executable here when the shim engine examines it, which happens for programs that were run and for some that were merely present — so it is evidence of existence and interest, not proof of execution.

## When you'd reach for this

An analyst reaches for AppCompatCacheParser when examining ShimCache for historical execution evidence, often after checking UserAssist or before parsing AmCache, as it converts the registry's AppCompatCache into a readable CSV, providing file names, sizes, and timestamps that manual analysis cannot easily extract. They may prefer it over AmCacheParser when focusing on ShimCache-specific data rather than AmCache's more detailed but differently structured entries.

**Sources:** <https://hackers-arise.com/digital-forensics-registry-analysis-for-beginners-part-3-evidence-of-execution/> · <https://hivesecurity.gitlab.io/blog/dfir-incident-response-complete-guide-2026/> · <https://nullsec.us/windows-10-11-appcompatcache-deep-dive/>

## Synopsis

```
AppCompatCacheParser [options]
```

## Options

All 13 options parsed from the captured help text. The final column is filled in by review.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-f` | f | Full path to SYSTEM hive to process. If this option is not specified, the live Registry will be used |  |
| `--csv` | csv | Directory to save CSV formatted results to. Be sure to include the full path in double quotes |  |
| `--csvf` | csvf | File name to save CSV formatted results to. When present, overrides default name |  |
| `-c` | c | The ControlSet to parse. Default is to extract all control sets [default: -1] |  |
| `-t` | — | Sorts last modified timestamps in descending order |  |
| `--dt` | dt | The custom date/time format to use when displaying time stamps. See https://goo.gl/CNVq0k for options [default: yyyy-MM-dd HH:mm:ss] |  |
| `--nl` | — | When true, ignore transaction log files for dirty hives |  |
| `--debug` | — | Show debug information during processing |  |
| `--trace` | — | Show trace information during processing |  |
| `-?` | — | Show help and usage information |  |
| `-h` | — | Show help and usage information |  |
| `--help` | — | Show help and usage information |  |
| `--version` | — | Show version information |  |

## Gotchas

_TODO: operational traps._

## See also

[`PECmd`](../windows-artifacts/PECmd.md), [`MFTECmd`](../windows-artifacts/MFTECmd.md), [`AmcacheParser`](../windows-artifacts/AmcacheParser.md)
