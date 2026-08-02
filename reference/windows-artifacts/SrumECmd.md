<!-- generated-by: scripts/generate_pages.py -->
# SrumECmd

**Kit:** FLARE-VM / SIFT (Eric Zimmerman tools)  **Capability:** Parse ESE / SRUM / Amcache databases  **Version:** 2026.5.0+880ad26bcb011976a8fc521eea63fc5e6e65ba02
**Captured:** `cyberlab-aio` via `--help` on 2026-08-01  [raw](../../capture/cyberlab-aio/help/SrumECmd.help.txt)

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Description:

## Synopsis

```
SrumECmd [options]
```

## Common invocations

_TODO: up to 8 task-titled invocations._

## Options

All 11 options parsed from the captured help text. The final column is filled in by review.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-f` | f | SRUDB.dat file to parse |  |
| `-r` | r | SOFTWARE hive to process. This is optional, but recommended |  |
| `-d` | d | Directory to recursively process, looking for SRUDB.dat and SOFTWARE hive. This mode is primarily used with KAPE so both SRUDB.dat and SOFTWARE hive can be located |  |
| `--csv` | csv | Directory to save CSV formatted results to. Be sure to include the full path in double quotes |  |
| `--dt` | dt | The custom date/time format to use when displaying time stamps. See https://goo.gl/CNVq0k for options [default: yyyy-MM-dd HH:mm:ss] |  |
| `--debug` | — | Show debug information during processing |  |
| `--trace` | — | Show trace information during processing |  |
| `-?` | — | Show help and usage information |  |
| `-h` | — | Show help and usage information |  |
| `--help` | — | Show help and usage information |  |
| `--version` | — | Show version information |  |

## Gotchas

_TODO: operational traps._

## See also

[`esedbexport`](../windows-artifacts/esedbexport.md), [`esedbinfo`](../windows-artifacts/esedbinfo.md), [`AmcacheParser`](../windows-artifacts/AmcacheParser.md)
