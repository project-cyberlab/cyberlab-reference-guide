<!-- generated-by: scripts/generate_pages.py -->
# foremost

| | |
|---|---|
| **Kit** | Kali Linux · SIFT Workstation |
| **Capability** | Carve files out of unstructured data; Extract files and payloads from traffic |
| **Version** | 1.5.7 |
| **Captured from** | `cyberlab-aio` via `-h` on 2026-08-10 — [raw help output](../../capture/cyberlab-aio/help/foremost.help.txt) |

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Carve files out of an image or raw data by header and footer signatures.

## When you'd reach for this

An analyst reaches for foremost when recovering lost files from disk images or drives, using command line switches to specify built-in file types or configuration files for headers and footers; they may run it after creating an image with tools like dd, and choose it over similar tools due to its reliability and speed from using internal data structures of file formats.

**Sources:** <http://foremost.sourceforge.net/> · <https://www.kali.org/tools/foremost/>

## Common invocations

```
# Carve JPEGs, PDFs, DOCs, XLS from disk image
foremost -t doc,jpg,pdf,xls -i image.dd
```

## Options

All 11 options parsed from the captured help text; 8 reviewed with usage guidance.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-V` | — | - display copyright information and exit |  |
| `-t` | — | - specify file type. (-t jpeg,pdf ...) | Restrict carving to given types (`jpg`, `pdf`, `all`). Narrowing this is the difference between a usable result and 40,000 files. |
| `-d` | — | - turn on indirect block detection (for UNIX file-systems) |  |
| `-i` | — | - specify input file (default is stdin) | Input file or device to carve from. |
| `-a` | — | - Write all headers, perform no error detection (corrupted files) | Write all headers found, even without a valid footer. |
| `-w` | — | - Only write the audit file, do not write any detected files to the disk | Write the audit file only, carving nothing — a cheap dry run. |
| `-o` | — | - set output directory (defaults to output) | Output directory — must be empty or foremost refuses to run. |
| `-c` | — | - set configuration file to use (defaults to foremost.conf) | Use a custom configuration file to add signatures. |
| `-q` | — | - enables quick mode. Search are performed on 512 byte boundaries. | Quick mode: scan only sector boundaries. Much faster, misses embedded files. |
| `-Q` | — | - enables quiet mode. Suppress output messages. |  |
| `-v` | — | - verbose mode. Logs all messages to screen | Verbose output. |

## Gotchas

- Carving recovers content but **not filenames or timestamps** — those live in filesystem metadata that carving bypasses. Use [`tsk_recover`](tsk_recover.md) when the filesystem is intact and carve only what it cannot reach.
- The output directory must be empty; foremost aborts otherwise. This trips scripted reruns constantly.

## See also

[`scalpel`](../examine-the-filesystem/scalpel.md), [`binwalk`](../examine-the-filesystem/binwalk.md), [`bulk_extractor`](../examine-the-filesystem/bulk_extractor.md), [`tcpxtract`](../examine-the-filesystem/tcpxtract.md), [`tcpflow`](../network-analysis/tcpflow.md)
