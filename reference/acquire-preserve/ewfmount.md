<!-- generated-by: scripts/generate_pages.py -->
# ewfmount

**Kit:** Kali Linux · SIFT Workstation  **Capability:** Inspect or mount a forensic image container
**Captured:** `cyberlab-aio` via `--help` on 2026-08-01  [raw](../../capture/cyberlab-aio/help/ewfmount.help.txt)

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Invalid argument: ewfmount

## Synopsis

```
ewfmount [ -f format ] [ -X extended_options ] [ -hvV ] image mount_point
```

## Common invocations

<!-- candidates mined from cyberlab; verify each flag against the options table below before treating as reviewed -->
```
# from cyberlab 57-forensic-acquisition
sudo ewfmount /evidence/case01.E01 /mnt/ewf
```

## Options

All 5 options parsed from the captured help text. The final column is filled in by review.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-f` | — | specify the input format, options: raw (default), files (restricted to logical volume files) |  |
| `-h` | — | shows this help |  |
| `-v` | — | verbose output to stderr, while ewfmount will remain running in the foreground |  |
| `-V` | — | print version |  |
| `-X` | — | extended options to pass to sub system |  |

## Gotchas

_TODO: operational traps._

## See also

[`ewfinfo`](../acquire-preserve/ewfinfo.md), `ewfverify`, [`ewfexport`](../acquire-preserve/ewfexport.md), [`affinfo`](../acquire-preserve/affinfo.md), [`affcat`](../acquire-preserve/affcat.md), [`img_stat`](../acquire-preserve/img_stat.md), [`ntfs-3g`](../acquire-preserve/ntfs-3g.md), [`vshadowinfo`](../acquire-preserve/vshadowinfo.md)
