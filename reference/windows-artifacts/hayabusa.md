<!-- generated-by: scripts/generate_pages.py -->
# hayabusa

| | |
|---|---|
| **Kit** | SIFT / Security Onion (Sigma-based log hunting) |
| **Capability** | Parse Windows event logs |
| **Version** | error: unexpected argument '--version' found |
| **Captured from** | `cyberlab-aio` via `help` on 2026-08-11 — [raw help output](../../capture/cyberlab-aio/help/hayabusa.help.txt) |

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Scan Windows event logs against a bundled Sigma rule set and produce a ranked timeline of what looks like attacker activity. It is built for speed over a whole log directory, so it is the first pass that tells you which hosts and which hours deserve a closer look.

## When you'd reach for this

An analyst reaches for Hayabusa when generating fast forensics timelines from Windows event logs, either after collecting logs for offline analysis or during live-response investigations; they may run it before importing data into tools like Elastic Stack or Timesketch, as it consolidates events into structured formats and leverages Sigma rules for detection, offering speed and compatibility with enterprise-scale analysis platforms.

**Sources:** <https://github.com/Yamato-Security/hayabusa>

## Synopsis

```
hayabusa.exe <COMMAND> [OPTIONS]
hayabusa.exe help <COMMAND> or hayabusa.exe <COMMAND> -h
```

## Options

_No option definitions could be parsed from this tool's help output. It may be subcommand-driven or have no flags; needs manual review._

## Gotchas

_TODO: operational traps._

## See also

[`evtxexport`](../windows-artifacts/evtxexport.md), [`evtxinfo`](../windows-artifacts/evtxinfo.md), [`EvtxECmd`](../windows-artifacts/EvtxECmd.md), [`chainsaw`](../windows-artifacts/chainsaw.md)
