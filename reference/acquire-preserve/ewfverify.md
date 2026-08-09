<!-- generated-by: scripts/generate_pages.py -->
# ewfverify

| | |
|---|---|
| **Kit** | Kali Linux · SIFT Workstation |
| **Capability** | Inspect or mount a forensic image container |
| **Captured from** | `cyberlab-aio` via `--help` on 2026-08-09 — [raw help output](../../capture/cyberlab-aio/help/ewfverify.help.txt) |

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Recompute an EWF/E01 image's hashes and check them against the values stored at acquisition.

## Synopsis

```
ewfverify [ -A codepage ] [ -d digest_type ] [ -f format ]
[ -l log_filename ] [ -p process_buffer_size ]
[ -hqvVwx ] ewf_files
```

## Common invocations

```
# Verify EWF image integrity and validity
ewfverify image.E01
# Verify EWF file integrity against original data
ewfverify floppy.E01
# Verify data integrity of E01 file against stored hash
ewfverify -f files logical.E01
# Verify EWF image integrity after acquisition
ewfverify /Cases/001/001_2017_USB_Gold.E01
```

## Options

All 11 options parsed from the captured help text; 9 reviewed with usage guidance.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-A` | — | codepage of header section, options: ascii (default), windows-874, windows-932, windows-936, windows-949, windows-950, windows-1250, windows-1251, windows-1252, windows-1253, windows-1254, windows-125 | Header codepage. |
| `-d` | — | calculate additional digest (hash) types besides md5, options: sha1, sha256 | Also verify an additional digest such as sha256, when one was recorded at acquisition. |
| `-f` | — | specify the input format, options: raw (default), files (restricted to logical volume files) | Output format. |
| `-h` | — | shows this help |  |
| `-l` | — | logs verification errors and the digest (hash) to the log_filename | Write the verification result to a log file — the artefact worth keeping with the case, not just terminal output. |
| `-p` | — | specify the process buffer size (default is the chunk size) | Process buffer size. |
| `-q` | — | quiet shows minimal status information | Minimal output, for scripted checks. |
| `-v` | — | verbose output to stderr | Verbose diagnostics to stderr. |
| `-V` | — | print version |  |
| `-w` | — | zero sectors on checksum error (mimic EnCase like behavior) | Wipe sectors that could not be read. |
| `-x` | — | use the chunk data instead of the buffered read and write functions. | Bypass the buffered read/write path. |

## Gotchas

- This reads every byte, so it takes as long as the acquisition did. Budget for that rather than discovering it mid-deadline.
- A pass proves the image matches what was recorded **at acquisition**. It says nothing about whether the acquisition captured the device correctly — a disk failing mid-image produces a verifiable image of incomplete data.

## See also

[`ewfinfo`](../acquire-preserve/ewfinfo.md), [`ewfmount`](../acquire-preserve/ewfmount.md), [`ewfexport`](../acquire-preserve/ewfexport.md), [`affinfo`](../acquire-preserve/affinfo.md), [`affcat`](../acquire-preserve/affcat.md), [`img_stat`](../acquire-preserve/img_stat.md), [`ntfs-3g`](../acquire-preserve/ntfs-3g.md), [`vshadowinfo`](../acquire-preserve/vshadowinfo.md)
