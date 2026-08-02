<!-- generated-by: scripts/generate_pages.py -->
# dc3dd

**Kit:** Kali Linux · SIFT Workstation  **Capability:** Image a disk, volume or device  **Version:** dc3dd (dc3dd) 7.2.646
**Captured:** `cyberlab-aio` via `--help` on 2026-08-02  [raw](../../capture/cyberlab-aio/help/dc3dd.help.txt)

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

dc3dd [OPTION 1] [OPTION 2] ... [OPTION N]

## Synopsis

```
------
```

## Common invocations

<!-- candidates mined from cyberlab; verify each flag against the options table below before treating as reviewed -->
```
# from cyberlab 57-forensic-acquisition
sudo dc3dd if=/dev/sdX of=/evidence/case01.dd hash=sha256 log=/evidence/case01.log
```

## Options

All 3 options parsed from the captured help text. The final column is filled in by review.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `--help` | — | display this help and exit |  |
| `--version` | — | output version information and exit |  |
| `--flags` | — | display compile-time flags and exit |  |

## Gotchas

_TODO: operational traps._

## See also

[`dcfldd`](../acquire-preserve/dcfldd.md), [`dd`](../acquire-preserve/dd.md), [`ewfacquire`](../acquire-preserve/ewfacquire.md), [`affconvert`](../acquire-preserve/affconvert.md)
