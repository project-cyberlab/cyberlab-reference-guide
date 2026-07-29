<!-- generated-by: scripts/generate_pages.py -->
# AppCompatCacheParser

**Kit:** FLARE-VM / SIFT (Eric Zimmerman tools)  **Capability:** Parse execution and persistence artifacts  **Version:** 2026.5.0+0cf059f40c2f7b31acdccb142461945402217398
**Captured:** `cyberlab-aio` via `--help` on 2026-07-29  [raw](../../capture/cyberlab-aio/help/AppCompatCacheParser.help.txt)

## Purpose

Description:

## Synopsis

```
AppCompatCacheParser [options]
```

## Common invocations

_TODO: up to 8 task-titled invocations._

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

`PECmd`, `MFTECmd`, `AmcacheParser`
