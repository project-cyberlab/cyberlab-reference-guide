<!-- generated-by: scripts/generate_pages.py -->
# AmcacheParser

**Kit:** FLARE-VM / SIFT (Eric Zimmerman tools)  **Capability:** Parse ESE / SRUM / Amcache databases; Parse execution and persistence artifacts  **Version:** 2026.5.0+76dc8354aa98ce1e1c6f942abcfb09f583f411dd
**Captured:** `cyberlab-aio` via `--help` on 2026-07-29  [raw](../../capture/cyberlab-aio/help/AmcacheParser.help.txt)

## Purpose

Description:

## Synopsis

```
AmcacheParser [options]
```

## Common invocations

_TODO: up to 8 task-titled invocations._

## Options

All 15 options parsed from the captured help text. The final column is the judgement layer and is filled in by review.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-f` | f | Amcache.hve file to parse | |
| `-i` | — | Include file entries for Programs entries | |
| `-w` | w | Path to file containing SHA-1 hashes to *exclude* from the results. Blacklisting overrides whitelisting | |
| `-b` | b | Path to file containing SHA-1 hashes to *include* from the results. Blacklisting overrides whitelisting | |
| `--csv` | csv | Directory to save CSV formatted results to. Be sure to include the full path in double quotes | |
| `--csvf` | csvf | File name to save CSV formatted results to. When present, overrides default name | |
| `--dt` | dt | The custom date/time format to use when displaying time stamps. See https://goo.gl/CNVq0k for options. Default is: yyyy-MM-dd HH:mm:ss [default: yyyy-MM-dd HH:mm:ss] | |
| `--mp` | — | When true, display higher precision for timestamps | |
| `--nl` | — | When true, ignore transaction log files for dirty hives. Default is FALSE | |
| `--debug` | — | Show debug information during processing | |
| `--trace` | — | Show trace information during processing | |
| `-?` | — | Show help and usage information | |
| `-h` | — | Show help and usage information | |
| `--help` | — | Show help and usage information | |
| `--version` | — | Show version information | |

## Gotchas

_TODO: operational traps._

## See also

`esedbexport`, `esedbinfo`, `SrumECmd`, `PECmd`, `AppCompatCacheParser`, `MFTECmd`
