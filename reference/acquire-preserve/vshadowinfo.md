<!-- generated-by: scripts/generate_pages.py -->
# vshadowinfo

**Kit:** SIFT Workstation (libyal)  **Capability:** Inspect or mount a forensic image container
**Captured:** `cyberlab-aio` via `--help` on 2026-08-01  [raw](../../capture/cyberlab-aio/help/vshadowinfo.help.txt)

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Invalid argument: vshadowinfo

## Synopsis

```
vshadowinfo [ -o offset ] [ -ahvV ] source
```

## Common invocations

<!-- candidates mined from cyberlab; verify each flag against the options table below before treating as reviewed -->
```
# from cyberlab 06-windows-artifact-libs
vshadowinfo -V
# from cyberlab 06-windows-artifact-libs
vshadowinfo exercise/volume.raw
```

## Options

All 5 options parsed from the captured help text. The final column is filled in by review.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-a` | — | shows allocation information |  |
| `-h` | — | shows this help |  |
| `-o` | — | specify the volume offset in bytes |  |
| `-v` | — | verbose output to stderr |  |
| `-V` | — | print version |  |

## Gotchas

_TODO: operational traps._

## See also

[`ewfinfo`](../acquire-preserve/ewfinfo.md), [`ewfmount`](../acquire-preserve/ewfmount.md), [`ewfverify`](../acquire-preserve/ewfverify.md), [`ewfexport`](../acquire-preserve/ewfexport.md), [`affinfo`](../acquire-preserve/affinfo.md), [`affcat`](../acquire-preserve/affcat.md), [`img_stat`](../acquire-preserve/img_stat.md), [`ntfs-3g`](../acquire-preserve/ntfs-3g.md)
