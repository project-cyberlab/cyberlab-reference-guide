<!-- generated-by: scripts/generate_pages.py -->
# dumpcap

| | |
|---|---|
| **Kit** | REMnux · Kali Linux · FLARE-VM · SIFT Workstation |
| **Capability** | Capture live network traffic |
| **Captured from** | `cyberlab-aio` via `--help` on 2026-08-07 — [raw help output](../../capture/cyberlab-aio/help/dumpcap.help.txt) |
| **Documentation** | <https://www.wireshark.org> |

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Capture packets to a file. It does nothing else — which is the point.

## Synopsis

```
dumpcap [options] ...
```

## Options

All 48 options parsed from the captured help text; 20 reviewed with usage guidance.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-i` | interface | name or idx of interface (def: first non-loopback), or for remote capturing, use one of these formats: rpcap://<host>/<interface> TCP@<host>:<port> | Interface to capture from. `-D` lists what is available. |
| `--interface` | interface | name or idx of interface (def: first non-loopback), or for remote capturing, use one of these formats: rpcap://<host>/<interface> TCP@<host>:<port> | Interface to capture from. `-D` lists what is available. |
| `--ifname` | name | name to use in the capture file for a pipe from which we're capturing |  |
| `--ifdescr` | description | description to use in the capture file for a pipe from which we're capturing |  |
| `-f` | capture filter | packet filter in libpcap filter syntax | Capture filter in BPF syntax. Applied before writing, so anything it excludes is gone permanently. |
| `-s` | snaplen | packet snapshot length (def: appropriate maximum) | Snapshot length: truncate each packet. Headers only, when payload must not be recorded. |
| `--snapshot-length` | snaplen | packet snapshot length (def: appropriate maximum) | Snapshot length: truncate each packet. Headers only, when payload must not be recorded. |
| `-p` | — | don't capture in promiscuous mode | Do not enter promiscuous mode — only traffic for this host. |
| `--no-promiscuous-mode` | — | don't capture in promiscuous mode | Do not enter promiscuous mode — only traffic for this host. |
| `-I` | — | capture in monitor mode, if available | Monitor mode, for 802.11 management and control frames. |
| `--monitor-mode` | — | capture in monitor mode, if available | Monitor mode, for 802.11 management and control frames. |
| `-B` | buffer size | size of kernel buffer in MiB (def: 2MiB) | Kernel buffer size in MiB. Raise it first when a fast link reports drops; the default is small for modern traffic. |
| `--buffer-size` | buffer size | size of kernel buffer in MiB (def: 2MiB) | Kernel buffer size in MiB. Raise it first when a fast link reports drops; the default is small for modern traffic. |
| `-y` | link type | link layer type (def: first appropriate) | Force the link-layer type. |
| `--linktype` | link type | link layer type (def: first appropriate) | Force the link-layer type. |
| `-D` | — | print list of interfaces and exit | List interfaces and exit. |
| `--list-interfaces` | — | print list of interfaces and exit | List interfaces and exit. |
| `-L` | — | print list of link-layer types of iface and exit | List link-layer types for the chosen interface. |
| `--list-data-link-types` | — | print list of link-layer types of iface and exit | List link-layer types for the chosen interface. |
| `--list-time-stamp-types` | — | print list of timestamp types for iface and exit |  |
| `-d` | — | print generated BPF code for capture filter | Print the compiled BPF for a filter, to check it means what you think before capturing hours of the wrong thing. |
| `-S` | — | print statistics for each interface once per second | Print per-interface packet statistics once a second, for confirming traffic is arriving before committing to a long capture. |
| `-M` | — | for -D, -L, and -S, produce machine-readable output | Machine-readable output for `-D`, `-L` and `-S`. |
| `-c` | packet count | stop after n packets (def: infinite) | Stop after N packets. |
| `-a` | autostop cond | duration:NUM - stop after NUM seconds filesize:NUM - stop this file after NUM kB files:NUM - stop after NUM files packets:NUM - stop after NUM packets | Autostop condition — duration, filesize or files. |
| `--autostop` | autostop cond | duration:NUM - stop after NUM seconds filesize:NUM - stop this file after NUM kB files:NUM - stop after NUM files packets:NUM - stop after NUM packets | An analyst would use the --autostop flag when they need to automatically halt packet capture after a specified duration, upon reaching a certain number of files, or when a capture file reaches a defined size limit. |
| `-w` | filename | name of file to save (def: tempfile) | Output file. Without it, dumpcap writes to a temporary file and tells you where, which is rarely what you meant. |
| `-g` | — | enable group read access on the output file(s) |  |
| `-b` | ringbuffer opt | duration:NUM - switch to next file after NUM secs filesize:NUM - switch to next file after NUM kB files:NUM - ringbuffer: replace after NUM files packets:NUM - ringbuffer: replace after NUM packets in | Ring buffer: roll to a new file on duration, filesize or count. The difference between a capture that runs overnight and one that fills the disk at 3am. |
| `--ring-buffer` | ringbuffer opt | duration:NUM - switch to next file after NUM secs filesize:NUM - switch to next file after NUM kB files:NUM - ringbuffer: replace after NUM files packets:NUM - ringbuffer: replace after NUM packets in | Ring buffer: roll to a new file on duration, filesize or count. The difference between a capture that runs overnight and one that fills the disk at 3am. |
| `-n` | — | use pcapng format instead of pcap (default) | pcapng output (the default). |
| `-P` | — | use libpcap format instead of pcapng | Legacy pcap output, for a tool that cannot read pcapng. |
| `--capture-comment` | comment | add a capture comment to the output file (only for pcapng) |  |
| `--temp-dir` | directory | write temporary files to this directory (default: /tmp) |  |
| `--log-level` | level | sets the active log level ("critical", "warning", etc.) |  |
| `--log-fatal` | level | sets level to abort the program ("critical" or "warning") |  |
| `--log-domains` | [!]list | comma separated list of the active log domains |  |
| `--log-debug` | [!]list | comma separated list of domains with "debug" level |  |
| `--log-noisy` | [!]list | comma separated list of domains with "noisy" level |  |
| `--log-file` | path | file to output messages to (in addition to stderr) |  |
| `-N` | packet_limit | maximum number of packets buffered within dumpcap |  |
| `-C` | byte_limit | maximum number of bytes used for buffering packets within dumpcap |  |
| `-t` | — | use a separate thread per interface |  |
| `-q` | — | don't report packet capture counts | Quiet — no packet-count updates. |
| `-v` | — | print version information and exit |  |
| `--version` | — | print version information and exit |  |
| `-h` | — | display this help and exit |  |
| `--help` | — | display this help and exit |  |

## Gotchas

- This is deliberately minimal: it captures and it does not dissect. That is why it is the right thing to run as the privileged process and why [`tshark`](tshark.md) shells out to it — the analysis code never needs the capture privilege.
- Filtering here is destructive. A capture filter that was slightly wrong cannot be widened afterwards; capture broadly and filter at analysis time whenever the disk allows it.
- Drops are reported at the end, not during. Check the count before treating a capture as complete — a busy link with the default buffer loses packets silently.

## See also

[`tshark`](../acquire-preserve/tshark.md)
