<!-- generated-by: scripts/generate_pages.py -->
# editcap

**Kit:** REMnux · Kali Linux · FLARE-VM · SIFT Workstation  **Capability:** Split, merge or repair capture files  **Version:** Git v4.0.17
**Captured:** `cyberlab-aio` via `--help` on 2026-07-29  [raw](../../capture/cyberlab-aio/help/editcap.help.txt)  **Docs:** <https://www.wireshark.org>

## Purpose

Capture and analyze network traffic with this sniffer.

## Synopsis

```
editcap [options] ... <infile> <outfile> [ <packet#>[-<packet#>] ... ]
```

## Common invocations

_TODO: up to 8 task-titled invocations._

## Options

All 25 options parsed from the captured help text. The final column is the judgement layer and is filled in by review.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-r` | — | keep the selected packets; default is to delete them. | |
| `-A` | start time | only read packets whose timestamp is after (or equal to) the given time. | |
| `-B` | stop time | only read packets whose timestamp is before the given time. Time format for -A/-B options is YYYY-MM-DDThh:mm:ss[.nnnnnnnnn][Z\|+-hh:mm] Unix epoch timestamps are also supported. | |
| `--novlan` | — | remove vlan info from packets before checking for duplicates. | |
| `-d` | — | remove packet if duplicate (window == 5). | |
| `-D` | dup window | remove packet if duplicate; configurable <dup window>. Valid <dup window> values are 0 to 1000000. NOTE: A <dup window> of 0 with -V (verbose option) is useful to print MD5 hashes. | |
| `-w` | dup time window | remove packet if duplicate packet is found EQUAL TO OR LESS THAN <dup time window> prior to current packet. A <dup time window> is specified in relative seconds (e.g. 0.000001). NOTE: The use of the ' | |
| `-s` | snaplen | truncate each packet to max. <snaplen> bytes of data. | |
| `-L` | — | adjust the frame (i.e. reported) length when chopping and/or snapping. | |
| `-t` | time adjustment | adjust the timestamp of each packet. <time adjustment> is in relative seconds (e.g. -0.5). | |
| `-o` | change offset | When used in conjunction with -E, skip some bytes from the beginning of the packet. This allows one to preserve some bytes, in order to have some headers untouched. | |
| `--seed` | seed | When used in conjunction with -E, set the seed to use for the pseudo-random number generator. This allows one to repeat a particular sequence of errors. | |
| `-I` | bytes to ignore | ignore the specified number of bytes at the beginning of the frame during MD5 hash calculation, unless the frame is too short, then the full frame is used. Useful to remove duplicated packets taken on | |
| `-c` | packets per file | split the packet output to different files based on uniform packet counts with a maximum of <packets per file> each. | |
| `-i` | seconds per file | split the packet output to different files based on uniform time intervals with a maximum of <seconds per file> each. | |
| `-F` | capture type | set the output file type; default is pcapng. An empty "-F" option will list the file types. | |
| `-T` | encap type | set the output file encapsulation type; default is the same as the input file. An empty "-T" option will list the encapsulation types. | |
| `--discard-all-secrets` | — | Discard all decryption secrets from the input file when writing the output file. Does not discard secrets added by "--inject-secrets" in the same command line. | |
| `--capture-comment` | comment | Add a capture file comment, if supported. | |
| `--discard-capture-comment` | — | Discard capture file comments from the input file when writing the output file. Does not discard comments added by "--capture-comment" in the same command line. | |
| `-h` | — | display this help and exit. | |
| `--help` | — | display this help and exit. | |
| `-V` | — | verbose output. If -V is used with any of the 'Duplicate Packet Removal' options (-d, -D or -w) then Packet lengths and MD5 hashes are printed to standard-error. | |
| `-v` | — | print version information and exit. | |
| `--version` | — | print version information and exit. | |

## Gotchas

_TODO: operational traps._

## See also

`mergecap`, `reordercap`
