<!-- generated-by: scripts/generate_pages.py -->
# tshark

**Kit:** REMnux · Kali Linux · FLARE-VM · SIFT Workstation  **Capability:** Capture live network traffic; Read and filter packet captures
**Captured:** `cyberlab-aio` via `--help` on 2026-08-01  [raw](../../capture/cyberlab-aio/help/tshark.help.txt)  **Docs:** <https://www.wireshark.org>

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Read, filter and dissect network captures from the command line.

## Synopsis

```
tshark [options] ...
```

## Common invocations

<!-- candidates mined from cyberlab; verify each flag against the options table below before treating as reviewed -->
```
# from cyberlab 07-network-pcap
tshark --version | head -n 1
# from cyberlab 07-network-pcap
tshark -r exercise/sample.pcap -q -z io,phs | head -n 30
# from cyberlab 07-network-pcap
tshark -r exercise/sample.pcap -Y 'http.request' -T fields -e ip.dst -e http.host -e http.request.uri
# from cyberlab 07-network-pcap
tshark -r exercise/sample.pcap -Y 'dns.flags.response == 0' -T fields -e dns.qry.name | sort -u
# from cyberlab 07-network-pcap
tshark -r exercise/sample.pcap -Y 'http.request' -T fields -e http.host -e http.request.uri
# from cyberlab 24-wireshark-deep
tshark -r exercise/sample.pcap -c 20
# from cyberlab 24-wireshark-deep
tshark -r exercise/sample.pcap -Y "dns.flags.response == 0" -T fields -e dns.qry.name
# from cyberlab 24-wireshark-deep
tshark -r exercise/sample.pcap -Y "http.request" -T fields -e http.host -e http.request.uri
```

## Options

All 75 options parsed from the captured help text; 12 reviewed with usage guidance.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-i` | interface | name or idx of interface (def: first non-loopback) | Capture live from an interface instead of reading a file. |
| `--interface` | interface | name or idx of interface (def: first non-loopback) |  |
| `-f` | capture filter | packet filter in libpcap filter syntax | Apply a *capture* filter (BPF syntax) before packets are stored. |
| `-s` | snaplen | packet snapshot length (def: appropriate maximum) |  |
| `--snapshot-length` | snaplen | packet snapshot length (def: appropriate maximum) |  |
| `-p` | — | don't capture in promiscuous mode |  |
| `--no-promiscuous-mode` | — | don't capture in promiscuous mode |  |
| `-I` | — | capture in monitor mode, if available |  |
| `--monitor-mode` | — | capture in monitor mode, if available |  |
| `-B` | buffer size | size of kernel buffer (def: 2MB) |  |
| `--buffer-size` | buffer size | size of kernel buffer (def: 2MB) |  |
| `-y` | link type | link layer type (def: first appropriate) |  |
| `--linktype` | link type | link layer type (def: first appropriate) |  |
| `-D` | — | print list of interfaces and exit |  |
| `--list-interfaces` | — | print list of interfaces and exit |  |
| `-L` | — | print list of link-layer types of iface and exit |  |
| `--list-data-link-types` | — | print list of link-layer types of iface and exit |  |
| `--list-time-stamp-types` | — | print list of timestamp types for iface and exit |  |
| `-c` | packet count | stop after n packets (def: infinite) | Stop after N packets — a fast way to sample a huge capture. |
| `-a` | autostop cond. | duration:NUM - stop after NUM seconds filesize:NUM - stop this file after NUM KB files:NUM - stop after NUM files packets:NUM - stop after NUM packets |  |
| `--autostop` | autostop cond. | duration:NUM - stop after NUM seconds filesize:NUM - stop this file after NUM KB files:NUM - stop after NUM files packets:NUM - stop after NUM packets |  |
| `-b` | ringbuffer opt. | duration:NUM - switch to next file after NUM secs filesize:NUM - switch to next file after NUM KB files:NUM - ringbuffer: replace after NUM files packets:NUM - switch to next file after NUM packets in |  |
| `--ring-buffer` | ringbuffer opt. | duration:NUM - switch to next file after NUM secs filesize:NUM - switch to next file after NUM KB files:NUM - ringbuffer: replace after NUM files packets:NUM - switch to next file after NUM packets in |  |
| `-r` | infile | set the filename to read from (or '-' for stdin) | Read from a capture file — the normal forensic mode. |
| `--read-file` | infile | set the filename to read from (or '-' for stdin) |  |
| `-2` | — | perform a two-pass analysis | Two-pass analysis, so fields needing later context resolve. |
| `-M` | packet count | perform session auto reset |  |
| `-R` | read filter | packet Read filter in Wireshark display filter syntax (requires -2) |  |
| `--read-filter` | read filter | packet Read filter in Wireshark display filter syntax (requires -2) |  |
| `-Y` | display filter | packet displaY filter in Wireshark display filter syntax | Apply a *display* filter (Wireshark syntax) after dissection. |
| `--display-filter` | display filter | packet displaY filter in Wireshark display filter syntax |  |
| `-n` | — | disable all name resolutions (def: "mNd" enabled, or as set in preferences) | Disable name resolution. Also stops DNS lookups leaking from an evidence host — use it by default on an investigation. |
| `-N` | name resolve flags | enable specific name resolution(s): "mnNtdv" |  |
| `-H` | hosts file | read a list of entries from a hosts file, which will then be written to a capture file. (Implies -W n) |  |
| `--enable-protocol` | proto_name | enable dissection of proto_name |  |
| `--disable-protocol` | proto_name | disable dissection of proto_name |  |
| `--enable-heuristic` | short_name | enable dissection of heuristic protocol |  |
| `--disable-heuristic` | short_name | disable dissection of heuristic protocol |  |
| `-w` | outfile\|- | write packets to a pcapng-format file named "outfile" (or '-' for stdout) | Write the (filtered) packets to a new capture file. |
| `--capture-comment` | comment | add a capture file comment, if supported |  |
| `-C` | config profile | start with specified configuration profile |  |
| `-F` | output file type | set the output file type, default is pcapng an empty "-F" option will list the file types |  |
| `-V` | — | add output of packet tree (Packet Details) |  |
| `-O` | protocols | Only show packet details of these protocols, comma separated |  |
| `-P` | — | print packet summary even when writing to a file |  |
| `--print` | — | print packet summary even when writing to a file |  |
| `-S` | separator | the line separator to print between packets |  |
| `-x` | — | add output of hex and ASCII dump (Packet Bytes) | Hex and ASCII dump of packet contents. |
| `--hexdump` | hexoption | add hexdump, set options for data source and ASCII dump all dump all data sources (-x default) frames dump only frame data source ascii include ASCII dump text (-x default) delimit delimit ASCII dump  |  |
| `-j` | protocolfilter | protocols layers filter if -T ek\|pdml\|json selected (e.g. "ip ip.flags text", filter does not expand child nodes, unless child is specified also in the filter) |  |
| `-J` | protocolfilter | top level protocol filter if -T ek\|pdml\|json selected (e.g. "http tcp", filter which expands all child nodes) |  |
| `-e` | field | field to print if -Tfields selected (e.g. tcp.port, _ws.col.Info) this option can be repeated to print multiple fields | With `-T fields`, name each field to print. Repeatable. |
| `-l` | — | flush standard output after each packet |  |
| `-q` | — | be more quiet on stdout (e.g. when using statistics) | Suppress per-packet output, for use with `-z` statistics. |
| `-Q` | — | only log true errors to stderr (quieter than -q) |  |
| `-g` | — | enable group read access on the output file(s) |  |
| `-W` | n | Save extra information in the file, if supported. n = write network address resolution information |  |
| `-U` | tap_name | PDUs export mode, see the man page for details |  |
| `-z` | statistics | various statistics, see the man page for details | Run a statistics tap (conversations, endpoints, protocol tree). |
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

- **`-f` and `-Y` are different languages.** `-f` is BPF and applies at capture time; `-Y` is the Wireshark display filter and applies to a file. Passing display syntax to `-f` fails, sometimes silently.
- Name resolution is on by default and will emit DNS queries from the analysis host. Use `-n` when touching evidence.
- `-T fields` prints nothing useful without at least one `-e`.

## See also

[`dumpcap`](../acquire-preserve/dumpcap.md), [`capinfos`](../network-analysis/capinfos.md), [`ngrep`](../network-analysis/ngrep.md), [`tcpflow`](../network-analysis/tcpflow.md)
