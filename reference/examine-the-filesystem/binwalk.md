<!-- generated-by: scripts/generate_pages.py -->
# binwalk

**Kit:** REMnux · Kali Linux  **Capability:** Carve files out of unstructured data; Detect and reverse packing; Find hidden data
**Captured:** `cyberlab-aio` via `--help` on 2026-07-29  [raw](../../capture/cyberlab-aio/help/binwalk.help.txt)  **Docs:** <https://github.com/ReFirmLabs/binwalk>

## Purpose

Extract and analyze firmware images.

## Synopsis

```
binwalk [OPTIONS] [FILE1] [FILE2] [FILE3] ...
```

## Common invocations

<!-- candidates mined from cyberlab; verify each flag against the options table below before treating as reviewed -->
```
# from cyberlab 33-binwalk-firmware
binwalk --help | head -n 3
# from cyberlab 33-binwalk-firmware
binwalk firmware.bin
# from cyberlab 33-binwalk-firmware
binwalk -e firmware.bin
# from cyberlab 33-binwalk-firmware
binwalk -E firmware.bin
```

## Options

All 102 options parsed from the captured help text. The final column is the judgement layer and is filled in by review.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-B` | — | Scan target file(s) for common file signatures | |
| `--signature` | — | Scan target file(s) for common file signatures | |
| `-R` | str | Scan target file(s) for the specified sequence of bytes | |
| `--raw` | str | Scan target file(s) for the specified sequence of bytes | |
| `-A` | — | Scan target file(s) for common executable opcode signatures | |
| `--opcodes` | — | Scan target file(s) for common executable opcode signatures | |
| `-m` | file | Specify a custom magic file to use | |
| `--magic` | file | Specify a custom magic file to use | |
| `-b` | — | Disable smart signature keywords | |
| `--dumb` | — | Disable smart signature keywords | |
| `-I` | — | Show results marked as invalid | |
| `--invalid` | — | Show results marked as invalid | |
| `-x` | str | Exclude results that match <str> | |
| `--exclude` | str | Exclude results that match <str> | |
| `-y` | str | Only show results that match <str> | |
| `--include` | str | Only show results that match <str> | |
| `-e` | — | Automatically extract known file types | |
| `--extract` | — | Automatically extract known file types | |
| `-D` | type[:ext[:cmd | Extract <type> signatures (regular expression), give the files an extension of <ext>, and execute <cmd> | |
| `--dd` | type[:ext[:cmd | Extract <type> signatures (regular expression), give the files an extension of <ext>, and execute <cmd> | |
| `-M` | — | Recursively scan extracted files | |
| `--matryoshka` | — | Recursively scan extracted files | |
| `-d` | int | Limit matryoshka recursion depth (default: 8 levels deep) | |
| `--depth` | int | Limit matryoshka recursion depth (default: 8 levels deep) | |
| `-C` | str | Extract files/folders to a custom directory (default: current working directory) | |
| `--directory` | str | Extract files/folders to a custom directory (default: current working directory) | |
| `-j` | int | Limit the size of each extracted file | |
| `--size` | int | Limit the size of each extracted file | |
| `-n` | int | Limit the number of extracted files | |
| `--count` | int | Limit the number of extracted files | |
| `-0` | str | Execute external extraction utilities with the specified user's privileges | |
| `--run-as` | str | Execute external extraction utilities with the specified user's privileges | |
| `-1` | — | Do not sanitize extracted symlinks that point outside the extraction directory (dangerous) | |
| `--preserve-symlinks` | — | Do not sanitize extracted symlinks that point outside the extraction directory (dangerous) | |
| `-r` | — | Delete carved files after extraction | |
| `--rm` | — | Delete carved files after extraction | |
| `-z` | — | Carve data from files, but don't execute extraction utilities | |
| `--carve` | — | Carve data from files, but don't execute extraction utilities | |
| `-V` | — | Extract into sub-directories named by the offset | |
| `--subdirs` | — | Extract into sub-directories named by the offset | |
| `-E` | — | Calculate file entropy | |
| `--entropy` | — | Calculate file entropy | |
| `-F` | — | Use faster, but less detailed, entropy analysis | |
| `--fast` | — | Use faster, but less detailed, entropy analysis | |
| `-J` | — | Save plot as a PNG | |
| `--save` | — | Save plot as a PNG | |
| `-Q` | — | Omit the legend from the entropy plot graph | |
| `--nlegend` | — | Omit the legend from the entropy plot graph | |
| `-N` | — | Do not generate an entropy plot graph | |
| `--nplot` | — | Do not generate an entropy plot graph | |
| `-H` | float | Set the rising edge entropy trigger threshold (default: 0.95) | |
| `--high` | float | Set the rising edge entropy trigger threshold (default: 0.95) | |
| `-L` | float | Set the falling edge entropy trigger threshold (default: 0.85) | |
| `--low` | float | Set the falling edge entropy trigger threshold (default: 0.85) | |
| `-W` | — | Perform a hexdump / diff of a file or files | |
| `--hexdump` | — | Perform a hexdump / diff of a file or files | |
| `-G` | — | Only show lines containing bytes that are the same among all files | |
| `--green` | — | Only show lines containing bytes that are the same among all files | |
| `-i` | — | Only show lines containing bytes that are different among all files | |
| `--red` | — | Only show lines containing bytes that are different among all files | |
| `-U` | — | Only show lines containing bytes that are different among some files | |
| `--blue` | — | Only show lines containing bytes that are different among some files | |
| `-u` | — | Only display lines that are the same between all files | |
| `--similar` | — | Only display lines that are the same between all files | |
| `-w` | — | Diff all files, but only display a hex dump of the first file | |
| `--terse` | — | Diff all files, but only display a hex dump of the first file | |
| `-X` | — | Scan for raw deflate compression streams | |
| `--deflate` | — | Scan for raw deflate compression streams | |
| `-Z` | — | Scan for raw LZMA compression streams | |
| `--lzma` | — | Scan for raw LZMA compression streams | |
| `-P` | — | Perform a superficial, but faster, scan | |
| `--partial` | — | Perform a superficial, but faster, scan | |
| `-S` | — | Stop after the first result | |
| `--stop` | — | Stop after the first result | |
| `-l` | int | Number of bytes to scan | |
| `--length` | int | Number of bytes to scan | |
| `-o` | int | Start scan at this file offset | |
| `--offset` | int | Start scan at this file offset | |
| `-O` | int | Add a base address to all printed offsets | |
| `--base` | int | Add a base address to all printed offsets | |
| `-K` | int | Set file block size | |
| `--block` | int | Set file block size | |
| `-g` | int | Reverse every n bytes before scanning | |
| `--swap` | int | Reverse every n bytes before scanning | |
| `-f` | file | Log results to file | |
| `--log` | file | Log results to file | |
| `-c` | — | Log results to file in CSV format | |
| `--csv` | — | Log results to file in CSV format | |
| `-t` | — | Format output to fit the terminal window | |
| `--term` | — | Format output to fit the terminal window | |
| `-q` | — | Suppress output to stdout | |
| `--quiet` | — | Suppress output to stdout | |
| `-v` | — | Enable verbose output | |
| `--verbose` | — | Enable verbose output | |
| `-h` | — | Show help output | |
| `--help` | — | Show help output | |
| `-a` | str | Only scan files whose names match this regex | |
| `--finclude` | str | Only scan files whose names match this regex | |
| `-p` | str | Do not scan files whose names match this regex | |
| `--fexclude` | str | Do not scan files whose names match this regex | |
| `-s` | int | Enable the status server on the specified port | |
| `--status` | int | Enable the status server on the specified port | |

## Gotchas

_TODO: operational traps._

## See also

`foremost`, `scalpel`, `tcpxtract`, `upx`, `die`, `diec`, `7za`, `unzip`
