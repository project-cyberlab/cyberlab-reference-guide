<!-- generated-by: scripts/generate_pages.py -->
# inetsim

| | |
|---|---|
| **Kit** | REMnux · Kali Linux |
| **Capability** | Simulate network services for detonation |
| **Version** | INetSim 1.3.2 |
| **Captured from** | `cyberlab-aio` via `--help` on 2026-08-07 — [raw help output](../../capture/cyberlab-aio/help/inetsim.help.txt) |
| **Documentation** | <https://www.inetsim.org/> |

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Emulate common network services and interact with malware.

## When you'd reach for this

An analyst reaches for inetsim when setting up a simulated internet environment for malware analysis, running it before detonating a sample to intercept network traffic and avoid exposing real services. They configure it alongside tools like Wireshark and Fiddler, preferring it for its ability to mimic network responses and capture traffic without requiring actual internet connectivity.

**Sources:** <https://github.com/gl0bal01/intel-codex/blob/main/Security/Analysis/sop-malware-analysis.md> · <https://seanthegeek.net/posts/beginning-malware-analysis/>

## Synopsis

```
/usr/bin/inetsim [options]
```

## Options

All 14 options parsed from the captured help text. The final column is filled in by review.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `--help` | — | Print this help message. |  |
| `--version` | — | Show version information. |  |
| `--config` | filename | Configuration file to use. |  |
| `--log-dir` | directory | Directory logfiles are written to. |  |
| `--data-dir` | directory | Directory containing service data. |  |
| `--report-dir` | directory | Directory reports are written to. |  |
| `--bind-address` | IP address | Default IP address to bind services to. Overrides configuration option 'default_bind_address'. |  |
| `--max-childs` | num | Default maximum number of child processes per service. Overrides configuration option 'default_max_childs'. |  |
| `--user` | username | Default user to run services. Overrides configuration option 'default_run_as_user'. |  |
| `--faketime-init-delta` | secs | Initial faketime delta (seconds). Overrides configuration option 'faketime_init_delta'. |  |
| `--faketime-auto-delay` | secs | Delay for auto incrementing faketime (seconds). Overrides configuration option 'faketime_auto_delay'. |  |
| `--faketime-auto-incr` | secs | Delta for auto incrementing faketime (seconds). Overrides configuration option 'faketime_auto_increment'. |  |
| `--session` | id | Session id to use. Defaults to main process id. |  |
| `--pidfile` | filename | Pid file to use. Defaults to '/var/run/inetsim.pid'. |  |

## Gotchas

_TODO: operational traps._
