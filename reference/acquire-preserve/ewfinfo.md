<!-- generated-by: scripts/generate_pages.py -->
# ewfinfo

**Kit:** Kali Linux · SIFT Workstation  **Capability:** Inspect or mount a forensic image container
**Captured:** `cyberlab-aio` via `--help` on 2026-08-01  [raw](../../capture/cyberlab-aio/help/ewfinfo.help.txt)

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Invalid argument: ewfinfo

## Synopsis

```
ewfinfo [ -A codepage ] [ -d date_format ] [ -f format ]
[ -ehimvVx ] ewf_files
```

## Common invocations

<!-- candidates mined from cyberlab; verify each flag against the options table below before treating as reviewed -->
```
# from cyberlab 57-forensic-acquisition
ewfinfo /evidence/case01.E01
```

## Options

All 9 options parsed from the captured help text. The final column is filled in by review.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-A` | — | codepage of header section, options: ascii (default), windows-874, windows-932, windows-936, windows-949, windows-950, windows-1250, windows-1251, windows-1252, windows-1253, windows-1254, windows-125 |  |
| `-d` | — | specify the date format, options: ctime (default), dm (day/month), md (month/day), iso8601 |  |
| `-e` | — | only show EWF read error information |  |
| `-f` | — | specify the output format, options: text (default), dfxml |  |
| `-h` | — | shows this help |  |
| `-i` | — | only show EWF acquiry information |  |
| `-m` | — | only show EWF media information |  |
| `-v` | — | verbose output to stderr |  |
| `-V` | — | print version |  |

## Gotchas

_TODO: operational traps._

## See also

`ewfmount`, `ewfverify`, [`ewfexport`](../acquire-preserve/ewfexport.md), [`affinfo`](../acquire-preserve/affinfo.md), [`affcat`](../acquire-preserve/affcat.md), [`img_stat`](../acquire-preserve/img_stat.md), [`ntfs-3g`](../acquire-preserve/ntfs-3g.md), [`vshadowinfo`](../acquire-preserve/vshadowinfo.md)
