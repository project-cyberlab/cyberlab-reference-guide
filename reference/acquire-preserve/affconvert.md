<!-- generated-by: scripts/generate_pages.py -->
# affconvert

| | |
|---|---|
| **Kit** | Kali Linux · SIFT Workstation |
| **Capability** | Image a disk, volume or device |
| **Version** | affconvert version 3.7.20 |
| **Captured from** | `cyberlab-aio` via `--help` on 2026-08-11 — [raw help output](../../capture/cyberlab-aio/help/affconvert.help.txt) |

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Convert between AFF and raw images in either direction. The usual reason is a tool that only reads one of them; keep the original, because converting to raw discards the metadata and hashes AFF was carrying.

## When you'd reach for this

When an analyst needs to convert files between RAW and AFF formats, they use affconvert, often after acquiring raw data or before processing with other AFF tools, as it directly handles format conversion unlike affcopy which focuses on reordering and recompression.

**Sources:** <https://www.kali.org/tools/afflib/>

## Synopsis

```
affconvert [options] file1 [... files]
```

## Common invocations

```
# Convert between raw disk images and AFF files
affconvert file1.raw
# Convert between AFF and raw formats for data processing
affconvert file1.raw file2.raw file3.raw
```

## Options

_No option definitions could be parsed from this tool's help output. It may be subcommand-driven or have no flags; needs manual review._

## Gotchas

_TODO: operational traps._

## See also

[`dc3dd`](../acquire-preserve/dc3dd.md), [`dcfldd`](../acquire-preserve/dcfldd.md), [`dd`](../acquire-preserve/dd.md), [`ewfacquire`](../acquire-preserve/ewfacquire.md)
