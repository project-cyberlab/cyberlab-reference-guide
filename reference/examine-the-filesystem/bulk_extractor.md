<!-- generated-by: scripts/generate_pages.py -->
# bulk_extractor

**Kit:** REMnux · Kali Linux · SIFT Workstation  **Capability:** Carve files out of unstructured data; Search raw data for a pattern; Recover encryption keys from memory  **Version:** bulk_extractor 2.2.0
**Captured:** `cyberlab-aio` via `--help` on 2026-08-01  [raw](../../capture/cyberlab-aio/help/bulk_extractor.help.txt)  **Docs:** <https://github.com/simsong/bulk_extractor/>

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Extract interesting strings from binary files.

## Synopsis

```
bulk_extractor [OPTION...] image_name
```

## Common invocations

<!-- candidates mined from cyberlab; verify each flag against the options table below before treating as reviewed -->
```
# from cyberlab 02-memory-forensics
bulk_extractor -V
# from cyberlab 02-memory-forensics
bulk_extractor -o be_out sample.mem
# from cyberlab 05-file-carving
bulk_extractor -o /tmp/bulk_out exercise/sample.dd
# from cyberlab 05-file-carving
bulk_extractor -o /tmp/ak_bulk exercise/sample.dd
# from cyberlab 20-volatility-deep
bulk_extractor -o be_out exercise/memdump.raw
# from cyberlab 47-ransomware-memory-case
bulk_extractor -E aes -E zip -o be_out memory.raw
# from cyberlab 47-ransomware-memory-case
bulk_extractor -E aes -o exercise/be_out exercise/memory.raw
# from cyberlab 51-linux-triage-workflow
bulk_extractor -o be_out disk.raw
```

## Options

All 69 options parsed from the captured help text. The final column is filled in by review.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-A` | arg | Offset added (in bytes) to feature locations (default: 0) |  |
| `--offset_add` | arg | Offset added (in bytes) to feature locations (default: 0) |  |
| `-b` | arg | Path of file whose contents are prepended to top of all feature files |  |
| `--banner_file` | arg | Path of file whose contents are prepended to top of all feature files |  |
| `-C` | arg | Size of context window reported in bytes (default: 16) |  |
| `--context_window` | arg | Size of context window reported in bytes (default: 16) |  |
| `-d` | — | enable debug-level diagnostic logging |  |
| `--debug` | — | enable debug-level diagnostic logging |  |
| `-E` | arg | disable all scanners except the one specified. Same as -x all -E scanner. |  |
| `--enable_exclusive` | arg | disable all scanners except the one specified. Same as -x all -E scanner. |  |
| `-e` | arg | enable a scanner (can be repeated) |  |
| `--enable` | arg | enable a scanner (can be repeated) |  |
| `-x` | arg | disable a scanner (can be repeated) |  |
| `--disable` | arg | disable a scanner (can be repeated) |  |
| `-f` | arg | search for a pattern (can be repeated) |  |
| `--find` | arg | search for a pattern (can be repeated) |  |
| `-F` | arg | read patterns to search from a file (can be repeated) |  |
| `--find_file` | arg | read patterns to search from a file (can be repeated) |  |
| `--find-case-sensitive` | — | make -f and -F patterns case-sensitive |  |
| `-G` | arg | page size in bytes (default: 16777216) |  |
| `--pagesize` | arg | page size in bytes (default: 16777216) |  |
| `-g` | arg | margin size in bytes (default: 4194304) |  |
| `--marginsize` | arg | margin size in bytes (default: 4194304) |  |
| `-j` | arg | number of threads (default: 12) |  |
| `--threads` | arg | number of threads (default: 12) |  |
| `-J` | — | read and process data in the primary thread |  |
| `--no_threads` | — | read and process data in the primary thread |  |
| `-M` | arg | max recursion depth (default: 12) |  |
| `--max_depth` | arg | max recursion depth (default: 12) |  |
| `--max_bad_alloc_errors` | arg | max bad allocation errors (default: 3) |  |
| `--max_minute_wait` | arg | maximum number of minutes to wait until all data are read (default: 60) |  |
| `--log-level` | arg | diagnostic log level: trace, debug, info, warning, error, critical, or off |  |
| `--log-file` | arg | diagnostic log file (default: <outdir>/bulk_extractor.log) |  |
| `--notify_main_thread` | — | Display notifications in the main thread after phase1 completes. Useful for running with ThreadSanitizer |  |
| `--notify_async` | — | Display notificaitons asynchronously (default) |  |
| `-o` | arg | output directory [REQUIRED] |  |
| `--outdir` | arg | output directory [REQUIRED] |  |
| `-P` | arg | directories for scanner shared libraries (can be repeated). Default directories include /usr/local/lib/bulk_extractor, /usr/lib/bulk_extractor and any directories specified in the BE_PATH environment  |  |
| `--scanner_dir` | arg | directories for scanner shared libraries (can be repeated). Default directories include /usr/local/lib/bulk_extractor, /usr/lib/bulk_extractor and any directories specified in the BE_PATH environment  |  |
| `-p` | arg | print the value of <path>[:length][/h][/r] with optional length, hex output, or raw output. |  |
| `--path` | arg | print the value of <path>[:length][/h][/r] with optional length, hex output, or raw output. |  |
| `-q` | — | no status or performance output |  |
| `--quit` | — | no status or performance output |  |
| `-r` | arg | file to read alert list from |  |
| `--alert_list` | arg | file to read alert list from |  |
| `-R` | — | treat image file as a directory to recursively explore |  |
| `--recurse` | — | treat image file as a directory to recursively explore |  |
| `-S` | arg | set a name=value option (can be repeated) |  |
| `--set` | arg | set a name=value option (can be repeated) |  |
| `-s` | arg | random sampling parameter frac[:passes] |  |
| `--sampling` | arg | random sampling parameter frac[:passes] |  |
| `-V` | — | Display PACKAGE_VERSION (currently) 2.2.0-DEVELOP |  |
| `--version` | — | Display PACKAGE_VERSION (currently) 2.2.0-DEVELOP |  |
| `-w` | arg | file to read stop list from |  |
| `--stop_list` | arg | file to read stop list from |  |
| `-Y` | arg | specify <start>[-end] of area on disk to scan |  |
| `--scan` | arg | specify <start>[-end] of area on disk to scan |  |
| `-z` | arg | specify a starting page number |  |
| `--page_start` | arg | specify a starting page number |  |
| `-Z` | — | wipe the output directory (recursively) before starting |  |
| `--zap` | — | wipe the output directory (recursively) before starting |  |
| `-0` | — | disable real-time notification |  |
| `--no_notify` | — | disable real-time notification |  |
| `-1` | — | version 1.0 notification (console-output) |  |
| `--version1` | — | version 1.0 notification (console-output) |  |
| `-H` | — | report information about each scanner |  |
| `--info_scanners` | — | report information about each scanner |  |
| `-h` | — | print help screen |  |
| `--help` | — | print help screen |  |

## Gotchas

_TODO: operational traps._

## See also

[`foremost`](../examine-the-filesystem/foremost.md), [`scalpel`](../examine-the-filesystem/scalpel.md), [`binwalk`](../examine-the-filesystem/binwalk.md), [`tcpxtract`](../examine-the-filesystem/tcpxtract.md), [`rafind2`](../examine-the-filesystem/rafind2.md), [`strings`](../examine-the-filesystem/strings.md), [`grep`](../examine-the-filesystem/grep.md), [`xxd`](../examine-the-filesystem/xxd.md)
