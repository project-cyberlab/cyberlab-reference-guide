<!-- generated-by: scripts/generate_pages.py -->
# ssdeep

**Kit:** REMnux · Kali Linux · SIFT Workstation  **Capability:** Verify evidence integrity with hashes; Compare or cluster samples; Find hidden data  **Version:** 2.14.1
**Captured:** `cyberlab-aio` via `-h` on 2026-08-01  [raw](../../capture/cyberlab-aio/help/ssdeep.help.txt)  **Docs:** <https://ssdeep-project.github.io/ssdeep/index.html>

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Compute Context Triggered Piecewise Hashes (CTPH), also known as fuzzy hashes.

## Synopsis

```
ssdeep [-m file] [-k file] [-dpgvrsblcxa] [-t val] [-h|-V] [FILES]
```

## Common invocations

<!-- candidates mined from cyberlab; verify each flag against the options table below before treating as reviewed -->
```
# from cyberlab 08-malware-static-triage
ssdeep -V
# from cyberlab 08-malware-static-triage
ssdeep exercise/sample.bin
# from cyberlab 32-remnux-static-triage
ssdeep sample.exe > baseline.txt
# from cyberlab 32-remnux-static-triage
ssdeep -m baseline.txt sample_mod.exe
# from cyberlab 32-remnux-static-triage
ssdeep exercise/sample.exe > exercise/baseline.txt
# from cyberlab 32-remnux-static-triage
ssdeep -m exercise/baseline.txt exercise/sample_mod.exe
```

## Options

_No option definitions could be parsed from this tool's help output. It may be subcommand-driven or have no flags; needs manual review._

## Gotchas

_TODO: operational traps._

## See also

[`rahash2`](../acquire-preserve/rahash2.md), [`sha256sum`](../acquire-preserve/sha256sum.md), [`md5sum`](../acquire-preserve/md5sum.md), [`sigtool`](../acquire-preserve/sigtool.md), [`radiff2`](../malware-triage-static/radiff2.md), [`binwalk`](../examine-the-filesystem/binwalk.md)
