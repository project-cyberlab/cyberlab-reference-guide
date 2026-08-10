<!-- generated-by: scripts/generate_pages.py -->
# bdeinfo

| | |
|---|---|
| **Kit** | SIFT Workstation (libyal) |
| **Capability** | Inspect or mount a forensic image container |
| **Captured from** | `cyberlab-aio` via `--help` on 2026-08-10 — [raw help output](../../capture/cyberlab-aio/help/bdeinfo.help.txt) |

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Use bdeinfo to determine information about a BitLocker Drive

## Synopsis

```
bdeinfo [ -k keys ] [ -o offset ] [ -p password ]
[ -r password ] [ -s filename ] [ -hvV ] source
```

## Common invocations

```
# Retrieve BitLocker encryption details from a drive
bdeinfo -p Password /dev/sda1
# Extract BitLocker encryption details from disk image
bdeinfo -o $((512*128)) image.dd
# Extract BitLocker volume details including recovery key and encryption method
bdeinfo -o $((512*2048)) ~/xmount_pount/Bitlocker_physisch_test.dd
```

## Options

All 8 options parsed from the captured help text; 5 reviewed with usage guidance.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-h` | — | shows this help |  |
| `-k` | — | the full volume encryption key and tweak key formatted in base16 and separated by a : character e.g. FVEK:TWEAK |  |
| `-o` | — | specify the volume offset in bytes | An analyst would use the -o flag with bdeinfo when specifying the correct byte offset for a BitLocker-encrypted volume in a disk image, after confirming the volume's presence through hexdump analysis or partition layout checks. |
| `-p` | — | specify the password/passphrase | An analyst would use the -p flag when providing a password to access a BitLocker-encrypted volume during forensic examination. |
| `-r` | — | specify the recovery password | An analyst would use the -r flag when providing a recovery password to access a BitLocker Drive Encrypted volume. |
| `-s` | — | specify the file containing the startup key. typically this file has the extension .BEK | An analyst would use the -s flag when providing a file containing a startup key to unlock a BitLocker-encrypted volume. |
| `-v` | — | verbose output to stderr | An analyst would use the -v flag when they need detailed error, verbose, or debug output during the analysis of a BitLocker Drive Encrypted volume. |
| `-V` | — | print version |  |

## Gotchas

_TODO: operational traps._

## See also

[`ewfinfo`](../acquire-preserve/ewfinfo.md), [`ewfmount`](../acquire-preserve/ewfmount.md), [`ewfverify`](../acquire-preserve/ewfverify.md), [`ewfexport`](../acquire-preserve/ewfexport.md), [`affinfo`](../acquire-preserve/affinfo.md), [`affcat`](../acquire-preserve/affcat.md), [`img_stat`](../acquire-preserve/img_stat.md), [`ntfs-3g`](../acquire-preserve/ntfs-3g.md)
