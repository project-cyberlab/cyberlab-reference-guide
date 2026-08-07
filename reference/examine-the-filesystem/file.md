<!-- generated-by: scripts/generate_pages.py -->
# file

| | |
|---|---|
| **Kit** | REMnux · FLARE-VM · SIFT Workstation |
| **Capability** | Inspect metadata for one file or inode; Identify what a file actually is |
| **Version** | file-5.44 |
| **Captured from** | `cyberlab-aio` via `--help` on 2026-08-07 — [raw help output](../../capture/cyberlab-aio/help/file.help.txt) |
| **Documentation** | <https://github.com/file/file> |

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Identify a file's type from its contents rather than its name, using magic signatures.

## Synopsis

```
file [OPTION...] [FILE...]
```

## Options

All 54 options parsed from the captured help text; 20 reviewed with usage guidance.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `--help` | — | display this help and exit |  |
| `-v` | — | output version information and exit |  |
| `--version` | — | output version information and exit |  |
| `-m` | LIST | use LIST as a colon-separated list of magic number files | Use an alternative magic database. |
| `--magic-file` | LIST | use LIST as a colon-separated list of magic number files | Use an alternative magic database. |
| `-z` | — | try to look inside compressed files | Look inside compressed files and report what they contain rather than reporting a compressed stream. |
| `--uncompress` | — | try to look inside compressed files | Look inside compressed files and report what they contain rather than reporting a compressed stream. |
| `-Z` | — | only print the contents of compressed files | Same, without reporting the compression itself. |
| `--uncompress-noreport` | — | only print the contents of compressed files | Same, without reporting the compression itself. |
| `-b` | — | do not prepend filenames to output lines | Omit the filename, leaving just the type — for pipelines and for-loops. |
| `--brief` | — | do not prepend filenames to output lines | Omit the filename, leaving just the type — for pipelines and for-loops. |
| `-c` | — | print the parsed form of the magic file, use in conjunction with -m to debug a new magic file before installing it |  |
| `--checking-printout` | — | print the parsed form of the magic file, use in conjunction with -m to debug a new magic file before installing it |  |
| `-e` | TEST | exclude TEST from the list of test to be performed for file. Valid tests are: apptype, ascii, cdf, compress, csv, elf, encoding, soft, tar, json, text, tokens | Exclude a test type, when one is misfiring on a corpus. |
| `--exclude` | TEST | exclude TEST from the list of test to be performed for file. Valid tests are: apptype, ascii, cdf, compress, csv, elf, encoding, soft, tar, json, text, tokens | Exclude a test type, when one is misfiring on a corpus. |
| `--exclude-quiet` | TEST | like exclude, but ignore unknown tests |  |
| `-f` | FILE | read the filenames to be examined from FILE | Read the list of files to test from a file, for a corpus. |
| `--files-from` | FILE | read the filenames to be examined from FILE | Read the list of files to test from a file, for a corpus. |
| `-F` | STRING | use string as separator instead of `:' |  |
| `--separator` | STRING | use string as separator instead of `:' |  |
| `-i` | — | output MIME type strings (--mime-type and --mime-encoding) | Print a MIME type instead of prose. The form to use when the output feeds a script rather than a person. |
| `--mime` | — | output MIME type strings (--mime-type and --mime-encoding) | Print a MIME type instead of prose. The form to use when the output feeds a script rather than a person. |
| `--apple` | — | output the Apple CREATOR/TYPE |  |
| `--extension` | — | output a slash-separated list of extensions |  |
| `--mime-type` | — | output the MIME type | MIME type only, without the encoding. |
| `--mime-encoding` | — | output the MIME encoding | Character encoding only. |
| `-k` | — | don't stop at the first match | Keep going after the first match and print every rule that fired. Files crafted to defeat identification often match more than one signature, and the disagreement is the finding. |
| `--keep-going` | — | don't stop at the first match | Keep going after the first match and print every rule that fired. Files crafted to defeat identification often match more than one signature, and the disagreement is the finding. |
| `-l` | — | list magic strength |  |
| `--list` | — | list magic strength |  |
| `-L` | — | follow symlinks (default if POSIXLY_CORRECT is set) | Follow symlinks and report the target. |
| `--dereference` | — | follow symlinks (default if POSIXLY_CORRECT is set) | Follow symlinks and report the target. |
| `-h` | — | don't follow symlinks (default if POSIXLY_CORRECT is not set) (default) | Do not follow symlinks — report the link itself. |
| `--no-dereference` | — | don't follow symlinks (default if POSIXLY_CORRECT is not set) (default) | Do not follow symlinks — report the link itself. |
| `-n` | — | do not buffer output |  |
| `--no-buffer` | — | do not buffer output |  |
| `-N` | — | do not pad output | Do not pad filenames to align the output. |
| `--no-pad` | — | do not pad output | Do not pad filenames to align the output. |
| `-0` | — | terminate filenames with ASCII NUL | Print a NUL after the filename, for safe piping into `xargs -0`. |
| `--print0` | — | terminate filenames with ASCII NUL | Print a NUL after the filename, for safe piping into `xargs -0`. |
| `-p` | — | preserve access times on files | Preserve the access time on the files examined — the flag that stops a triage sweep from rewriting timestamps across the evidence. |
| `--preserve-date` | — | preserve access times on files | Preserve the access time on the files examined — the flag that stops a triage sweep from rewriting timestamps across the evidence. |
| `-P` | — | set file engine parameter limits bytes 7340032 max bytes to look inside file elf_notes 256 max ELF notes processed elf_phnum 2048 max ELF prog sections processed elf_shnum 32768 max ELF sections proce | Tune a parser limit, e.g. `bytes` or `indir`. |
| `--parameter` | — | set file engine parameter limits bytes 7340032 max bytes to look inside file elf_notes 256 max ELF notes processed elf_phnum 2048 max ELF prog sections processed elf_shnum 32768 max ELF sections proce | Tune a parser limit, e.g. `bytes` or `indir`. |
| `-r` | — | don't translate unprintable chars to \ooo | Print raw bytes rather than escaping unprintables. |
| `--raw` | — | don't translate unprintable chars to \ooo | Print raw bytes rather than escaping unprintables. |
| `-s` | — | treat special (block/char devices) files as ordinary ones | Read block and character devices too. Needed to type a raw disk, which `file` otherwise refuses. |
| `--special-files` | — | treat special (block/char devices) files as ordinary ones | Read block and character devices too. Needed to type a raw disk, which `file` otherwise refuses. |
| `-S` | — | disable system call sandboxing | Disable the sandbox. Only when seccomp blocks a legitimate test, and never on untrusted input if avoidable. |
| `--no-sandbox` | — | disable system call sandboxing | Disable the sandbox. Only when seccomp blocks a legitimate test, and never on untrusted input if avoidable. |
| `-C` | — | compile file specified by -m | Compile a magic file to its indexed form. |
| `--compile` | — | compile file specified by -m | Compile a magic file to its indexed form. |
| `-d` | — | print debugging messages |  |
| `--debug` | — | print debugging messages |  |

## Gotchas

- Magic reads the first few hundred bytes. Prepend a valid header to anything and `file` will report the header — it is a fast triage signal, not an authority on content.
- `-p` preserves atime. Without it, typing a directory tree updates access times across the evidence, which is the kind of avoidable contamination that gets noticed later.
- An 'ASCII text' verdict on something you expected to be binary usually means it is base64 or hex, not that it is harmless.

## See also

[`istat`](../examine-the-filesystem/istat.md), [`ils`](../examine-the-filesystem/ils.md), `stat`, [`die`](../malware-triage-static/die.md), [`diec`](../malware-triage-static/diec.md)
