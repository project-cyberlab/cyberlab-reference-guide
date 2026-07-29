<!-- generated-by: scripts/generate_pages.py -->
# mactime

**Kit:** REMnux · Kali Linux · SIFT Workstation  **Capability:** Build a filesystem MAC-time timeline
**Captured:** `cyberlab-aio` via `--help` on 2026-07-29  [raw](../../capture/cyberlab-aio/help/mactime.help.txt)  **Docs:** <https://www.sleuthkit.org/sleuthkit>

## Purpose

Analyze disk images and recover files from them.

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

All 9 options parsed from the captured help text. The final column is the judgement layer and is filled in by review.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-b` | — | Specifies the body file location, else STDIN is used | |
| `-d` | — | Output in comma delimited format | |
| `-h` | — | Display a header with session information | |
| `-y` | — | Dates are displayed in ISO 8601 format | |
| `-m` | — | Dates have month as number instead of word (does not work with -y) | |
| `-z` | — | Specify the timezone the data came from (in the local system format) (does not work with -y) | |
| `-g` | — | Specifies the group file location, else GIDs are used | |
| `-p` | — | Specifies the password file location, else UIDs are used | |
| `-V` | — | Prints the version to STDOUT | |

## Gotchas

_TODO: operational traps._

## See also

`fls`, `tsk_gettimes`
