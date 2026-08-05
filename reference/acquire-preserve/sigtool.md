<!-- generated-by: scripts/generate_pages.py -->
# sigtool

| | |
|---|---|
| **Kit** | REMnux · SIFT Workstation |
| **Capability** | Verify evidence integrity with hashes; Scan with signatures for known-bad |
| **Version** | ClamAV 1.4.3 |
| **Captured from** | `cyberlab-aio` via `--help` on 2026-08-05 — [raw help output](../../capture/cyberlab-aio/help/sigtool.help.txt) |
| **Documentation** | <https://www.clamav.net> |

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Inspect and build ClamAV signature databases: unpack a .cvd, list its signatures, or generate a new one from a sample. The bridge between 'ClamAV detects this' and 'here is exactly which signature fired and why'.

## Options

All 35 options parsed from the captured help text; 1 reviewed with usage guidance.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `--help` | — | Show this help |  |
| `-h` | — | Show this help |  |
| `--version` | — | Print version number and exit |  |
| `-V` | — | Print version number and exit |  |
| `--quiet` | — | Be quiet, output only error messages |  |
| `--debug` | — | Enable debug messages |  |
| `--stdout` | — | Write to stdout instead of stderr. Does not affect 'debug' messages. |  |
| `--hex-dump` | — | Convert data from stdin to a hex string and print it on stdout | An analyst would use the --hex-dump flag when needing to generate a hexadecimal representation of a file's contents for detailed forensic examination or signature creation. |
| `--md5` | FILES | Generate MD5 checksum from stdin or MD5 sigs for FILES |  |
| `--sha1` | FILES | Generate SHA1 checksum from stdin or SHA1 sigs for FILES |  |
| `--sha256` | FILES | Generate SHA256 checksum from stdin or SHA256 sigs for FILES |  |
| `--mdb` | FILES | Generate .mdb (section hash) sigs |  |
| `--imp` | FILES | Generate .imp (import table hash) sigs |  |
| `--html-normalise` | FILE | Create normalised parts of HTML file |  |
| `--ascii-normalise` | FILE | Create normalised text file from ascii source |  |
| `--utf16-decode` | FILE | Decode UTF16 encoded files |  |
| `--info` | FILE | -i FILE Print database information |  |
| `--max-bad-sigs` | NUMBER | Maximum number of mismatched signatures When building a CVD. Default: 3000 |  |
| `--flevel` | FLEVEL | Specify a custom flevel. Default: 213 |  |
| `--cvd-version` | NUMBER | Specify the version number to use for the build. Default is to use the value+1 from the current CVD in --datadir. If no datafile is found the default behaviour is to prompt for a version number, this  |  |
| `--no-cdiff` | — | Don't generate .cdiff file |  |
| `--unsigned` | — | Create unsigned database file (.cud) |  |
| `--hybrid` | — | Create a hybrid (standard and bytecode) database file |  |
| `--print-certs` | FILE | Print Authenticode details from a PE |  |
| `--server` | ADDR | ClamAV Signing Service address |  |
| `--datadir` | DIR | Use DIR as default database directory |  |
| `--unpack` | FILE | -u FILE Unpack a CVD/CLD file |  |
| `--unpack-current` | SHORTNAME | Unpack local CVD/CLD into cwd |  |
| `--list-sigs` | FILE (optional) | -l[FILE] List signature names |  |
| `--find-sigs` | REGEX | -fREGEX Find signatures matching REGEX |  |
| `--decode-sigs` | — | Decode signatures from stdin |  |
| `--vba` | FILE | Extract VBA/Word6 macro code |  |
| `--vba-hex` | FILE | Extract Word6 macro code with hex values |  |
| `--run-cdiff` | FILE | -r FILE Execute update script FILE in cwd |  |
| `--tempdir` | DIRECTORY | Create temporary files in DIRECTORY |  |

## Gotchas

_TODO: operational traps._

## See also

[`rahash2`](../acquire-preserve/rahash2.md), [`ssdeep`](../acquire-preserve/ssdeep.md), [`sha256sum`](../acquire-preserve/sha256sum.md), [`md5sum`](../acquire-preserve/md5sum.md), [`yara`](../malware-triage-static/yara.md), [`yarac`](../malware-triage-static/yarac.md), [`clamscan`](../malware-triage-static/clamscan.md), [`freshclam`](../malware-triage-static/freshclam.md)
