<!-- generated-by: scripts/generate_pages.py -->
# hivexsh

| | |
|---|---|
| **Kit** | Kali Linux |
| **Capability** | Parse registry hives |
| **Captured from** | `cyberlab-aio` via `help` on 2026-08-06 — [raw help output](../../capture/cyberlab-aio/help/hivexsh.help.txt) |

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

If you think this file is a valid Windows binary hive file (_not_

## When you'd reach for this

When an analyst needs to examine Windows Registry hive files, they use hivexsh after obtaining the hive file (e.g., via virt-cat or guestfish) to navigate and inspect its keys and subkeys, as it is specifically designed for this task and provides interactive shell commands for structured exploration.

**Sources:** <https://libguestfs.org/hivexsh.1.html> · <https://manpages.ubuntu.com/manpages/xenial/man1/hivexsh.1.html>

## Options

_No option definitions could be parsed from this tool's help output. It may be subcommand-driven or have no flags; needs manual review._

## Gotchas

_TODO: operational traps._

## See also

[`rip.pl`](../windows-artifacts/rip.pl.md), [`regripper`](../windows-artifacts/regripper.md), [`regfexport`](../windows-artifacts/regfexport.md), [`regfinfo`](../windows-artifacts/regfinfo.md), [`regfmount`](../windows-artifacts/regfmount.md), [`regipy-dump`](../windows-artifacts/regipy-dump.md), [`regipy-parse-header`](../windows-artifacts/regipy-parse-header.md), [`regipy-plugins-run`](../windows-artifacts/regipy-plugins-run.md)
