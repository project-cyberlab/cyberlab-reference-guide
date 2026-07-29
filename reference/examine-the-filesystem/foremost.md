<!-- generated-by: scripts/generate_pages.py -->
# foremost

**Kit:** Kali Linux · SIFT Workstation  **Capability:** Carve files out of unstructured data; Extract files and payloads from traffic  **Version:** 1.5.7
**Captured:** `cyberlab-aio` via `-h` on 2026-07-29  [raw](../../capture/cyberlab-aio/help/foremost.help.txt)

## Purpose

foremost version 1.5.7 by Jesse Kornblum, Kris Kendall, and Nick Mikus.

## Common invocations

<!-- candidates mined from cyberlab; verify each flag against the options table below before treating as reviewed -->
```
# from cyberlab 05-file-carving
foremost -V
# from cyberlab 05-file-carving
foremost -t jpg,pdf -i exercise/sample.dd -o /tmp/foremost_out
# from cyberlab 05-file-carving
foremost -t jpg,pdf -i exercise/sample.dd -o /tmp/ak_foremost
# from cyberlab 33-binwalk-firmware
foremost -i firmware.bin -o foremost_out
```

## Options

All 11 options parsed from the captured help text. The final column is the judgement layer and is filled in by review.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-V` | — | - display copyright information and exit | |
| `-t` | — | - specify file type. (-t jpeg,pdf ...) | |
| `-d` | — | - turn on indirect block detection (for UNIX file-systems) | |
| `-i` | — | - specify input file (default is stdin) | |
| `-a` | — | - Write all headers, perform no error detection (corrupted files) | |
| `-w` | — | - Only write the audit file, do not write any detected files to the disk | |
| `-o` | — | - set output directory (defaults to output) | |
| `-c` | — | - set configuration file to use (defaults to foremost.conf) | |
| `-q` | — | - enables quick mode. Search are performed on 512 byte boundaries. | |
| `-Q` | — | - enables quiet mode. Suppress output messages. | |
| `-v` | — | - verbose mode. Logs all messages to screen | |

## Gotchas

_TODO: operational traps._

## See also

`scalpel`, `binwalk`, `tcpxtract`, `tcpflow`
