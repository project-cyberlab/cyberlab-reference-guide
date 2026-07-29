<!-- generated-by: scripts/generate_pages.py -->
# dumpcap

**Kit:** REMnux · Kali Linux · FLARE-VM · SIFT Workstation  **Capability:** Capture live network traffic
**Captured:** `cyberlab-aio` via `--help` on 2026-07-29  [raw](../../capture/cyberlab-aio/help/dumpcap.help.txt)  **Docs:** <https://www.wireshark.org>

## Purpose

Capture and analyze network traffic with this sniffer.

## Synopsis

```
dumpcap [options] ...
```

## Common invocations

_TODO: up to 8 task-titled invocations._

## Options

All 44 options parsed from the captured help text. The final column is filled in by review.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-i` | interface | name or idx of interface (def: first non-loopback), or for remote capturing, use one of these formats: rpcap://<host>/<interface> TCP@<host>:<port> |  |
| `--interface` | interface | name or idx of interface (def: first non-loopback), or for remote capturing, use one of these formats: rpcap://<host>/<interface> TCP@<host>:<port> |  |
| `--ifname` | name | name to use in the capture file for a pipe from which we're capturing |  |
| `--ifdescr` | description | description to use in the capture file for a pipe from which we're capturing |  |
| `-f` | capture filter | packet filter in libpcap filter syntax |  |
| `-s` | snaplen | packet snapshot length (def: appropriate maximum) |  |
| `--snapshot-length` | snaplen | packet snapshot length (def: appropriate maximum) |  |
| `-p` | — | don't capture in promiscuous mode |  |
| `--no-promiscuous-mode` | — | don't capture in promiscuous mode |  |
| `-I` | — | capture in monitor mode, if available |  |
| `--monitor-mode` | — | capture in monitor mode, if available |  |
| `-B` | buffer size | size of kernel buffer in MiB (def: 2MiB) |  |
| `--buffer-size` | buffer size | size of kernel buffer in MiB (def: 2MiB) |  |
| `-y` | link type | link layer type (def: first appropriate) |  |
| `--linktype` | link type | link layer type (def: first appropriate) |  |
| `-D` | — | print list of interfaces and exit |  |
| `--list-interfaces` | — | print list of interfaces and exit |  |
| `-L` | — | print list of link-layer types of iface and exit |  |
| `--list-data-link-types` | — | print list of link-layer types of iface and exit |  |
| `--list-time-stamp-types` | — | print list of timestamp types for iface and exit |  |
| `-d` | — | print generated BPF code for capture filter |  |
| `-S` | — | print statistics for each interface once per second |  |
| `-M` | — | for -D, -L, and -S, produce machine-readable output |  |
| `-c` | packet count | stop after n packets (def: infinite) |  |
| `-w` | filename | name of file to save (def: tempfile) |  |
| `-g` | — | enable group read access on the output file(s) |  |
| `-n` | — | use pcapng format instead of pcap (default) |  |
| `-P` | — | use libpcap format instead of pcapng |  |
| `--capture-comment` | comment | add a capture comment to the output file (only for pcapng) |  |
| `--temp-dir` | directory | write temporary files to this directory (default: /tmp) |  |
| `--log-level` | level | sets the active log level ("critical", "warning", etc.) |  |
| `--log-fatal` | level | sets level to abort the program ("critical" or "warning") |  |
| `--log-domains` | !]list | comma separated list of the active log domains |  |
| `--log-debug` | !]list | comma separated list of domains with "debug" level |  |
| `--log-noisy` | !]list | comma separated list of domains with "noisy" level |  |
| `--log-file` | path | file to output messages to (in addition to stderr) |  |
| `-N` | packet_limit | maximum number of packets buffered within dumpcap |  |
| `-C` | byte_limit | maximum number of bytes used for buffering packets within dumpcap |  |
| `-t` | — | use a separate thread per interface |  |
| `-q` | — | don't report packet capture counts |  |
| `-v` | — | print version information and exit |  |
| `--version` | — | print version information and exit |  |
| `-h` | — | display this help and exit |  |
| `--help` | — | display this help and exit |  |

## Gotchas

_TODO: operational traps._

## See also

`tshark`
