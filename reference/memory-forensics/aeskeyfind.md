<!-- generated-by: scripts/generate_pages.py -->
# aeskeyfind

**Kit:** REMnux · Kali Linux · SIFT Workstation  **Capability:** Recover encryption keys from memory
**Captured:** `cyberlab-aio` via `--help` on 2026-07-29  [raw](../../capture/cyberlab-aio/help/aeskeyfind.help.txt)  **Docs:** <https://citp.princeton.edu/our-work/memory/>

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Find 128-bit and 256-bit AES keys in a memory image.

## Synopsis

```
aeskeyfind [OPTION]... MEMORY-IMAGE
```

## Common invocations

<!-- candidates mined from cyberlab; verify each flag against the options table below before treating as reviewed -->
```
# from cyberlab 02-memory-forensics
aeskeyfind 2>&1 | head -n 1
# from cyberlab 02-memory-forensics
aeskeyfind sample.mem
```

## Options

All 3 options parsed from the captured help text. The final column is filled in by review.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-v` | — | verbose output -- prints the extended keys and the constraints on the rows of the key schedule |  |
| `-q` | — | don't display a progress bar |  |
| `-h` | — | displays this help message |  |

## Gotchas

_TODO: operational traps._

## See also

[`rsakeyfind`](../memory-forensics/rsakeyfind.md)
