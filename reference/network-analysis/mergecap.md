<!-- generated-by: scripts/generate_pages.py -->
# mergecap

**Kit:** REMnux · Kali Linux · FLARE-VM · SIFT Workstation  **Capability:** Split, merge or repair capture files  **Version:** Git v4.0.17
**Captured:** `cyberlab-aio` via `--help` on 2026-08-01  [raw](../../capture/cyberlab-aio/help/mergecap.help.txt)  **Docs:** <https://www.wireshark.org>

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Capture and analyze network traffic with this sniffer.

## Synopsis

```
mergecap [options] -w <outfile>|- <infile> [<infile> ...]
```

## Common invocations

_TODO: up to 8 task-titled invocations._

## Options

All 7 options parsed from the captured help text. The final column is filled in by review.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-a` | — | concatenate rather than merge files. default is to merge based on frame timestamps. |  |
| `-s` | snaplen | truncate packets to <snaplen> bytes of data. |  |
| `-h` | — | display this help and exit. |  |
| `--help` | — | display this help and exit. |  |
| `-V` | — | verbose output. |  |
| `-v` | — | print version information and exit. |  |
| `--version` | — | print version information and exit. |  |

## Gotchas

_TODO: operational traps._

## See also

[`editcap`](../network-analysis/editcap.md), [`reordercap`](../network-analysis/reordercap.md)
