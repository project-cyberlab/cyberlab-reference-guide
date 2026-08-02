<!-- generated-by: scripts/generate_pages.py -->
# ewfverify

**Kit:** Kali Linux · SIFT Workstation  **Capability:** Inspect or mount a forensic image container
**Captured:** `cyberlab-aio` via `--help` on 2026-08-01  [raw](../../capture/cyberlab-aio/help/ewfverify.help.txt)

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Invalid argument: ewfverify

## Synopsis

```
ewfverify [ -A codepage ] [ -d digest_type ] [ -f format ]
[ -l log_filename ] [ -p process_buffer_size ]
[ -hqvVwx ] ewf_files
```

## Common invocations

<!-- candidates mined from cyberlab; verify each flag against the options table below before treating as reviewed -->
```
# from cyberlab 57-forensic-acquisition
ewfverify /evidence/case01.E01
```

## Options

All 11 options parsed from the captured help text. The final column is filled in by review.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-A` | — | codepage of header section, options: ascii (default), windows-874, windows-932, windows-936, windows-949, windows-950, windows-1250, windows-1251, windows-1252, windows-1253, windows-1254, windows-125 |  |
| `-d` | — | calculate additional digest (hash) types besides md5, options: sha1, sha256 |  |
| `-f` | — | specify the input format, options: raw (default), files (restricted to logical volume files) |  |
| `-h` | — | shows this help |  |
| `-l` | — | logs verification errors and the digest (hash) to the log_filename |  |
| `-p` | — | specify the process buffer size (default is the chunk size) |  |
| `-q` | — | quiet shows minimal status information |  |
| `-v` | — | verbose output to stderr |  |
| `-V` | — | print version |  |
| `-w` | — | zero sectors on checksum error (mimic EnCase like behavior) |  |
| `-x` | — | use the chunk data instead of the buffered read and write functions. |  |

## Gotchas

_TODO: operational traps._

## See also

[`ewfinfo`](../acquire-preserve/ewfinfo.md), [`ewfmount`](../acquire-preserve/ewfmount.md), [`ewfexport`](../acquire-preserve/ewfexport.md), [`affinfo`](../acquire-preserve/affinfo.md), [`affcat`](../acquire-preserve/affcat.md), [`img_stat`](../acquire-preserve/img_stat.md), [`ntfs-3g`](../acquire-preserve/ntfs-3g.md), [`vshadowinfo`](../acquire-preserve/vshadowinfo.md)
