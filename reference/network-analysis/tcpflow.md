<!-- generated-by: scripts/generate_pages.py -->
# tcpflow

| | |
|---|---|
| **Kit** | REMnux · Kali Linux · SIFT Workstation |
| **Capability** | Read and filter packet captures; Extract files and payloads from traffic |
| **Version** | TCPFLOW 1.6.1 |
| **Captured from** | `cyberlab-aio` via `--help` on 2026-08-05 — [raw help output](../../capture/cyberlab-aio/help/tcpflow.help.txt) |
| **Documentation** | <https://downloads.digitalcorpora.org/downloads/tcpflow/> |

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Reassemble TCP streams from a capture and write each conversation to its own file. Where a packet tool shows you frames, this gives you the bytes each side actually sent, in order — which is what you need to read a protocol or recover a transferred file.

## Synopsis

```
tcpflow [-aBcCDhIpsvVZ] [-b max_bytes] [-d debug_level]
[-[eE] scanner] [-f max_fds] [-F[ctTXMkmg]] [-h|--help] [-i iface]
[-l files...] [-L semlock] [-m min_bytes] [-o outdir] [-r file] [-R file]
[-S name=value] [-T template] [-U|--relinquish-privileges user] [-v|--verbose]
[-w file] [-x scanner] [-X xmlfile] [-z|--chroot dir] [expression]
```

## Options

All 33 options parsed from the captured help text. The final column is filled in by review.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-a` | — | do ALL post-processing. |  |
| `-b` | max_bytes | max number of bytes per flow to save |  |
| `-d` | debug_level | debug level; default is 1 |  |
| `-f` | — | maximum number of file descriptors to use |  |
| `-h` | — | print this help message (-hh for more help) |  |
| `-H` | — | print detailed information about each scanner |  |
| `-i` | — | network interface on which to listen |  |
| `-I` | — | write for each flow another file *.findx to provide byte-indexed timestamps |  |
| `-g` | — | output each flow in alternating colors (note change!) |  |
| `-l` | — | treat non-flag arguments as input files rather than a pcap expression |  |
| `-L` | — | semlock - specifies that writes are locked using a named semaphore |  |
| `-p` | — | don't use promiscuous mode |  |
| `-q` | — | quiet mode - do not print warnings |  |
| `-r` | file | read packets from tcpdump pcap file (may be repeated) |  |
| `-R` | file | read packets from tcpdump pcap file TO FINISH CONNECTIONS |  |
| `-v` | — | verbose operation equivalent to -d 10 |  |
| `-V` | — | print version number and exit |  |
| `-w` | — | file : write packets not processed to file |  |
| `-o` | — | outdir : specify output directory (default '.') |  |
| `-X` | — | filename : DFXML output to filename |  |
| `-m` | — | bytes : specifies skip that starts a new stream (default 16777216). |  |
| `-Z` | — | do not decompress gzip-compressed HTTP transactions |  |
| `-K` | — | output\|keep pcap flow structure. |  |
| `-U` | user | relinquish privleges and become user (if running as root) |  |
| `-z` | dir | chroot to dir (requires that -U be used). |  |
| `-E` | scanner | - turn off all scanners except scanner |  |
| `-B` | — | binary output, even with -c or -C (normally -c or -C turn it off) |  |
| `-c` | — | console print only (don't create files) |  |
| `-C` | — | console print only, but without the display of source/dest header |  |
| `-0` | — | don't print newlines after packets when printing to console |  |
| `-s` | — | strip non-printable characters (change to '.') |  |
| `-J` | — | output json format. |  |
| `-D` | — | output in hex (useful to combine with -c or -C) |  |

## Gotchas

_TODO: operational traps._

## See also

[`tshark`](../acquire-preserve/tshark.md), [`capinfos`](../network-analysis/capinfos.md), [`ngrep`](../network-analysis/ngrep.md), [`tcpxtract`](../examine-the-filesystem/tcpxtract.md), [`foremost`](../examine-the-filesystem/foremost.md)
