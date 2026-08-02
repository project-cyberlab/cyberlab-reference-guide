#!/usr/bin/env python3
"""The judgement layer, kept separate from generated content.

Generated pages carry facts read off the binary. This file carries the things a
binary cannot tell you: why you would reach for a flag, and what will bite you.

Kept apart from generate_pages.py deliberately -- regenerating pages from fresh
captures must never destroy curation, and a reviewer must be able to see, in
one place, exactly which claims are human judgement rather than captured fact.

`when` keys only ANNOTATE flags that already exist in a page's options table.
They cannot introduce a flag, so this file cannot reintroduce the fabrication
problem it exists to avoid.
"""
from __future__ import annotations

ENRICHMENT: dict[str, dict] = {

    # Invocations are written by hand, one task per entry. Every flag used in
    # them exists in that tool's capture, because the linter checks flags found
    # in fenced blocks against the captured help and fails the build on one
    # that does not. The task line matters as much as the command: a bare
    # command is something to copy, a labelled one is something to learn.

    # --- Purposes -----------------------------------------------------------
    # Written because the parsed ones were unusable. parse_purpose takes the
    # first plausible line of the help text, and for these tools that line was
    # a banner, a field label or a synopsis: "Description:", "or:  dd OPTION",
    # "hashcat (v6.2.6) starting in help mode". Each of these says what the
    # tool is for to someone who has not met it.

    "AppCompatCacheParser": {
        "purpose": "Parse the Application Compatibility Cache (Shimcache) out "
                   "of the SYSTEM registry hive. Windows records an executable "
                   "here when the shim engine examines it, which happens for "
                   "programs that were run and for some that were merely "
                   "present — so it is evidence of existence and interest, not "
                   "proof of execution.",
    },
    "RECmd": {
        "purpose": "Query and export Windows registry hives from the command "
                   "line, using batch files of plugin definitions to pull "
                   "known-interesting keys in one pass. The batch approach is "
                   "the point: it turns 'check the usual persistence "
                   "locations' into one reproducible command.",
    },
    "SrumECmd": {
        "purpose": "Parse the System Resource Usage Monitor database, which "
                   "Windows keeps for roughly 30 days. It records bytes sent "
                   "and received per application per user — the artifact that "
                   "answers 'how much data left this host, and which process "
                   "sent it?' long after the network logs have rolled.",
    },
    "dd": {
        "purpose": "Copy data block by block, without interpreting it. In "
                   "forensics this is the plain-raw imaging tool: it will read "
                   "a whole device including unallocated space, but it has no "
                   "hashing, no error recovery and no metadata. Prefer "
                   "`dc3dd`, `dcfldd` or `ewfacquire` for evidence; reach for "
                   "`dd` when you need a byte range and nothing else.",
    },
    "xxd": {
        "purpose": "Produce a hex dump, or reverse one back into binary with "
                   "`-r`. The reverse direction is what distinguishes it from "
                   "a viewer: edit the hex, convert it back, and you have "
                   "carved or patched a file without a hex editor.",
    },
    "hashcat": {
        "purpose": "Recover passwords from hashes using GPU-accelerated "
                   "guessing — dictionary, rule-mutated, mask and brute-force "
                   "attacks across several hundred hash types. In DFIR it is "
                   "usually pointed at credentials recovered from a host to "
                   "establish what an attacker could have reused elsewhere.",
    },
    "nping": {
        "purpose": "Craft and send arbitrary network packets, and report what "
                   "comes back. Unlike `ping` it will build TCP, UDP, ICMP or "
                   "raw ARP probes with chosen flags and payloads, which makes "
                   "it the tool for asking a firewall or an IDS a precise "
                   "question about what it permits.",
    },
    "regripper": {
        "purpose": "Run plugins against a Windows registry hive and print what "
                   "each finds. The plugins encode where the interesting keys "
                   "live and how to interpret them, so it answers 'what is in "
                   "this hive that matters?' without you memorising key paths.",
    },
    "rip.pl": {
        "purpose": "The command-line entry point to RegRipper — run one plugin "
                   "or a whole profile against a registry hive. Scriptable in "
                   "a way the GUI is not, which is what makes it the form used "
                   "in a pipeline.",
    },
    "hayabusa": {
        "purpose": "Scan Windows event logs against a bundled Sigma rule set "
                   "and produce a ranked timeline of what looks like attacker "
                   "activity. It is built for speed over a whole log directory, "
                   "so it is the first pass that tells you which hosts and "
                   "which hours deserve a closer look.",
    },
    "tcpflow": {
        "purpose": "Reassemble TCP streams from a capture and write each "
                   "conversation to its own file. Where a packet tool shows "
                   "you frames, this gives you the bytes each side actually "
                   "sent, in order — which is what you need to read a protocol "
                   "or recover a transferred file.",
    },
    "tcpxtract": {
        "purpose": "Carve files out of network traffic by signature, without "
                   "understanding the protocol that carried them. Useful when "
                   "a transfer is not something a dissector recognises and you "
                   "only need the payload.",
    },
    "sigtool": {
        "purpose": "Inspect and build ClamAV signature databases: unpack a "
                   ".cvd, list its signatures, or generate a new one from a "
                   "sample. The bridge between 'ClamAV detects this' and "
                   "'here is exactly which signature fired and why'.",
    },
    "freshclam": {
        "purpose": "Update ClamAV's signature databases. Worth knowing in an "
                   "air-gapped lab, where it will fail silently and leave "
                   "`clamscan` quietly scanning with signatures that are "
                   "months old.",
    },
    "pcodedmp": {
        "purpose": "Disassemble the VBA p-code stored alongside macro source "
                   "in an Office document. The two can disagree: an attacker "
                   "can leave innocuous source in place while the p-code that "
                   "actually executes does something else, and this is how you "
                   "see the difference.",
    },
    "pdf-parser.py": {
        "purpose": "Walk a PDF's object graph and show what each object "
                   "contains, decoding streams on request. Where `pdfid` "
                   "counts suspicious keywords, this resolves references and "
                   "shows the actual content — the step from 'this PDF "
                   "contains JavaScript' to 'here is the JavaScript'.",
    },
    "pdf-parser": {
        "purpose": "Walk a PDF's object graph and show what each object "
                   "contains, decoding streams on request. Where `pdfid` "
                   "counts suspicious keywords, this resolves references and "
                   "shows the actual content — the step from 'this PDF "
                   "contains JavaScript' to 'here is the JavaScript'.",
    },
    "affinfo": {
        "purpose": "Print the metadata of an AFF forensic container: acquisition "
                   "details, hashes and segment layout. The AFF equivalent of "
                   "`ewfinfo`, and the fastest way to see what an .aff file "
                   "claims about its own provenance.",
    },
    "affcat": {
        "purpose": "Stream the raw contents of an AFF container to stdout, so "
                   "tools that cannot read AFF can be fed the image through a "
                   "pipe rather than a full conversion to raw.",
    },
    "affconvert": {
        "purpose": "Convert between AFF and raw images in either direction. The "
                   "usual reason is a tool that only reads one of them; keep "
                   "the original, because converting to raw discards the "
                   "metadata and hashes AFF was carrying.",
    },
    "md5sum": {
        "purpose": "Compute or verify MD5 checksums. Still everywhere in DFIR "
                   "for matching files against hash sets, but MD5 is broken "
                   "for collisions — use it to say two files are the same, "
                   "never to prove a file is what it claims.",
    },
    "openssl": {
        "purpose": "The general-purpose crypto toolkit: inspect certificates, "
                   "compute digests, encrypt and decrypt, and speak TLS to a "
                   "service. In analysis it is most often used to read a "
                   "certificate a sample presented, or to decrypt a blob once "
                   "the key is known.",
    },
    "regipy-dump": {
        "purpose": "Dump a registry hive to JSON with regipy, so the contents "
                   "can be searched, diffed or fed into other tooling rather "
                   "than read key by key.",
    },
    "regipy-plugins-run": {
        "purpose": "Run regipy's plugins over a hive and emit structured "
                   "results. The Python counterpart to RegRipper, and the "
                   "easier one to embed in a pipeline because the output is "
                   "JSON rather than formatted text.",
    },
    "regipy-diff": {
        "purpose": "Diff two registry hives and report what changed between "
                   "them. The artifact-level version of a before-and-after "
                   "detonation: snapshot, run the sample, snapshot again, and "
                   "read the delta.",
    },
    "regipy-parse-header": {
        "purpose": "Print a hive's header — sequence numbers, timestamp and "
                   "whether it was cleanly unmounted. A dirty hive means "
                   "transaction logs still hold recent changes, so this is the "
                   "check that tells you whether you are reading the whole "
                   "story.",
    },
    "hydra": {
        "purpose": "Test credentials against a network service across many "
                   "protocols. In an authorised engagement it answers whether "
                   "a recovered password works elsewhere; it is loud, it locks "
                   "accounts, and it belongs nowhere near production without "
                   "written permission.",
    },

    "mmls": {
        "purpose": "Display the partition layout of a disk image, including "
                   "unallocated gaps.",
        "invocations": [
            {"task": "First look at an unknown disk image",
             "cmd": "mmls {{image.dd}}"},
            {"task": "The offset you need for every other TSK tool is the "
                     "Start column, in sectors",
             "cmd": "mmls {{image.dd}}   # then: fls -o {{2048}} {{image.dd}}"},
            {"task": "Force the volume-system type when detection guesses wrong",
             "cmd": "mmls -t dos {{image.dd}}"},
            {"task": "Read an E01 rather than a raw image",
             "cmd": "mmls -i ewf {{image.E01}}"},
            {"task": "4Kn drive, where the 512-byte default computes every "
                     "offset wrong",
             "cmd": "mmls -b 4096 {{image.dd}}"},
            {"task": "Show only the gaps, where a hidden partition would sit",
             "cmd": "mmls -A {{image.dd}}"},
        ],
        "when": {
            "-t": "Force the volume-system type when auto-detection guesses wrong "
                  "(`-t list` shows the options).",
            "-i": "Set the image format for non-raw evidence such as E01 or AFF.",
            "-o": "Read a volume system nested at an offset — rare, but needed for "
                  "nested containers.",
            "-b": "Set the device sector size; required on 4Kn drives where the "
                  "512-byte default is wrong.",
            "-a": "Show allocated volumes only, when the gap entries are noise.",
            "-A": "Show unallocated space only — where a hidden or deleted "
                  "partition would show up.",
            "-r": "Recurse into nested volume systems (e.g. an extended partition).",
            "-B": "Print volume sizes in bytes rather than sectors, when reporting.",
            "-v": "Verbose diagnostics to stderr when an image will not parse.",
        },
        "gotchas": [
            "The **Start** column is in sectors. That value is what every other "
            "TSK tool wants for `-o`. Multiplying by the sector size here is the "
            "single most common mistake in a TSK workflow.",
            "If `mmls` reports no partition table, the image may be a single "
            "volume rather than a whole disk — try `fsstat` on it directly at "
            "offset 0 before assuming the image is corrupt.",
        ],
    },

    "icat": {
        "purpose": "Extract the contents of a file by inode, including deleted files.",
        "when": {
            "-r": "Attempt recovery of a deleted file — the reason you usually "
                  "reach for icat.",
            "-R": "Recover with slack space included, when you want everything the "
                  "blocks still hold.",
            "-s": "Include slack space in the output.",
            "-h": "Skip holes in sparse files so the output is not padded with zeroes.",
            "-o": "Partition offset in sectors, from `mmls`.",
            "-f": "Force the filesystem type when detection is wrong.",
            "-i": "Image format for non-raw evidence.",
            "-k": "Supply a decryption password for an encrypted volume.",
        },
        "gotchas": [
            "Always redirect to a file (`icat ... > out.bin`). Binary content "
            "dumped to a terminal will corrupt your session.",
            "A deleted inode listed by `fls -d` may return nothing or garbage: the "
            "metadata survived but the blocks were reallocated. Empty output is "
            "evidence, not a tool failure.",
        ],
    },

    "istat": {
        "purpose": "Show the full metadata for one inode: times, size, and the "
                   "blocks it occupies.",
        "when": {
            "-z": "Set the time zone for the displayed timestamps.",
            "-s": "Apply a clock skew in seconds for a known-bad system clock.",
            "-N": "Limit how many block addresses are printed for a large file.",
            "-o": "Partition offset in sectors, from `mmls`.",
            "-r": "Include recovery information for a deleted inode.",
        },
        "gotchas": [
            "The block list is what lets you prove whether a deleted file is still "
            "recoverable — cross-check it before promising a recovery.",
        ],
    },

    "mactime": {
        "purpose": "Turn a TSK body file into a human-readable chronological timeline.",
        "when": {
            "-b": "Read the body file produced by `fls -m` — the normal input.",
            "-d": "Emit CSV rather than the default text, for spreadsheets or "
                  "further tooling.",
            "-z": "Time zone of the evidence machine. Getting this wrong shifts "
                  "the whole timeline.",
            "-y": "Print dates ISO-style (year first), which sorts correctly.",
            "-m": "Print month numerically instead of by name.",
            "-g": "Map group IDs to names using a supplied group file.",
            "-p": "Map user IDs to names using a supplied passwd file.",
            "-h": "Produce HTML output for a report.",
        },
        "gotchas": [
            "`mactime` reports in the time zone you give it, not the one embedded "
            "in the evidence. An unstated `-z` silently produces a plausible, "
            "wrong timeline — state it explicitly every run.",
            "A date range is passed as a trailing argument "
            "(`mactime -b body.txt 2026-01-01..2026-02-01`), not as a flag.",
        ],
    },

    "yara": {
        "purpose": "Scan files, directories or live processes against YARA rules.",
        "when": {
            "-r": "Recurse into directories — the usual mode when triaging a tree.",
            "-s": "Print the matching strings and their offsets. Essential for "
                  "verifying a hit is real rather than trusting the rule name.",
            "-f": "Fast matching mode; faster but can miss some overlapping matches.",
            "-c": "Print only the count of matches per file, for a quick sweep.",
            "-n": "Print files that do NOT match — useful for finding the odd one out.",
            "-w": "Suppress warnings, which are noisy on large third-party rulesets.",
            "-m": "Print rule metadata, which usually carries author and reference.",
            "-t": "Scan only rules carrying a given tag.",
            "-d": "Define an external variable a rule expects, e.g. `-d filename=x`.",
            "-C": "Load a pre-compiled ruleset (from `yarac`) instead of source.",
            "-p": "Use N threads to speed up a large scan.",
            "-i": "Scan only the rule with the given identifier.",
        },
        "gotchas": [
            "A rule that references an external variable fails to compile unless "
            "you supply it with `-d`. This is the most common 'the rule is broken' "
            "false alarm.",
            "Scanning a live process needs a PID rather than a path, and root.",
            "Compile large rulesets once with `yarac` and scan with `-C`; "
            "recompiling thousands of rules per scan dominates runtime.",
        ],
    },

    "clamscan": {
        "purpose": "Scan files and directories with the ClamAV signature engine.",
        "when": {
            "-r": "Recurse into subdirectories.",
            "-i": "Print infected files only — the flag that makes output usable.",
            "--bell": "Audible alert on detection; useful during a long live scan.",
            "--move": "Quarantine detections into a directory. Never point this at "
                      "evidence you must preserve.",
            "--copy": "Copy rather than move detections, preserving the original.",
            "--exclude": "Skip paths matching a regex — noisy or irrelevant trees.",
            "--include": "Restrict the scan to paths matching a regex.",
            "--log": "Write results to a log file for the case record.",
            "--file-list": "Scan exactly the paths listed in a file.",
            "--tempdir": "Redirect temp extraction; important when scanning large "
                         "archives on a small root filesystem.",
            "--quiet": "Only report errors, for scripted runs.",
            "--no-summary": "Suppress the trailing summary block when parsing output.",
        },
        "gotchas": [
            "Without `-i` the output lists every clean file too, which buries the "
            "hits in a large tree.",
            "`--move` and `--remove` MUTATE evidence. On an investigation, scan a "
            "copy or use `--copy` — a quarantine action on original evidence is "
            "not defensible.",
            "Signatures must be current for the result to mean anything; a stale "
            "database yields a comfortable and worthless clean result.",
        ],
    },

    "floss": {
        "purpose": "Extract strings from a binary, including obfuscated strings that "
                   "`strings` cannot see.",
        "when": {
            "-n": "Minimum string length; raise it to cut noise on large binaries.",
            "-j": "Emit JSON, for feeding results into other tooling.",
            "-q": "Quiet mode — just the strings, for piping.",
            "-v": "Verbose progress; FLOSS emulation can be slow and silent otherwise.",
            "--color": "Control colour output when redirecting to a file.",
        },
        "gotchas": [
            "FLOSS emulates code to recover decoded strings, so it is far slower "
            "than `strings` and can take minutes on a large sample. Budget for it.",
            "It is built for Windows PE files. Pointing it at an ELF or a script "
            "gives you little more than plain `strings` would.",
        ],
    },

    "foremost": {
        "purpose": "Carve files out of an image or raw data by header and footer "
                   "signatures.",
        "when": {
            "-t": "Restrict carving to given types (`jpg`, `pdf`, `all`). Narrowing "
                  "this is the difference between a usable result and 40,000 files.",
            "-i": "Input file or device to carve from.",
            "-o": "Output directory — must be empty or foremost refuses to run.",
            "-c": "Use a custom configuration file to add signatures.",
            "-a": "Write all headers found, even without a valid footer.",
            "-w": "Write the audit file only, carving nothing — a cheap dry run.",
            "-q": "Quick mode: scan only sector boundaries. Much faster, misses "
                  "embedded files.",
            "-v": "Verbose output.",
        },
        "gotchas": [
            "Carving recovers content but **not filenames or timestamps** — those "
            "live in filesystem metadata that carving bypasses. Use `tsk_recover` "
            "when the filesystem is intact and carve only what it cannot reach.",
            "The output directory must be empty; foremost aborts otherwise. This "
            "trips scripted reruns constantly.",
        ],
    },

    "binwalk": {
        "purpose": "Find and extract embedded files and filesystems inside a binary "
                   "blob or firmware image.",
        "when": {
            "-e": "Extract what is found, rather than only listing it.",
            "-M": "Recurse into extracted files (matryoshka) — for nested firmware.",
            "-d": "Limit recursion depth; unbounded `-M` can explode.",
            "-C": "Choose the output directory for extractions.",
            "-y": "Only report signatures matching this string.",
            "-x": "Exclude signatures matching this string, to cut false hits.",
            "-A": "Scan for executable opcodes to identify architecture.",
            "-E": "Entropy analysis — the fast way to spot encryption or compression.",
        },
        "gotchas": [
            "**Always timeout-guard binwalk in a harness.** Signature scanning on a "
            "large or synthetic image can run effectively forever; this project has "
            "been bitten by exactly that.",
            "`-e -M` on an unknown blob can produce an enormous directory tree. Set "
            "`-d` and carve into a scratch filesystem, not your case directory.",
            "A signature hit is a guess based on magic bytes. Confirm with `file` "
            "or entropy before reporting an embedded filesystem as fact.",
        ],
    },

    "olevba": {
        "purpose": "Extract and analyse VBA macros from Office documents.",
        "when": {
            "-a": "Show only the analysis results, skipping the macro source.",
            "-c": "Show only the macro source code.",
            "-t": "Triage mode — one compact line per file, ideal for a batch.",
            "-d": "Show the deobfuscated macro source.",
            "--decode": "Display all the decoded strings the analyser recovered.",
            "--reveal": "Substitute deobfuscated values back into the source, which "
                        "is the most readable view of a hostile macro.",
            "-p": "Supply a password for an encrypted document.",
            "-z": "Read documents from inside a zip archive.",
            "--show-pcode": "Disassemble the stored p-code — catches macros where "
                            "the VBA source and compiled p-code disagree.",
            "-l": "Set log level when diagnosing a parse failure.",
        },
        "gotchas": [
            "**VBA source and p-code can differ.** Malware abuses this so the "
            "readable source looks benign while the p-code executes. If a document "
            "is suspicious but the source is clean, check `--show-pcode`.",
            "Run this on a copy, in an isolated VM. Nothing here executes the "
            "macro, but the sample itself is still live malware.",
        ],
    },

    "vol": {
        "purpose": "Extract and analyse artifacts from a memory image using "
                   "Volatility 3 plugins.",
        "when": {
            "-f": "The memory image to analyse — required for almost every plugin.",
            "-o": "Directory for files the plugin dumps (processes, DLLs, files).",
            "-r": "Choose the renderer: `csv`/`json` when feeding another tool.",
            "-q": "Quiet — suppress the progress and INFO banner when scripting.",
            "-v": "Increase verbosity while diagnosing a symbol-table failure.",
            "-s": "Point at a local symbol-table directory — the fix for an "
                  "air-gapped host that cannot download symbols.",
            "-p": "Add a directory of custom plugins.",
            "--offline": "Never attempt a network fetch for symbols. Use this on "
                         "evidence networks so a scan cannot stall on a download.",
            "-c": "Load saved configuration from a JSON file.",
        },
        "gotchas": [
            "**Timeout-guard `vol` in any harness.** On a synthetic or truncated "
            "memory image it has pinned a core at 99% indefinitely on this project. "
            "Never run it unbounded in an automated pass.",
            "Volatility 3 takes plugin names, not v2 syntax: `windows.pslist`, not "
            "`--profile=... pslist`. Most 'plugin not found' errors are pasted v2 "
            "commands.",
            "The first run against an unfamiliar image downloads symbol tables. On "
            "an isolated network that hangs — pre-stage symbols and use `--offline`.",
        ],
    },

    "tshark": {
        "purpose": "Read, filter and dissect network captures from the command line.",
        "when": {
            "-r": "Read from a capture file — the normal forensic mode.",
            "-i": "Capture live from an interface instead of reading a file.",
            "-Y": "Apply a *display* filter (Wireshark syntax) after dissection.",
            "-f": "Apply a *capture* filter (BPF syntax) before packets are stored.",
            "-T": "Choose output format; `-T fields` gives parseable columns.",
            "-e": "With `-T fields`, name each field to print. Repeatable.",
            "-c": "Stop after N packets — a fast way to sample a huge capture.",
            "-q": "Suppress per-packet output, for use with `-z` statistics.",
            "-z": "Run a statistics tap (conversations, endpoints, protocol tree).",
            "-n": "Disable name resolution. Also stops DNS lookups leaking from an "
                  "evidence host — use it by default on an investigation.",
            "-w": "Write the (filtered) packets to a new capture file.",
            "-x": "Hex and ASCII dump of packet contents.",
            "-2": "Two-pass analysis, so fields needing later context resolve.",
        },
        "gotchas": [
            "**`-f` and `-Y` are different languages.** `-f` is BPF and applies at "
            "capture time; `-Y` is the Wireshark display filter and applies to a "
            "file. Passing display syntax to `-f` fails, sometimes silently.",
            "Name resolution is on by default and will emit DNS queries from the "
            "analysis host. Use `-n` when touching evidence.",
            "`-T fields` prints nothing useful without at least one `-e`.",
        ],
    },

    "capa": {
        "purpose": "Identify the capabilities of a binary by matching rules against "
                   "its disassembly, mapped to MITRE ATT&CK.",
        "when": {
            "-v": "Verbose: show which rules matched and where.",
            "-j": "JSON output, for feeding a triage pipeline.",
            "-r": "Use an alternate rules directory.",
            "-s": "Point at the library-identification signatures.",
            "-t": "Only run rules carrying a given tag.",
            "--os": "Force the target OS when auto-detection is wrong.",
            "-q": "Quiet output for scripted use.",
            "--restrict-to-functions": "Analyse only the named functions — useful "
                                       "on a large binary you have already triaged.",
        },
        "gotchas": [
            "capa reports *capabilities*, not verdicts. 'Can encrypt data' describes "
            "a backup tool as readily as ransomware — it narrows where to look.",
            "Packed samples yield almost nothing useful. Unpack first, or capa will "
            "just describe the packer stub.",
        ],
    },

    "strings": {
        "purpose": "Print sequences of printable characters found in a binary file.",
        "when": {
            "-n": "Minimum length. Default 4 is noisy; 8–10 cuts most false hits.",
            "-o": "Print the byte offset of each string — lets you seek back to it.",
            "-U": "Control how unicode is handled; needed for UTF-16 Windows strings.",
        },
        "gotchas": [
            "GNU `strings` reads only initialised, loaded sections by default. Use "
            "`-a` to scan the whole file — malware routinely hides outside them.",
            "It finds ASCII by default and will miss UTF-16LE strings that Windows "
            "binaries are full of. When a PE looks empty, that is usually why — "
            "reach for `floss` instead.",
        ],
    },

    "tsk_recover": {
        "purpose": "Bulk-export files from an image to a directory.",
        "when": {
            "-a": "Recover allocated (live) files only.",
            "-e": "Recover every file, allocated and deleted — the usual choice.",
            "-d": "Recover from a specified directory inode rather than the root.",
            "-o": "Partition offset in sectors, from `mmls`.",
            "-f": "Force the filesystem type.",
            "-i": "Image format for non-raw evidence.",
        },
        "gotchas": [
            "Default behaviour recovers only *deleted* files, which surprises people "
            "expecting a full export. Use `-e` for everything.",
            "This preserves paths and names, unlike carving. Prefer it whenever the "
            "filesystem metadata is intact, and carve only what it cannot reach.",
        ],
    },

    "log2timeline.py": {
        "purpose": "Extract timestamped events from evidence into a Plaso storage "
                   "file, the first half of a super-timeline.",
        "when": {
            "--parsers": "Restrict to specific parsers. A targeted run is minutes "
                         "instead of hours.",
            "--storage_file": "Where the .plaso output goes.",
            "-f": "Use a file filter to limit what gets processed.",
            "--hashers": "Compute hashes during extraction, saving a second pass.",
            "--workers": "Number of worker processes; tune to the host's cores.",
            "--status_view": "Change progress display; `none` for clean logs.",
            "--vss_stores": "Also process Volume Shadow Copies — often where the "
                            "pre-attack state survives.",
            "-z": "Time zone of the source machine.",
        },
        "gotchas": [
            "This produces a .plaso database, **not** a timeline you can read. "
            "`psort.py` is the second half; running only this looks like nothing "
            "happened.",
            "A full run on a disk image can take hours and tens of GB. Scope with "
            "`--parsers` unless you genuinely need everything.",
        ],
    },

    "psort.py": {
        "purpose": "Filter, sort and output the events in a Plaso storage file.",
        "when": {
            "-o": "Output format — `l2tcsv`, `dynamic`, `json`, or a timeline tool.",
            "-w": "Write output to a file rather than stdout.",
            "-q": "Quiet, for scripted runs.",
            "--analysis": "Run analysis plugins (tagging, sessionizing) over events.",
        },
        "gotchas": [
            "The date filter is a positional argument, not a flag. Filtering to the "
            "incident window is what makes a multi-million-event timeline usable.",
            "Output ordering follows the storage file, so always sort or filter "
            "explicitly rather than assuming chronology.",
        ],
    },

    "upx": {
        "purpose": "Pack and unpack executables with the UPX compressor.",
        "when": {
            "-d": "Decompress — the only flag you normally want in analysis.",
            "-t": "Test the file's integrity without writing anything.",
            "-l": "List compression info about the file.",
            "-k": "Keep a backup of the original file.",
            "-f": "Force the operation on a file UPX considers questionable.",
            "-q": "Quiet output.",
        },
        "gotchas": [
            "**Work on a copy.** `upx -d` rewrites the file in place, mutating your "
            "sample and invalidating its hash.",
            "Malware routinely uses a modified UPX header so stock `upx -d` refuses. "
            "Failure to unpack is itself an indicator, not a dead end.",
        ],
    },

    "xortool": {
        "purpose": "Recover the key length and key of an XOR-encrypted file by "
                   "frequency analysis.",
        "when": {
            "-l": "Fix the key length when you already know it.",
            "-c": "Give the most frequent character of the plaintext — usually `20` "
                  "(space) for text, `00` for binaries. This is the flag that makes "
                  "or breaks the attack.",
            "-m": "Maximum key length to consider.",
            "-b": "Brute-force the most frequent character rather than guessing.",
        },
        "gotchas": [
            "Output lands in an `xortool_out/` directory, not stdout. People "
            "routinely think it did nothing.",
            "`-c 00` is right far more often than the default for packed binaries, "
            "because null padding dominates.",
        ],
    },

    "pdfid": {
        "purpose": "Count the PDF tags that make a document *do* something, "
                   "and print the tally. A PDF is a set of objects, and a "
                   "handful of tag names are the ones that can execute or "
                   "fetch: `/JavaScript` and `/JS` carry script, `/OpenAction` "
                   "and `/AA` run something when the file opens or on an "
                   "event, `/Launch` starts an external program, "
                   "`/EmbeddedFile` carries another file inside this one, and "
                   "`/URI` reaches the network. A normal invoice has none of "
                   "them. Output is one line per tag with a count, so the "
                   "judgement is simply: are any non-zero, and does this "
                   "document have any business containing them? It parses "
                   "nothing and decodes nothing -- it is the ten-second look "
                   "that tells you whether to spend an hour with pdf-parser.",
        "when": {
            "-s": "Scan a directory of PDFs rather than a single file.",
            "-a": "Display all keyword counts, including zero entries.",
            "-e": "Include extra keywords beyond the default set.",
            "-d": "Disarm the PDF — neutralise /JS and /JavaScript. Produces a "
                  "safe-to-open copy; never overwrite the original.",
            "-n": "Hide zero-count keywords to shorten the output.",
            "-c": "CSV output for batch triage.",
            "-m": "Only report files scoring above a minimum, for a large sweep.",
        },
        "gotchas": [
            "`pdfid` **counts keywords; it does not parse**. A high `/JS` count is a "
            "reason to look, not proof of malice — and a crafted PDF can hide "
            "content from it. Follow up with `pdf-parser`.",
            "`/OpenAction` plus `/JS` is the classic auto-execute pair worth "
            "prioritising in triage.",
        ],
    },

    # --- Acquisition -------------------------------------------------------
    # The E01 workflow: acquire, inspect, verify, convert. This is the first
    # step of every investigation and was the least documented part of the
    # guide until the tools existed in the kit to capture from.

    "ewfacquire": {
        "purpose": "Acquire a disk, volume or device into an EWF/E01 evidence "
                   "container, with the case metadata and hashes stored inside "
                   "the image itself.",
        "when": {
            "-t": "Set the output name, without extension — ewfacquire appends "
                  "`.E01`, `.E02`… itself. The one flag you always pass.",
            "-2": "Write a second copy in the same pass. Two independent copies "
                  "for the cost of one read, which matters when the source is "
                  "failing and may not survive a second acquisition.",
            "-c": "Trade size against time. `best` on a slow USB source is often "
                  "faster overall than `none`, because the bottleneck is the "
                  "read, not the CPU.",
            "-d": "Add sha1 or sha256 alongside the default md5. Worth doing "
                  "once, at acquisition: md5 alone is increasingly challenged, "
                  "and rehashing later means reading the whole image again.",
            "-C": "Case number, stored in the image header.",
            "-D": "Description, stored in the image header.",
            "-e": "Examiner name, stored in the image header.",
            "-E": "Evidence number, stored in the image header.",
            "-N": "Free-text notes, stored in the image header. These five "
                  "metadata flags are the reason to choose E01 over a raw `dd` "
                  "image: the container describes its own provenance.",
            "-f": "Choose the EWF variant. `encase6` is the safe default for "
                  "interoperability; pick the format the tool that will read it "
                  "expects, not the newest one available.",
            "-S": "Segment size. The 1.4 GiB default suits FAT32 and optical "
                  "media; raise it on a modern filesystem to avoid hundreds of "
                  "fragments.",
            "-b": "Sectors per chunk. Larger chunks read faster but lose more "
                  "data to each unreadable sector.",
            "-g": "Error granularity — how much data around a bad sector is "
                  "discarded. Lower values preserve more of a failing disk at "
                  "the cost of speed.",
            "-r": "Read retries before giving up on a sector. Raise it for a "
                  "dying drive; lower it when retries are heating a drive that "
                  "may not survive the acquisition.",
            "-w": "Zero unreadable sectors instead of aborting, the way EnCase "
                  "does. Keeps offsets aligned so the filesystem still parses.",
            "-R": "Resume an interrupted acquisition at a safe point, instead of "
                  "restarting a multi-hour read.",
            "-u": "Unattended — suppresses the interactive prompts. Required "
                  "for any scripted or headless acquisition.",
            "-q": "Minimal status output, for logs.",
            "-l": "Write the acquisition log, including errors and hashes, to a "
                  "file. This is the record you cite later; do not skip it.",
            "-o": "Start at an offset rather than sector 0.",
            "-B": "Acquire a fixed number of bytes rather than the whole device — "
                  "with `-o`, the way to image one region.",
            "-m": "Record the media type (fixed, removable, optical, memory) in "
                  "the header.",
            "-M": "Record whether this is a physical device or a logical volume.",
            "-P": "Override bytes-per-sector. Needed on 4Kn drives where the "
                  "512-byte assumption is wrong.",
            "-p": "Process buffer size — a throughput tuning knob.",
            "-T": "Supply a CUE file when imaging optical media, so the track "
                  "layout is preserved.",
            "-s": "Swap byte pairs for a big-endian source. Rare, and wrong "
                  "unless you know the source endianness differs.",
            "-A": "Header codepage, for non-ASCII metadata.",
            "-x": "Bypass the buffered read/write path.",
            "-v": "Verbose diagnostics to stderr — worth capturing alongside "
                  "`-l` when a source is throwing read errors.",
        },
        "gotchas": [
            "The case metadata flags default to literal placeholder strings — "
            "`case_number`, `examiner_name`, `evidence_number`. Omit them and the "
            "image ships with those placeholders recorded as fact, which is worse "
            "than an empty field because it looks filled in.",
            "`-t` takes the name **without** an extension. Passing `image.E01` "
            "produces `image.E01.E01`.",
            "Acquisition is not verification. `ewfacquire` records hashes; proving "
            "the image still matches them later is `ewfverify`.",
        ],
    },

    "ewfinfo": {
        "purpose": "Show the metadata, hashes and acquisition details recorded "
                   "inside an EWF/E01 image.",
        "when": {
            "-i": "Acquisition details only — who imaged it, when, with what.",
            "-m": "Media details only — geometry, sector size, media type.",
            "-e": "Read errors recorded at acquisition. Check this before "
                  "trusting a clean-looking image: unreadable sectors are noted "
                  "here, not in the filesystem.",
            "-f": "Emit DFXML instead of text, when the output feeds a tool "
                  "rather than a person.",
            "-d": "Date format. `iso8601` is the unambiguous choice for a report.",
            "-A": "Header codepage, for images with non-ASCII metadata.",
            "-v": "Verbose diagnostics to stderr.",
        },
        "gotchas": [
            "This reads the header only. It reports the hash that was recorded at "
            "acquisition; it does not recompute it, so it cannot tell you the "
            "image is still intact. Use `ewfverify` for that.",
        ],
    },

    "ewfverify": {
        "purpose": "Recompute an EWF/E01 image's hashes and check them against "
                   "the values stored at acquisition.",
        "when": {
            "-d": "Also verify an additional digest such as sha256, when one was "
                  "recorded at acquisition.",
            "-l": "Write the verification result to a log file — the artefact "
                  "worth keeping with the case, not just terminal output.",
            "-q": "Minimal output, for scripted checks.",
            "-f": "Output format.",
            "-p": "Process buffer size.",
            "-A": "Header codepage.",
            "-v": "Verbose diagnostics to stderr.",
            "-w": "Wipe sectors that could not be read.",
            "-x": "Bypass the buffered read/write path.",
        },
        "gotchas": [
            "This reads every byte, so it takes as long as the acquisition did. "
            "Budget for that rather than discovering it mid-deadline.",
            "A pass proves the image matches what was recorded **at acquisition**. "
            "It says nothing about whether the acquisition captured the device "
            "correctly — a disk failing mid-image produces a verifiable image of "
            "incomplete data.",
        ],
    },

    "ewfexport": {
        "purpose": "Convert an EWF/E01 image to raw, or to another EWF format, "
                   "including extracting a subset of it.",
        "when": {
            "-t": "Target name. `-` writes to stdout, which lets the image be "
                  "piped straight into another tool without staging a full raw "
                  "copy on disk.",
            "-f": "Output format — `raw` for tools that cannot read EWF, or "
                  "another EWF variant for compatibility.",
            "-o": "Start offset, to export a region rather than the whole image.",
            "-B": "Number of bytes to export — with `-o`, extracts one partition.",
            "-S": "Segment size for the output.",
            "-c": "Compression for an EWF target.",
            "-d": "Calculate an additional digest over the exported data.",
            "-u": "Unattended, for scripted conversion.",
            "-q": "Minimal output.",
            "-l": "Log the export.",
            "-s": "Swap byte pairs.",
            "-b": "Sectors per chunk.",
            "-p": "Process buffer size.",
            "-A": "Header codepage.",
            "-v": "Verbose diagnostics to stderr.",
            "-w": "Zero sectors that cannot be read.",
            "-x": "Bypass the buffered read/write path.",
        },
        "gotchas": [
            "Exporting to raw discards the metadata and hashes that justified "
            "using E01. Keep the original: the raw copy is a working artefact, "
            "not the evidence.",
            "A raw export needs the full uncompressed size in free space. E01 "
            "compression routinely hides a 2 TB image inside 700 GB.",
        ],
    },

    # --- The Sleuth Kit, remainder -----------------------------------------
    # fls, icat, istat and mmls are already curated. These four complete the
    # set. Every TSK tool shares -f/-i/-b/-o/-P/-B/-v/-V, so the shared flags
    # are explained the same way on each page rather than differently, which
    # is what a reader flipping between them needs.

    "fsstat": {
        "purpose": "Report a filesystem's layout and parameters: type, block "
                   "size, inode range, and the geometry every other TSK tool "
                   "needs.",
        "when": {
            "-t": "Print only the filesystem type. The scriptable form when all "
                  "you need is a yes/no on what this volume is.",
            "-f": "Force the filesystem type when detection is wrong or the "
                  "superblock is damaged (`-f list` shows the options).",
            "-o": "Offset, in **sectors**, of the filesystem inside the image. "
                  "Take it from `mmls`; this is the flag that ties the two "
                  "tools together.",
            "-i": "Set the image format for non-raw evidence such as E01 or AFF.",
            "-b": "Device sector size. Needed on 4Kn drives, where the 512-byte "
                  "default silently computes every offset wrong.",
            "-P": "Pool type, for APFS or LVM containers that hold the volume.",
            "-B": "Starting block within a pool volume.",
            "-k": "Password for an encrypted volume.",
            "-v": "Verbose diagnostics to stderr, useful when detection fails.",
        },
        "gotchas": [
            "Run this first. Block size and inode range from `fsstat` are what "
            "make `blkls`, `icat` and `ils` output interpretable — starting "
            "anywhere else means guessing at the numbers they print.",
            "If it reports the wrong type or refuses the volume, the `-o` offset "
            "is wrong far more often than the image is corrupt.",
        ],
    },

    "ffind": {
        "purpose": "Find the file name that points at a given inode — the "
                   "reverse of a directory lookup.",
        "when": {
            "-a": "Show every name for the inode. Hard-linked files have more "
                  "than one, and stopping at the first hides that.",
            "-d": "Deleted names only. The direct answer to \"what was this "
                  "inode called before it was removed?\"",
            "-u": "Undeleted names only, when a recycled inode is returning "
                  "stale hits.",
            "-f": "Force the filesystem type (`-f list` shows the options).",
            "-o": "Offset, in sectors, from `mmls`.",
            "-i": "Image format for non-raw evidence such as E01 or AFF.",
            "-b": "Device sector size; required on 4Kn drives.",
            "-P": "Pool type, for APFS or LVM containers.",
            "-B": "Starting block within a pool volume.",
            "-v": "Verbose diagnostics to stderr.",
        },
        "gotchas": [
            "Inodes are reused. A name returned for a deleted inode may belong "
            "to whatever claimed it next, not to the file you are chasing — "
            "corroborate with `istat` timestamps before naming it in a report.",
            "This is the tool for the question `icat` provokes: you carved data "
            "out by inode and now need to say what it was called.",
        ],
    },

    "blkls": {
        "purpose": "Extract filesystem blocks — by default the unallocated "
                   "ones, which is the input a carver wants.",
        "when": {
            "-A": "Unallocated blocks. The default and the usual intent: pipe "
                  "this into `foremost` or `scalpel` so the carver reads only "
                  "free space instead of the whole image.",
            "-a": "Allocated blocks only — the inverse, when isolating live data.",
            "-e": "Every block, including filesystem metadata.",
            "-s": "Slack space only: the tail of the last block of each file, "
                  "where fragments of previous contents survive. A distinct "
                  "hunt from carving free space, and it ignores the other flags.",
            "-l": "List block details rather than emitting their contents.",
            "-f": "Force the filesystem type (`-f list` shows the options).",
            "-o": "Offset, in sectors, from `mmls`.",
            "-i": "Image format for non-raw evidence such as E01 or AFF.",
            "-b": "Device sector size; required on 4Kn drives.",
            "-P": "Pool type, for APFS or LVM containers.",
            "-B": "Starting block within a pool volume.",
            "-v": "Verbose diagnostics to stderr.",
        },
        "gotchas": [
            "Output goes to stdout and is the size of the free space — redirect "
            "it to a file on a volume that can hold it, not into a pager.",
            "Block offsets in the extracted stream do **not** match offsets in "
            "the original image, because only unallocated blocks were written. "
            "Use `-l` if you need to map a hit back to its real location.",
        ],
    },

    "ils": {
        "purpose": "List inode metadata, including inodes that no longer have a "
                   "name pointing at them.",
        "when": {
            "-p": "Orphan inodes — allocated content with no directory entry. "
                  "Files that were unlinked while still open, and a standard "
                  "hiding place worth checking explicitly.",
            "-O": "Unallocated inodes that were still open at the time of "
                  "imaging (UFS/ExtX). The same trick, caught mid-deletion.",
            "-e": "Every inode, allocated or not.",
            "-a": "Allocated inodes only.",
            "-A": "Unallocated inodes only — deleted file metadata that often "
                  "survives after the name is gone.",
            "-l": "Linked inodes (a name still points at them).",
            "-L": "Unlinked inodes (nothing does).",
            "-z": "Unused inodes.",
            "-Z": "Used inodes.",
            "-m": "mactime format — the form `mactime` consumes to build a "
                  "timeline. This is how deleted-file metadata reaches the "
                  "timeline at all.",
            "-s": "Correct for a known clock skew on the source machine, in "
                  "seconds, so times line up with other evidence.",
            "-f": "Force the filesystem type (`-f list` shows the options).",
            "-o": "Offset, in sectors, from `mmls`.",
            "-i": "Image format for non-raw evidence such as E01 or AFF.",
            "-b": "Device sector size; required on 4Kn drives.",
            "-P": "Pool type, for APFS or LVM containers.",
            "-B": "Starting block within a pool volume.",
            "-v": "Verbose diagnostics to stderr.",
        },
        "gotchas": [
            "`ils` finds metadata with no name; `ffind` turns an inode back into "
            "a name; `icat` extracts its content. Deleted-file work is usually "
            "all three in sequence.",
            "An inode surviving does not mean its data did. The blocks it points "
            "at may already be reallocated, so `icat` can return another file's "
            "contents entirely.",
        ],
    },

    # --- Windows artifacts, Eric Zimmerman's tools -------------------------
    # These share a house style: -f or -d for input, --csv/--json/--html for
    # output, --vss, --dedupe, --dt. Explaining the shared flags identically on
    # each page is deliberate; a reader moving between them should not have to
    # re-read the same idea in different words.

    "PECmd": {
        "purpose": "Parse Windows Prefetch files into evidence of what executed, "
                   "when, how often, and which files each run touched.",
        "when": {
            "-d": "Recurse a directory — the normal mode, since Prefetch is only "
                  "meaningful as a set. Point it at `C:\\Windows\\Prefetch`.",
            "-f": "A single .pf file, when chasing one binary.",
            "--csv": "Write CSV to a directory. This is the output that matters: "
                     "Prefetch is a timeline source, and Timeline Explorer or a "
                     "spreadsheet is where the pattern shows up.",
            "--csvf": "Override the generated CSV filename.",
            "--json": "JSON output, when the results feed another tool.",
            "--jsonf": "Override the generated JSON filename.",
            "--html": "XHTML report, for handing to someone who will not open a CSV.",
            "-k": "Highlight extra keywords in the output. `temp` and `tmp` are "
                  "highlighted by default; add the names you are hunting.",
            "-o": "Save the decompressed Prefetch bytes. Win10+ Prefetch is "
                  "MAM-compressed, so this is how you get something another tool "
                  "or a hex editor can read.",
            "-q": "Suppress the per-file detail. Worth it on a large directory "
                  "when the CSV is the real output.",
            "--vss": "Also parse every Volume Shadow Copy on the drive. Prefetch "
                     "rolls over at 1024 entries on Win10+, so shadow copies are "
                     "often the only place an older execution still exists.",
            "--dedupe": "Drop duplicates by SHA-1 across the source and the shadow "
                        "copies. Effectively mandatory with `--vss`, which "
                        "otherwise returns the same file many times over.",
            "--dt": "Custom timestamp format for the output.",
            "--mp": "Higher-precision timestamps, when ordering events within the "
                    "same second matters.",
        },
        "gotchas": [
            "Prefetch proves a program **ran**; it does not prove who ran it or "
            "what it did. Pair it with event logs or `AmcacheParser` before "
            "attributing anything.",
            "Absence is not evidence of absence. Prefetch can be disabled, is "
            "commonly off on SSD-era server builds, and rolls over — a missing "
            "entry means nothing on its own.",
            "The last-run timestamps are the eight most recent executions only. "
            "Older runs are gone from the file even though the run count keeps "
            "counting them.",
        ],
    },

    "EvtxECmd": {
        "purpose": "Parse Windows event logs into a normalised, filterable CSV, "
                   "mapping the useful fields out of the XML payload.",
        "when": {
            "-d": "Recurse a directory of .evtx files — the usual mode when "
                  "working from a collected `winevt\\Logs`.",
            "-f": "A single log, when you already know which one matters.",
            "--csv": "Write CSV to a directory. The normal output, and the form "
                     "the rest of a timeline workflow expects.",
            "--csvf": "Override the generated CSV filename.",
            "--json": "JSON output, for feeding another tool.",
            "--jsonf": "Override the generated JSON filename.",
            "--xml": "XML output.",
            "--xmlf": "Override the generated XML filename.",
            "--inc": "Process only these Event IDs. The fastest way to cut a "
                     "multi-gigabyte log down to the question being asked — "
                     "ranges are allowed (`4624,4625,5410-5500`).",
            "--exc": "Process everything except these Event IDs. `--inc` wins if "
                     "both are given.",
            "--sd": "Drop events older than this date (UTC).",
            "--ed": "Drop events newer than this date (UTC). With `--sd`, scopes "
                    "the parse to the incident window instead of all history.",
            "--maps": "Where the event maps live. The maps are what turn raw XML "
                      "into named columns; without the right ones, useful fields "
                      "stay buried in the payload.",
            "--sync": "Pull the latest maps from upstream. Worth doing before a "
                      "big parse — map coverage improves continuously.",
            "--vss": "Also parse every Volume Shadow Copy on the drive, which is "
                     "where cleared or rotated logs may survive.",
            "--dedupe": "Drop duplicates by SHA-1 across the source and shadow "
                        "copies. Use it whenever `--vss` is on.",
            "--tdt": "Seconds of tolerance for time-discrepancy detection — flags "
                     "records whose timestamps disagree, a clock-tampering signal.",
            "--fj": "Export all available data in JSON rather than the mapped "
                    "subset.",
            "--met": "Show per-log metrics about what was processed.",
            "--dt": "Custom timestamp format for the output.",
        },
        "gotchas": [
            "Without a map for an Event ID, the interesting values stay inside "
            "the XML payload rather than becoming columns. If an expected field "
            "is missing, the map is usually the reason, not the log.",
            "A cleared log is itself the finding: Security 1102 and System 104 "
            "record the clearing. Include them explicitly when hunting "
            "anti-forensics.",
            "Event log timestamps are recorded in UTC but `--sd`/`--ed` are only "
            "as good as your assumption about the host's clock. Corroborate "
            "before building a timeline on them.",
        ],
    },

    "AmcacheParser": {
        "purpose": "Parse Amcache.hve — the record of programs present on a "
                   "host, with SHA-1 hashes, including binaries that have since "
                   "been deleted.",
        "when": {
            "-f": "The Amcache.hve to parse.",
            "-i": "Include file entries associated with Programs entries. More "
                  "complete, and noisier.",
            "-b": "Whitelist of SHA-1 hashes to include.",
            "-w": "Blacklist of SHA-1 hashes to exclude. Blacklisting overrides "
                  "whitelisting, so a hash in both is dropped — the safe default "
                  "when suppressing known-good noise.",
            "--csv": "Write CSV to a directory. The usual output.",
            "--csvf": "Override the generated CSV filename.",
            "--nl": "Ignore transaction logs for a dirty hive. Leave this off "
                    "unless you know why you want it: skipping the logs means "
                    "parsing a hive that is missing its most recent changes.",
            "--dt": "Custom timestamp format for the output.",
            "--mp": "Higher-precision timestamps.",
        },
        "gotchas": [
            "Amcache records that a binary was **present**, not that it ran. It "
            "is evidence of existence; Prefetch and event logs are evidence of "
            "execution. Conflating the two is the standard error with this "
            "artifact.",
            "It carries SHA-1 for entries, which makes it the fastest way to tie "
            "a deleted binary to threat intelligence long after the file is gone.",
            "The hive is usually dirty when collected from a live host. Let the "
            "transaction logs replay — the entries only in the logs are the most "
            "recent, which is normally the part you care about.",
        ],
    },

    # --- Memory and bulk data ----------------------------------------------
    # volatility3 and bulk_extractor both list short and long forms as separate
    # rows, so both spellings are annotated. Saying "see -x" on the long form
    # would leave whichever one the reader looked up first unexplained.

    "volatility3": {
        "purpose": "Analyse a memory image. These are the framework-wide "
                   "options; each plugin adds its own, shown by "
                   "`volatility3 <plugin> --help`.",
        "when": {
            "-f": "The memory image. Almost every invocation starts here.",
            "--file": "The memory image. Almost every invocation starts here.",
            "-r": "Output renderer. `csv` or `jsonl` when the result feeds "
                  "another tool; `pretty` is for reading, not for parsing.",
            "--renderer": "Output renderer. `csv` or `jsonl` when the result "
                          "feeds another tool; `pretty` is for reading.",
            "-o": "Directory for files the plugin writes — dumped processes, "
                  "extracted DLLs. Required before any `--dump` plugin option "
                  "does anything useful.",
            "--output-dir": "Directory for files the plugin writes. Required "
                            "before any `--dump` plugin option is useful.",
            "-s": "Where to find symbol tables. The usual fix when a Linux or "
                  "macOS image will not resolve: the ISF for that exact kernel "
                  "has to be reachable.",
            "--symbol-dirs": "Where to find symbol tables — the usual fix when a "
                             "Linux or macOS image will not resolve.",
            "--offline": "Never fetch symbols online. Use it on an analysis host "
                         "that must not touch the network, and expect failures "
                         "unless the ISFs are already local.",
            "-u": "Point at an alternative ISF repository.",
            "--remote-isf-url": "Point at an alternative ISF repository.",
            "--clear-cache": "Drop cached items. First thing to try when results "
                             "look stale or an image was replaced in place.",
            "--cache-path": "Move the cache somewhere with room; it grows.",
            "--parallelism": "Enable process or thread parallelism. Off by "
                             "default, and worth turning on for a long scan.",
            "--filters": "Filter rows as `[+-]column,pattern`, so a plugin that "
                         "returns thousands of rows can be narrowed without a "
                         "second pass.",
            "--hide-columns": "Drop columns from the output to keep a wide table "
                              "readable.",
            "-p": "Additional plugin directories, for plugins outside the tree.",
            "--plugin-dirs": "Additional plugin directories.",
            "-l": "Also write output to a log file.",
            "--log": "Also write output to a log file.",
            "-q": "Suppress progress feedback, for scripted runs.",
            "--quiet": "Suppress progress feedback, for scripted runs.",
            "-v": "More verbose output; repeat for more.",
            "--verbosity": "More verbose output; repeat for more.",
            "-c": "Load options from a JSON config.",
            "--config": "Load options from a JSON config.",
            "-e": "Override a single configuration setting.",
            "--extend": "Override a single configuration setting.",
            "--write-config": "Write the resolved configuration to config.json — "
                              "useful for making a complex run reproducible.",
            "--save-config": "Write the resolved configuration to a named file.",
            "--single-location": "The image URI, when it is not a plain local "
                                 "file (`-f` is shorthand for this).",
            "--single-swap-locations": "Supply swap files alongside the image, so "
                                       "paged-out memory can be resolved.",
            "--stackers": "Control the layer stackers used to interpret the image.",
        },
        "gotchas": [
            "Symbols are the usual failure, not the image. Windows profiles are "
            "generated automatically, but Linux and macOS need an ISF matching "
            "the exact kernel build — same version is not enough.",
            "Volatility 3 dropped the Volatility 2 profile system entirely, so "
            "`--profile` from older notes and blog posts does not exist here.",
            "It has pinned CPU indefinitely on a malformed image before. Run long "
            "analyses under a timeout rather than assuming progress.",
        ],
    },

    "bulk_extractor": {
        "purpose": "Scan an image for features — email addresses, URLs, credit "
                   "card numbers, EXIF, keys — without parsing the filesystem "
                   "at all, so deleted and unallocated content is included.",
        "when": {
            "-o": "Output directory. Required, and it must not already exist "
                  "unless you also pass `-Z`.",
            "--outdir": "Output directory. Required.",
            "-E": "Run exactly one scanner and disable the rest. The fastest way "
                  "to answer a single question instead of a full sweep.",
            "--enable_exclusive": "Run exactly one scanner and disable the rest.",
            "-e": "Enable a scanner that is off by default, repeatable.",
            "--enable": "Enable a scanner that is off by default, repeatable.",
            "-x": "Disable a scanner, repeatable. Turning off the noisy ones is "
                  "usually a bigger speed win than adding threads.",
            "--disable": "Disable a scanner, repeatable.",
            "-f": "Search for a regex pattern, repeatable.",
            "--find": "Search for a regex pattern, repeatable.",
            "-F": "Read search patterns from a file — the practical form when "
                  "hunting a list of indicators.",
            "--find_file": "Read search patterns from a file.",
            "--find-case-sensitive": "Make `-f`/`-F` case-sensitive; they are not "
                                     "by default.",
            "-w": "Stop list: features to suppress. This is how you cut the "
                  "known-good noise that otherwise buries the findings.",
            "--stop_list": "Stop list of features to suppress.",
            "-r": "Alert list: features to flag prominently — the inverse of a "
                  "stop list, for known-bad indicators.",
            "--alert_list": "Alert list of features to flag prominently.",
            "-j": "Thread count. Defaults to the core count; lower it when the "
                  "scan is competing with other work.",
            "--threads": "Thread count.",
            "-J": "Single-threaded. Slow, but the first thing to try when a scan "
                  "crashes or results look non-deterministic.",
            "--no_threads": "Single-threaded — use when debugging a crash.",
            "-s": "Random sampling as `frac[:passes]`. Scans a fraction of a huge "
                  "image to judge whether a full run is worth the hours.",
            "--sampling": "Random sampling as `frac[:passes]`.",
            "-Y": "Restrict the scan to a byte range, when `mmls` already told "
                  "you which region matters.",
            "--scan": "Restrict the scan to a `<start>[-end]` byte range.",
            "-R": "Treat the input as a directory and recurse it, rather than as "
                  "a disk image.",
            "--recurse": "Treat the input as a directory and recurse it.",
            "-C": "Bytes of context stored around each hit. Raise it when a bare "
                  "match is not enough to judge relevance.",
            "--context_window": "Bytes of context stored around each hit.",
            "-M": "Maximum recursion depth into nested containers. Lower it if a "
                  "zip bomb or deeply nested archive stalls the scan.",
            "--max_depth": "Maximum recursion depth into nested containers.",
            "-Z": "Wipe the output directory first. Convenient for reruns and "
                  "destructive by definition — never point it at a directory "
                  "holding results you still need.",
            "--zap": "Wipe the output directory first — destructive.",
            "-q": "Suppress status and performance output.",
            "--quit": "Suppress status and performance output.",
            "-H": "Report what each scanner does. Worth reading once; the scanner "
                  "set is the tool.",
            "--info_scanners": "Report what each scanner does.",
            "-S": "Set a scanner option as `name=value`, repeatable.",
            "--set": "Set a scanner option as `name=value`, repeatable.",
            "-P": "Additional directories to load scanner plugins from.",
            "--scanner_dir": "Additional directories to load scanner plugins from.",
            "-A": "Add an offset to reported feature locations — use it when "
                  "scanning a carved fragment so offsets still refer to the "
                  "original image.",
            "--offset_add": "Add an offset to reported feature locations.",
            "-b": "Prepend a banner file to every feature file, e.g. a case "
                  "header.",
            "--banner_file": "Prepend a banner file to every feature file.",
            "-G": "Page size read per pass.",
            "--pagesize": "Page size read per pass.",
            "-g": "Margin carried between pages, so a feature spanning a page "
                  "boundary is still found.",
            "--marginsize": "Margin carried between pages, so features spanning a "
                            "page boundary are still found.",
            "-z": "Start at a given page number, to resume a long scan.",
            "--page_start": "Start at a given page number.",
            "-p": "Print the value at a path, with optional length and hex or raw "
                  "output — inspection rather than scanning.",
            "--path": "Print the value at a path, for inspection rather than "
                      "scanning.",
            "--log-level": "Diagnostic log level.",
            "--log-file": "Diagnostic log file; defaults inside the output "
                          "directory.",
            "-d": "Debug-level diagnostic logging.",
            "--max_minute_wait": "How long to wait for all data to be read before "
                                 "giving up — raise it for slow or failing media.",
            "--max_bad_alloc_errors": "Allocation failures tolerated before "
                                      "aborting.",
        },
        "gotchas": [
            "It ignores the filesystem completely. That is the point — it finds "
            "content in unallocated space and slack that a filesystem-aware tool "
            "cannot reach — but it also means a hit carries no filename and no "
            "timestamp. Map the offset back with `ffind`/`istat` before naming "
            "a file in a report.",
            "Feature files are raw pattern matches, not verified findings. The "
            "credit-card scanner in particular flags anything passing a Luhn "
            "check, which includes plenty of ordinary numbers.",
            "Output is large and the scan is long. Sample with `-s` on a "
            "multi-terabyte image before committing to a full pass.",
        ],
    },

    # --- Packet capture handling -------------------------------------------

    "editcap": {
        "purpose": "Cut, split, deduplicate and convert capture files — the "
                   "tool that makes an unmanageable pcap workable before "
                   "analysis starts.",
        "when": {
            "-A": "Keep only packets at or after this timestamp.",
            "-B": "Keep only packets before this timestamp. With `-A`, this is "
                  "how a multi-gigabyte capture becomes the incident window.",
            "-c": "Split into files of N packets each. The standard fix for a "
                  "capture too large for Wireshark to open.",
            "-i": "Split into files covering N seconds each — the same fix, when "
                  "time is the natural unit.",
            "-d": "Drop duplicate packets using the default 5-packet window. "
                  "Captures taken from a SPAN port routinely see each packet "
                  "twice, which distorts every count downstream.",
            "-D": "Drop duplicates with an explicit window, when `-d`'s default "
                  "is too narrow.",
            "-w": "Drop duplicates within a time window rather than a packet "
                  "count.",
            "--novlan": "Ignore VLAN tags when comparing for duplicates, so the "
                        "same frame seen on two VLANs collapses to one.",
            "-r": "Invert the selection: keep the specified packets instead of "
                  "deleting them. Easy to forget, and it reverses the meaning of "
                  "the whole command.",
            "-s": "Truncate each packet to N bytes. Strips payload while keeping "
                  "headers — the usual way to share a capture without its "
                  "contents.",
            "-L": "Adjust the recorded frame length to match after truncating, so "
                  "the file is not self-inconsistent.",
            "-t": "Shift every timestamp by a relative amount. This is how a "
                  "capture from a host with a skewed clock is aligned to the "
                  "rest of the timeline.",
            "-F": "Output file format; pcapng by default. An empty `-F` lists "
                  "the choices.",
            "-T": "Output encapsulation type, when the link type must change.",
            "--discard-all-secrets": "Strip embedded decryption secrets before "
                                     "handing the file to someone else.",
            "--capture-comment": "Attach a comment to the file — a place to "
                                 "record provenance that travels with the "
                                 "capture.",
            "--discard-capture-comment": "Remove existing comments on output.",
            "-I": "Ignore N leading bytes when comparing for duplicates.",
            "-o": "With `-E`, skip bytes before introducing errors.",
            "--seed": "With `-E`, fix the random seed so a corrupted-capture test "
                      "is reproducible.",
            "-V": "Verbose; with the duplicate options it reports what was "
                  "removed rather than silently dropping packets.",
        },
        "gotchas": [
            "`-r` inverts the selection. Without it the named packets are "
            "**deleted**, which is the opposite of what most people intend the "
            "first time.",
            "Deduplication is a heuristic over a window, not a proof. A genuine "
            "retransmission looks like a duplicate, and dropping it destroys the "
            "evidence that a retransmission occurred.",
            "Splitting renumbers packets per output file. Frame numbers cited "
            "from a split file do not refer to the original capture.",
        ],
    },

    "ngrep": {
        "purpose": "Grep packet payloads, live or from a capture, with BPF "
                   "filtering — pattern matching on the wire.",
        "when": {
            "-I": "Read from a pcap file instead of an interface. The safe mode: "
                  "no capture privileges and no risk of touching live traffic.",
            "-O": "Write matched packets to a pcap, turning a search into a "
                  "smaller capture that Wireshark can open.",
            "-i": "Case-insensitive match — usually what you want for protocol "
                  "keywords and hostnames.",
            "-w": "Match the pattern as a whole word, to stop a short string "
                  "matching inside longer ones.",
            "-X": "Treat the pattern as hexadecimal, for matching binary "
                  "signatures rather than text.",
            "-x": "Print payloads as a hexdump — necessary when the protocol is "
                  "not text.",
            "-v": "Invert the match, to see everything that is *not* the known "
                  "traffic.",
            "-t": "Print a timestamp on every match.",
            "-T": "Print the delta since the previous match; twice for delta from "
                  "the first. Useful for spotting beaconing intervals.",
            "-n": "Stop after N packets.",
            "-A": "Also print N packets following each match, for the response to "
                  "the request that matched.",
            "-d": "Choose the capture interface rather than the pcap default.",
            "-p": "Do not enter promiscuous mode — capture only traffic addressed "
                  "to this host.",
            "-s": "Set the BPF capture length.",
            "-S": "Limit how much of a matched packet is shown.",
            "-W": "Output format: `byline` is far more readable for text "
                  "protocols than the default.",
            "-F": "Read the BPF filter from a file, when it is too long to be "
                  "comfortable on a command line.",
            "-M": "Single-line matching instead of multi-line.",
            "-D": "Replay a pcap at its recorded timing rather than as fast as "
                  "possible.",
            "-e": "Show empty packets, which are otherwise hidden.",
            "-q": "Suppress the reception hash marks.",
            "-l": "Line-buffer stdout, so output appears when piped.",
            "-c": "Force the column width.",
            "-P": "Set the character shown for non-printable bytes.",
            "-N": "Show sub-protocol numbers.",
            "-R": "Skip privilege revocation.",
            "-K": "Send packets to kill matched connections. This **writes to the "
                  "network** — it is not an analysis option, and it does not "
                  "belong anywhere near evidence handling.",
        },
        "gotchas": [
            "It matches within individual packets. A string split across TCP "
            "segments will not be found — reassembly is `tshark`'s job, not "
            "this one's.",
            "`-K` is the one flag here that changes the world instead of "
            "observing it. Everything else reads; that one transmits.",
            "Matching payload on a live interface needs capture privileges, and "
            "on a busy link `ngrep` drops packets silently. Capture first, "
            "search the file afterwards, when the answer has to be complete.",
        ],
    },

    "MFTECmd": {
        "purpose": "Parse NTFS metadata files — $MFT, $J, $Boot, $SDS, $I30 — "
                   "into CSV or bodyfile, including entries for deleted files.",
        "when": {
            "-f": "The metadata file to parse. Required, and the file type is "
                  "detected from its contents rather than its name.",
            "-m": "Supply the $MFT alongside a $J. Without it the journal shows "
                  "file names with no path, because the parent directory only "
                  "exists in the $MFT.",
            "--csv": "Write CSV to a directory. The normal output.",
            "--csvf": "Override the generated CSV filename.",
            "--json": "JSON output, for a pipeline.",
            "--jsonf": "Override the generated JSON filename.",
            "--body": "Bodyfile output, which is what `mactime` consumes — the "
                      "bridge from NTFS metadata into a classic timeline.",
            "--bodyf": "Override the generated bodyfile name.",
            "--bdl": "Drive letter to record in the bodyfile. Required with "
                     "`--body`, because a bodyfile path is meaningless without "
                     "the volume it came from.",
            "--blf": "Use LF rather than CRLF, when the output is going to a "
                     "Unix toolchain.",
            "--de": "Dump full detail for one entry, as `Entry` or `Entry-Seq`. "
                    "The flag for interrogating a single suspicious file.",
            "--fls": "List a directory's contents from the $MFT, for the entry "
                     "given by `--de`.",
            "--dd": "Directory to write an exported FILE record to.",
            "--do": "Offset of the FILE record to dump, decimal or hex.",
            "--ds": "Dump a security descriptor from $SDS by Id — how you get "
                    "from a file to the ACL that was on it.",
            "--dr": "Dump resident files out of the $MFT. Small files live "
                    "entirely inside their MFT record, so this recovers content "
                    "with no data runs to follow.",
            "--ir": "Include resident data inline in the output rather than as "
                    "separate files.",
            "--re": "Restrict resident extraction to these extensions.",
            "--rm": "Cap the size of resident data included.",
            "--rs": "Recover slack space from FILE records. Old entries survive "
                    "in the unused tail of a record, so this reaches deleted "
                    "metadata that a straight parse skips.",
            "--at": "Include all $STANDARD_INFORMATION timestamps rather than "
                    "only those that differ from $FILE_NAME. Differences between "
                    "the two attribute sets are the classic timestomping signal, "
                    "so include them when that is the question.",
            "--sn": "Include DOS 8.3 short names.",
            "--fl": "Condensed file listing instead of the full attribute dump.",
            "--vss": "Also parse every Volume Shadow Copy, which is where an "
                     "older $MFT still holds entries the live one has reused.",
            "--dedupe": "Drop duplicates by SHA-1 across the source and shadow "
                        "copies. Use it whenever `--vss` is on.",
            "--dt": "Custom timestamp format for the output.",
        },
        "gotchas": [
            "$MFT entries are reused. A deleted file's record is overwritten by "
            "the next file that needs it, so an entry describing a deleted file "
            "may already belong to something else — check the sequence number "
            "before asserting the two are the same file.",
            "$STANDARD_INFORMATION timestamps are trivially forged; $FILE_NAME "
            "timestamps are not, because they update only through the kernel. "
            "`--at` is what lets you compare them, and a mismatch is the "
            "strongest cheap indicator of timestomping.",
            "Parsing a live volume's $MFT copied with a normal file copy will "
            "fail — it is locked. Extract it with a forensic tool or from a "
            "shadow copy.",
        ],
    },

    "tshark": {
        "purpose": "Wireshark's command line: capture, filter, dissect and "
                   "export packet data, including fields for a timeline.",
        "when": {
            "-r": "Read a capture file. The safe default — analysis needs no "
                  "privileges and cannot disturb the wire.",
            "-i": "Capture live from an interface instead. Needs capture rights, "
                  "and on a busy link a live dissect will drop packets.",
            "-f": "**Capture** filter, in BPF syntax. Applied before packets are "
                  "written, so what it drops is gone forever.",
            "-Y": "**Display** filter, in Wireshark syntax. Applied after "
                  "capture, so nothing is lost and it can be changed later. "
                  "Confusing these two is the classic tshark mistake.",
            "-R": "Read filter, which needs `-2`. Prefer `-Y` unless you know "
                  "why you want this one.",
            "-2": "Two-pass analysis, so fields that depend on later packets — "
                  "reassembly, response times, stream indexes — are populated.",
            "-T": "Output format. `fields` with `-e` is how you get CSV for a "
                  "timeline; `json` and `ek` feed other tools.",
            "-e": "Which field to print, repeatable. Only meaningful with "
                  "`-T fields`, and the ordering is the column ordering.",
            "-c": "Stop after N packets — the fast way to sample a huge file "
                  "before committing to a full pass.",
            "-a": "Autostop condition for a live capture: duration, filesize or "
                  "file count.",
            "-b": "Ring buffer: roll to a new file on time or size, so a long "
                  "capture cannot fill the disk.",
            "-w": "Write packets out rather than dissecting them, which is much "
                  "faster when you only want a filtered subset.",
            "-D": "List interfaces and exit — how you find the right `-i` value.",
            "-L": "List the link-layer types an interface supports.",
            "-s": "Snapshot length; truncates each packet as it is captured.",
            "-p": "Do not enter promiscuous mode.",
            "-I": "Monitor mode, for capturing 802.11 management frames.",
            "-B": "Kernel buffer size. Raise it when a fast link is dropping "
                  "packets at capture time.",
            "-y": "Force the link-layer type.",
            "-M": "Reset dissector state every N packets, to bound memory on a "
                  "very long capture.",
        },
        "gotchas": [
            "Capture filters (`-f`) and display filters (`-Y`) use **different "
            "syntaxes** and apply at different times. `-f` discards packets "
            "permanently; `-Y` only hides them. Reaching for the wrong one is "
            "the most common way to destroy evidence with this tool.",
            "Dissecting live on a busy link drops packets silently. Capture to a "
            "file first, analyse afterwards, whenever completeness matters.",
            "`-T fields` prints nothing useful without `-e`. It is not an error, "
            "just empty output, which reads like the filter matched nothing.",
        ],
    },

    "chainsaw": {
        "purpose": "Hunt through Windows event logs with Sigma rules and "
                   "built-in detection logic, at speed.",
        "when": {
            "--num-threads": "Cap the thread count. Defaults to every core, "
                             "which is usually right on a dedicated analysis "
                             "box and rude on a shared one.",
            "--no-banner": "Suppress the banner, for clean output in a report or "
                           "a pipeline.",
        },
        "gotchas": [
            "The interesting options live on the subcommands — `hunt`, `search`, "
            "`dump` — not at the top level captured here. Run "
            "`chainsaw hunt --help` for the ones that matter.",
            "Rules are not bundled with the binary. Without a Sigma rule set and "
            "the mapping file, `hunt` runs and finds nothing, which looks "
            "identical to a clean host.",
        ],
    },

    "diec": {
        "purpose": "Identify a file's format, compiler, linker and packer from "
                   "the command line — the scriptable half of Detect It Easy.",
        "when": {
            "-r": "Recurse a directory. This is the flag that makes `diec` the "
                  "right tool for a corpus, where the GUI handles one sample.",
            "-d": "Deep scan: look past the entry point for signatures a quick "
                  "pass misses. Slower, and worth it on anything suspicious.",
            "-u": "Heuristic scan, for packers with no exact signature. Raises "
                  "false positives, so treat a heuristic-only hit as a lead.",
            "-g": "Aggressive scan — the most thorough and the noisiest.",
            "-a": "Scan every type rather than stopping at the detected format.",
            "-e": "Show entropy. High entropy with no packer signature is the "
                  "interesting case: something is compressed or encrypted and "
                  "nothing recognises it.",
            "-i": "Show file info — size, format, architecture.",
            "-S": "Ask for one specific piece of info, e.g. `-S Hash#MD5`. The "
                  "form to use when scripting rather than reading.",
            "-U": "Hide unknown results, to cut noise across a large scan.",
            "-b": "Verbose output, including which signature matched.",
            "-l": "Profile signature performance — for tuning a slow scan, not "
                  "for analysis.",
            "-j": "JSON output, for a pipeline.",
        },
        "gotchas": [
            "`diec` and the GUI share a signature set, so they agree by "
            "construction. Use this for corpora and reports; use "
            "[the GUI](die-gui.md) when you need to browse *why* something "
            "matched.",
            "A packer name is a signature match, not proof. Custom and modified "
            "packers match nothing, so silence is not the same as clean.",
            "Deep and aggressive scans cost real time on a large directory. "
            "Sample before committing to a full corpus run.",
        ],
    },

    "dumpcap": {
        "purpose": "Capture packets to a file. It does nothing else — which is "
                   "the point.",
        "when": {
            "-i": "Interface to capture from. `-D` lists what is available.",
            "-w": "Output file. Without it, dumpcap writes to a temporary file "
                  "and tells you where, which is rarely what you meant.",
            "-f": "Capture filter in BPF syntax. Applied before writing, so "
                  "anything it excludes is gone permanently.",
            "-b": "Ring buffer: roll to a new file on duration, filesize or "
                  "count. The difference between a capture that runs overnight "
                  "and one that fills the disk at 3am.",
            "-a": "Autostop condition — duration, filesize or files.",
            "-c": "Stop after N packets.",
            "-s": "Snapshot length: truncate each packet. Headers only, when "
                  "payload must not be recorded.",
            "-B": "Kernel buffer size in MiB. Raise it first when a fast link "
                  "reports drops; the default is small for modern traffic.",
            "-p": "Do not enter promiscuous mode — only traffic for this host.",
            "-I": "Monitor mode, for 802.11 management and control frames.",
            "-D": "List interfaces and exit.",
            "-L": "List link-layer types for the chosen interface.",
            "-S": "Print per-interface packet statistics once a second, for "
                  "confirming traffic is arriving before committing to a "
                  "long capture.",
            "-d": "Print the compiled BPF for a filter, to check it means what "
                  "you think before capturing hours of the wrong thing.",
            "-M": "Machine-readable output for `-D`, `-L` and `-S`.",
            "-y": "Force the link-layer type.",
            "-n": "pcapng output (the default).",
            "-P": "Legacy pcap output, for a tool that cannot read pcapng.",
            "-q": "Quiet — no packet-count updates.",
        },
        "gotchas": [
            "This is deliberately minimal: it captures and it does not dissect. "
            "That is why it is the right thing to run as the privileged process "
            "and why `tshark` shells out to it — the analysis code never needs "
            "the capture privilege.",
            "Filtering here is destructive. A capture filter that was slightly "
            "wrong cannot be widened afterwards; capture broadly and filter at "
            "analysis time whenever the disk allows it.",
            "Drops are reported at the end, not during. Check the count before "
            "treating a capture as complete — a busy link with the default "
            "buffer loses packets silently.",
        ],
    },

    "oledump.py": {
        "purpose": "List and extract the streams inside an OLE2 file — the "
                   "container behind legacy Office documents and many malicious "
                   "attachments.",
        "when": {
            "-s": "Select a stream by number, or `a` for all. Everything else "
                  "operates on the selection, so this usually comes first.",
            "-d": "Dump the selected stream raw, for carving an embedded "
                  "payload out to a file.",
            "-x": "Hex dump, when the stream is binary and you need to see "
                  "structure.",
            "-a": "ASCII dump, for a quick look at mostly-text content.",
            "-A": "ASCII dump with run-length encoding, which collapses long "
                  "runs of padding that otherwise bury the content.",
            "-S": "Strings dump — the fastest way to see whether a stream holds "
                  "anything readable.",
            "-v": "Decompress VBA. Macro streams are stored compressed, so "
                  "without this the source looks like binary noise. This is the "
                  "flag the tool exists for.",
            "--vbadecompresscorrupt": "Decompress as far as possible and show "
                                      "it, for a deliberately corrupted macro "
                                      "stream that defeats a clean decompress.",
            "--vbadecompressskipattributes": "Skip the attribute preamble and "
                                             "show only the macro body.",
            "-r": "Treat the input as a raw stream rather than an OLE file, for "
                  "a stream already carved out elsewhere.",
            "-T": "Head and tail only, to glance at a large stream.",
            "-t": "Apply a translation such as `utf16` when the stream is "
                  "wide-character text.",
            "-m": "Print the full manual, which documents the plugin and "
                  "selection syntax this summary cannot cover.",
        },
        "gotchas": [
            "The stream letters in the listing are the finding: `M` marks a "
            "macro stream and `O` an embedded object. A document with neither "
            "is not carrying either, whatever else it contains.",
            "OOXML files — .docx, .xlsx — are ZIP archives, not OLE2. Unzip "
            "first and run this against the extracted `vbaProject.bin`.",
            "Reading a decompressed macro is not analysing it. `olevba` adds "
            "the keyword and IOC pass; this tool gets you the bytes.",
        ],
    },

    "file": {
        "purpose": "Identify a file's type from its contents rather than its "
                   "name, using magic signatures.",
        "when": {
            "-i": "Print a MIME type instead of prose. The form to use when the "
                  "output feeds a script rather than a person.",
            "--mime-type": "MIME type only, without the encoding.",
            "--mime-encoding": "Character encoding only.",
            "-b": "Omit the filename, leaving just the type — for pipelines and "
                  "for-loops.",
            "-z": "Look inside compressed files and report what they contain "
                  "rather than reporting a compressed stream.",
            "-Z": "Same, without reporting the compression itself.",
            "-k": "Keep going after the first match and print every rule that "
                  "fired. Files crafted to defeat identification often match "
                  "more than one signature, and the disagreement is the finding.",
            "-f": "Read the list of files to test from a file, for a corpus.",
            "-L": "Follow symlinks and report the target.",
            "-h": "Do not follow symlinks — report the link itself.",
            "-m": "Use an alternative magic database.",
            "-C": "Compile a magic file to its indexed form.",
            "-s": "Read block and character devices too. Needed to type a raw "
                  "disk, which `file` otherwise refuses.",
            "-r": "Print raw bytes rather than escaping unprintables.",
            "-p": "Preserve the access time on the files examined — the flag "
                  "that stops a triage sweep from rewriting timestamps across "
                  "the evidence.",
            "-e": "Exclude a test type, when one is misfiring on a corpus.",
            "-0": "Print a NUL after the filename, for safe piping into `xargs -0`.",
            "-N": "Do not pad filenames to align the output.",
            "-P": "Tune a parser limit, e.g. `bytes` or `indir`.",
            "-S": "Disable the sandbox. Only when seccomp blocks a legitimate "
                  "test, and never on untrusted input if avoidable.",
        },
        "gotchas": [
            "Magic reads the first few hundred bytes. Prepend a valid header to "
            "anything and `file` will report the header — it is a fast triage "
            "signal, not an authority on content.",
            "`-p` preserves atime. Without it, typing a directory tree updates "
            "access times across the evidence, which is the kind of avoidable "
            "contamination that gets noticed later.",
            "An 'ASCII text' verdict on something you expected to be binary "
            "usually means it is base64 or hex, not that it is harmless.",
        ],
    },

    "rabin2": {
        "purpose": "Report the structure of a binary — headers, sections, "
                   "imports, exports, strings, symbols — for any format radare2 "
                   "understands.",
        "when": {
            "-I": "The header summary: format, architecture, bits, endianness, "
                  "stripped, and whether NX, PIE and canaries are on. The usual "
                  "first command on an unknown binary.",
            "-i": "Imports. What a binary asks the OS for is the fastest read on "
                  "what it can do.",
            "-E": "Exports — the entry points a DLL offers.",
            "-s": "Symbols, when the binary is not stripped.",
            "-S": "Sections with their sizes and permissions. A section that is "
                  "both writable and executable is worth a second look.",
            "-z": "Strings from the data sections.",
            "-zz": "Strings from the whole file, including sections a normal "
                   "pass skips.",
            "-l": "Linked libraries.",
            "-e": "Entrypoint address.",
            "-c": "Class information, for Objective-C, Java and .NET binaries.",
            "-R": "Relocations.",
            "-H": "Headers in full detail.",
            "-j": "JSON output, for a pipeline.",
            "-q": "Quiet, minimal formatting — easier to parse in a shell.",
            "-k": "Query a specific field rather than printing everything.",
            "-O": "Patch the binary. Read-only work never needs this, and using "
                  "it on evidence modifies it.",
            "-a": "Force the architecture when detection is wrong.",
            "-b": "Force the bit width, 32 or 64.",
            "-A": "List all sub-binaries in a fat/universal file.",
            "-x": "Extract the sub-binaries of a fat file.",
            "-v": "Version.",
        },
        "gotchas": [
            "This is the static, scriptable half of radare2. Nothing here "
            "executes the binary, which makes it safe to run over a corpus of "
            "samples — unlike opening them in a debugger.",
            "The security flags in `-I` describe the *binary*, not the running "
            "process. NX and ASLR also depend on the loader and the OS.",
            "`-z` misses strings outside the data sections, which is where "
            "packed and obfuscated samples hide theirs. Try `-zz` before "
            "concluding a sample has none.",
        ],
    },

    "volshell": {
        "purpose": "An interactive Python shell over a memory image, with "
                   "Volatility's object model loaded — for questions no plugin "
                   "answers.",
        "when": {
            "-f": "The memory image.",
            "--file": "The memory image.",
            "-w": "Treat the image as Windows.",
            "--windows": "Treat the image as Windows.",
            "-l": "Treat the image as Linux.",
            "--linux": "Treat the image as Linux.",
            "-m": "Treat the image as macOS.",
            "--mac": "Treat the image as macOS.",
            "--pid": "Enter with a process context already selected, so `cc()` "
                     "is not the first thing you type.",
            "--script": "Run a Python script against the image and drop into "
                        "the shell afterwards — the repeatable form of an "
                        "interactive session.",
            "--script-only": "Run the script and exit. This is how an "
                             "exploratory session becomes an automated one.",
            "-s": "Where to find symbol tables — the usual fix when a Linux or "
                  "macOS image will not resolve.",
            "--symbol-dirs": "Where to find symbol tables.",
            "-o": "Directory for files written out of the shell.",
            "--output-dir": "Directory for files written out of the shell.",
            "--offline": "Never fetch symbols online.",
            "--clear-cache": "Drop cached items when results look stale.",
            "-q": "Quiet.",
            "--quiet": "Quiet.",
            "-v": "More verbose output.",
            "--verbosity": "More verbose output.",
        },
        "gotchas": [
            "Reach for this when a plugin nearly answers the question but not "
            "quite. If a plugin exists, use the plugin — it is tested and this "
            "is not.",
            "Findings from an interactive session are not reproducible by "
            "default. Move anything that matters into `--script` so the result "
            "can be regenerated and reviewed.",
            "The same symbol requirement as `volatility3` applies: without an "
            "ISF matching the exact kernel build, a Linux or macOS image will "
            "not resolve at all.",
        ],
    },

    "objdump": {
        "purpose": "Disassemble and dump the contents of an object file or "
                   "executable — sections, symbols, relocations and code.",
        "when": {
            "-d": "Disassemble the executable sections. The common case.",
            "-D": "Disassemble everything, including data. Use it when code has "
                  "been hidden in a section not marked executable.",
            "-x": "All headers at once — the fastest orientation on an unknown "
                  "object.",
            "-f": "The file header alone: format, architecture, entry point.",
            "-p": "Format-specific private headers. On a PE this is where the "
                  "import table and data directories live.",
            "-h": "Section headers with sizes, addresses and flags.",
            "-t": "The symbol table, when the binary is not stripped.",
            "-T": "Dynamic symbols — what a shared object exports and imports.",
            "-r": "Relocations.",
            "-R": "Dynamic relocations, which reveal the PLT/GOT layout.",
            "-s": "Full contents of each section as a hex dump.",
            "-j": "Restrict the operation to one section, so a `-s` or `-d` on a "
                  "large binary stays readable.",
            "-S": "Interleave source with disassembly. Only useful when debug "
                  "info survived, which for malware it has not.",
            "-l": "Annotate with file and line numbers from debug info.",
            "-C": "Demangle C++ symbols into something readable.",
            "-b": "Force the file format when detection fails.",
            "-m": "Force the architecture, needed for raw shellcode with no "
                  "container to describe it.",
            "-M": "Pass a disassembler option, e.g. `intel` for Intel syntax "
                  "instead of AT&T.",
            "-g": "Debug information, if present.",
            "-w": "Wide output that does not truncate long symbol names.",
            "-z": "Do not collapse blocks of zero bytes, when the padding "
                  "itself matters.",
        },
        "gotchas": [
            "Disassembly starts where the section says code starts. Packed and "
            "self-modifying binaries decrypt themselves at runtime, so a static "
            "pass shows the unpacking stub and nothing about the payload.",
            "Default output is AT&T syntax. Most Windows malware documentation "
            "is Intel, so `-M intel` avoids constant mental translation.",
            "`-d` skips sections not marked executable, which is precisely where "
            "code gets hidden. `-D` is slower and sees them.",
        ],
    },

    "readelf": {
        "purpose": "Display the structure of an ELF file — headers, sections, "
                   "segments, symbols, notes and dynamic linkage.",
        "when": {
            "-h": "The ELF header: type, architecture, entry point. First thing "
                  "to run on an unknown Linux binary.",
            "-S": "Section headers.",
            "-l": "Program headers, which describe what the loader maps. A "
                  "section table can be stripped or faked; the program headers "
                  "must be right or the binary will not run.",
            "-d": "The dynamic section — needed libraries, RPATH, and the init "
                  "and fini arrays that run before and after `main`.",
            "-s": "The symbol table.",
            "--dyn-syms": "Dynamic symbols only — what the binary imports and "
                          "exports at runtime.",
            "-n": "Notes, including the build ID that ties a stripped binary to "
                  "its debug symbols.",
            "-r": "Relocations.",
            "-u": "Unwind information.",
            "-x": "Hex dump of a named section.",
            "-p": "String dump of a named section — the targeted alternative to "
                  "running `strings` over the whole file.",
            "-a": "Everything. Verbose, and the right first move when you do "
                  "not yet know what you are looking for.",
            "-C": "Demangle C++ symbols.",
            "-D": "Use the dynamic symbol table rather than the static one.",
            "-W": "Wide output that does not truncate.",
            "-t": "Section details in full.",
            "-e": "Header summary: file, section and program headers together.",
        },
        "gotchas": [
            "The section header table is optional at runtime. Malware strips or "
            "corrupts it to break tools, and the binary still runs — when "
            "sections look wrong, read `-l` instead, because the loader must be "
            "able to.",
            "`DT_INIT` and `DT_INIT_ARRAY` in `-d` run before `main`. Code "
            "placed there executes even if `main` looks harmless.",
            "An `RPATH` or `RUNPATH` pointing somewhere writable is a hijack "
            "waiting to happen, and it shows up here.",
        ],
    },

    "nmap": {
        "purpose": "Discover hosts, ports and services, and fingerprint what is "
                   "listening.",
        "when": {
            "-sS": "SYN scan — the default when running privileged. Fast, and it "
                   "does not complete the handshake.",
            "-sT": "Full TCP connect, when you lack the privileges for `-sS`.",
            "-sU": "UDP scan. Slow and unreliable by nature, but DNS, SNMP and "
                   "DHCP live there and a TCP-only sweep never sees them.",
            "-sn": "Host discovery only, no port scan — mapping what exists "
                   "before deciding what to probe.",
            "-Pn": "Skip discovery and treat every host as up. The flag for "
                   "networks that drop ping, and the reason a scan that "
                   "'found nothing' sometimes finds plenty.",
            "-p": "Which ports. `-p-` is all 65535 and takes far longer than "
                  "people expect.",
            "-F": "Fast scan of the top 100 ports.",
            "--top-ports": "Scan the N most common ports — the usual "
                           "time/coverage compromise.",
            "-sV": "Probe for service and version. This talks to the service "
                   "properly, so it is louder and slower than a port scan.",
            "--version-intensity": "How hard `-sV` tries, 0 to 9.",
            "--version-light": "Intensity 2 — much faster, misses more.",
            "--version-all": "Intensity 9.",
            "-O": "OS fingerprint from the TCP/IP stack. A guess with a "
                  "confidence, not a fact.",
            "--osscan-guess": "Report near matches rather than staying silent.",
            "-A": "Aggressive: version, OS, scripts and traceroute together. "
                  "Convenient and unmistakably noisy.",
            "-T": "Timing template 0-5. `-T4` is the usual choice on a LAN; "
                  "`-T0` and `-T1` exist for evading rate-based detection and "
                  "take hours.",
            "--script": "Run NSE scripts. The category matters — `vuln` and "
                        "`exploit` scripts actively test, and `exploit` can "
                        "change the target.",
            "--script-args": "Arguments for those scripts.",
            "--script-help": "Explain what a script does before running it, "
                             "which is worth doing for anything outside `safe`.",
            "-oA": "Write all three output formats at once. Do this always — "
                   "rerunning a scan to get a different format wastes time and "
                   "produces different results.",
            "-oN": "Normal output to a file.",
            "-oX": "XML output, for tooling.",
            "-oG": "Greppable output.",
            "--open": "Show only open ports, cutting the closed-port noise.",
            "-v": "Verbose; repeat for more.",
            "-n": "No reverse DNS, which is often the single biggest speed-up.",
            "-e": "Choose the interface to scan from.",
            "-S": "Spoof the source address.",
            "-D": "Decoy scan.",
            "-6": "Scan IPv6. Hosts frequently expose more on v6 than v4 "
                  "because the firewall rules were never mirrored.",
            "--exclude": "Skip these hosts. The safety flag: use it for anything "
                         "fragile before starting a range scan.",
            "--excludefile": "Skip the hosts listed in a file.",
            "--max-retries": "Cap retransmissions on a lossy link.",
            "--host-timeout": "Give up on a host after this long, so one dead "
                              "host cannot stall a range.",
            "--traceroute": "Trace the path to each host.",
        },
        "gotchas": [
            "Scanning is not passive. `-sV` and NSE talk to services properly, "
            "`--script exploit` may change the target, and everything here is "
            "recorded by anything watching. Have authorisation before running "
            "it, and use `--exclude` for hosts that must not be touched.",
            "`-p-` on a /24 is a very different job from the default scan. "
            "Scope the ports before scoping the hosts.",
            "A closed port and a filtered port are different findings. "
            "'Filtered' means something dropped the probe, which is information "
            "about the network rather than about the host.",
        ],
    },
}
