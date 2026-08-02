<!-- generated-by: scripts/generate_pages.py -->
# ewfinfo

**Kit:** Kali Linux · SIFT Workstation  **Capability:** Inspect or mount a forensic image container
**Captured:** `cyberlab-aio` via `--help` on 2026-08-01  [raw](../../capture/cyberlab-aio/help/ewfinfo.help.txt)

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Show the metadata, hashes and acquisition details recorded inside an EWF/E01 image.

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

All 9 options parsed from the captured help text; 7 reviewed with usage guidance.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-A` | — | codepage of header section, options: ascii (default), windows-874, windows-932, windows-936, windows-949, windows-950, windows-1250, windows-1251, windows-1252, windows-1253, windows-1254, windows-125 | Header codepage, for images with non-ASCII metadata. |
| `-d` | — | specify the date format, options: ctime (default), dm (day/month), md (month/day), iso8601 | Date format. `iso8601` is the unambiguous choice for a report. |
| `-e` | — | only show EWF read error information | Read errors recorded at acquisition. Check this before trusting a clean-looking image: unreadable sectors are noted here, not in the filesystem. |
| `-f` | — | specify the output format, options: text (default), dfxml | Emit DFXML instead of text, when the output feeds a tool rather than a person. |
| `-h` | — | shows this help |  |
| `-i` | — | only show EWF acquiry information | Acquisition details only — who imaged it, when, with what. |
| `-m` | — | only show EWF media information | Media details only — geometry, sector size, media type. |
| `-v` | — | verbose output to stderr | Verbose diagnostics to stderr. |
| `-V` | — | print version |  |

## Gotchas

- This reads the header only. It reports the hash that was recorded at acquisition; it does not recompute it, so it cannot tell you the image is still intact. Use [`ewfverify`](ewfverify.md) for that.

## See also

[`ewfmount`](../acquire-preserve/ewfmount.md), [`ewfverify`](../acquire-preserve/ewfverify.md), [`ewfexport`](../acquire-preserve/ewfexport.md), [`affinfo`](../acquire-preserve/affinfo.md), [`affcat`](../acquire-preserve/affcat.md), [`img_stat`](../acquire-preserve/img_stat.md), [`ntfs-3g`](../acquire-preserve/ntfs-3g.md), [`vshadowinfo`](../acquire-preserve/vshadowinfo.md)
