<!-- generated-by: scripts/generate_pages.py -->
# hivexsh

| | |
|---|---|
| **Kit** | Kali Linux |
| **Capability** | Parse registry hives |
| **Captured from** | `cyberlab-aio` via `help` on 2026-08-05 — [raw help output](../../capture/cyberlab-aio/help/hivexsh.help.txt) |

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

If you think this file is a valid Windows binary hive file (_not_

## When you'd reach for this

An analyst reaches for hivexsh when examining pagefile.sys to extract and analyze carved registry hive fragments, often after initial string or artifact extraction, to process regf and hbin blocks for registry keys, command-line patterns, or credential indicators; they may use it in conjunction with RegRipper or Registry Explorer for deeper analysis, as it specifically handles registry data recovery from pagefile.sys fragments.

**Sources:** <https://www.pagefilesysparser.com/en>

## Options

_No option definitions could be parsed from this tool's help output. It may be subcommand-driven or have no flags; needs manual review._

## Gotchas

_TODO: operational traps._

## See also

[`rip.pl`](../windows-artifacts/rip.pl.md), [`regripper`](../windows-artifacts/regripper.md), [`regfexport`](../windows-artifacts/regfexport.md), [`regfinfo`](../windows-artifacts/regfinfo.md), [`regfmount`](../windows-artifacts/regfmount.md), [`regipy-dump`](../windows-artifacts/regipy-dump.md), [`regipy-parse-header`](../windows-artifacts/regipy-parse-header.md), [`regipy-plugins-run`](../windows-artifacts/regipy-plugins-run.md)
