<!-- generated-by: scripts/generate_pages.py -->
# tcpxtract

| | |
|---|---|
| **Kit** | REMnux · SIFT Workstation |
| **Capability** | Carve files out of unstructured data; Extract files and payloads from traffic |
| **Version** | tcpxtract v1.0.1 |
| **Captured from** | `cyberlab-aio` via `--help` on 2026-08-08 — [raw help output](../../capture/cyberlab-aio/help/tcpxtract.help.txt) |
| **Documentation** | <http://tcpxtract.sourceforge.net/> |

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Carve files out of network traffic by signature, without understanding the protocol that carried them. Useful when a transfer is not something a dissector recognises and you only need the payload.

## When you'd reach for this

When an analyst needs to extract files from network traffic, they use tcpxtract on pcap capture files or live traffic, as it supports 26 file formats and allows custom configurations via its config file. They may run it after capturing traffic with tools that generate pcap files, preferring it over similar tools due to its flexibility in adding new formats and reliance on file signatures for accurate extraction.

**Sources:** <https://www.freshports.org/net/tcpxtract/>

## Synopsis

```
tcpxtract [OPTIONS] [[-d <DEVICE>] [-f <FILE>]]
```

## Options

All 12 options parsed from the captured help text; 1 reviewed with usage guidance.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `--file` | FILE | to specify an input capture file instead of a device |  |
| `-f` | FILE | to specify an input capture file instead of a device |  |
| `--device` | DEVICE | to specify an input device (i.e. eth0) |  |
| `-d` | DEVICE | to specify an input device (i.e. eth0) |  |
| `--config` | FILE | use FILE as the config file |  |
| `-c` | FILE | use FILE as the config file |  |
| `--output` | DIRECTORY | dump files to DIRECTORY instead of current directory | An analyst would use the -o flag when performing a live capture from a network interface to specify the output directory for extracted files. |
| `-o` | DIRECTORY | dump files to DIRECTORY instead of current directory | An analyst would use the -o flag when performing a live capture from a network interface to specify the output directory for extracted files. |
| `--version` | — | display the version number of this program |  |
| `-v` | — | display the version number of this program |  |
| `--help` | — | display this lovely screen |  |
| `-h` | — | display this lovely screen |  |

## Gotchas

_TODO: operational traps._

## See also

[`foremost`](../examine-the-filesystem/foremost.md), [`scalpel`](../examine-the-filesystem/scalpel.md), [`binwalk`](../examine-the-filesystem/binwalk.md), [`bulk_extractor`](../examine-the-filesystem/bulk_extractor.md), [`tcpflow`](../network-analysis/tcpflow.md)
