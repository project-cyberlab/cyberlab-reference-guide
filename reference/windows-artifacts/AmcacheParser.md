<!-- generated-by: scripts/generate_pages.py -->
# AmcacheParser

| | |
|---|---|
| **Kit** | FLARE-VM / SIFT (Eric Zimmerman tools) |
| **Capability** | Parse ESE / SRUM / Amcache databases; Parse execution and persistence artifacts |
| **Version** | 2026.5.0 |
| **Captured from** | `cyberlab-aio` via `--help` on 2026-08-04 — [raw help output](../../capture/cyberlab-aio/help/AmcacheParser.help.txt) |

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Parse Amcache.hve — the record of programs present on a host, with SHA-1 hashes, including binaries that have since been deleted.

## When you'd reach for this

An analyst reaches for AmcacheParser after manually examining the AmCache hive with Registry Explorer or when needing structured CSV output for timeline analysis, as it automates extraction of AmCache data into a CSV file, which is more efficient than manual methods or RegRipper’s plugin-based reports. They may run it following the extraction of the Amcache.hve file and before analyzing results in Timeline Explorer, prioritizing its automation and compatibility with further analysis tools.

**Sources:** <https://www.mennovanveenendaal.com/posts/The-Windows-AmCache-and-ShimCache-Artifacts/>

## Synopsis

```
AmcacheParser [options]
```

## Options

All 15 options parsed from the captured help text; 9 reviewed with usage guidance.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-f` | f | Amcache.hve file to parse | The Amcache.hve to parse. |
| `-i` | — | Include file entries for Programs entries | Include file entries associated with Programs entries. More complete, and noisier. |
| `-w` | w | Path to file containing SHA-1 hashes to *exclude* from the results. Blacklisting overrides whitelisting | Blacklist of SHA-1 hashes to exclude. Blacklisting overrides whitelisting, so a hash in both is dropped — the safe default when suppressing known-good noise. |
| `-b` | b | Path to file containing SHA-1 hashes to *include* from the results. Blacklisting overrides whitelisting | Whitelist of SHA-1 hashes to include. |
| `--csv` | csv | Directory to save CSV formatted results to. Be sure to include the full path in double quotes | Write CSV to a directory. The usual output. |
| `--csvf` | csvf | File name to save CSV formatted results to. When present, overrides default name | Override the generated CSV filename. |
| `--dt` | dt | The custom date/time format to use when displaying time stamps. See https://goo.gl/CNVq0k for options. Default is: yyyy-MM-dd HH:mm:ss [default: yyyy-MM-dd HH:mm:ss] | Custom timestamp format for the output. |
| `--mp` | — | When true, display higher precision for timestamps | Higher-precision timestamps. |
| `--nl` | — | When true, ignore transaction log files for dirty hives. Default is FALSE | Ignore transaction logs for a dirty hive. Leave this off unless you know why you want it: skipping the logs means parsing a hive that is missing its most recent changes. |
| `--debug` | — | Show debug information during processing |  |
| `--trace` | — | Show trace information during processing |  |
| `-?` | — | Show help and usage information |  |
| `-h` | — | Show help and usage information |  |
| `--help` | — | Show help and usage information |  |
| `--version` | — | Show version information |  |

## Gotchas

- Amcache records that a binary was **present**, not that it ran. It is evidence of existence; Prefetch and event logs are evidence of execution. Conflating the two is the standard error with this artifact.
- It carries SHA-1 for entries, which makes it the fastest way to tie a deleted binary to threat intelligence long after the file is gone.
- The hive is usually dirty when collected from a live host. Let the transaction logs replay — the entries only in the logs are the most recent, which is normally the part you care about.

## See also

[`esedbexport`](../windows-artifacts/esedbexport.md), [`esedbinfo`](../windows-artifacts/esedbinfo.md), [`SrumECmd`](../windows-artifacts/SrumECmd.md), [`PECmd`](../windows-artifacts/PECmd.md), [`AppCompatCacheParser`](../windows-artifacts/AppCompatCacheParser.md), [`MFTECmd`](../windows-artifacts/MFTECmd.md)
