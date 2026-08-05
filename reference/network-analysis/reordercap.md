<!-- generated-by: scripts/generate_pages.py -->
# reordercap

| | |
|---|---|
| **Kit** | REMnux · Kali Linux · FLARE-VM · SIFT Workstation |
| **Capability** | Split, merge or repair capture files |
| **Version** | Reordercap (Wireshark) 4.0.17. |
| **Captured from** | `cyberlab-aio` via `--help` on 2026-08-05 — [raw help output](../../capture/cyberlab-aio/help/reordercap.help.txt) |
| **Documentation** | <https://www.wireshark.org> |

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Capture and analyze network traffic with this sniffer.

## When you'd reach for this

An analyst uses reordercap when packets in a capture file are out of chronological order, running it after capturing or extracting the file to reorder packets by timestamp; they avoid using the same input and output file to prevent malformation, and prefer it over manual sorting or other tools because it automatically detects file formats and compression.

**Sources:** <https://manpages.debian.org/testing/wireshark-common/reordercap.1.en.html> · <https://tshark.dev/edit/reordercap/>

## Synopsis

```
reordercap [options] <infile> <outfile>
```

## Options

All 3 options parsed from the captured help text; 1 reviewed with usage guidance.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-n` | — | don't write to output file if the input file is ordered. | An analyst would use the -n flag when verifying if a pcap file is already in chronological order to avoid unnecessary processing and output file creation. |
| `-h` | — | display this help and exit. |  |
| `-v` | — | print version information and exit. |  |

## Gotchas

_TODO: operational traps._

## See also

[`editcap`](../network-analysis/editcap.md), [`mergecap`](../network-analysis/mergecap.md)
