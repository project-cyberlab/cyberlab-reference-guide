<!-- generated-by: scripts/generate_pages.py -->
# ngrep

| | |
|---|---|
| **Kit** | REMnux · SIFT Workstation |
| **Capability** | Read and filter packet captures |
| **Version** | V1.47.1 |
| **Captured from** | `cyberlab-aio` via `--help` on 2026-08-05 — [raw help output](../../capture/cyberlab-aio/help/ngrep.help.txt) |
| **Documentation** | <https://github.com/jpr5/ngrep/> |

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Grep packet payloads, live or from a capture, with BPF filtering — pattern matching on the wire.

## When you'd reach for this

An analyst reaches for ngrep when searching for specific patterns in network traffic, such as detecting "login" in Telnet sessions, using switches like -w, -i, and -t for precise matching and timestamps; they may run it alongside tcpdump to analyze captured packets, preferring it over tcpdump for its grep-style filtering and intuitive regular expression handling.

**Sources:** <https://www.admin-magazine.com/Articles/Network-Grep>

## Synopsis

```
ngrep <-hNXViwqpevxlDtTRM> <-IO pcap_dump> <-n num> <-d dev> <-A num>
<-s snaplen> <-S limitlen> <-W normal|byline|single|none> <-c cols>
<-P char> <-F file>             <-K count>
<match expression> <bpf filter>
```

## Common invocations

```
# Monitor SMTP traffic across all network interfaces
ngrep -d any port 25
# Monitor HTTP traffic with line-based packet display on port 80
ngrep -W byline port 80
# Search PCAP for specific string occurrences in packets
ngrep -w 'm' -I /tmp/dns.dump
# Search DNS dump for ns3 entries with timestamps and replay packets
ngrep -tD ns3 -I /tmp/dns.dump
# Search network dump for traffic on specific port
ngrep -I /tmp/dns.dump port 80
# Monitor network syslog traffic for error occurrences
ngrep -d any 'error' port syslog
```

## Options

All 29 options parsed from the captured help text; 27 reviewed with usage guidance.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-h` | — | is help/usage |  |
| `-V` | — | is version information |  |
| `-q` | — | is be quiet (don't print packet reception hash marks) | Suppress the reception hash marks. |
| `-e` | — | is show empty packets | Show empty packets, which are otherwise hidden. |
| `-i` | — | is ignore case | Case-insensitive match — usually what you want for protocol keywords and hostnames. |
| `-v` | — | is invert match | Invert the match, to see everything that is *not* the known traffic. |
| `-R` | — | is don't do privilege revocation logic | Skip privilege revocation. |
| `-x` | — | is print in alternate hexdump format | Print payloads as a hexdump — necessary when the protocol is not text. |
| `-X` | — | is interpret match expression as hexadecimal | Treat the pattern as hexadecimal, for matching binary signatures rather than text. |
| `-w` | — | is word-regex (expression must match as a word) | Match the pattern as a whole word, to stop a short string matching inside longer ones. |
| `-p` | — | is don't go into promiscuous mode | Do not enter promiscuous mode — capture only traffic addressed to this host. |
| `-l` | — | is make stdout line buffered | Line-buffer stdout, so output appears when piped. |
| `-D` | — | is replay pcap_dumps with their recorded time intervals | Replay a pcap at its recorded timing rather than as fast as possible. |
| `-t` | — | is print timestamp every time a packet is matched | Print a timestamp on every match. |
| `-T` | — | is print delta timestamp every time a packet is matched specify twice for delta from first match | Print the delta since the previous match; twice for delta from the first. Useful for spotting beaconing intervals. |
| `-M` | — | is don't do multi-line match (do single-line match instead) | Single-line matching instead of multi-line. |
| `-I` | — | is read packet stream from pcap format file pcap_dump | Read from a pcap file instead of an interface. The safe mode: no capture privileges and no risk of touching live traffic. |
| `-O` | — | is dump matched packets in pcap format to pcap_dump | Write matched packets to a pcap, turning a search into a smaller capture that Wireshark can open. |
| `-n` | — | is look at only num packets | Stop after N packets. |
| `-A` | — | is dump num packets after a match | Also print N packets following each match, for the response to the request that matched. |
| `-s` | — | is set the bpf caplen | Set the BPF capture length. |
| `-S` | — | is set the limitlen on matched packets | Limit how much of a matched packet is shown. |
| `-W` | — | is set the dump format (normal, byline, single, none) | Output format: `byline` is far more readable for text protocols than the default. |
| `-c` | — | is force the column width to the specified size | Force the column width. |
| `-P` | — | is set the non-printable display char to what is specified | Set the character shown for non-printable bytes. |
| `-F` | — | is read the bpf filter from the specified file | Read the BPF filter from a file, when it is too long to be comfortable on a command line. |
| `-N` | — | is show sub protocol number | Show sub-protocol numbers. |
| `-d` | — | is use specified device instead of the pcap default | Choose the capture interface rather than the pcap default. |
| `-K` | — | is send N packets to kill observed connections | Send packets to kill matched connections. This **writes to the network** — it is not an analysis option, and it does not belong anywhere near evidence handling. |

## Gotchas

- It matches within individual packets. A string split across TCP segments will not be found — reassembly is [`tshark`](../acquire-preserve/tshark.md)'s job, not this one's.
- `-K` is the one flag here that changes the world instead of observing it. Everything else reads; that one transmits.
- Matching payload on a live interface needs capture privileges, and on a busy link `ngrep` drops packets silently. Capture first, search the file afterwards, when the answer has to be complete.

## See also

[`tshark`](../acquire-preserve/tshark.md), [`capinfos`](../network-analysis/capinfos.md), [`tcpflow`](../network-analysis/tcpflow.md)
