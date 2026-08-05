<!-- generated-by: scripts/generate_pages.py -->
# dcfldd

| | |
|---|---|
| **Kit** | Kali Linux · SIFT Workstation |
| **Capability** | Image a disk, volume or device |
| **Version** | dcfldd (dcfldd) 1.9 |
| **Captured from** | `cyberlab-aio` via `--help` on 2026-08-05 — [raw help output](../../capture/cyberlab-aio/help/dcfldd.help.txt) |

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Enhanced version of dd for forensics and security.

## When you'd reach for this

An analyst uses dcfldd when creating a verified forensic copy of a disk drive for investigation, ensuring write protection is enabled before imaging and verifying the image with hashing tools afterward, as it provides enhanced forensic features like progress tracking and error handling compared to standard dd or dc3dd.

**Sources:** <https://dohost.us/index.php/2025/11/01/creating-a-forensic-image-of-the-disk-drive-dd-dc3dd-dcfldd/> · <https://github.com/mukul975/Anthropic-Cybersecurity-Skills/blob/main/skills/acquiring-disk-image-with-dd-and-dcfldd/SKILL.md>

## Synopsis

```
dcfldd [OPTION]...
```

## Common invocations

```
# Overwrite disk with pattern to erase data securely
dcfldd pattern="00FFAACC" of=/dev/sda
# Clone disk to image file for forensic analysis
dcfldd if=/dev/sda of=/path/to/output.img
# Create zero-filled test file for analysis
dcfldd if=/dev/zero of=test bs=50M count=2
# Create a 100MB zero-filled test file
dcfldd if=/dev/zero of=test bs=1M count=100
# Create a zero-filled test file for forensic analysis or data testing
dcfldd if=/dev/zero of=test bs=100M count=1
# Create forensic disk image
dcfldd if=[/dev/sda] of=[disk.img] statusinterval=[256]
```

## Options

All 2 options parsed from the captured help text. The final column is filled in by review.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `--help` | — | display this help and exit |  |
| `--version` | — | output version information and exit |  |

## Gotchas

_TODO: operational traps._

## See also

[`dc3dd`](../acquire-preserve/dc3dd.md), [`dd`](../acquire-preserve/dd.md), [`ewfacquire`](../acquire-preserve/ewfacquire.md), [`affconvert`](../acquire-preserve/affconvert.md)
