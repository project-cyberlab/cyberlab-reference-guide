<!-- generated-by: scripts/generate_pages.py -->
# PECmd

**Kit:** FLARE-VM / SIFT (Eric Zimmerman tools)  **Capability:** Parse execution and persistence artifacts  **Version:** 2026.5.0+bde430c69ba4d97fea8b71fdddb6df7849419c10
**Captured:** `cyberlab-aio` via `--help` on 2026-08-01  [raw](../../capture/cyberlab-aio/help/PECmd.help.txt)

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Description:

## Synopsis

```
PECmd [options]
```

## Common invocations

_TODO: up to 8 task-titled invocations._

## Options

All 20 options parsed from the captured help text. The final column is filled in by review.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-f` | f | File to process. Either this or -d is required |  |
| `-d` | d | Directory to recursively process. Either this or -f is required |  |
| `-k` | k | Comma separated list of keywords to highlight in output. By default, 'temp' and 'tmp' are highlighted. Any additional keywords will be added to these |  |
| `-o` | o | When specified, save prefetch file bytes to the given path. Useful to look at decompressed Win10 files |  |
| `-q` | — | Do not dump full details about each file processed. Speeds up processing when using --json or --csv |  |
| `--csv` | csv | Directory to save CSV formatted results to. Be sure to include the full path in double quotes |  |
| `--csvf` | csvf | File name to save CSV formatted results to. When present, overrides default name |  |
| `--json` | json | Directory to save JSON formatted results to. Be sure to include the full path in double quotes |  |
| `--jsonf` | jsonf | File name to save JSON formatted results to. When present, overrides default name |  |
| `--html` | html | Directory to save xhtml formatted results to. Be sure to include the full path in double quotes |  |
| `--dt` | dt | The custom date/time format to use when displaying time stamps. See https://goo.gl/CNVq0k for options [default: yyyy-MM-dd HH:mm:ss] |  |
| `--mp` | — | When true, display higher precision for timestamps |  |
| `--vss` | — | Process all Volume Shadow Copies that exist on drive specified by -f or -d |  |
| `--dedupe` | — | Deduplicate -f or -d & VSCs based on SHA-1. First file found wins |  |
| `--debug` | — | Show debug information during processing |  |
| `--trace` | — | Show trace information during processing |  |
| `-?` | — | Show help and usage information |  |
| `-h` | — | Show help and usage information |  |
| `--help` | — | Show help and usage information |  |
| `--version` | — | Show version information |  |

## Gotchas

_TODO: operational traps._

## See also

[`AppCompatCacheParser`](../windows-artifacts/AppCompatCacheParser.md), [`MFTECmd`](../windows-artifacts/MFTECmd.md), [`AmcacheParser`](../windows-artifacts/AmcacheParser.md)
