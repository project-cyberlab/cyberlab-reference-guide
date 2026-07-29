<!-- generated-by: scripts/generate_pages.py -->
# tcpxtract

**Kit:** REMnux · SIFT Workstation  **Capability:** Carve files out of unstructured data; Extract files and payloads from traffic  **Version:** tcpxtract v1.0.1
**Captured:** `cyberlab-aio` via `--help` on 2026-07-29  [raw](../../capture/cyberlab-aio/help/tcpxtract.help.txt)  **Docs:** <http://tcpxtract.sourceforge.net/>

## Purpose

Extract files from network traffic.

## Synopsis

```
tcpxtract [OPTIONS] [[-d <DEVICE>] [-f <FILE>]]
```

## Common invocations

<!-- candidates mined from cyberlab; verify each flag against the options table below before treating as reviewed -->
```
# from cyberlab 05-file-carving
tcpxtract --version 2>&1 | head -n 1
# from cyberlab 05-file-carving
tcpxtract -f exercise/sample.pcap -o /tmp/tcpxtract_out
# from cyberlab 05-file-carving
tcpxtract -f exercise/sample.pcap -o /tmp/ak_tcp
```

## Options

All 12 options parsed from the captured help text. The final column is the judgement layer and is filled in by review.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `--file` | FILE | to specify an input capture file instead of a device | |
| `-f` | FILE | to specify an input capture file instead of a device | |
| `--device` | DEVICE | to specify an input device (i.e. eth0) | |
| `-d` | DEVICE | to specify an input device (i.e. eth0) | |
| `--config` | FILE | use FILE as the config file | |
| `-c` | FILE | use FILE as the config file | |
| `--output` | DIRECTORY | dump files to DIRECTORY instead of current directory | |
| `-o` | DIRECTORY | dump files to DIRECTORY instead of current directory | |
| `--version` | — | display the version number of this program | |
| `-v` | — | display the version number of this program | |
| `--help` | — | display this lovely screen | |
| `-h` | — | display this lovely screen | |

## Gotchas

_TODO: operational traps._

## See also

`foremost`, `scalpel`, `binwalk`, `tcpflow`
