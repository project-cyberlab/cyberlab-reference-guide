<!-- generated-by: scripts/generate_pages.py -->
# ngrep

**Kit:** REMnux · SIFT Workstation  **Capability:** Read and filter packet captures  **Version:** V1.47.1
**Captured:** `cyberlab-aio` via `--help` on 2026-07-29  [raw](../../capture/cyberlab-aio/help/ngrep.help.txt)  **Docs:** <https://github.com/jpr5/ngrep/>

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Look for patterns in network traffic.

## Synopsis

```
ngrep <-hNXViwqpevxlDtTRM> <-IO pcap_dump> <-n num> <-d dev> <-A num>
<-s snaplen> <-S limitlen> <-W normal|byline|single|none> <-c cols>
<-P char> <-F file>             <-K count>
<match expression> <bpf filter>
```

## Common invocations

<!-- candidates mined from cyberlab; verify each flag against the options table below before treating as reviewed -->
```
# from cyberlab 07-network-pcap
ngrep -V 2>&1 | head -n 1
# from cyberlab 07-network-pcap
ngrep -I exercise/sample.pcap -q -W byline 'User-Agent'
# from cyberlab 07-network-pcap
ngrep -I exercise/sample.pcap -q -W byline 'User-Agent' | grep -i 'User-Agent'
# from cyberlab 24-wireshark-deep
ngrep -I exercise/sample.pcap -q -W byline "User-Agent"
# from cyberlab 24-wireshark-deep
ngrep -I exercise/sample.pcap -q -W byline "User-Agent" | grep -i "User-Agent"
```

## Options

All 29 options parsed from the captured help text. The final column is filled in by review.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-h` | — | is help/usage |  |
| `-V` | — | is version information |  |
| `-q` | — | is be quiet (don't print packet reception hash marks) |  |
| `-e` | — | is show empty packets |  |
| `-i` | — | is ignore case |  |
| `-v` | — | is invert match |  |
| `-R` | — | is don't do privilege revocation logic |  |
| `-x` | — | is print in alternate hexdump format |  |
| `-X` | — | is interpret match expression as hexadecimal |  |
| `-w` | — | is word-regex (expression must match as a word) |  |
| `-p` | — | is don't go into promiscuous mode |  |
| `-l` | — | is make stdout line buffered |  |
| `-D` | — | is replay pcap_dumps with their recorded time intervals |  |
| `-t` | — | is print timestamp every time a packet is matched |  |
| `-T` | — | is print delta timestamp every time a packet is matched specify twice for delta from first match |  |
| `-M` | — | is don't do multi-line match (do single-line match instead) |  |
| `-I` | — | is read packet stream from pcap format file pcap_dump |  |
| `-O` | — | is dump matched packets in pcap format to pcap_dump |  |
| `-n` | — | is look at only num packets |  |
| `-A` | — | is dump num packets after a match |  |
| `-s` | — | is set the bpf caplen |  |
| `-S` | — | is set the limitlen on matched packets |  |
| `-W` | — | is set the dump format (normal, byline, single, none) |  |
| `-c` | — | is force the column width to the specified size |  |
| `-P` | — | is set the non-printable display char to what is specified |  |
| `-F` | — | is read the bpf filter from the specified file |  |
| `-N` | — | is show sub protocol number |  |
| `-d` | — | is use specified device instead of the pcap default |  |
| `-K` | — | is send N packets to kill observed connections |  |

## Gotchas

_TODO: operational traps._

## See also

[`tshark`](../acquire-preserve/tshark.md), [`capinfos`](../network-analysis/capinfos.md), [`tcpflow`](../network-analysis/tcpflow.md)
