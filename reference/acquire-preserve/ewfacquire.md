<!-- generated-by: scripts/generate_pages.py -->
# ewfacquire

| | |
|---|---|
| **Kit** | Kali Linux · SIFT Workstation |
| **Capability** | Image a disk, volume or device |
| **Captured from** | `cyberlab-aio` via `--help` on 2026-08-07 — [raw help output](../../capture/cyberlab-aio/help/ewfacquire.help.txt) |

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Acquire a disk, volume or device into an EWF/E01 evidence container, with the case metadata and hashes stored inside the image itself.

## Synopsis

```
ewfacquire [ -A codepage ] [ -b number_of_sectors ]
[ -B number_of_bytes ] [ -c compression_values ]
[ -C case_number ] [ -d digest_type ] [ -D description ]
[ -e examiner_name ] [ -E evidence_number ] [ -f format ]
[ -g number_of_sectors ] [ -l log_filename ]
[ -m media_type ] [ -M media_flags ] [ -N notes ]
```

## Common invocations

```
# Create EWF image from device or file
ewfacquire /dev/sda
# Convert RAW to EWF or image a device
ewfacquire myfile.raw
# Convert split optical disc RAW to EWF image
ewfacquire -T optical.cue optical.iso
# Convert RAW image to EWF format
ewfacquire -c best -m fixed -t myfile -S 1T -u [-q] myfile.raw
```

## Options

All 32 options parsed from the captured help text; 30 reviewed with usage guidance.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-A` | — | codepage of header section, options: ascii (default), windows-874, windows-932, windows-936, windows-949, windows-950, windows-1250, windows-1251, windows-1252, windows-1253, windows-1254, windows-125 | Header codepage, for non-ASCII metadata. |
| `-b` | — | specify the number of sectors to read at once (per chunk), options: 16, 32, 64 (default), 128, 256, 512, 1024, 2048, 4096, 8192, 16384 or 32768 | Sectors per chunk. Larger chunks read faster but lose more data to each unreadable sector. |
| `-B` | — | specify the number of bytes to acquire (default is all bytes) | Acquire a fixed number of bytes rather than the whole device — with `-o`, the way to image one region. |
| `-c` | — | specify the compression values as: level or method:level compression method options: deflate (default), bzip2 (bzip2 is only supported by EWF2 formats) compression level options: none (default), empty | Trade size against time. `best` on a slow USB source is often faster overall than `none`, because the bottleneck is the read, not the CPU. |
| `-C` | — | specify the case number (default is case_number). | Case number, stored in the image header. |
| `-d` | — | calculate additional digest (hash) types besides md5, options: sha1, sha256 | Add sha1 or sha256 alongside the default md5. Worth doing once, at acquisition: md5 alone is increasingly challenged, and rehashing later means reading the whole image again. |
| `-D` | — | specify the description (default is description). | Description, stored in the image header. |
| `-e` | — | specify the examiner name (default is examiner_name). | Examiner name, stored in the image header. |
| `-E` | — | specify the evidence number (default is evidence_number). | Evidence number, stored in the image header. |
| `-f` | — | specify the EWF file format to write to, options: ewf, smart, ftk, encase2, encase3, encase4, encase5, encase6 (default), encase7, encase7-v2, linen5, linen6, linen7, ewfx | Choose the EWF variant. `encase6` is the safe default for interoperability; pick the format the tool that will read it expects, not the newest one available. |
| `-g` | — | specify the number of sectors to be used as error granularity | Error granularity — how much data around a bad sector is discarded. Lower values preserve more of a failing disk at the cost of speed. |
| `-h` | — | shows this help |  |
| `-l` | — | logs acquiry errors and the digest (hash) to the log_filename | Write the acquisition log, including errors and hashes, to a file. This is the record you cite later; do not skip it. |
| `-m` | — | specify the media type, options: fixed (default), removable, optical, memory | Record the media type (fixed, removable, optical, memory) in the header. |
| `-M` | — | specify the media flags, options: logical, physical (default) | Record whether this is a physical device or a logical volume. |
| `-N` | — | specify the notes (default is notes). | Free-text notes, stored in the image header. These five metadata flags are the reason to choose E01 over a raw `dd` image: the container describes its own provenance. |
| `-o` | — | specify the offset to start to acquire (default is 0) | Start at an offset rather than sector 0. |
| `-p` | — | specify the process buffer size (default is the chunk size) | Process buffer size — a throughput tuning knob. |
| `-P` | — | specify the number of bytes per sector (default is 512) (use this to override the automatic bytes per sector detection) | Override bytes-per-sector. Needed on 4Kn drives where the 512-byte assumption is wrong. |
| `-q` | — | quiet shows minimal status information | Minimal status output, for logs. |
| `-r` | — | specify the number of retries when a read error occurs (default is 2) | Read retries before giving up on a sector. Raise it for a dying drive; lower it when retries are heating a drive that may not survive the acquisition. |
| `-R` | — | resume acquiry at a safe point | Resume an interrupted acquisition at a safe point, instead of restarting a multi-hour read. |
| `-s` | — | swap byte pairs of the media data (from AB to BA) (use this for big to little endian conversion and vice versa) | Swap byte pairs for a big-endian source. Rare, and wrong unless you know the source endianness differs. |
| `-S` | — | specify the segment file size in bytes (default is 1.4 GiB) (minimum is 1.0 MiB, maximum is 7.9 EiB for encase6 and encase7 format and 1.9 GiB for other formats) | Segment size. The 1.4 GiB default suits FAT32 and optical media; raise it on a modern filesystem to avoid hundreds of fragments. |
| `-t` | — | specify the target file (without extension) to write to | Set the output name, without extension — ewfacquire appends `.E01`, `.E02`… itself. The one flag you always pass. |
| `-T` | — | specify the file containing the table of contents (TOC) of an optical disc. The TOC file must be in the CUE format. | Supply a CUE file when imaging optical media, so the track layout is preserved. |
| `-u` | — | unattended mode (disables user interaction) | Unattended — suppresses the interactive prompts. Required for any scripted or headless acquisition. |
| `-v` | — | verbose output to stderr | Verbose diagnostics to stderr — worth capturing alongside `-l` when a source is throwing read errors. |
| `-V` | — | print version |  |
| `-w` | — | zero sectors on read error (mimic EnCase like behavior) | Zero unreadable sectors instead of aborting, the way EnCase does. Keeps offsets aligned so the filesystem still parses. |
| `-x` | — | use the chunk data instead of the buffered read and write functions. | Bypass the buffered read/write path. |
| `-2` | — | specify the secondary target file (without extension) to write to | Write a second copy in the same pass. Two independent copies for the cost of one read, which matters when the source is failing and may not survive a second acquisition. |

## Gotchas

- The case metadata flags default to literal placeholder strings — `case_number`, `examiner_name`, `evidence_number`. Omit them and the image ships with those placeholders recorded as fact, which is worse than an empty field because it looks filled in.
- `-t` takes the name **without** an extension. Passing `image.E01` produces `image.E01.E01`.
- Acquisition is not verification. `ewfacquire` records hashes; proving the image still matches them later is [`ewfverify`](ewfverify.md).

## See also

[`dc3dd`](../acquire-preserve/dc3dd.md), [`dcfldd`](../acquire-preserve/dcfldd.md), [`dd`](../acquire-preserve/dd.md), [`affconvert`](../acquire-preserve/affconvert.md)
