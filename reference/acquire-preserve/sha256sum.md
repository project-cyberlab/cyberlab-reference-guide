<!-- generated-by: scripts/generate_pages.py -->
# sha256sum

**Kit:** Base OS — present on every Linux image  **Capability:** Verify evidence integrity with hashes  **Version:** sha256sum (GNU coreutils) 9.1
**Captured:** `cyberlab-aio` via `--help` on 2026-08-01  [raw](../../capture/cyberlab-aio/help/sha256sum.help.txt)

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Print or check SHA256 (256-bit) checksums.

## Synopsis

```
sha256sum [OPTION]... [FILE]...
```

## Common invocations

<!-- candidates mined from cyberlab; verify each flag against the options table below before treating as reviewed -->
```
# from cyberlab 01-disk-forensics
sha256sum /tmp/recovered.txt
# from cyberlab 04-registry-analysis
sha256sum exercise/SYSTEM_sample.hive
# from cyberlab 05-file-carving
sha256sum /tmp/ak_tcp/*.jpg
# from cyberlab 10-malicious-documents
sha256sum exercise/sample.doc
# from cyberlab 21-yara-authoring
sha256sum exercise/eicar_sample.txt
# from cyberlab 26-metasploit-workflow
sha256sum exercise/scan.xml
# from cyberlab 32-remnux-static-triage
sha256sum exercise/sample.exe
# from cyberlab 33-binwalk-firmware
sha256sum firmware.bin
```

## Options

All 17 options parsed from the captured help text. The final column is filled in by review.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-b` | — | read in binary mode |  |
| `--binary` | — | read in binary mode |  |
| `-c` | — | read checksums from the FILEs and check them |  |
| `--check` | — | read checksums from the FILEs and check them |  |
| `--tag` | — | create a BSD-style checksum |  |
| `-t` | — | read in text mode (default) |  |
| `--text` | — | read in text mode (default) |  |
| `-z` | — | end each output line with NUL, not newline, and disable file name escaping |  |
| `--zero` | — | end each output line with NUL, not newline, and disable file name escaping |  |
| `--ignore-missing` | — | don't fail or report status for missing files |  |
| `--quiet` | — | don't print OK for each successfully verified file |  |
| `--status` | — | don't output anything, status code shows success |  |
| `--strict` | — | exit non-zero for improperly formatted checksum lines |  |
| `-w` | — | warn about improperly formatted checksum lines |  |
| `--warn` | — | warn about improperly formatted checksum lines |  |
| `--help` | — | display this help and exit |  |
| `--version` | — | output version information and exit |  |

## Gotchas

_TODO: operational traps._

## See also

[`rahash2`](../acquire-preserve/rahash2.md), [`ssdeep`](../acquire-preserve/ssdeep.md), [`md5sum`](../acquire-preserve/md5sum.md), [`sigtool`](../acquire-preserve/sigtool.md)
