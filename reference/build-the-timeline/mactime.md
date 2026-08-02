<!-- generated-by: scripts/generate_pages.py -->
# mactime

**Kit:** REMnux · Kali Linux · SIFT Workstation  **Capability:** Build a filesystem MAC-time timeline
**Captured:** `cyberlab-aio` via `--help` on 2026-08-01  [raw](../../capture/cyberlab-aio/help/mactime.help.txt)  **Docs:** <https://www.sleuthkit.org/sleuthkit>

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Turn a TSK body file into a human-readable chronological timeline.

## Common invocations

<!-- candidates mined from cyberlab; verify each flag against the options table below before treating as reviewed -->
```
# from cyberlab 01-disk-forensics
mactime -b /tmp/bodyfile.txt -d > /tmp/timeline.csv
# from cyberlab 03-timeline-analysis
mactime -V
# from cyberlab 03-timeline-analysis
mactime -b /tmp/body.txt -d > /tmp/mactime.csv
# from cyberlab 22-sleuthkit-mastery
mactime -b exercise/bodyfile.txt -d > exercise/timeline.csv
# from cyberlab 22-sleuthkit-mastery
mactime -b exercise/bodyfile.txt -d | tail
# from cyberlab 23-plaso-supertimeline
mactime -d -b exercise/bodyfile.txt > timeline.csv
# from cyberlab 23-plaso-supertimeline
mactime -d -b exercise/bodyfile.txt | awk -F',' '$3 ~ /b/' | sort
# from cyberlab 23-plaso-supertimeline
mactime -d -b exercise/bodyfile.txt | awk -F',' '$3 ~ /b/' | sort | head -n 1
```

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
