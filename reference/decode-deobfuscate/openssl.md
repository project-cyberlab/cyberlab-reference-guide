<!-- generated-by: scripts/generate_pages.py -->
# openssl

| | |
|---|---|
| **Kit** | Base OS — present on every Linux image |
| **Capability** | Decode, decrypt or transform encoded data |
| **Captured from** | `cyberlab-aio` via `--help` on 2026-08-10 — [raw help output](../../capture/cyberlab-aio/help/openssl.help.txt) |

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

The general-purpose crypto toolkit: inspect certificates, compute digests, encrypt and decrypt, and speak TLS to a service. In analysis it is most often used to read a certificate a sample presented, or to decrypt a blob once the key is known.

## When you'd reach for this

An analyst reaches for openssl when testing SSL/TLS connections to servers (e.g., using s_client to connect to ports like 993 or 995) or generating cryptographic digests (e.g., MD5 or SHA1) for file integrity checks. They may run these commands before verifying server configurations or after obtaining data for forensic analysis, as openssl provides direct command-line tools for these tasks without requiring additional software. They might prefer it over similar tools for its simplicity in quick tests or when specific functions like base64 encoding/decoding are needed.

**Sources:** <https://www.golinuxcloud.com/openssl-cheatsheet/> · <https://www.madboa.com/geek/openssl/>

## Common invocations

```
# Verify certificate validity and trust chain
openssl verify cert.pem
```

## Options

_No option definitions could be parsed from this tool's help output. It may be subcommand-driven or have no flags; needs manual review._

## Gotchas

_TODO: operational traps._

## See also

[`cyberchef`](../decode-deobfuscate/cyberchef.md), [`base64dump.py`](../malware-triage-static/base64dump.py.md), [`rax2`](../decode-deobfuscate/rax2.md), [`xxd`](../examine-the-filesystem/xxd.md), [`numbers-to-string.py`](../malware-triage-static/numbers-to-string.py.md)
