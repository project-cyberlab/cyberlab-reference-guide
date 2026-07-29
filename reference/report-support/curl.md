<!-- generated-by: scripts/generate_pages.py -->
# curl

**Kit:** REMnux  **Capability:** Fetch and verify external references  **Version:** curl 7.88.1
**Captured:** `cyberlab-aio` via `--help` on 2026-07-29  [raw](../../capture/cyberlab-aio/help/curl.help.txt)  **Docs:** <https://curl.se>

## Purpose

Interact with servers via supported protocols, including HTTP, HTTPS, FTP, IMAP, etc. using this command-line tool.

## Synopsis

```
curl [options...] <url>
```

## Common invocations

<!-- candidates mined from cyberlab; verify each flag against the options table below before treating as reviewed -->
```
# from cyberlab 38-network-emulation
curl -s http://127.0.0.1/malware.bin -o /tmp/served.bin && file /tmp/served.bin
# from cyberlab 38-network-emulation
curl -s "http://$TARGET_DOMAIN/gate.php?id=203.0.113.10" -o /tmp/beacon_reply.bin
```

## Options

All 22 options parsed from the captured help text. The final column is filled in by review.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-d` | data | HTTP POST data |  |
| `--data` | data | HTTP POST data |  |
| `-f` | — | Fail fast with no output on HTTP errors |  |
| `--fail` | — | Fail fast with no output on HTTP errors |  |
| `-h` | category | Get help for commands |  |
| `--help` | category | Get help for commands |  |
| `-i` | — | Include protocol response headers in the output |  |
| `--include` | — | Include protocol response headers in the output |  |
| `-o` | file | Write to file instead of stdout |  |
| `--output` | file | Write to file instead of stdout |  |
| `-O` | — | Write output to a file named as the remote file |  |
| `--remote-name` | — | Write output to a file named as the remote file |  |
| `-s` | — | Silent mode |  |
| `--silent` | — | Silent mode |  |
| `-T` | file | Transfer local FILE to destination |  |
| `--upload-file` | file | Transfer local FILE to destination |  |
| `-A` | name | Send User-Agent <name> to server |  |
| `--user-agent` | name | Send User-Agent <name> to server |  |
| `-v` | — | Make the operation more talkative |  |
| `--verbose` | — | Make the operation more talkative |  |
| `-V` | — | Show version number and quit |  |
| `--version` | — | Show version number and quit |  |

## Gotchas

_TODO: operational traps._

## See also

`wget`
