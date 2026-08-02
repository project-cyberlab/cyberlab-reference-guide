<!-- generated-by: scripts/generate_pages.py -->
# bdeinfo

| | |
|---|---|
| **Kit** | SIFT Workstation (libyal) |
| **Capability** | Inspect or mount a forensic image container |
| **Captured from** | `cyberlab-aio` via `--help` on 2026-08-02 — [raw help output](../../capture/cyberlab-aio/help/bdeinfo.help.txt) |

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Use bdeinfo to determine information about a BitLocker Drive

## Synopsis

```
bdeinfo [ -k keys ] [ -o offset ] [ -p password ]
[ -r password ] [ -s filename ] [ -hvV ] source
```

## Options

All 8 options parsed from the captured help text. The final column is filled in by review.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-h` | — | shows this help |  |
| `-k` | — | the full volume encryption key and tweak key formatted in base16 and separated by a : character e.g. FVEK:TWEAK |  |
| `-o` | — | specify the volume offset in bytes |  |
| `-p` | — | specify the password/passphrase |  |
| `-r` | — | specify the recovery password |  |
| `-s` | — | specify the file containing the startup key. typically this file has the extension .BEK |  |
| `-v` | — | verbose output to stderr |  |
| `-V` | — | print version |  |

## Gotchas

_TODO: operational traps._

## See also

[`ewfinfo`](../acquire-preserve/ewfinfo.md), [`ewfmount`](../acquire-preserve/ewfmount.md), [`ewfverify`](../acquire-preserve/ewfverify.md), [`ewfexport`](../acquire-preserve/ewfexport.md), [`affinfo`](../acquire-preserve/affinfo.md), [`affcat`](../acquire-preserve/affcat.md), [`img_stat`](../acquire-preserve/img_stat.md), [`ntfs-3g`](../acquire-preserve/ntfs-3g.md)
