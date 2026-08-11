<!-- generated-by: scripts/generate_pages.py -->
# nping

| | |
|---|---|
| **Kit** | Kali Linux · FLARE-VM |
| **Capability** | Probe or scan hosts and services |
| **Captured from** | `cyberlab-aio` via `--help` on 2026-08-11 — [raw help output](../../capture/cyberlab-aio/help/nping.help.txt) |

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Craft and send arbitrary network packets, and report what comes back. Unlike `ping` it will build TCP, UDP, ICMP or raw ARP probes with chosen flags and payloads, which makes it the tool for asking a firewall or an IDS a precise question about what it permits.

## When you'd reach for this

An analyst reaches for nping when they need to send custom network packets for testing or forensic analysis, such as probing specific ports or crafting ICMP requests, often after identifying a target range or before verifying network behavior. They may choose it over similar tools due to its detailed target specification options, support for CIDR and octet ranges, and flexibility in packet crafting, as demonstrated in the examples and documentation.

**Sources:** <https://nmap.org/book/nping-man.html>

## Synopsis

```
nping [Probe mode] [Options] {target specification}
```

## Common invocations

```
# Test host reachability and open ports
nping scanme.nmap.org
# Test target port responsiveness with two rounds
nping --tcp -c 2 1.1.1.1 -p 100-102
# Testing network connectivity via echo server
nping --echo-server "public" -e wlan0 -vvv
# Test network host with custom TCP packet parameters
nping --tcp -p 80 --flags rst --ttl 2 192.168.1.1
# Send ICMP time-exceeded packets to test network path
nping --icmp --icmp-type time --delay 500ms 192.168.254.254
# Test TCP port responsiveness across multiple hosts with delays
nping --tcp -c 1 --delay 500ms 1.1.1.1 2.2.2.2 3.3.3.3 -p 137-139
```

## Options

All 85 options parsed from the captured help text; 3 reviewed with usage guidance.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `--tcp-connect` | — | Unprivileged TCP connect probe mode. |  |
| `--tcp` | — | TCP probe mode. | An analyst would use the --tcp flag when sending TCP packets to specific ports as part of network testing or scanning, such as in the example where it is used with --flags rst to send a reset packet to port 80. |
| `--udp` | — | UDP probe mode. |  |
| `--icmp` | — | ICMP probe mode. |  |
| `--arp` | — | ARP/RARP probe mode. |  |
| `--tr` | — | Traceroute mode (can only be used with TCP/UDP/ICMP modes). |  |
| `--traceroute` | — | Traceroute mode (can only be used with TCP/UDP/ICMP modes). |  |
| `-p` | port spec | Set destination port(s). | An analyst would use the -p flag when testing specific TCP ports on a target host, such as checking if a web server is listening on port 80. |
| `--dest-port` | port spec | Set destination port(s). | An analyst would use the --dest-port flag when testing connectivity to a specific service on a target host, such as verifying HTTPS availability on port 443. |
| `-g` | portnumber | Try to use a custom source port. |  |
| `--source-port` | portnumber | Try to use a custom source port. |  |
| `--seq` | seqnumber | Set sequence number. |  |
| `--flags` | flag list | Set TCP flags (ACK,PSH,RST,SYN,FIN...) |  |
| `--ack` | acknumber | Set ACK number. |  |
| `--win` | size | Set window size. |  |
| `--badsum` | — | Use a random invalid checksum. |  |
| `--icmp-type` | type | ICMP type. |  |
| `--icmp-code` | code | ICMP code. |  |
| `--icmp-id` | id | Set identifier. |  |
| `--icmp-seq` | n | Set sequence number. |  |
| `--icmp-redirect-addr` | addr | Set redirect address. |  |
| `--icmp-param-pointer` | pnt | Set parameter problem pointer. |  |
| `--icmp-advert-lifetime` | time | Set router advertisement lifetime. |  |
| `--icmp-advert-entry` | IP,pref | Add router advertisement entry. |  |
| `--icmp-orig-time` | — | <timestamp> : Set originate timestamp. |  |
| `--icmp-recv-time` | — | <timestamp> : Set receive timestamp. |  |
| `--icmp-trans-time` | timestamp | Set transmit timestamp. |  |
| `--arp-type` | type | Type: ARP, ARP-reply, RARP, RARP-reply. |  |
| `--arp-sender-mac` | mac | Set sender MAC address. |  |
| `--arp-sender-ip` | — | <addr> : Set sender IP address. |  |
| `--arp-target-mac` | mac | Set target MAC address. |  |
| `--arp-target-ip` | — | <addr> : Set target IP address. |  |
| `-S` | — | Set source IP address. |  |
| `--source-ip` | — | Set source IP address. |  |
| `--dest-ip` | addr | Set destination IP address (used as an alternative to {target specification} ). |  |
| `--tos` | tos | Set type of service field (8bits). |  |
| `--id` | — | <id> : Set identification field (16 bits). |  |
| `--df` | — | Set Don't Fragment flag. |  |
| `--mf` | — | Set More Fragments flag. |  |
| `--evil` | — | Set Reserved / Evil flag. |  |
| `--ttl` | hops | Set time to live [0-255]. |  |
| `--badsum-ip` | — | Use a random invalid checksum. |  |
| `--ip-options` | S\|R [route]\|L [route]\|T\|U  | Set IP options |  |
| `--mtu` | size | Set MTU. Packets get fragmented if MTU is small enough. |  |
| `-6` | — | Use IP version 6. |  |
| `--IPv6` | — | Use IP version 6. |  |
| `--hop-limit` | — | Set hop limit (same as IPv4 TTL). |  |
| `--traffic-class` | class | : Set traffic class. |  |
| `--flow` | label | Set flow label. |  |
| `--dest-mac` | mac | Set destination mac address. (Disables ARP resolution) |  |
| `--source-mac` | mac | Set source MAC address. |  |
| `--ether-type` | type | Set EtherType value. |  |
| `--data` | hex string | Include a custom payload. |  |
| `--data-string` | text | Include a custom ASCII text. |  |
| `--data-length` | len | Include len random bytes as payload. |  |
| `--echo-client` | passphrase | Run Nping in client mode. |  |
| `--echo-server` | passphrase | Run Nping in server mode. |  |
| `--echo-port` | port | Use custom <port> to listen or connect. |  |
| `--no-crypto` | — | Disable encryption and authentication. |  |
| `--once` | — | Stop the server after one connection. |  |
| `--safe-payloads` | — | Erase application data in echoed packets. |  |
| `--delay` | time | Adjust delay between probes. |  |
| `--rate` | — | <rate> : Send num packets per second. |  |
| `-h` | — | Display help information. |  |
| `--help` | — | Display help information. |  |
| `-V` | — | Display current version number. |  |
| `--version` | — | Display current version number. |  |
| `-c` | n | Stop after <n> rounds. |  |
| `--count` | n | Stop after <n> rounds. |  |
| `-e` | name | Use supplied network interface. |  |
| `--interface` | name | Use supplied network interface. |  |
| `-H` | — | Do not display sent packets. |  |
| `--hide-sent` | — | Do not display sent packets. |  |
| `-N` | — | Do not try to capture replies. |  |
| `--no-capture` | — | Do not try to capture replies. |  |
| `--privileged` | — | Assume user is fully privileged. |  |
| `--unprivileged` | — | Assume user lacks raw socket privileges. |  |
| `--send-eth` | — | Send packets at the raw Ethernet layer. |  |
| `--send-ip` | — | Send packets using raw IP sockets. |  |
| `--bpf-filter` | filter spec | Specify custom BPF filter. |  |
| `-v` | — | Increment verbosity level by one. |  |
| `-d` | — | Increment debugging level by one. |  |
| `-q` | — | Decrease verbosity level by one. |  |
| `--quiet` | — | Set verbosity and debug level to minimum. |  |
| `--debug` | — | Set verbosity and debug to the max level. |  |

## Gotchas

_TODO: operational traps._

## See also

[`nmap`](../network-analysis/nmap.md), [`arp-scan`](../network-analysis/arp-scan.md)
