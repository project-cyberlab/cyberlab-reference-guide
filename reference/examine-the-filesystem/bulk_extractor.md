<!-- generated-by: scripts/generate_pages.py -->
# bulk_extractor

**Kit:** REMnux · Kali Linux · SIFT Workstation  **Capability:** Carve files out of unstructured data; Search raw data for a pattern; Recover encryption keys from memory  **Version:** bulk_extractor 2.2.0
**Captured:** `cyberlab-aio` via `--help` on 2026-08-02  [raw](../../capture/cyberlab-aio/help/bulk_extractor.help.txt)  **Docs:** <https://github.com/simsong/bulk_extractor/>

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Scan an image for features — email addresses, URLs, credit card numbers, EXIF, keys — without parsing the filesystem at all, so deleted and unallocated content is included.

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

All 69 options parsed from the captured help text; 58 reviewed with usage guidance.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-A` | arg | Offset added (in bytes) to feature locations (default: 0) | Add an offset to reported feature locations — use it when scanning a carved fragment so offsets still refer to the original image. |
| `--offset_add` | arg | Offset added (in bytes) to feature locations (default: 0) | Add an offset to reported feature locations. |
| `-b` | arg | Path of file whose contents are prepended to top of all feature files | Prepend a banner file to every feature file, e.g. a case header. |
| `--banner_file` | arg | Path of file whose contents are prepended to top of all feature files | Prepend a banner file to every feature file. |
| `-C` | arg | Size of context window reported in bytes (default: 16) | Bytes of context stored around each hit. Raise it when a bare match is not enough to judge relevance. |
| `--context_window` | arg | Size of context window reported in bytes (default: 16) | Bytes of context stored around each hit. |
| `-d` | — | enable debug-level diagnostic logging | Debug-level diagnostic logging. |
| `--debug` | — | enable debug-level diagnostic logging | Debug-level diagnostic logging. |
| `-E` | arg | disable all scanners except the one specified. Same as -x all -E scanner. | Run exactly one scanner and disable the rest. The fastest way to answer a single question instead of a full sweep. |
| `--enable_exclusive` | arg | disable all scanners except the one specified. Same as -x all -E scanner. | Run exactly one scanner and disable the rest. |
| `-e` | arg | enable a scanner (can be repeated) | Enable a scanner that is off by default, repeatable. |
| `--enable` | arg | enable a scanner (can be repeated) | Enable a scanner that is off by default, repeatable. |
| `-x` | arg | disable a scanner (can be repeated) | Disable a scanner, repeatable. Turning off the noisy ones is usually a bigger speed win than adding threads. |
| `--disable` | arg | disable a scanner (can be repeated) | Disable a scanner, repeatable. |
| `-f` | arg | search for a pattern (can be repeated) | Search for a regex pattern, repeatable. |
| `--find` | arg | search for a pattern (can be repeated) | Search for a regex pattern, repeatable. |
| `-F` | arg | read patterns to search from a file (can be repeated) | Read search patterns from a file — the practical form when hunting a list of indicators. |
| `--find_file` | arg | read patterns to search from a file (can be repeated) | Read search patterns from a file. |
| `--find-case-sensitive` | — | make -f and -F patterns case-sensitive | Make `-f`/`-F` case-sensitive; they are not by default. |
| `-G` | arg | page size in bytes (default: 16777216) | Page size read per pass. |
| `--pagesize` | arg | page size in bytes (default: 16777216) | Page size read per pass. |
| `-g` | arg | margin size in bytes (default: 4194304) | Margin carried between pages, so a feature spanning a page boundary is still found. |
| `--marginsize` | arg | margin size in bytes (default: 4194304) | Margin carried between pages, so features spanning a page boundary are still found. |
| `-j` | arg | number of threads (default: 12) | Thread count. Defaults to the core count; lower it when the scan is competing with other work. |
| `--threads` | arg | number of threads (default: 12) | Thread count. |
| `-J` | — | read and process data in the primary thread | Single-threaded. Slow, but the first thing to try when a scan crashes or results look non-deterministic. |
| `--no_threads` | — | read and process data in the primary thread | Single-threaded — use when debugging a crash. |
| `-M` | arg | max recursion depth (default: 12) | Maximum recursion depth into nested containers. Lower it if a zip bomb or deeply nested archive stalls the scan. |
| `--max_depth` | arg | max recursion depth (default: 12) | Maximum recursion depth into nested containers. |
| `--max_bad_alloc_errors` | arg | max bad allocation errors (default: 3) | Allocation failures tolerated before aborting. |
| `--max_minute_wait` | arg | maximum number of minutes to wait until all data are read (default: 60) | How long to wait for all data to be read before giving up — raise it for slow or failing media. |
| `--log-level` | arg | diagnostic log level: trace, debug, info, warning, error, critical, or off | Diagnostic log level. |
| `--log-file` | arg | diagnostic log file (default: <outdir>/bulk_extractor.log) | Diagnostic log file; defaults inside the output directory. |
| `--notify_main_thread` | — | Display notifications in the main thread after phase1 completes. Useful for running with ThreadSanitizer |  |
| `--notify_async` | — | Display notificaitons asynchronously (default) |  |
| `-o` | arg | output directory [REQUIRED] | Output directory. Required, and it must not already exist unless you also pass `-Z`. |
| `--outdir` | arg | output directory [REQUIRED] | Output directory. Required. |
| `-P` | arg | directories for scanner shared libraries (can be repeated). Default directories include /usr/local/lib/bulk_extractor, /usr/lib/bulk_extractor and any directories specified in the BE_PATH environment  | Additional directories to load scanner plugins from. |
| `--scanner_dir` | arg | directories for scanner shared libraries (can be repeated). Default directories include /usr/local/lib/bulk_extractor, /usr/lib/bulk_extractor and any directories specified in the BE_PATH environment  | Additional directories to load scanner plugins from. |
| `-p` | arg | print the value of <path>[:length][/h][/r] with optional length, hex output, or raw output. | Print the value at a path, with optional length and hex or raw output — inspection rather than scanning. |
| `--path` | arg | print the value of <path>[:length][/h][/r] with optional length, hex output, or raw output. | Print the value at a path, for inspection rather than scanning. |
| `-q` | — | no status or performance output | Suppress status and performance output. |
| `--quit` | — | no status or performance output | Suppress status and performance output. |
| `-r` | arg | file to read alert list from | Alert list: features to flag prominently — the inverse of a stop list, for known-bad indicators. |
| `--alert_list` | arg | file to read alert list from | Alert list of features to flag prominently. |
| `-R` | — | treat image file as a directory to recursively explore | Treat the input as a directory and recurse it, rather than as a disk image. |
| `--recurse` | — | treat image file as a directory to recursively explore | Treat the input as a directory and recurse it. |
| `-S` | arg | set a name=value option (can be repeated) | Set a scanner option as `name=value`, repeatable. |
| `--set` | arg | set a name=value option (can be repeated) | Set a scanner option as `name=value`, repeatable. |
| `-s` | arg | random sampling parameter frac[:passes] | Random sampling as `frac[:passes]`. Scans a fraction of a huge image to judge whether a full run is worth the hours. |
| `--sampling` | arg | random sampling parameter frac[:passes] | Random sampling as `frac[:passes]`. |
| `-V` | — | Display PACKAGE_VERSION (currently) 2.2.0-DEVELOP |  |
| `--version` | — | Display PACKAGE_VERSION (currently) 2.2.0-DEVELOP |  |
| `-w` | arg | file to read stop list from | Stop list: features to suppress. This is how you cut the known-good noise that otherwise buries the findings. |
| `--stop_list` | arg | file to read stop list from | Stop list of features to suppress. |
| `-Y` | arg | specify <start>[-end] of area on disk to scan | Restrict the scan to a byte range, when `mmls` already told you which region matters. |
| `--scan` | arg | specify <start>[-end] of area on disk to scan | Restrict the scan to a `<start>[-end]` byte range. |
| `-z` | arg | specify a starting page number | Start at a given page number, to resume a long scan. |
| `--page_start` | arg | specify a starting page number | Start at a given page number. |
| `-Z` | — | wipe the output directory (recursively) before starting | Wipe the output directory first. Convenient for reruns and destructive by definition — never point it at a directory holding results you still need. |
| `--zap` | — | wipe the output directory (recursively) before starting | Wipe the output directory first — destructive. |
| `-0` | — | disable real-time notification |  |
| `--no_notify` | — | disable real-time notification |  |
| `-1` | — | version 1.0 notification (console-output) |  |
| `--version1` | — | version 1.0 notification (console-output) |  |
| `-H` | — | report information about each scanner | Report what each scanner does. Worth reading once; the scanner set is the tool. |
| `--info_scanners` | — | report information about each scanner | Report what each scanner does. |
| `-h` | — | print help screen |  |
| `--help` | — | print help screen |  |

## Gotchas

- It ignores the filesystem completely. That is the point — it finds content in unallocated space and slack that a filesystem-aware tool cannot reach — but it also means a hit carries no filename and no timestamp. Map the offset back with [`ffind`](ffind.md)/[`istat`](istat.md) before naming a file in a report.
- Feature files are raw pattern matches, not verified findings. The credit-card scanner in particular flags anything passing a Luhn check, which includes plenty of ordinary numbers.
- Output is large and the scan is long. Sample with `-s` on a multi-terabyte image before committing to a full pass.

## See also

[`foremost`](../examine-the-filesystem/foremost.md), [`scalpel`](../examine-the-filesystem/scalpel.md), [`binwalk`](../examine-the-filesystem/binwalk.md), [`tcpxtract`](../examine-the-filesystem/tcpxtract.md), [`rafind2`](../examine-the-filesystem/rafind2.md), [`strings`](../examine-the-filesystem/strings.md), `grep`, [`xxd`](../examine-the-filesystem/xxd.md)
