<!-- generated-by: scripts/generate_pages.py -->
# grep

**Kit:** Base OS — present on every Linux image  **Capability:** Search raw data for a pattern  **Version:** grep (GNU grep) 3.8
**Captured:** `cyberlab-aio` via `--help` on 2026-07-29  [raw](../../capture/cyberlab-aio/help/grep.help.txt)

## Purpose

Search for PATTERNS in each FILE.

## Synopsis

```
grep [OPTION]... PATTERNS [FILE]...
```

## Common invocations

<!-- candidates mined from cyberlab; verify each flag against the options table below before treating as reviewed -->
```
# from cyberlab 02-memory-forensics
grep -i "benign.lab.local" be_out/url.txt
# from cyberlab 02-memory-forensics
grep -i "analyst@lab.local" be_out/email.txt
# from cyberlab 03-timeline-analysis
grep filestat /tmp/timeline.csv | sort -t',' -k1,2 | head -n 1
# from cyberlab 04-registry-analysis
grep -i "ComputerName" /tmp/system_dump.txt | head
# from cyberlab 05-file-carving
grep -v '^#' /etc/scalpel/scalpel.conf | grep -qi jpg || printf '\njpg y 20000000 \\xff\\xd8\\xff \\xff\\xd9\n' >> /etc/scalpel/scalpel.conf
# from cyberlab 05-file-carving
grep -E 'jpg:|pdf:' /tmp/ak_foremost/audit.txt
# from cyberlab 06-windows-artifact-libs
grep -c "Record number" /tmp/security_events.txt
# from cyberlab 06-windows-artifact-libs
grep "Event Identifier" /tmp/security_events.txt | awk -F: '{print $2}' | sort | uniq -c | sort -rn | head -1
```

## Options

All 81 options parsed from the captured help text. The final column is the judgement layer and is filled in by review.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-E` | — | PATTERNS are extended regular expressions | |
| `--extended-regexp` | — | PATTERNS are extended regular expressions | |
| `-F` | — | PATTERNS are strings | |
| `--fixed-strings` | — | PATTERNS are strings | |
| `-G` | — | PATTERNS are basic regular expressions | |
| `--basic-regexp` | — | PATTERNS are basic regular expressions | |
| `-P` | — | PATTERNS are Perl regular expressions | |
| `--perl-regexp` | — | PATTERNS are Perl regular expressions | |
| `-e` | PATTERNS | use PATTERNS for matching | |
| `--regexp` | PATTERNS | use PATTERNS for matching | |
| `-f` | FILE | take PATTERNS from FILE | |
| `--file` | FILE | take PATTERNS from FILE | |
| `-i` | — | ignore case distinctions in patterns and data | |
| `--ignore-case` | — | ignore case distinctions in patterns and data | |
| `--no-ignore-case` | — | do not ignore case distinctions (default) | |
| `-w` | — | match only whole words | |
| `--word-regexp` | — | match only whole words | |
| `-x` | — | match only whole lines | |
| `--line-regexp` | — | match only whole lines | |
| `-z` | — | a data line ends in 0 byte, not newline | |
| `--null-data` | — | a data line ends in 0 byte, not newline | |
| `-s` | — | suppress error messages | |
| `--no-messages` | — | suppress error messages | |
| `-v` | — | select non-matching lines | |
| `--invert-match` | — | select non-matching lines | |
| `-V` | — | display version information and exit | |
| `--version` | — | display version information and exit | |
| `--help` | — | display this help text and exit | |
| `-m` | NUM | stop after NUM selected lines | |
| `--max-count` | NUM | stop after NUM selected lines | |
| `-b` | — | print the byte offset with output lines | |
| `--byte-offset` | — | print the byte offset with output lines | |
| `-n` | — | print line number with output lines | |
| `--line-number` | — | print line number with output lines | |
| `--line-buffered` | — | flush output on every line | |
| `-H` | — | print file name with output lines | |
| `--with-filename` | — | print file name with output lines | |
| `-h` | — | suppress the file name prefix on output | |
| `--no-filename` | — | suppress the file name prefix on output | |
| `--label` | LABEL | use LABEL as the standard input file name prefix | |
| `-o` | — | show only nonempty parts of lines that match | |
| `--only-matching` | — | show only nonempty parts of lines that match | |
| `-q` | — | suppress all normal output | |
| `--quiet` | — | suppress all normal output | |
| `--silent` | — | suppress all normal output | |
| `--binary-files` | TYPE | assume that binary files are TYPE; TYPE is 'binary', 'text', or 'without-match' | |
| `-a` | — | equivalent to --binary-files=text | |
| `--text` | — | equivalent to --binary-files=text | |
| `-I` | — | equivalent to --binary-files=without-match | |
| `-d` | ACTION | how to handle directories; ACTION is 'read', 'recurse', or 'skip' | |
| `--directories` | ACTION | how to handle directories; ACTION is 'read', 'recurse', or 'skip' | |
| `-D` | ACTION | how to handle devices, FIFOs and sockets; ACTION is 'read' or 'skip' | |
| `--devices` | ACTION | how to handle devices, FIFOs and sockets; ACTION is 'read' or 'skip' | |
| `-r` | — | like --directories=recurse | |
| `--recursive` | — | like --directories=recurse | |
| `-R` | — | likewise, but follow all symlinks | |
| `--dereference-recursive` | — | likewise, but follow all symlinks | |
| `--include` | GLOB | search only files that match GLOB (a file pattern) | |
| `--exclude` | GLOB | skip files that match GLOB | |
| `--exclude-from` | FILE | skip files that match any file pattern from FILE | |
| `--exclude-dir` | GLOB | skip directories that match GLOB | |
| `-L` | — | print only names of FILEs with no selected lines | |
| `--files-without-match` | — | print only names of FILEs with no selected lines | |
| `-l` | — | print only names of FILEs with selected lines | |
| `--files-with-matches` | — | print only names of FILEs with selected lines | |
| `-c` | — | print only a count of selected lines per FILE | |
| `--count` | — | print only a count of selected lines per FILE | |
| `-T` | — | make tabs line up (if needed) | |
| `--initial-tab` | — | make tabs line up (if needed) | |
| `-Z` | — | print 0 byte after FILE name | |
| `--null` | — | print 0 byte after FILE name | |
| `-B` | NUM | print NUM lines of leading context | |
| `--before-context` | NUM | print NUM lines of leading context | |
| `-A` | NUM | print NUM lines of trailing context | |
| `--after-context` | NUM | print NUM lines of trailing context | |
| `-C` | NUM | print NUM lines of output context | |
| `--context` | NUM | print NUM lines of output context | |
| `--group-separator` | SEP | print SEP on line between matches with context | |
| `--no-group-separator` | — | do not print separator for matches with context | |
| `-U` | — | do not strip CR characters at EOL (MSDOS/Windows) | |
| `--binary` | — | do not strip CR characters at EOL (MSDOS/Windows) | |

## Gotchas

_TODO: operational traps._

## See also

`rafind2`, `strings`, `xxd`
