<!-- generated-by: scripts/generate_pages.py -->
# aeskeyfind

| | |
|---|---|
| **Kit** | REMnux · Kali Linux · SIFT Workstation |
| **Capability** | Recover encryption keys from memory |
| **Captured from** | `cyberlab-aio` via `--help` on 2026-08-11 — [raw help output](../../capture/cyberlab-aio/help/aeskeyfind.help.txt) |
| **Documentation** | <https://citp.princeton.edu/our-work/memory/> |

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Find 128-bit and 256-bit AES keys in a memory image.

## When you'd reach for this

An analyst reaches for aeskeyfind after creating a memory dump using a tool like Volatility to recover AES keys from the dump, as it is specifically designed to locate 128-bit and 256-bit AES keys in memory images; they would run it after the dump is created and before exporting the keys, preferring it over similar tools due to its focus on AES key recovery from memory dumps.

**Sources:** <https://medium.com/@Frogjump/aeskeyfind-in-kali-linux-72ba6a8ea2fd>

## Synopsis

```
aeskeyfind [OPTION]... MEMORY-IMAGE
```

## Options

All 3 options parsed from the captured help text; 1 reviewed with usage guidance.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-v` | — | verbose output -- prints the extended keys and the constraints on the rows of the key schedule | An analyst would use the -v flag when examining memory images to obtain detailed verbose output, including extended keys and constraints on the rows of the key schedule, to aid in forensic analysis. |
| `-q` | — | don't display a progress bar |  |
| `-h` | — | displays this help message |  |

## Gotchas

_TODO: operational traps._

## See also

[`rsakeyfind`](../memory-forensics/rsakeyfind.md), [`bulk_extractor`](../examine-the-filesystem/bulk_extractor.md)
