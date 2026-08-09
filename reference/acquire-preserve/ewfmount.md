<!-- generated-by: scripts/generate_pages.py -->
# ewfmount

| | |
|---|---|
| **Kit** | Kali Linux · SIFT Workstation |
| **Capability** | Inspect or mount a forensic image container |
| **Captured from** | `cyberlab-aio` via `--help` on 2026-08-09 — [raw help output](../../capture/cyberlab-aio/help/ewfmount.help.txt) |

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Use ewfmount to mount an Expert Witness Compression Format (EWF) image file

## Synopsis

```
ewfmount [ -f format ] [ -X extended_options ] [ -hvV ] image mount_point
```

## Common invocations

```
# Mount EWF image to a folder for forensic analysis
ewfmount image.E01 <folder>
# Mount EWF image to access its file system
ewfmount image.E01 mount_point
# Mount logical image to access files
ewfmount -f files image.L01 mount_point
# Mount EWF image to access disk as physical device
ewfmount /Cases/001/001_2017_USB_Gold.E01 /mnt/ewf
# Mount EWF image to a folder for file system access
ewfmount image.E01 <folder>
```

## Options

All 5 options parsed from the captured help text; 1 reviewed with usage guidance.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-f` | — | specify the input format, options: raw (default), files (restricted to logical volume files) | An analyst would use the -f flag when mounting a logical evidence file (such as a L01 or Lx01 file) to access metadata about loose files or directories rather than a disk image. |
| `-h` | — | shows this help |  |
| `-v` | — | verbose output to stderr, while ewfmount will remain running in the foreground |  |
| `-V` | — | print version |  |
| `-X` | — | extended options to pass to sub system |  |

## Gotchas

_TODO: operational traps._

## See also

[`ewfinfo`](../acquire-preserve/ewfinfo.md), [`ewfverify`](../acquire-preserve/ewfverify.md), [`ewfexport`](../acquire-preserve/ewfexport.md), [`affinfo`](../acquire-preserve/affinfo.md), [`affcat`](../acquire-preserve/affcat.md), [`img_stat`](../acquire-preserve/img_stat.md), [`ntfs-3g`](../acquire-preserve/ntfs-3g.md), [`vshadowinfo`](../acquire-preserve/vshadowinfo.md)
