<!-- generated-by: scripts/generate_pages.py -->
# tshark

| | |
|---|---|
| **Kit** | REMnux · Kali Linux · FLARE-VM · SIFT Workstation |
| **Capability** | Capture live network traffic; Read and filter packet captures |
| **Captured from** | `cyberlab-aio` via `--help` on 2026-08-02 — [raw help output](../../capture/cyberlab-aio/help/tshark.help.txt) |
| **Documentation** | <https://www.wireshark.org> |

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Wireshark's command line: capture, filter, dissect and export packet data, including fields for a timeline.

## Synopsis

```
tshark [options] ...
```

## Options

All 75 options parsed from the captured help text; 19 reviewed with usage guidance.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-i` | interface | name or idx of interface (def: first non-loopback) | Capture live from an interface instead. Needs capture rights, and on a busy link a live dissect will drop packets. |
| `--interface` | interface | name or idx of interface (def: first non-loopback) | Capture live from an interface instead. Needs capture rights, and on a busy link a live dissect will drop packets. |
| `-f` | capture filter | packet filter in libpcap filter syntax | **Capture** filter, in BPF syntax. Applied before packets are written, so what it drops is gone forever. |
| `-s` | snaplen | packet snapshot length (def: appropriate maximum) | Snapshot length; truncates each packet as it is captured. |
| `--snapshot-length` | snaplen | packet snapshot length (def: appropriate maximum) | Snapshot length; truncates each packet as it is captured. |
| `-p` | — | don't capture in promiscuous mode | Do not enter promiscuous mode. |
| `--no-promiscuous-mode` | — | don't capture in promiscuous mode | Do not enter promiscuous mode. |
| `-I` | — | capture in monitor mode, if available | Monitor mode, for capturing 802.11 management frames. |
| `--monitor-mode` | — | capture in monitor mode, if available | Monitor mode, for capturing 802.11 management frames. |
| `-B` | buffer size | size of kernel buffer (def: 2MB) | Kernel buffer size. Raise it when a fast link is dropping packets at capture time. |
| `--buffer-size` | buffer size | size of kernel buffer (def: 2MB) | Kernel buffer size. Raise it when a fast link is dropping packets at capture time. |
| `-y` | link type | link layer type (def: first appropriate) | Force the link-layer type. |
| `--linktype` | link type | link layer type (def: first appropriate) | Force the link-layer type. |
| `-D` | — | print list of interfaces and exit | List interfaces and exit — how you find the right `-i` value. |
| `--list-interfaces` | — | print list of interfaces and exit | List interfaces and exit — how you find the right `-i` value. |
| `-L` | — | print list of link-layer types of iface and exit | List the link-layer types an interface supports. |
| `--list-data-link-types` | — | print list of link-layer types of iface and exit | List the link-layer types an interface supports. |
| `--list-time-stamp-types` | — | print list of timestamp types for iface and exit |  |
| `-c` | packet count | stop after n packets (def: infinite) | Stop after N packets — the fast way to sample a huge file before committing to a full pass. |
| `-a` | autostop cond | duration:NUM - stop after NUM seconds filesize:NUM - stop this file after NUM KB files:NUM - stop after NUM files packets:NUM - stop after NUM packets | Autostop condition for a live capture: duration, filesize or file count. |
| `--autostop` | autostop cond | duration:NUM - stop after NUM seconds filesize:NUM - stop this file after NUM KB files:NUM - stop after NUM files packets:NUM - stop after NUM packets | Autostop condition for a live capture: duration, filesize or file count. |
| `-b` | ringbuffer opt | duration:NUM - switch to next file after NUM secs filesize:NUM - switch to next file after NUM KB files:NUM - ringbuffer: replace after NUM files packets:NUM - switch to next file after NUM packets in | Ring buffer: roll to a new file on time or size, so a long capture cannot fill the disk. |
| `--ring-buffer` | ringbuffer opt | duration:NUM - switch to next file after NUM secs filesize:NUM - switch to next file after NUM KB files:NUM - ringbuffer: replace after NUM files packets:NUM - switch to next file after NUM packets in | Ring buffer: roll to a new file on time or size, so a long capture cannot fill the disk. |
| `-r` | infile | set the filename to read from (or '-' for stdin) | Read a capture file. The safe default — analysis needs no privileges and cannot disturb the wire. |
| `--read-file` | infile | set the filename to read from (or '-' for stdin) | Read a capture file. The safe default — analysis needs no privileges and cannot disturb the wire. |
| `-2` | — | perform a two-pass analysis | Two-pass analysis, so fields that depend on later packets — reassembly, response times, stream indexes — are populated. |
| `-M` | packet count | perform session auto reset | Reset dissector state every N packets, to bound memory on a very long capture. |
| `-R` | read filter | packet Read filter in Wireshark display filter syntax (requires -2) | Read filter, which needs `-2`. Prefer `-Y` unless you know why you want this one. |
| `--read-filter` | read filter | packet Read filter in Wireshark display filter syntax (requires -2) | Read filter, which needs `-2`. Prefer `-Y` unless you know why you want this one. |
| `-Y` | display filter | packet displaY filter in Wireshark display filter syntax | **Display** filter, in Wireshark syntax. Applied after capture, so nothing is lost and it can be changed later. Confusing these two is the classic tshark mistake. |
| `--display-filter` | display filter | packet displaY filter in Wireshark display filter syntax | **Display** filter, in Wireshark syntax. Applied after capture, so nothing is lost and it can be changed later. Confusing these two is the classic tshark mistake. |
| `-n` | — | disable all name resolutions (def: "mNd" enabled, or as set in preferences) |  |
| `-N` | name resolve flags | enable specific name resolution(s): "mnNtdv" |  |
| `-H` | hosts file | read a list of entries from a hosts file, which will then be written to a capture file. (Implies -W n) |  |
| `--enable-protocol` | proto_name | enable dissection of proto_name |  |
| `--disable-protocol` | proto_name | disable dissection of proto_name |  |
| `--enable-heuristic` | short_name | enable dissection of heuristic protocol |  |
| `--disable-heuristic` | short_name | disable dissection of heuristic protocol |  |
| `-w` | outfile\|- | write packets to a pcapng-format file named "outfile" (or '-' for stdout) | Write packets out rather than dissecting them, which is much faster when you only want a filtered subset. |
| `--capture-comment` | comment | add a capture file comment, if supported |  |
| `-C` | config profile | start with specified configuration profile |  |
| `-F` | output file type | set the output file type, default is pcapng an empty "-F" option will list the file types |  |
| `-V` | — | add output of packet tree (Packet Details) |  |
| `-O` | protocols | Only show packet details of these protocols, comma separated |  |
| `-P` | — | print packet summary even when writing to a file |  |
| `--print` | — | print packet summary even when writing to a file |  |
| `-S` | separator | the line separator to print between packets |  |
| `-x` | — | add output of hex and ASCII dump (Packet Bytes) |  |
| `--hexdump` | hexoption | add hexdump, set options for data source and ASCII dump all dump all data sources (-x default) frames dump only frame data source ascii include ASCII dump text (-x default) delimit delimit ASCII dump  |  |
| `-j` | protocolfilter | protocols layers filter if -T ek\|pdml\|json selected (e.g. "ip ip.flags text", filter does not expand child nodes, unless child is specified also in the filter) |  |
| `-J` | protocolfilter | top level protocol filter if -T ek\|pdml\|json selected (e.g. "http tcp", filter which expands all child nodes) |  |
| `-e` | field | field to print if -Tfields selected (e.g. tcp.port, _ws.col.Info) this option can be repeated to print multiple fields | Which field to print, repeatable. Only meaningful with `-T fields`, and the ordering is the column ordering. |
| `-l` | — | flush standard output after each packet |  |
| `-q` | — | be more quiet on stdout (e.g. when using statistics) |  |
| `-Q` | — | only log true errors to stderr (quieter than -q) |  |
| `-g` | — | enable group read access on the output file(s) |  |
| `-W` | n | Save extra information in the file, if supported. n = write network address resolution information |  |
| `-U` | tap_name | PDUs export mode, see the man page for details |  |
| `-z` | statistics | various statistics, see the man page for details |  |
| `--export-tls-session-keys` | keyfile | export TLS Session Keys to a file named "keyfile" |  |
| `--color` | — | color output text similarly to the Wireshark GUI, requires a terminal with 24-bit color support Also supplies color attributes to pdml and psml formats (Note that attributes are nonstandard) |  |
| `--no-duplicate-keys` | — | If -T json is specified, merge duplicate keys in an object into a single key with as value a json array containing all values |  |
| `--temp-dir` | directory | write temporary files to this directory (default: /tmp) |  |
| `--log-level` | level | sets the active log level ("critical", "warning", etc.) |  |
| `--log-fatal` | level | sets level to abort the program ("critical" or "warning") |  |
| `--log-domains` | [!]list | comma separated list of the active log domains |  |
| `--log-debug` | [!]list | comma separated list of domains with "debug" level |  |
| `--log-noisy` | [!]list | comma separated list of domains with "noisy" level |  |
| `--log-file` | path | file to output messages to (in addition to stderr) |  |
| `-h` | — | display this help and exit |  |
| `--help` | — | display this help and exit |  |
| `-v` | — | display version info and exit |  |
| `--version` | — | display version info and exit |  |
| `-K` | keytab | keytab file to use for kerberos decryption |  |
| `-G` | report | dump one of several available reports and exit default report="fields" use "-G help" for more help |  |

## Gotchas

- Capture filters (`-f`) and display filters (`-Y`) use **different syntaxes** and apply at different times. `-f` discards packets permanently; `-Y` only hides them. Reaching for the wrong one is the most common way to destroy evidence with this tool.
- Dissecting live on a busy link drops packets silently. Capture to a file first, analyse afterwards, whenever completeness matters.
- `-T fields` prints nothing useful without `-e`. It is not an error, just empty output, which reads like the filter matched nothing.

## See also

[`dumpcap`](../acquire-preserve/dumpcap.md), [`capinfos`](../network-analysis/capinfos.md), [`ngrep`](../network-analysis/ngrep.md), [`tcpflow`](../network-analysis/tcpflow.md)
