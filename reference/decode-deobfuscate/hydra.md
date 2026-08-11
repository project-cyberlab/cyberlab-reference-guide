<!-- generated-by: scripts/generate_pages.py -->
# hydra

| | |
|---|---|
| **Kit** | Kali Linux · SIFT Workstation |
| **Capability** | Crack passwords and hashes |
| **Version** | Hydra v9.4 |
| **Captured from** | `cyberlab-aio` via `--help` on 2026-08-11 — [raw help output](../../capture/cyberlab-aio/help/hydra.help.txt) |

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Test credentials against a network service across many protocols. In an authorised engagement it answers whether a recovered password works elsewhere; it is loud, it locks accounts, and it belongs nowhere near production without written permission.

## When you'd reach for this

An analyst reaches for Hydra after enumeration and gathering web-form details from tools like Burp Suite, running it for online brute-force attacks on SSH or web forms; they choose it over similar tools like John the Ripper because Hydra operates online, making it suitable for live targets requiring real-time credential testing.

**Sources:** <https://crackerfrank.hashnode.dev/cracking-passwords-with-hydra-a-tryhackme-walkthrough> · <https://hackproofhacks.com/blog/password-cracking-with-hydra-hacking-series/> · <https://www.freecodecamp.org/news/how-to-use-hydra-pentesting-tutorial/>

## Options

_No option definitions could be parsed from this tool's help output. It may be subcommand-driven or have no flags; needs manual review._

## Gotchas

_TODO: operational traps._

## See also

[`hashcat`](../decode-deobfuscate/hashcat.md), [`john`](../decode-deobfuscate/john.md)
