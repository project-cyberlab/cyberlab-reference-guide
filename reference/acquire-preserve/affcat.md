<!-- generated-by: scripts/generate_pages.py -->
# affcat

**Kit:** Kali Linux · SIFT Workstation  **Capability:** Inspect or mount a forensic image container  **Version:** affcat version 3.7.20
**Captured:** `cyberlab-aio` via `--help` on 2026-08-02  [raw](../../capture/cyberlab-aio/help/affcat.help.txt)

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Stream the raw contents of an AFF container to stdout, so tools that cannot read AFF can be fed the image through a pipe rather than a full conversion to raw.

## Synopsis

```
affcat [options] infile [... more infiles]
```

## Options

All 7 options parsed from the captured help text. The final column is filled in by review.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-q` | — | --- quiet; don't print to STDERR if a page is skipped |  |
| `-n` | — | --- noisy; tell when pages are skipped. |  |
| `-l` | — | --- List all of the segment names |  |
| `-L` | — | --- List segment names, lengths, and args |  |
| `-d` | — | --- debug. Print the page numbers to stderr as data goes to stdout |  |
| `-b` | — | --- Output BADFALG for bad blocks (default is NULLs) |  |
| `-v` | — | --- Just print the version number and exit. |  |

## Gotchas

_TODO: operational traps._

## See also

[`ewfinfo`](../acquire-preserve/ewfinfo.md), [`ewfmount`](../acquire-preserve/ewfmount.md), [`ewfverify`](../acquire-preserve/ewfverify.md), [`ewfexport`](../acquire-preserve/ewfexport.md), [`affinfo`](../acquire-preserve/affinfo.md), [`img_stat`](../acquire-preserve/img_stat.md), [`ntfs-3g`](../acquire-preserve/ntfs-3g.md), [`vshadowinfo`](../acquire-preserve/vshadowinfo.md)
