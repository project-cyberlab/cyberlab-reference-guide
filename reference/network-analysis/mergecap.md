<!-- generated-by: scripts/generate_pages.py -->
# mergecap

| | |
|---|---|
| **Kit** | REMnux · Kali Linux · FLARE-VM · SIFT Workstation |
| **Capability** | Split, merge or repair capture files |
| **Version** | Mergecap (Wireshark) 4.0.17. |
| **Captured from** | `cyberlab-aio` via `--help` on 2026-08-10 — [raw help output](../../capture/cyberlab-aio/help/mergecap.help.txt) |
| **Documentation** | <https://www.wireshark.org> |

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Capture and analyze network traffic with this sniffer.

## When you'd reach for this

An analyst reaches for mergecap when merging multiple pcap files captured sequentially into a single file, often running it after capturing or before analysis to consolidate data; they choose it over append mode to maintain correct timestamps and avoid misordering packets, as demonstrated in the documentation.

**Sources:** <https://osqa-ask.wireshark.org/questions/31113/wireshark-merging-pcap-files/> · <https://osqa-ask.wireshark.org/questions/39951/how-to-simultaneously-filter-and-merge-several-pcap-files/> · <https://wiki.wireshark.org/Tools>

## Synopsis

```
mergecap [options] -w <outfile>|- <infile> [<infile> ...]
```

## Common invocations

```
# Merge multiple pcap files into a single capture file
mergecap *.pcap -w merged.pcapng
# Merge two network capture files into a single unified pcap file
mergecap -w compare.pcap a.pcap b-shifted.pcap
# Merge capture files into single output file
mergecap -a -w outoforder.pcap download-good.pcap
```

## Options

All 7 options parsed from the captured help text; 1 reviewed with usage guidance.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-a` | — | concatenate rather than merge files. default is to merge based on frame timestamps. | An analyst would use the -a flag when they need to concatenate input files in the order they are provided, without reordering packets based on timestamps. |
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
