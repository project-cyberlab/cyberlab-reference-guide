# fls

**Kit:** SIFT Workstation · REMnux · Kali (`sleuthkit`) **Category:** Filesystem analysis
**Version:** The Sleuth Kit 4.11.1 **Docs:** <https://wiki.sleuthkit.org/index.php?title=Fls>
**Verified:** 2026-07-29 from `cyberlab-aio:v1` — raw output in [`capture/fls.help.txt`](../../capture/fls.help.txt)

> **Worked example of the format.** Every option below was read off the real
> binary, not written from memory. See [docs/FORMAT.md](../../docs/FORMAT.md).

---

## Purpose

List file and directory names in a disk image, including deleted entries.

## Synopsis

```
fls [-adDFlhpruvV] [-f fstype] [-i imgtype] [-b dev_sector_size] [-m dir/]
    [-o imgoffset] [-z ZONE] [-s seconds] image [images] [inode]
```

If `[inode]` is not given, the root directory is used.

> **Note:** the usage line above advertises only `[-adDFlhpruvV]`, but the tool
> also accepts `-P`, `-B`, `-S` and `-k`. They are documented below.

## Common invocations

```
# List the root directory of an image
fls {{path/to/image.dd}}

# List a partition that starts at a sector offset (the usual case for a full disk)
fls -o {{2048}} {{path/to/image.dd}}

# Show deleted entries only — the fast answer to "what was removed?"
fls -d -o {{2048}} {{path/to/image.dd}}

# Recurse the whole filesystem showing full paths, deleted files included
fls -rp -o {{2048}} {{path/to/image.dd}}

# Recurse showing ONLY deleted files with full paths
fls -rpd -o {{2048}} {{path/to/image.dd}}

# Long listing (sizes, MAC times) like ls -l, in a named time zone
fls -l -z {{EST5EDT}} -o {{2048}} {{path/to/image.dd}}

# Emit a body file for timelining, then build the timeline with mactime
fls -r -m {{/}} -o {{2048}} {{path/to/image.dd}} > {{path/to/body.txt}}

# List the contents of one directory by inode number
fls -o {{2048}} {{path/to/image.dd}} {{inode}}
```

## Options — complete

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-a` | — | Display `.` and `..` entries | Rarely; they are hidden by default as noise |
| `-d` | — | Display deleted entries only | Recovery hunts — isolates what was removed |
| `-D` | — | Display only directories | Mapping structure without file noise |
| `-F` | — | Display only files | Excluding directories from a listing |
| `-l` | — | Display long version (like `ls -l`) | When you need sizes, UID/GID and MAC times |
| `-p` | — | Display full path for each file | Almost always with `-r`; otherwise output is ambiguous |
| `-r` | — | Recurse on directory entries | Walking a whole filesystem rather than one directory |
| `-u` | — | Display undeleted entries only | The inverse of `-d`; filtering live files |
| `-m` | `dir/` | Output in mactime input format, with `dir/` as the mount point | Building a super-timeline; feeds `mactime` |
| `-h` | — | Include MD5 checksum hash in mactime output | Timeline work where you also need file hashes |
| `-f` | `fstype` | Filesystem type (`-f list` for supported types) | When auto-detection fails or is wrong |
| `-i` | `imgtype` | Image format (`-i list` for supported types) | Non-raw images: E01, AFF, etc. |
| `-b` | `dev_sector_size` | Device sector size in bytes | 4Kn drives, where the 512-byte assumption breaks |
| `-o` | `imgoffset` | Offset into the image, in sectors | **The most common flag** — targeting a partition in a full-disk image |
| `-P` | `pooltype` | Pool container type (`-P list` for supported types) | APFS / logical volume containers |
| `-B` | `pool_volume_block` | Starting block, pool volumes only | Selecting a volume inside a pool |
| `-S` | `snap_id` | Snapshot ID (APFS only) | Examining a specific APFS snapshot |
| `-k` | `password` | Decryption password for encrypted volumes | BitLocker/FileVault-style encrypted volumes |
| `-z` | `ZONE` | Time zone of the original machine (e.g. `EST5EDT`, `GMT`) | Only meaningful with `-l`; wrong TZ silently skews every timestamp |
| `-s` | `seconds` | Time skew of the original machine, in seconds | Only with `-l`/`-m`; correcting a known-bad system clock |
| `-v` | — | Verbose output to stderr | Debugging why an image will not parse |
| `-V` | — | Print version | Recording tool provenance in your notes |

## Gotchas

- **`-o` is in sectors, not bytes.** Get it from `mmls` first. A wrong offset
  usually yields "Cannot determine file system type", not an obvious error.
- **`-z` only affects `-l` output.** Setting it without `-l` changes nothing,
  which makes a wrong-timezone timeline easy to produce and hard to notice.
- **Deleted entries may have unrecoverable content.** `fls -d` listing a name
  does not mean `icat` will return its data — the blocks may be reallocated.
- **`-r` on a large image is slow and noisy.** Pipe to a file, then grep it,
  rather than scrolling.

## See also

- `mmls` — partition table; where you get the `-o` value
- `icat` — extract the content of an inode `fls` found
- `istat` — detailed metadata for one inode
- `mactime` — consumes the `-m` body file to build the timeline
- `tsk_recover` — bulk export of allocated/deleted files
