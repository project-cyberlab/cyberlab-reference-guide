<!-- generated-by: scripts/generate_pages.py -->
# nmap

**Kit:** Kali Linux · FLARE-VM  **Capability:** Probe or scan hosts and services  **Version:** Nmap version 7.93
**Captured:** `cyberlab-aio` via `--help` on 2026-07-29  [raw](../../capture/cyberlab-aio/help/nmap.help.txt)

## Purpose

Nmap 7.93 ( https://nmap.org )

## Synopsis

```
nmap [Scan Type(s)] [Options] {target specification}
```

## Common invocations

<!-- candidates mined from cyberlab; verify each flag against the options table below before treating as reviewed -->
```
# from cyberlab 11-offensive-kali
nmap --version
# from cyberlab 11-offensive-kali
nmap -sT -Pn -p 1-1024 127.0.0.1
# from cyberlab 26-metasploit-workflow
nmap -sV -Pn -p 1-1000 -oN scan.txt "$TARGET"
# from cyberlab 26-metasploit-workflow
nmap -sV -Pn -oX scan.xml "$TARGET"
# from cyberlab 41-web-app-testing
nmap -sV -p 80,443,8080 "$TARGET"
# from cyberlab 41-web-app-testing
nmap -p 80,443 --script http-title,http-headers,http-server-header "$TARGET"
# from cyberlab 41-web-app-testing
nmap -p 8000 --script http-title 127.0.0.1
```

## Options

All 60 options parsed from the captured help text. The final column is filled in by review.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `--exclude` | host1 | Exclude hosts/networks |  |
| `--excludefile` | exclude_file | Exclude list from file |  |
| `--dns-servers` | serv1 | Specify custom DNS servers |  |
| `--system-dns` | — | Use OS's DNS resolver |  |
| `--traceroute` | — | Trace hop path to each host |  |
| `--scanflags` | flags | Customize TCP scan flags |  |
| `-b` | FTP relay host | FTP bounce scan |  |
| `-p` | port ranges | Only scan specified ports Ex: -p22; -p1-65535; -p U:53,111,137,T:21-25,80,139,8080,S:9 |  |
| `--exclude-ports` | port ranges | Exclude the specified ports from scanning |  |
| `-F` | — | Fast mode - Scan fewer ports than the default scan |  |
| `-r` | — | Scan ports sequentially - don't randomize |  |
| `--top-ports` | number | Scan <number> most common ports |  |
| `--port-ratio` | ratio | Scan ports more common than <ratio> |  |
| `--version-intensity` | level | Set from 0 (light) to 9 (try all probes) |  |
| `--version-light` | — | Limit to most likely probes (intensity 2) |  |
| `--version-all` | — | Try every single probe (intensity 9) |  |
| `--version-trace` | — | Show detailed version scan activity (for debugging) |  |
| `--script` | Lua scripts | <Lua scripts> is a comma separated list of directories, script-files or script-categories |  |
| `--script-args` | n1=v1 | provide arguments to scripts |  |
| `--script-args-file` | filename | provide NSE script args in a file |  |
| `--script-trace` | — | Show all data sent and received |  |
| `--script-updatedb` | — | Update the script database. |  |
| `--script-help` | Lua scripts | Show help about scripts. <Lua scripts> is a comma-separated list of script-files or script-categories. |  |
| `-O` | — | Enable OS detection |  |
| `--osscan-limit` | — | Limit OS detection to promising targets |  |
| `--osscan-guess` | — | Guess OS more aggressively |  |
| `--max-retries` | tries | Caps number of port scan probe retransmissions. |  |
| `--host-timeout` | time | Give up on target after this long |  |
| `--min-rate` | number | Send packets no slower than <number> per second |  |
| `--max-rate` | number | Send packets no faster than <number> per second |  |
| `-D` | decoy1 | Cloak a scan with decoys |  |
| `-S` | IP_Address | Spoof source address |  |
| `-e` | iface | Use specified interface |  |
| `--proxies` | url1 | Relay connections through HTTP/SOCKS4 proxies |  |
| `--data` | hex string | Append a custom payload to sent packets |  |
| `--data-string` | string | Append a custom ASCII string to sent packets |  |
| `--data-length` | num | Append random data to sent packets |  |
| `--ip-options` | options | Send packets with specified ip options |  |
| `--ttl` | val | Set IP time-to-live field |  |
| `--spoof-mac` | mac address/prefix/vendor name | Spoof your MAC address |  |
| `--badsum` | — | Send packets with a bogus TCP/UDP/SCTP checksum |  |
| `-v` | — | Increase verbosity level (use -vv or more for greater effect) |  |
| `-d` | — | Increase debugging level (use -dd or more for greater effect) |  |
| `--reason` | — | Display the reason a port is in a particular state |  |
| `--open` | — | Only show open (or possibly open) ports |  |
| `--packet-trace` | — | Show all packets sent and received |  |
| `--iflist` | — | Print host interfaces and routes (for debugging) |  |
| `--append-output` | — | Append to rather than clobber specified output files |  |
| `--resume` | filename | Resume an aborted scan |  |
| `--noninteractive` | — | Disable runtime interactions via keyboard |  |
| `--stylesheet` | path/URL | XSL stylesheet to transform XML output to HTML |  |
| `--webxml` | — | Reference stylesheet from Nmap.Org for more portable XML |  |
| `--no-stylesheet` | — | Prevent associating of XSL stylesheet w/XML output |  |
| `-6` | — | Enable IPv6 scanning |  |
| `-A` | — | Enable OS detection, version detection, script scanning, and traceroute |  |
| `--datadir` | dirname | Specify custom Nmap data file location |  |
| `--privileged` | — | Assume that the user is fully privileged |  |
| `--unprivileged` | — | Assume the user lacks raw socket privileges |  |
| `-V` | — | Print version number |  |
| `-h` | — | Print this help summary page. |  |

## Gotchas

_TODO: operational traps._

## See also

`nping`
