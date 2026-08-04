<!-- generated-by: scripts/generate_pages.py -->
# pinfo.py

| | |
|---|---|
| **Kit** | Kali Linux · SIFT Workstation |
| **Capability** | Build a super-timeline from many artifact sources |
| **Version** | plaso - pinfo version 20260512 |
| **Captured from** | `cyberlab-aio` via `--help` on 2026-08-04 — [raw help output](../../capture/cyberlab-aio/help/pinfo.py.help.txt) |

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Shows information about a Plaso storage file, for example how it was collected, what information was extracted from a source, etc.

## Synopsis

```
pinfo.py [-h] [--troubles] [-V] [--logfile FILENAME]
[--process_memory_limit SIZE] [--compare STORAGE_FILE]
[--output_format FORMAT] [--hash TYPE] [--report TYPE]
[--sections SECTIONS_LIST] [-v] [-w OUTPUTFILE]
[PATH]
```

## Options

All 20 options parsed from the captured help text. The final column is filled in by review.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-h` | — | Show this help message and exit. |  |
| `--help` | — | Show this help message and exit. |  |
| `--troubles` | — | Show troubleshooting information. |  |
| `-V` | — | Show the version information. |  |
| `--version` | — | Show the version information. |  |
| `--logfile` | FILENAME | Path of the file in which to store log messages, by default this file will be named: "pinfo- YYYYMMDDThhmmss.log.gz". Note that the file will be gzip compressed if the extension is ".gz". |  |
| `--log_file` | FILENAME | Path of the file in which to store log messages, by default this file will be named: "pinfo- YYYYMMDDThhmmss.log.gz". Note that the file will be gzip compressed if the extension is ".gz". |  |
| `--log-file` | FILENAME | Path of the file in which to store log messages, by default this file will be named: "pinfo- YYYYMMDDThhmmss.log.gz". Note that the file will be gzip compressed if the extension is ".gz". |  |
| `--process_memory_limit` | SIZE | Maximum amount of memory (data segment) a process is allowed to allocate in bytes, where 0 represents no limit. The default limit is 4294967296 (4 GiB). This applies to both the main (foreman) process |  |
| `--process-memory-limit` | SIZE | Maximum amount of memory (data segment) a process is allowed to allocate in bytes, where 0 represents no limit. The default limit is 4294967296 (4 GiB). This applies to both the main (foreman) process |  |
| `--compare` | STORAGE_FILE | The path of the storage file to compare against. |  |
| `--output_format` | FORMAT | Format of the output, the default is: text. Supported options: json, markdown, text. |  |
| `--output-format` | FORMAT | Format of the output, the default is: text. Supported options: json, markdown, text. |  |
| `--hash` | TYPE | Type of hash to output in file_hashes report. Supported options: md5, sha1, sha256 |  |
| `--report` | TYPE | Report on specific information. Supported options: browser_search, chrome_extension, environment_variables, file_hashes, list, none, windows_services, winevt_providers |  |
| `--sections` | SECTIONS_LIST | List of sections to output. This is a comma separated list where each entry is the name of a section. Use " --sections list" to list the available sections and " --sections all" to show all available  |  |
| `-v` | — | Print verbose output. |  |
| `--verbose` | — | Print verbose output. |  |
| `-w` | OUTPUTFILE | Output filename. |  |
| `--write` | OUTPUTFILE | Output filename. |  |

## Gotchas

_TODO: operational traps._

## See also

[`log2timeline.py`](../build-the-timeline/log2timeline.py.md), [`psort.py`](../build-the-timeline/psort.py.md)
