<!-- generated-by: scripts/generate_pages.py -->
# file

**Kit:** REMnux · FLARE-VM · SIFT Workstation  **Capability:** Inspect metadata for one file or inode; Identify what a file actually is  **Version:** file-5.44
**Captured:** `cyberlab-aio` via `--help` on 2026-08-01  [raw](../../capture/cyberlab-aio/help/file.help.txt)  **Docs:** <https://github.com/file/file>

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Identify file type using "magic" numbers.

## Synopsis

```
file [OPTION...] [FILE...]
```

## Common invocations

<!-- candidates mined from cyberlab; verify each flag against the options table below before treating as reviewed -->
```
# from cyberlab 33-binwalk-firmware
file foremost_out/jpg/*.jpg 2>/dev/null || file foremost_out/*/*
# from cyberlab 35-radare2-intro
file exercise/hello
# from cyberlab 38-network-emulation
file /tmp/beacon_reply.bin # -> data / HTML (INetSim default object)
```

## Options

All 54 options parsed from the captured help text. The final column is filled in by review.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `--help` | — | display this help and exit |  |
| `-v` | — | output version information and exit |  |
| `--version` | — | output version information and exit |  |
| `-m` | LIST | use LIST as a colon-separated list of magic number files |  |
| `--magic-file` | LIST | use LIST as a colon-separated list of magic number files |  |
| `-z` | — | try to look inside compressed files |  |
| `--uncompress` | — | try to look inside compressed files |  |
| `-Z` | — | only print the contents of compressed files |  |
| `--uncompress-noreport` | — | only print the contents of compressed files |  |
| `-b` | — | do not prepend filenames to output lines |  |
| `--brief` | — | do not prepend filenames to output lines |  |
| `-c` | — | print the parsed form of the magic file, use in conjunction with -m to debug a new magic file before installing it |  |
| `--checking-printout` | — | print the parsed form of the magic file, use in conjunction with -m to debug a new magic file before installing it |  |
| `-e` | TEST | exclude TEST from the list of test to be performed for file. Valid tests are: apptype, ascii, cdf, compress, csv, elf, encoding, soft, tar, json, text, tokens |  |
| `--exclude` | TEST | exclude TEST from the list of test to be performed for file. Valid tests are: apptype, ascii, cdf, compress, csv, elf, encoding, soft, tar, json, text, tokens |  |
| `--exclude-quiet` | TEST | like exclude, but ignore unknown tests |  |
| `-f` | FILE | read the filenames to be examined from FILE |  |
| `--files-from` | FILE | read the filenames to be examined from FILE |  |
| `-F` | STRING | use string as separator instead of `:' |  |
| `--separator` | STRING | use string as separator instead of `:' |  |
| `-i` | — | output MIME type strings (--mime-type and --mime-encoding) |  |
| `--mime` | — | output MIME type strings (--mime-type and --mime-encoding) |  |
| `--apple` | — | output the Apple CREATOR/TYPE |  |
| `--extension` | — | output a slash-separated list of extensions |  |
| `--mime-type` | — | output the MIME type |  |
| `--mime-encoding` | — | output the MIME encoding |  |
| `-k` | — | don't stop at the first match |  |
| `--keep-going` | — | don't stop at the first match |  |
| `-l` | — | list magic strength |  |
| `--list` | — | list magic strength |  |
| `-L` | — | follow symlinks (default if POSIXLY_CORRECT is set) |  |
| `--dereference` | — | follow symlinks (default if POSIXLY_CORRECT is set) |  |
| `-h` | — | don't follow symlinks (default if POSIXLY_CORRECT is not set) (default) |  |
| `--no-dereference` | — | don't follow symlinks (default if POSIXLY_CORRECT is not set) (default) |  |
| `-n` | — | do not buffer output |  |
| `--no-buffer` | — | do not buffer output |  |
| `-N` | — | do not pad output |  |
| `--no-pad` | — | do not pad output |  |
| `-0` | — | terminate filenames with ASCII NUL |  |
| `--print0` | — | terminate filenames with ASCII NUL |  |
| `-p` | — | preserve access times on files |  |
| `--preserve-date` | — | preserve access times on files |  |
| `-P` | — | set file engine parameter limits bytes 7340032 max bytes to look inside file elf_notes 256 max ELF notes processed elf_phnum 2048 max ELF prog sections processed elf_shnum 32768 max ELF sections proce |  |
| `--parameter` | — | set file engine parameter limits bytes 7340032 max bytes to look inside file elf_notes 256 max ELF notes processed elf_phnum 2048 max ELF prog sections processed elf_shnum 32768 max ELF sections proce |  |
| `-r` | — | don't translate unprintable chars to \ooo |  |
| `--raw` | — | don't translate unprintable chars to \ooo |  |
| `-s` | — | treat special (block/char devices) files as ordinary ones |  |
| `--special-files` | — | treat special (block/char devices) files as ordinary ones |  |
| `-S` | — | disable system call sandboxing |  |
| `--no-sandbox` | — | disable system call sandboxing |  |
| `-C` | — | compile file specified by -m |  |
| `--compile` | — | compile file specified by -m |  |
| `-d` | — | print debugging messages |  |
| `--debug` | — | print debugging messages |  |

## Gotchas

_TODO: operational traps._

## See also

[`istat`](../examine-the-filesystem/istat.md), [`ils`](../examine-the-filesystem/ils.md), [`stat`](../examine-the-filesystem/stat.md), [`die`](../malware-triage-static/die.md), [`diec`](../malware-triage-static/diec.md)
