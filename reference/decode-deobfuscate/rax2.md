<!-- generated-by: scripts/generate_pages.py -->
# rax2

| | |
|---|---|
| **Kit** | REMnux · Kali Linux · SIFT Workstation |
| **Capability** | Decode, decrypt or transform encoded data |
| **Version** | rax2 6.1.9 |
| **Captured from** | `cyberlab-aio` via `--help` on 2026-08-04 — [raw help output](../../capture/cyberlab-aio/help/rax2.help.txt) |
| **Documentation** | <https://www.radare.org/n/radare2.html> |

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Examine binary files, including disassembling and debugging. Includes r2ai and decai plugins for LLM-powered analysis (API key or local Ollama required), plus the r2ghidra plugin for Ghidra decompilation via the pdg command.

## When you'd reach for this

An analyst reaches for rax2 when converting between numeric bases, decoding base64, or handling hex/IP conversions, often after extracting raw data from memory dumps or network traffic; they might run it before analyzing obfuscated shellcode or after extracting strings from a binary, preferring it over similar tools for its specific flags like -D, -i, and -C that streamline forensic tasks.

**Sources:** <https://github.com/project-cyberlab/cyberlab-reference-guide/blob/main/reference/decode-deobfuscate/rax2.md>

## Synopsis

```
rax2 [-h|...] [- | expr ...] # convert between numeric bases
int        ->  hex              ;  rax2 10
hex        ->  int              ;  rax2 0xa
-int       ->  hex              ;  rax2 -77
-hex       ->  int              ;  rax2 0xffffffb3
int        ->  bin              ;  rax2 b30
```

## Options

All 30 options parsed from the captured help text. The final column is filled in by review.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-a` | — | show ascii table ; rax2 -a |  |
| `-b` | base | output in <base> ; rax2 -b 10 0x46 |  |
| `-c` | — | output in C string ; rax2 -c 0x1234 # \x34\x12\x00\x00 |  |
| `-C` | — | dump as C byte array ; rax2 -C < bytes |  |
| `-d` | — | force integer ; rax2 -d 3 -> 3 instead of 0x3 |  |
| `-e` | — | swap endianness ; rax2 -e 0x33 |  |
| `-D` | — | base64 decode ; rax2 -D "aGVsbG8=" |  |
| `-E` | — | base64 encode ; rax2 -E "hello" |  |
| `-f` | — | floating point ; rax2 -f 6.3+2.1 |  |
| `-F` | — | stdin slurp code hex ; rax2 -F < shellcode.[c/py/js] |  |
| `-h` | — | help ; rax2 -h |  |
| `-H` | — | hash string ; rax2 -H linux osx |  |
| `-i` | — | IP address <-> LONG ; rax2 -i 3530468537 |  |
| `-j` | — | json format output ; rax2 -j 0x1234 # same as r2 -c '?j 0x1234' |  |
| `-k` | — | keep base ; rax2 -k 33+3 -> 36 |  |
| `-K` | — | randomart ; rax2 -K 0x34 1020304050 |  |
| `-n` | — | newline ; append newline to output (for -E/-D/-r/..) |  |
| `-o` | — | octalstr -> raw ; rax2 -o \162 \62 # r2 |  |
| `-q` | — | quiet mode ; rax2 -qC < /etc/hosts # be quiet |  |
| `-r` | — | r2 style output ; rax2 -r 0x1234 # same as r2 -c '? 0x1234' |  |
| `-s` | — | hexstr -> raw ; rax2 -s 43 4a 50 |  |
| `-S` | — | raw -> hexstr ; rax2 -S < /bin/ls > ls.hex |  |
| `-t` | — | tstamp -> str ; rax2 -t 1234567890 |  |
| `-u` | — | units ; rax2 -u 389289238 # 317.0M |  |
| `-v` | — | version ; rax2 -v |  |
| `-w` | — | signed word ; rax2 -w 0xffff 0xffff_ffff '0xff&0xfffff' |  |
| `-x` | — | output in hexpairs ; rax2 -x 0x1234 # 34120000 |  |
| `-X` | — | bin -> hex(bignum) ; rax2 -X 111111111 # 0x1ff |  |
| `-z` | — | str -> bin ; rax2 -z hello |  |
| `-Z` | — | bin -> str ; rax2 -Z 01000101 01110110 |  |

## Gotchas

_TODO: operational traps._

## See also

[`cyberchef`](../decode-deobfuscate/cyberchef.md), [`base64dump.py`](../malware-triage-static/base64dump.py.md), [`xxd`](../examine-the-filesystem/xxd.md), [`openssl`](../decode-deobfuscate/openssl.md), [`numbers-to-string.py`](../malware-triage-static/numbers-to-string.py.md)
