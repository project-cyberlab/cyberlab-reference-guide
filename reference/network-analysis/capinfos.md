<!-- generated-by: scripts/generate_pages.py -->
# capinfos

| | |
|---|---|
| **Kit** | REMnux · Kali Linux · FLARE-VM · SIFT Workstation |
| **Capability** | Read and filter packet captures |
| **Version** | Capinfos (Wireshark) 4.0.17. |
| **Captured from** | `cyberlab-aio` via `--help` on 2026-08-08 — [raw help output](../../capture/cyberlab-aio/help/capinfos.help.txt) |
| **Documentation** | <https://www.wireshark.org> |

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Capture and analyze network traffic with this sniffer.

## Synopsis

```
capinfos [options] <infile> ...
```

## Common invocations

```
# Generate tab-delimited report with pcap file metadata
capinfos -TtEc *.pcap
# Check duplicate packets in capture file
capinfos -c dupes.pcap
# Check capture file for duplicate packets
capinfos -c nodups.pcap
# Generate detailed capture file analysis report
capinfos mycapture.pcap
# Generate tabular report of capture file details
capinfos -T mycapture.pcap
# Generate tab report with pcap file metadata
capinfos -T -t -E -c *.pcap
```

## Options

All 4 options parsed from the captured help text. The final column is filled in by review.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-h` | — | display this help and exit |  |
| `--help` | — | display this help and exit |  |
| `-v` | — | display version info and exit |  |
| `--version` | — | display version info and exit |  |

## Gotchas

_TODO: operational traps._

## See also

[`tshark`](../acquire-preserve/tshark.md), [`ngrep`](../network-analysis/ngrep.md), [`tcpflow`](../network-analysis/tcpflow.md)
