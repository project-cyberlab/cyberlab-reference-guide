<!-- generated-by: scripts/generate_pages.py -->
# chainsaw

**Kit:** SIFT / Security Onion (Sigma-based log hunting)  **Capability:** Parse Windows event logs  **Version:** chainsaw 2.16.0
**Captured:** `cyberlab-aio` via `--help` on 2026-08-02  [raw](../../capture/cyberlab-aio/help/chainsaw.help.txt)

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Hunt through Windows event logs with Sigma rules and built-in detection logic, at speed.

## Synopsis

```
chainsaw [OPTIONS] <COMMAND>
```

## Options

All 6 options parsed from the captured help text; 2 reviewed with usage guidance.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `--no-banner` | — | Hide Chainsaw's banner | Suppress the banner, for clean output in a report or a pipeline. |
| `--num-threads` | NUM_THREADS | Limit the thread number (default: num of CPUs) | Cap the thread count. Defaults to every core, which is usually right on a dedicated analysis box and rude on a shared one. |
| `-h` | — | Print help |  |
| `--help` | — | Print help |  |
| `-V` | — | Print version |  |
| `--version` | — | Print version |  |

## Gotchas

- The interesting options live on the subcommands — `hunt`, `search`, `dump` — not at the top level captured here. Run `chainsaw hunt --help` for the ones that matter.
- Rules are not bundled with the binary. Without a Sigma rule set and the mapping file, `hunt` runs and finds nothing, which looks identical to a clean host.

## See also

[`evtxexport`](../windows-artifacts/evtxexport.md), [`evtxinfo`](../windows-artifacts/evtxinfo.md), [`EvtxECmd`](../windows-artifacts/EvtxECmd.md), [`hayabusa`](../windows-artifacts/hayabusa.md)
