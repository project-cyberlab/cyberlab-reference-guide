<!-- generated-by: scripts/generate_pages.py -->
# rsakeyfind

**Kit:** REMnux · Kali Linux · SIFT Workstation  **Capability:** Recover encryption keys from memory
**Captured:** `cyberlab-aio` via `(no args)` on 2026-07-29  [raw](../../capture/cyberlab-aio/help/rsakeyfind.help.txt)  **Docs:** <https://citp.princeton.edu/our-work/memory/>

## Purpose

Find BER-encoded RSA private keys in a memory image.

## Synopsis

```
rsakeyfind MEMORY-IMAGE [MODULUS-FILE]
```

## Common invocations

<!-- candidates mined from cyberlab; verify each flag against the options table below before treating as reviewed -->
```
# from cyberlab 02-memory-forensics
rsakeyfind 2>&1 | head -n 1
# from cyberlab 02-memory-forensics
rsakeyfind sample.mem
```

## Options

_No option definitions could be parsed from this tool's help output. It may be subcommand-driven or have no flags; needs manual review._

## Gotchas

_TODO: operational traps._

## See also

`aeskeyfind`
