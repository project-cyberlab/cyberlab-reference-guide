<!-- generated-by: scripts/generate_pages.py -->
# less

**Kit:** Base OS — present on every Linux image  **Capability:** Inspect files by hand  **Version:** version: No such file or directory
**Captured:** `cyberlab-aio` via `--help` on 2026-07-29  [raw](../../capture/cyberlab-aio/help/less.help.txt)

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

SSUUMMMMAARRYY OOFF LLEESSSS CCOOMMMMAANNDDSS

## Common invocations

_TODO: up to 8 task-titled invocations._

## Options

All 58 options parsed from the captured help text. The final column is filled in by review.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-?` | — | ........ --help Display help (from command line). |  |
| `-a` | — | ........ --search-skip-screen Search skips current screen. |  |
| `-A` | — | ........ --SEARCH-SKIP-SCREEN Search starts just after target line. |  |
| `-b` | _N | .... --buffers=[_N] Number of buffers. |  |
| `-B` | — | ........ --auto-buffers Don't automatically allocate buffers for pipes. |  |
| `-c` | — | ........ --clear-screen Repaint by clearing rather than scrolling. |  |
| `-d` | — | ........ --dumb Dumb terminal. |  |
| `-e` | — | .... --quit-at-eof --QUIT-AT-EOF Quit at end of file. |  |
| `-E` | — | .... --quit-at-eof --QUIT-AT-EOF Quit at end of file. |  |
| `-f` | — | ........ --force Force open non-regular files. |  |
| `-F` | — | ........ --quit-if-one-screen Quit if entire file fits on first screen. |  |
| `-g` | — | ........ --hilite-search Highlight only last match for searches. |  |
| `-G` | — | ........ --HILITE-SEARCH Don't highlight any matches for searches. |  |
| `-h` | _N | .... --max-back-scroll=[_N] Backward scroll limit. |  |
| `-i` | — | ........ --ignore-case Ignore case in searches that do not contain uppercase. |  |
| `-I` | — | ........ --IGNORE-CASE Ignore case in all searches. |  |
| `-j` | _N | .... --jump-target=[_N] Screen position of target lines. |  |
| `-J` | — | ........ --status-column Display a status column at left edge of screen. |  |
| `-k` | _f_i_l_e | . --lesskey-file=[_f_i_l_e] Use a lesskey file. |  |
| `-K` | — | ........ --quit-on-intr Exit less in response to ctrl-C. |  |
| `-L` | — | ........ --no-lessopen Ignore the LESSOPEN environment variable. |  |
| `-m` | — | .... --long-prompt --LONG-PROMPT Set prompt style. |  |
| `-M` | — | .... --long-prompt --LONG-PROMPT Set prompt style. |  |
| `-n` | — | .... --line-numbers --LINE-NUMBERS Don't use line numbers. |  |
| `-N` | — | .... --line-numbers --LINE-NUMBERS Don't use line numbers. |  |
| `-o` | _f_i_l_e | . --log-file=[_f_i_l_e] Copy to log file (standard input only). |  |
| `-O` | _f_i_l_e | . --LOG-FILE=[_f_i_l_e] Copy to log file (unconditionally overwrite). |  |
| `-p` | _p_a_t_t_e_r_n | --pattern=[_p_a_t_t_e_r_n] Start at pattern (from command line). |  |
| `-P` | _p_r_o_m_p_t | --prompt=[_p_r_o_m_p_t] Define new prompt. |  |
| `-q` | — | .... --quiet --QUIET --silent --SILENT Quiet the terminal bell. |  |
| `-Q` | — | .... --quiet --QUIET --silent --SILENT Quiet the terminal bell. |  |
| `-r` | — | .... --raw-control-chars --RAW-CONTROL-CHARS Output "raw" control characters. |  |
| `-R` | — | .... --raw-control-chars --RAW-CONTROL-CHARS Output "raw" control characters. |  |
| `-s` | — | ........ --squeeze-blank-lines Squeeze multiple blank lines. |  |
| `-S` | — | ........ --chop-long-lines Chop (truncate) long lines rather than wrapping. |  |
| `-t` | _t_a_g | .. --tag=[_t_a_g] Find a tag. |  |
| `-u` | — | .... --underline-special --UNDERLINE-SPECIAL Change handling of backspaces. |  |
| `-U` | — | .... --underline-special --UNDERLINE-SPECIAL Change handling of backspaces. |  |
| `-V` | — | ........ --version Display the version number of "less". |  |
| `-w` | — | ........ --hilite-unread Highlight first new line after forward-screen. |  |
| `-W` | — | ........ --HILITE-UNREAD Highlight first new line after any forward movement. |  |
| `-X` | — | ........ --no-init Don't use termcap init/deinit strings. |  |
| `-y` | _N | .... --max-forw-scroll=[_N] Forward scroll limit. |  |
| `-z` | _N | .... --window=[_N] Set size of window. |  |
| `-#` | _N | .... --shift=[_N] Set horizontal scroll amount (0 = one half screen width). |  |
| `--file-size` | — | Automatically determine the size of the input file. |  |
| `--follow-name` | — | The F command changes files if the input file is renamed. |  |
| `--incsearch` | — | Search file as each pattern character is typed in. |  |
| `--line-num-width` | N | Set the width of the -N line number field to N characters. |  |
| `--mouse` | — | Enable mouse input. |  |
| `--no-keypad` | — | Don't send termcap keypad init/deinit strings. |  |
| `--no-histdups` | — | Remove duplicates from command history. |  |
| `--rscroll` | C | Set the character used to mark truncated lines. |  |
| `--save-marks` | — | Retain marks across invocations of less. |  |
| `--status-col-width` | N | Set the width of the -J status column to N characters. |  |
| `--use-backslash` | — | Subsequent options use backslash as escape char. |  |
| `--use-color` | — | Enables colored text. |  |
| `--wheel-lines` | N | Each click of the mouse wheel moves N lines. |  |

## Gotchas

_TODO: operational traps._

## See also

[`xxd`](../examine-the-filesystem/xxd.md), [`ezhexviewer`](../report-support/ezhexviewer.md)
