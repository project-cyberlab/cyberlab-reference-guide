<!-- generated-by: scripts/generate_pages.py -->
# ssdeep

| | |
|---|---|
| **Kit** | REMnux · Kali Linux · SIFT Workstation |
| **Capability** | Verify evidence integrity with hashes; Compare or cluster samples; Find hidden data |
| **Version** | 2.14.1 |
| **Captured from** | `cyberlab-aio` via `-h` on 2026-08-10 — [raw help output](../../capture/cyberlab-aio/help/ssdeep.help.txt) |
| **Documentation** | <https://ssdeep-project.github.io/ssdeep/index.html> |

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Compute Context Triggered Piecewise Hashes (CTPH), also known as fuzzy hashes.

## When you'd reach for this

An analyst reaches for ssdeep when comparing files for similarity rather than exact matches, running commands like -r to generate fuzzy hashes and -x or -k to compare signatures, as it is a mainstream tool used by NIST and can detect partial overlaps between files.

**Sources:** <https://dfir.science/2017/07/How-To-Fuzzy-Hashing-with-SSDEEP-(similarity-matching).html> · <https://ssdeep-project.github.io/ssdeep/usage.html>

## Synopsis

```
ssdeep [-m file] [-k file] [-dpgvrsblcxa] [-t val] [-h|-V] [FILES]
```

## Common invocations

```
# Generate file hashes recursively for directory tree
ssdeep -r *
# Compare signature files to detect overlapping entries
ssdeep -r /etc >list1.txt
# Compare signature files to find matching or similar entries
ssdeep -r /usr >list2.txt
# Detect source code reuse by comparing file similarities
ssdeep -b foo.txt >hashes.txt
# Detect file similarities using fuzzy hash matching
ssdeep -b -m hashes.txt bar.txt
# Check if file matches known signature for identification
ssdeep -b -m sig.txt partial.avi
```

## Options

_No option definitions could be parsed from this tool's help output. It may be subcommand-driven or have no flags; needs manual review._

## Gotchas

_TODO: operational traps._

## See also

[`rahash2`](../acquire-preserve/rahash2.md), [`sha256sum`](../acquire-preserve/sha256sum.md), [`md5sum`](../acquire-preserve/md5sum.md), [`sigtool`](../acquire-preserve/sigtool.md), [`radiff2`](../malware-triage-static/radiff2.md), [`binwalk`](../examine-the-filesystem/binwalk.md)
