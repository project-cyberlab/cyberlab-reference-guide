<!-- generated-by: scripts/generate_pages.py -->
# SrumECmd

| | |
|---|---|
| **Kit** | FLARE-VM / SIFT (Eric Zimmerman tools) |
| **Capability** | Parse ESE / SRUM / Amcache databases |
| **Version** | 2026.5.0 |
| **Captured from** | `cyberlab-aio` via `--help` on 2026-08-02 — [raw help output](../../capture/cyberlab-aio/help/SrumECmd.help.txt) |

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Parse the System Resource Usage Monitor database, which Windows keeps for roughly 30 days. It records bytes sent and received per application per user — the artifact that answers 'how much data left this host, and which process sent it?' long after the network logs have rolled.

## Synopsis

```
SrumECmd [options]
```

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
