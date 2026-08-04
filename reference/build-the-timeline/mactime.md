<!-- generated-by: scripts/generate_pages.py -->
# mactime

| | |
|---|---|
| **Kit** | REMnux · Kali Linux · SIFT Workstation |
| **Capability** | Build a filesystem MAC-time timeline |
| **Captured from** | `cyberlab-aio` via `--help` on 2026-08-04 — [raw help output](../../capture/cyberlab-aio/help/mactime.help.txt) |
| **Documentation** | <https://www.sleuthkit.org/sleuthkit> |

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Turn a TSK body file into a human-readable chronological timeline.

## When you'd reach for this

An analyst reaches for mactime after gathering temporal data from file systems, logs, and other sources into a body file using tools like fls, to sort and merge the data into a single timeline. They would run it after collecting and consolidating all temporal data, as it is specifically designed to handle the body file format and create a chronological view, which is critical for event reconstruction. The passages do not explicitly compare it to similar tools, but emphasize its role in merging and sorting data from multiple sources into a unified timeline.

**Sources:** <https://github.com/sleuthkit/sleuthkit/wiki/Timelines>

## Options

All 9 options parsed from the captured help text; 8 reviewed with usage guidance.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-b` | — | Specifies the body file location, else STDIN is used | Read the body file produced by `fls -m` — the normal input. |
| `-d` | — | Output in comma delimited format | Emit CSV rather than the default text, for spreadsheets or further tooling. |
| `-h` | — | Display a header with session information | Produce HTML output for a report. |
| `-y` | — | Dates are displayed in ISO 8601 format | Print dates ISO-style (year first), which sorts correctly. |
| `-m` | — | Dates have month as number instead of word (does not work with -y) | Print month numerically instead of by name. |
| `-z` | — | Specify the timezone the data came from (in the local system format) (does not work with -y) | Time zone of the evidence machine. Getting this wrong shifts the whole timeline. |
| `-g` | — | Specifies the group file location, else GIDs are used | Map group IDs to names using a supplied group file. |
| `-p` | — | Specifies the password file location, else UIDs are used | Map user IDs to names using a supplied passwd file. |
| `-V` | — | Prints the version to STDOUT |  |

## Gotchas

- `mactime` reports in the time zone you give it, not the one embedded in the evidence. An unstated `-z` silently produces a plausible, wrong timeline — state it explicitly every run.
- A date range is passed as a trailing argument (`mactime -b body.txt 2026-01-01..2026-02-01`), not as a flag.

## See also

[`fls`](../examine-the-filesystem/fls.md), [`tsk_gettimes`](../build-the-timeline/tsk_gettimes.md)
