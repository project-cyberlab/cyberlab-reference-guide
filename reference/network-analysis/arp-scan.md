<!-- generated-by: scripts/generate_pages.py -->
# arp-scan

| | |
|---|---|
| **Kit** | SIFT Workstation |
| **Capability** | Probe or scan hosts and services |
| **Version** | arp-scan 1.10.0 |
| **Captured from** | `cyberlab-aio` via `--help` on 2026-08-11 — [raw help output](../../capture/cyberlab-aio/help/arp-scan.help.txt) |

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Target hosts must be specified on the command line unless the --file or

## When you'd reach for this

An analyst reaches for arp-scan when they need to verify the presence of a system with known IP and MAC addresses on a LAN, often running it first with a broadcast to determine the MAC address and then again targeting the specific MAC address for a quieter scan. They may use it after identifying a host via broadcast or before confirming its presence without alerting other network stations, as targeting a specific MAC avoids broadcasting to all devices.

**Sources:** <https://github.com/royhills/arp-scan/wiki/arp-scan-User-Guide>

## Synopsis

```
arp-scan [options] [hosts...]
```

## Options

_No option definitions could be parsed from this tool's help output. It may be subcommand-driven or have no flags; needs manual review._

## Gotchas

_TODO: operational traps._

## See also

[`nmap`](../network-analysis/nmap.md), [`nping`](../network-analysis/nping.md)
