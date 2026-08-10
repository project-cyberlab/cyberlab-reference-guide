<!-- generated-by: scripts/generate_pages.py -->
# ewfinfo

| | |
|---|---|
| **Kit** | Kali Linux · SIFT Workstation |
| **Capability** | Inspect or mount a forensic image container |
| **Captured from** | `cyberlab-aio` via `--help` on 2026-08-10 — [raw help output](../../capture/cyberlab-aio/help/ewfinfo.help.txt) |

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Show the metadata, hashes and acquisition details recorded inside an EWF/E01 image.

## When you'd reach for this

When an analyst is working with an E01 file, they run ewfinfo first to extract and save metadata such as imaging date and tool used, which is crucial for documentation and evidence reference. They may use ewfmount before accessing the raw image, and prefer ewfinfo over other tools because it specifically captures the metadata stored within the EWF wrapper.

**Sources:** <https://bromiley.medium.com/tooling-thursday-libewf-ec27b4564c2a> · <https://dfir.science/2017/11/EWF-Tools-working-with-Expert-Witness-Files-in-Linux.html>

## Synopsis

```
ewfinfo [ -A codepage ] [ -d date_format ] [ -f format ]
[ -ehimvVx ] ewf_files
```

## Common invocations

```
# Check EWF image details post-acquisition
ewfinfo /Cases/001/001_2017_USB_Gold.E01
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
