<!-- generated-by: scripts/generate_pages.py -->
# nmap

| | |
|---|---|
| **Kit** | Kali Linux · FLARE-VM |
| **Capability** | Probe or scan hosts and services |
| **Version** | Nmap version 7.93 |
| **Captured from** | `cyberlab-aio` via `--help` on 2026-08-09 — [raw help output](../../capture/cyberlab-aio/help/nmap.help.txt) |

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Discover hosts, ports and services, and fingerprint what is listening.

## Synopsis

```
nmap [Scan Type(s)] [Options] {target specification}
```

## Options

All 66 options parsed from the captured help text; 26 reviewed with usage guidance.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `--exclude` | host1[,host2][,host3] | Exclude hosts/networks | Skip these hosts. The safety flag: use it for anything fragile before starting a range scan. |
| `--excludefile` | exclude_file | Exclude list from file | Skip the hosts listed in a file. |
| `--dns-servers` | serv1[,serv2] | Specify custom DNS servers |  |
| `--system-dns` | — | Use OS's DNS resolver |  |
| `--traceroute` | — | Trace hop path to each host | Trace the path to each host. |
| `--scanflags` | flags | Customize TCP scan flags |  |
| `-b` | FTP relay host | FTP bounce scan |  |
| `-p` | port ranges | Only scan specified ports Ex: -p22; -p1-65535; -p U:53,111,137,T:21-25,80,139,8080,S:9 | Which ports. `-p-` is all 65535 and takes far longer than people expect. |
| `--exclude-ports` | port ranges | Exclude the specified ports from scanning |  |
| `-F` | — | Fast mode - Scan fewer ports than the default scan | Fast scan of the top 100 ports. |
| `-r` | — | Scan ports sequentially - don't randomize |  |
| `--top-ports` | number | Scan <number> most common ports | Scan the N most common ports — the usual time/coverage compromise. |
| `--port-ratio` | ratio | Scan ports more common than <ratio> |  |
| `--version-intensity` | level | Set from 0 (light) to 9 (try all probes) | How hard `-sV` tries, 0 to 9. |
| `--version-light` | — | Limit to most likely probes (intensity 2) | Intensity 2 — much faster, misses more. |
| `--version-all` | — | Try every single probe (intensity 9) | Intensity 9. |
| `--version-trace` | — | Show detailed version scan activity (for debugging) |  |
| `--script` | Lua scripts | <Lua scripts> is a comma separated list of directories, script-files or script-categories | Run NSE scripts. The category matters — `vuln` and `exploit` scripts actively test, and `exploit` can change the target. |
| `--script-args` | n1=v1,[n2=v2,...] | provide arguments to scripts | Arguments for those scripts. |
| `--script-args-file` | filename | provide NSE script args in a file | An analyst would use the --script-args-file flag when they need to specify multiple script arguments in a file rather than on the command line, allowing for easier management of complex or repeated argument sets. |
| `--script-trace` | — | Show all data sent and received |  |
| `--script-updatedb` | — | Update the script database. | An analyst would use the --script-updatedb flag when they have added, removed, or modified the categories of NSE scripts in the default scripts directory, requiring the script database to be updated. |
| `--script-help` | Lua scripts | Show help about scripts. <Lua scripts> is a comma-separated list of script-files or script-categories. | Explain what a script does before running it, which is worth doing for anything outside `safe`. |
| `-O` | — | Enable OS detection | OS fingerprint from the TCP/IP stack. A guess with a confidence, not a fact. |
| `--osscan-limit` | — | Limit OS detection to promising targets |  |
| `--osscan-guess` | — | Guess OS more aggressively | Report near matches rather than staying silent. |
| `-T` | 0-5 | Set timing template (higher is faster) | Timing template 0-5. `-T4` is the usual choice on a LAN; `-T0` and `-T1` exist for evading rate-based detection and take hours. |
| `--min-hostgroup` | — | Parallel host scan group sizes |  |
| `--min-parallelism` | — | Probe parallelization |  |
| `--min-rtt-timeout` | — | Specifies probe round trip time. |  |
| `--max-retries` | tries | Caps number of port scan probe retransmissions. | Cap retransmissions on a lossy link. |
| `--host-timeout` | time | Give up on target after this long | Give up on a host after this long, so one dead host cannot stall a range. |
| `--min-rate` | number | Send packets no slower than <number> per second |  |
| `--max-rate` | number | Send packets no faster than <number> per second |  |
| `-f` | — | fragment packets (optionally w/given MTU) |  |
| `--mtu` | val | fragment packets (optionally w/given MTU) |  |
| `-D` | decoy1,decoy2[,ME] | Cloak a scan with decoys | Decoy scan. |
| `-S` | IP_Address | Spoof source address | Spoof the source address. |
| `-e` | iface | Use specified interface | Choose the interface to scan from. |
| `--proxies` | url1,[url2] | Relay connections through HTTP/SOCKS4 proxies |  |
| `--data` | hex string | Append a custom payload to sent packets |  |
| `--data-string` | string | Append a custom ASCII string to sent packets |  |
| `--data-length` | num | Append random data to sent packets |  |
| `--ip-options` | options | Send packets with specified ip options |  |
| `--ttl` | val | Set IP time-to-live field |  |
| `--spoof-mac` | mac address | Spoof your MAC address |  |
| `--badsum` | — | Send packets with a bogus TCP/UDP/SCTP checksum |  |
| `-v` | — | Increase verbosity level (use -vv or more for greater effect) | Verbose; repeat for more. |
| `-d` | — | Increase debugging level (use -dd or more for greater effect) |  |
| `--reason` | — | Display the reason a port is in a particular state |  |
| `--open` | — | Only show open (or possibly open) ports | Show only open ports, cutting the closed-port noise. |
| `--packet-trace` | — | Show all packets sent and received |  |
| `--iflist` | — | Print host interfaces and routes (for debugging) |  |
| `--append-output` | — | Append to rather than clobber specified output files |  |
| `--resume` | filename | Resume an aborted scan |  |
| `--noninteractive` | — | Disable runtime interactions via keyboard |  |
| `--stylesheet` | path | XSL stylesheet to transform XML output to HTML |  |
| `--webxml` | — | Reference stylesheet from Nmap.Org for more portable XML |  |
| `--no-stylesheet` | — | Prevent associating of XSL stylesheet w/XML output |  |
| `-6` | — | Enable IPv6 scanning | Scan IPv6. Hosts frequently expose more on v6 than v4 because the firewall rules were never mirrored. |
| `-A` | — | Enable OS detection, version detection, script scanning, and traceroute | Aggressive: version, OS, scripts and traceroute together. Convenient and unmistakably noisy. |
| `--datadir` | dirname | Specify custom Nmap data file location |  |
| `--privileged` | — | Assume that the user is fully privileged |  |
| `--unprivileged` | — | Assume the user lacks raw socket privileges |  |
| `-V` | — | Print version number |  |
| `-h` | — | Print this help summary page. |  |

## Gotchas

- Scanning is not passive. `-sV` and NSE talk to services properly, `--script exploit` may change the target, and everything here is recorded by anything watching. Have authorisation before running it, and use `--exclude` for hosts that must not be touched.
- `-p-` on a /24 is a very different job from the default scan. Scope the ports before scoping the hosts.
- A closed port and a filtered port are different findings. 'Filtered' means something dropped the probe, which is information about the network rather than about the host.

## See also

[`nping`](../network-analysis/nping.md), [`arp-scan`](../network-analysis/arp-scan.md)
