<!-- generated-by: scripts/generate_pages.py -->
# editcap

| | |
|---|---|
| **Kit** | REMnux · Kali Linux · FLARE-VM · SIFT Workstation |
| **Capability** | Split, merge or repair capture files |
| **Version** | Editcap (Wireshark) 4.0.17. |
| **Captured from** | `cyberlab-aio` via `--help` on 2026-08-06 — [raw help output](../../capture/cyberlab-aio/help/editcap.help.txt) |
| **Documentation** | <https://www.wireshark.org> |

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Cut, split, deduplicate and convert capture files — the tool that makes an unmanageable pcap workable before analysis starts.

## When you'd reach for this

An analyst reaches for editcap when they need to remove duplicate packets or split a capture file into smaller segments, often running capinfos first to assess the file's structure, as it directly handles format editing and packet manipulation tasks that other tools like mergecap or tshark do not explicitly address.

**Sources:** <https://docsislab.wordpress.com/packet-capture/wireshark-command-line/> · <https://wiki.wireshark.org/Tools>

## Synopsis

```
editcap [options] ... <infile> <outfile> [ <packet#>[-<packet#>] ... ]
```

## Common invocations

```
# Remove duplicate packets from capture file
editcap -d dupes.pcap nodups.pcap
# Split capture into 200-packet segments
editcap -c 200 dbad.pcap dbadsplit.pcap
```

## Options

All 25 options parsed from the captured help text; 21 reviewed with usage guidance.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-r` | — | keep the selected packets; default is to delete them. | Invert the selection: keep the specified packets instead of deleting them. Easy to forget, and it reverses the meaning of the whole command. |
| `-A` | start time | only read packets whose timestamp is after (or equal to) the given time. | Keep only packets at or after this timestamp. |
| `-B` | stop time | only read packets whose timestamp is before the given time. Time format for -A/-B options is YYYY-MM-DDThh:mm:ss[.nnnnnnnnn][Z\|+-hh:mm] Unix epoch timestamps are also supported. | Keep only packets before this timestamp. With `-A`, this is how a multi-gigabyte capture becomes the incident window. |
| `--novlan` | — | remove vlan info from packets before checking for duplicates. | Ignore VLAN tags when comparing for duplicates, so the same frame seen on two VLANs collapses to one. |
| `-d` | — | remove packet if duplicate (window == 5). | Drop duplicate packets using the default 5-packet window. Captures taken from a SPAN port routinely see each packet twice, which distorts every count downstream. |
| `-D` | dup window | remove packet if duplicate; configurable <dup window>. Valid <dup window> values are 0 to 1000000. NOTE: A <dup window> of 0 with -V (verbose option) is useful to print MD5 hashes. | Drop duplicates with an explicit window, when `-d`'s default is too narrow. |
| `-w` | dup time window | remove packet if duplicate packet is found EQUAL TO OR LESS THAN <dup time window> prior to current packet. A <dup time window> is specified in relative seconds (e.g. 0.000001). NOTE: The use of the ' | Drop duplicates within a time window rather than a packet count. |
| `-s` | snaplen | truncate each packet to max. <snaplen> bytes of data. | Truncate each packet to N bytes. Strips payload while keeping headers — the usual way to share a capture without its contents. |
| `-L` | — | adjust the frame (i.e. reported) length when chopping and/or snapping. | Adjust the recorded frame length to match after truncating, so the file is not self-inconsistent. |
| `-t` | time adjustment | adjust the timestamp of each packet. <time adjustment> is in relative seconds (e.g. -0.5). | Shift every timestamp by a relative amount. This is how a capture from a host with a skewed clock is aligned to the rest of the timeline. |
| `-o` | change offset | When used in conjunction with -E, skip some bytes from the beginning of the packet. This allows one to preserve some bytes, in order to have some headers untouched. | With `-E`, skip bytes before introducing errors. |
| `--seed` | seed | When used in conjunction with -E, set the seed to use for the pseudo-random number generator. This allows one to repeat a particular sequence of errors. | With `-E`, fix the random seed so a corrupted-capture test is reproducible. |
| `-I` | bytes to ignore | ignore the specified number of bytes at the beginning of the frame during MD5 hash calculation, unless the frame is too short, then the full frame is used. Useful to remove duplicated packets taken on | Ignore N leading bytes when comparing for duplicates. |
| `-c` | packets per file | split the packet output to different files based on uniform packet counts with a maximum of <packets per file> each. | Split into files of N packets each. The standard fix for a capture too large for Wireshark to open. |
| `-i` | seconds per file | split the packet output to different files based on uniform time intervals with a maximum of <seconds per file> each. | Split into files covering N seconds each — the same fix, when time is the natural unit. |
| `-F` | capture type | set the output file type; default is pcapng. An empty "-F" option will list the file types. | Output file format; pcapng by default. An empty `-F` lists the choices. |
| `-T` | encap type | set the output file encapsulation type; default is the same as the input file. An empty "-T" option will list the encapsulation types. | Output encapsulation type, when the link type must change. |
| `--discard-all-secrets` | — | Discard all decryption secrets from the input file when writing the output file. Does not discard secrets added by "--inject-secrets" in the same command line. | Strip embedded decryption secrets before handing the file to someone else. |
| `--capture-comment` | comment | Add a capture file comment, if supported. | Attach a comment to the file — a place to record provenance that travels with the capture. |
| `--discard-capture-comment` | — | Discard capture file comments from the input file when writing the output file. Does not discard comments added by "--capture-comment" in the same command line. | Remove existing comments on output. |
| `-h` | — | display this help and exit. |  |
| `--help` | — | display this help and exit. |  |
| `-V` | — | verbose output. If -V is used with any of the 'Duplicate Packet Removal' options (-d, -D or -w) then Packet lengths and MD5 hashes are printed to standard-error. | Verbose; with the duplicate options it reports what was removed rather than silently dropping packets. |
| `-v` | — | print version information and exit. |  |
| `--version` | — | print version information and exit. |  |

## Gotchas

- `-r` inverts the selection. Without it the named packets are **deleted**, which is the opposite of what most people intend the first time.
- Deduplication is a heuristic over a window, not a proof. A genuine retransmission looks like a duplicate, and dropping it destroys the evidence that a retransmission occurred.
- Splitting renumbers packets per output file. Frame numbers cited from a split file do not refer to the original capture.

## See also

[`mergecap`](../network-analysis/mergecap.md), [`reordercap`](../network-analysis/reordercap.md)
