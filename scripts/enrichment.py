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


# Who answered what, captured before the researched blocks below merge into
# ENRICHMENT and make the two indistinguishable.
#
# The merge is deliberate -- a published answer is an answer, and rank_flags
# is right to skip a flag that already has one. But after it runs, nothing
# can tell a human judgement from a machine-generated one, and that broke the
# metric this loop is steered by: the fraction of flag attempts aimed at
# already-answered flags. Two notes were accepted and published, the next
# round measured against the merged dict, and the loop's own successes came
# back as redundant targeting. A phantom regression from 0% to 3% that would
# have been chased as a real one.
#
# Provenance is worth keeping for its own sake anyway. These two kinds of
# answer carry different weight, and once merged that distinction is gone.
HAND_ANSWERED: dict[str, frozenset] = {
    _c: frozenset((_r.get("when") or {})) for _c, _r in ENRICHMENT.items()
}
HAND_SCENARIOS: frozenset = frozenset(
    _c for _c, _r in ENRICHMENT.items() if _r.get("scenario"))


# Extracted worked commands, merged in above publish.py's boundary so the
# block survives regeneration. setdefault, so a hand-written invocations list
# always wins over an extracted one -- same rule as every other field here.
try:
    from invocations_data import INVOCATIONS as _INV
    for _c, _rows in _INV.items():
        ENRICHMENT.setdefault(_c, {}).setdefault("invocations", _rows)
except Exception:
    pass


# --- BEGIN researched scenarios (scripts/publish.py) ---
#
# Generated by scripts/publish.py from research the loop verified:
# retrieved from real documentation and walkthroughs, checked
# against the sources blind to the draft, and cited. Do not edit
# by hand -- rerun publish.py. Anything hand-written belongs in
# ENRICHMENT above, which always wins over this block.
RESEARCHED: dict[str, dict] = {
    '7za': {
        'scenario': 'An analyst reaches for 7za when needing to create or manipulate archives with precise control over case sensitivity, locked files, or exclusion of specific files, often running it after collecting digital evidence to securely compress and organize data. They may use switches like -ssc, -ssw, or -x! to tailor compression settings, preferring 7za over similar tools for its detailed command-line options that align with forensic requirements for accuracy and customization.',
        'sources': ['https://thedeveloperblog.com/7-zip-examples', 'https://www.tecmint.com/7zip-command-examples-in-linux/'],
    },
    'AmcacheParser': {
        'scenario': 'An analyst reaches for AmcacheParser after manually examining the AmCache hive with Registry Explorer or when needing structured CSV output for timeline analysis, as it automates extraction of AmCache data into a CSV file, which is more efficient than manual methods or RegRipper’s plugin-based reports. They may run it following the extraction of the Amcache.hve file and before analyzing results in Timeline Explorer, prioritizing its automation and compatibility with further analysis tools.',
        'sources': ['https://www.mennovanveenendaal.com/posts/The-Windows-AmCache-and-ShimCache-Artifacts/'],
    },
    'AppCompatCacheParser': {
        'scenario': "An analyst reaches for AppCompatCacheParser when examining ShimCache for historical execution evidence, often after checking UserAssist or before parsing AmCache, as it converts the registry's AppCompatCache into a readable CSV, providing file names, sizes, and timestamps that manual analysis cannot easily extract. They may prefer it over AmCacheParser when focusing on ShimCache-specific data rather than AmCache's more detailed but differently structured entries.",
        'sources': ['https://hackers-arise.com/digital-forensics-registry-analysis-for-beginners-part-3-evidence-of-execution/', 'https://hivesecurity.gitlab.io/blog/dfir-incident-response-complete-guide-2026/', 'https://nullsec.us/windows-10-11-appcompatcache-deep-dive/'],
    },
    'EvtxECmd': {
        'scenario': 'An analyst reaches for EvtxECmd when processing Windows Event Log (EVTX) files as part of a KAPE workflow, often after collecting event data or before generating actionable output through KAPE modules; they choose it because it is specifically integrated with KAPE and includes maps for structured EVTX analysis, which may offer more streamlined processing compared to standalone tools.',
        'sources': ['https://ericzimmerman.github.io/', 'https://github.com/AndrewRathbun/Awesome-KAPE'],
    },
    'JLECmd': {
        'scenario': 'An analyst reaches for JLECmd when parsing individual Jump Lists or extracting shell item data from .automaticDestinations-ms files, often after obtaining the files through forensic imaging or before analyzing the extracted .lnk files with other tools like LNK Tool. They may choose JLECmd over JumpList Explorer (JLE) when command-line processing is required, though JLE is preferred for its graphical interface.',
        'sources': ['https://www.cyberengage.org/post/jump-list-analysis-tool-jlecmd-exe'],
    },
    'PECmd': {
        'scenario': 'An analyst reaches for PECmd when processing Windows Prefetch files to extract execution details, often running it after collecting .pf files from a system or before exporting data for further analysis; they may use it over similar tools due to its structured output options like JSON or CSV, and its specific focus on Windows Prefetch parsing.',
        'sources': ['https://github.com/EricZimmerman/PECmd'],
    },
    'RBCmd': {
        'scenario': 'An analyst reaches for RBCmd when examining deleted files in the Recycle Bin to extract metadata like deletion time, original path, and file size from $I and $R files, often after manually identifying these files or directories; they may run it following initial file recovery attempts or alongside tools that recover $R files, preferring it for its ability to parse and output structured data (e.g., CSV) directly from $I files, which contain critical forensic information not easily accessible through other means.',
        'sources': ['https://medium.com/@jenito/recycle-bin-forensics-inside-the-digital-trash-can-dc6d1f479af8', 'https://www.cyberengage.org/post/recycle-bin-i-analyses-tool-i_parse_v1-1'],
    },
    'RECmd': {
        'scenario': 'An analyst reaches for RECmd during incident triage after checking event logs, file system changes, and amcache data to investigate persistence mechanisms like Run keys, services, or tasks; they use it alongside tools like EvtxECmd and MFTECmd to build a timeline of suspicious activity, as RECmd specifically targets registry artifacts for persistence analysis.',
        'sources': ['https://ridgelinecyber.com/resources/kape-ez-tools/', 'https://ridgelinecyber.com/training/modules/free/ir01-toolkit-setup/03-eztools/'],
    },
    'RecentFileCacheParser': {
        'scenario': 'An analyst reaches for RecentFileCacheParser when parsing a RecentFileCache.bcf file to extract recently accessed file paths, often after acquiring a forensic image or during artifact collection; they may run it before exporting data to CSV or JSON for structured analysis, preferring it over similar tools due to its specialized focus on .bcf files and clear export formatting options.',
        'sources': ['https://github.com/EricZimmerman/RecentFileCacheParser', 'https://github.com/wodzen/agent-forensics-skills/blob/main/skills/recentfilecacheparser/SKILL.md'],
    },
    'SBECmd': {
        'scenario': 'An analyst reaches for SBECmd when processing mounted forensic images to extract ShellBags data from NTUSER.DAT and UsrClass.dat files, often running it after mounting the image and before manual analysis or generating reports, as it automates parsing and outputs structured CSV files, making it preferable for large-scale investigations over manual tools.',
        'sources': ['https://cyber5w.com/blog/windows-shell-items-analysis', 'https://www.cyberengage.org/post/shell-bags-analysis-tool-sbecmd-exe-or-shellbagsexplorer-gui-version-very-important-artifact'],
    },
    'SrumECmd': {
        'scenario': 'An analyst reaches for SrumECmd during incident response after checking logs, processes, file changes, and persistence mechanisms to analyze data egress volume per application by processing SRUDB.dat and SOFTWARE hive data, as it specifically addresses network and application-based data movement insights not covered by other tools in the triage sequence.',
        'sources': ['https://ericzimmerman.github.io/', 'https://ridgelinecyber.com/resources/kape-ez-tools/', 'https://ridgelinecyber.com/training/modules/free/ir01-toolkit-setup/03-eztools/'],
    },
    'SumECmd': {
        'scenario': 'An analyst reaches for SumECmd after repairing corrupted UAL database files with Esentutl.exe /p to parse the Windows User Access Log (UAL) and generate CSV files correlating role access timestamps, GUIDs, and role names, as it specifically handles UAL logs that retain historical authentication data longer than typical event logs. They may use it alongside EDR telemetry and Security event logs to investigate suspicious activity, such as anomalous logins or appliance connections, due to its focus on UAL artifacts.',
        'sources': ['https://cloud.google.com/blog/topics/threat-intelligence/brickstorm-espionage-campaign', 'https://github.com/AndrewRathbun/Awesome-KAPE', 'https://github.com/S-RM/wiskess_rust'],
    },
    'WxTCmd': {
        'scenario': 'An analyst reaches for WxTCmd when examining Windows 10 timeline data to determine execution times or user activity, running it with the -f option on an ActivitiesCache.db file before opening the resulting CSV in EZviewer; they choose it over tools like JLECmd because WxTCmd specifically processes timeline files for execution details, whereas JLECmd handles Jump Lists for recent file access.',
        'sources': ['https://github.com/AndrewRathbun/Awesome-KAPE', 'https://github.com/AndrewRathbun/Awesome-KAPE/blob/main/README.md', 'https://github.com/Digital-Forensics-Discord-Server/ArtifactParsers'],
    },
    'XORSearch': {
        'scenario': 'An analyst reaches for XORSearch when searching for XOR, ROL, ROT, or SHIFT encoded strings in a binary file, particularly when suspecting malware obfuscation like hidden URLs; they may run it after extracting a suspicious file or before deeper analysis to decode potential hidden data, choosing it over similar tools due to its support for multiple encoding types and specific options like dictionary attacks for 32-bit keys.',
        'sources': ['https://blog.didierstevens.com/programs/xorsearch/'],
    },
    'aeskeyfind': {
        'scenario': 'An analyst reaches for aeskeyfind after creating a memory dump using a tool like Volatility to recover AES keys from the dump, as it is specifically designed to locate 128-bit and 256-bit AES keys in memory images; they would run it after the dump is created and before exporting the keys, preferring it over similar tools due to its focus on AES key recovery from memory dumps.',
        'sources': ['https://medium.com/@Frogjump/aeskeyfind-in-kali-linux-72ba6a8ea2fd'],
    },
    'affcat': {
        'scenario': 'An analyst reaches for affcat when examining AFF files to extract or verify specific segments, pages, or sectors of a disk image, often after acquiring or recovering data, as it allows precise control over output with options like -s, -p, -S, and -b, making it preferable for targeted forensic analysis over broader tools like affverify or affstats.',
        'sources': ['https://www.kali.org/tools/afflib/'],
    },
    'affconvert': {
        'scenario': 'When an analyst needs to convert files between RAW and AFF formats, they use affconvert, often after acquiring raw data or before processing with other AFF tools, as it directly handles format conversion unlike affcopy which focuses on reordering and recompression.',
        'sources': ['https://www.kali.org/tools/afflib/'],
    },
    'affinfo': {
        'scenario': 'An analyst reaches for affinfo when examining an AFF file to validate its integrity or extract metadata, often after acquiring the file or before decrypting it with a passphrase; they choose it for its specific capabilities to verify hashes, list segments, and identify file structures, which are critical for forensic analysis.',
        'sources': ['https://www.kali.org/tools/afflib/'],
    },
    'arp-scan': {
        'scenario': 'An analyst reaches for arp-scan when they need to verify the presence of a system with known IP and MAC addresses on a LAN, often running it first with a broadcast to determine the MAC address and then again targeting the specific MAC address for a quieter scan. They may use it after identifying a host via broadcast or before confirming its presence without alerting other network stations, as targeting a specific MAC avoids broadcasting to all devices.',
        'sources': ['https://github.com/royhills/arp-scan/wiki/arp-scan-User-Guide'],
    },
    'base64dump.py': {
        'scenario': 'An analyst reaches for base64dump.py when encountering malformed base64 or hexadecimal strings that require length adjustment or specific decoding, such as after initial detection using regular expressions. They may run it with options like -p (e.g., L4 or custom lambdas) to preprocess strings before decoding or -P to postprocess decoded data, as it allows handling of non-standard encodings and integrates built-in functions for tasks like UTF16-to-ASCII conversion, which other tools may not natively support.',
        'sources': ['https://github.com/DidierStevens/DidierStevensSuite/blob/master/base64dump.py'],
    },
    'bdeinfo': {
        'scenario': 'An analyst reaches for bdeinfo after confirming a partition is BitLocker encrypted using hex dumps and tools like fls, which cannot recognize BitLocker; they run it to extract volume details like the recovery key and encryption algorithm, preferring it over SleuthKit because SleuthKit does not support BitLocker.',
        'sources': ['https://bebinary4n6.blogspot.com/2020/01/how-to-handle-bitlocker-encrypted.html', 'https://www.aldeid.com/wiki/Category:Encryption/Bitlocker'],
    },
    'binwalk': {
        'scenario': 'An analyst reaches for binwalk when examining firmware images to identify embedded files, compressed data, or cryptographic keys, often after obtaining a firmware dump from a device; they may run it before deeper analysis to map contents or after extracting files for further inspection, preferring it for its entropy analysis and custom signature capabilities over tools lacking these specific features.',
        'sources': ['https://github.com/ReFirmLabs/binwalk/wiki/Usage', 'https://www.hardbreak.wiki/hardware-hacking/basics/tools/software-tools/binwalk'],
    },
    'blkls': {
        'scenario': 'An analyst uses blkls when recovering files from unallocated space after inodes are overwritten, running it after failed inode-based recovery attempts to extract raw unallocated data, then using carving tools like foremost or photorec on the output; they choose it over similar tools because it directly extracts unallocated space for carving when traditional file system metadata is unavailable.',
        'sources': ['https://github.com/sleuthkit/sleuthkit/wiki/Body-file', 'https://github.com/sleuthkit/sleuthkit/wiki/Timelines', 'https://oneuptime.com/blog/post/2026-03-02-how-to-use-sleuth-kit-for-file-system-forensics-on-ubuntu/view'],
    },
    'capa': {
        'scenario': 'An analyst reaches for capa after submitting a sample to CAPE for dynamic analysis, running it against the generated JSON report to extract capabilities, particularly when dealing with packed or obfuscated binaries where static analysis may fail. They may use it following unpacking or sandbox execution to bypass obfuscation limitations, preferring it over standalone static analysis tools due to its integration with dynamic reports and support for IDA Pro/Ghidra for enhanced feature extraction.',
        'sources': ['https://github.com/mandiant/capa', 'https://github.com/xuguowong/capa-SAST'],
    },
    'cyberchef': {
        'scenario': 'When an analyst needs to decrypt, decode, or transform data, they reach for CyberChef due to its versatile interface and client-side processing, which ensures no data is transmitted to third-party servers, making it preferable over tools that may not handle sensitive information as securely.',
        'sources': ['https://github.com/martinmathurine/Cryptography-Decryption-CyberChef-Lab', 'https://www.it-connect.tech/cyberchef-a-web-application-for-decrypting-decoding-and-transforming-data/'],
    },
    'dc3dd': {
        'scenario': 'An analyst reaches for dc3dd when imaging a disk with inline hash verification required, such as during forensic acquisition of a test device or system they own, ensuring the image matches the source through SHA-256 hashing logged in the acquisition file. They may run it after confirming authorization and before handing the image to another analyst, preferring it over similar tools for its detailed logging of hash, byte count, and completion status, which is critical for chain of custody and integrity verification.',
        'sources': ['https://github.com/plaintext-security/plaintext-labs/blob/main/forensics/02-acquisition-imaging/lab.md', 'https://www.kali.org/tools/dc3dd/'],
    },
    'dcfldd': {
        'scenario': "An analyst reaches for dcfldd when imaging a drive to create a forensic copy, ensuring the source device's permissions are restricted with chmod before use to prevent accidental writes; they run it with hash=md5,sha1 and hashlog to verify data integrity, preferring it over dd due to its safety features like multiple output paths and explicit write-blocking warnings.",
        'sources': ['https://dfir.blog/imaging-using-dcfldd/', 'https://www.mankier.com/1/dcfldd'],
    },
    'dd': {
        'scenario': 'An analyst reaches for dd when copying data between drives or sanitizing a drive, ensuring the syntax is correct before execution and using a write blocker to prevent accidental data loss; they may run it after verifying the source and target devices to avoid overwriting evidence, preferring dd for its direct, low-level data handling and reliability in forensic imaging tasks.',
        'sources': ['https://www.forensicfocus.com/articles/linux-dd-basics/'],
    },
    'dumpcap': {
        'scenario': 'An analyst reaches for dumpcap when capturing live network traffic with specific conditions like duration, file size, or packet count, often using options like -a or -b to automate stopping or file rotation; they may run it alongside tshark for analysis or use capinfos afterward to inspect capture files, preferring it over similar tools for its dedicated capture capabilities and precise control over capture parameters.',
        'sources': ['https://docsislab.wordpress.com/packet-capture/wireshark-command-line/', 'https://www.wireshark.org/docs/man-pages/dumpcap.html'],
    },
    'editcap': {
        'scenario': "An analyst reaches for editcap when they need to remove duplicate packets or split a capture file into smaller segments, often running capinfos first to assess the file's structure, as it directly handles format editing and packet manipulation tasks that other tools like mergecap or tshark do not explicitly address.",
        'sources': ['https://docsislab.wordpress.com/packet-capture/wireshark-command-line/', 'https://wiki.wireshark.org/Tools'],
    },
    'esedbexport': {
        'scenario': "When analyzing EDB files from applications like Active Directory, an analyst uses esedbexport after mounting the file via Docker, as shown in the example command, to extract structured data from the database. They might run it after obtaining the EDB file through imaging or extraction tools, and choose it because it is specifically designed for ESE databases, as indicated by the documentation's mention of its use in Windows Mail, Exchange, and Active Directory.",
        'sources': ['https://github.com/4k4xs4pH1r3/libesedb-utils/blob/master/libesedb.md', 'https://github.com/security-dockerfiles/esedbexport'],
    },
    'esedbinfo': {
        'scenario': 'An analyst reaches for esedbinfo when examining Extensible Storage Engine (ESE) Database Files (EDB) to retrieve metadata such as file format, page size, tables, columns, and indexes, as demonstrated by the example `esedbinfo Windows.edb`. They may run it after obtaining an EDB file from a system, such as one used by Exchange or Active Directory, to understand its structure before deeper analysis. The tool is chosen for its specific focus on ESE databases and its ability to provide detailed catalog information, as described in the documentation.',
        'sources': ['https://github.com/4k4xs4pH1r3/libesedb-utils/blob/master/libesedb.md', 'https://manpages.debian.org/unstable/libesedb-utils/esedbinfo.1.en.html'],
    },
    'evtxexport': {
        'scenario': 'An analyst reaches for evtxexport when exporting event records from an XML Event Log (.evtx) file, often after mounting a volume or image to access logs, as it supports exporting full event messages requiring SYSTEM and SOFTWARE registry files; they may use it after mounting a QEMU VM image and before analyzing event data in text or XML format, preferring it over similar tools for its ability to handle multi-language resources and full message exports.',
        'sources': ['https://github.com/libyal/libevtx/wiki/Tools'],
    },
    'evtxinfo': {
        'scenario': "An analyst reaches for evtxinfo after extracting EVTX files from memory dumps using tools like volatility's dumpfiles, running it to inspect file headers and chunk metadata before using evtxdump to parse event data, as it provides structural insights without full log parsing.",
        'sources': ['https://manpages.debian.org/unstable/libevtx-utils/evtxexport.1.en.html', 'https://www.rocheston.com/fire/', 'https://www.tophertimzen.com/resources/cs407/slides/week04_02-EventLogs.html'],
    },
    'ewfexport': {
        'scenario': 'An analyst reaches for ewfexport when they need to extract specific data from an EWF image, such as a partition or converting an E01 to another format, often after acquiring the image with ewfacquire; they may use it before further analysis to isolate relevant data, preferring it over other tools due to its flexibility in specifying byte ranges and output formats.',
        'sources': ['https://bromiley.medium.com/tooling-thursday-libewf-ec27b4564c2a', 'https://forensics.wiki/libewf/'],
    },
    'ewfinfo': {
        'scenario': 'When an analyst is working with an E01 file, they run ewfinfo first to extract and save metadata such as imaging date and tool used, which is crucial for documentation and evidence reference. They may use ewfmount before accessing the raw image, and prefer ewfinfo over other tools because it specifically captures the metadata stored within the EWF wrapper.',
        'sources': ['https://bromiley.medium.com/tooling-thursday-libewf-ec27b4564c2a', 'https://dfir.science/2017/11/EWF-Tools-working-with-Expert-Witness-Files-in-Linux.html'],
    },
    'ffind': {
        'scenario': 'An analyst reaches for ffind when searching for files based on string content or file signatures within a disk image, often after creating an image with tools like dd, as it efficiently locates files without requiring prior knowledge of inode numbers, making it preferable to manual searches or tools like fls for metadata-based queries.',
        'sources': ['https://github.com/sleuthkit/sleuthkit/wiki/Body-file', 'https://github.com/sleuthkit/sleuthkit/wiki/Timelines', 'https://hackernoon.com/getting-started-with-digital-forensics-using-the-sleuth-kit-c34a3wkg'],
    },
    'floss': {
        'scenario': 'An analyst reaches for FLOSS when examining an executable file containing obfuscated strings, as it automatically emulates decoding routines and extracts human-readable strings from memory differences; they may run it after initial static analysis to uncover hidden data, preferring it over manual emulation or other tools due to its automated comparison of memory states before and after decoding.',
        'sources': ['https://cloud.google.com/blog/topics/threat-intelligence/automatically-extracting-obfuscated-strings'],
    },
    'fls': {
        'scenario': "An analyst reaches for fls when gathering temporal data from file systems to create a timeline, running it with the '-m' flag and '-r' to recursively collect all files across each partition in a disk image; they may adjust time skew with '-s' to align with other systems, preferring fls over older tools like 'grave-robber' because it streamlines the process by eliminating the need for 'ils' and integrates directly with mactime for timeline generation.",
        'sources': ['https://github.com/sleuthkit/sleuthkit/wiki/Timelines'],
    },
    'foremost': {
        'scenario': 'An analyst reaches for foremost when recovering lost files from disk images or drives, using command line switches to specify built-in file types or configuration files for headers and footers; they may run it after creating an image with tools like dd, and choose it over similar tools due to its reliability and speed from using internal data structures of file formats.',
        'sources': ['http://foremost.sourceforge.net/', 'https://www.kali.org/tools/foremost/'],
    },
    'frida': {
        'scenario': "An analyst reaches for Frida when dynamically modifying a running mobile application's behavior, such as bypassing SSL pinning or decrypting obfuscated data, often running commands like `frida -U -f` or `frida -U -p` before injecting scripts; they choose it over similar tools because it allows real-time interaction and modification of processes without requiring source code access.",
        'sources': ['https://www.vaadata.com/en/blog/frida-the-tool-dedicated-to-mobile-application-security/'],
    },
    'frida-ps': {
        'scenario': 'An analyst reaches for frida-ps when they need to list processes on a remote device, such as after connecting via USB or identifying a specific device ID using frida-ls-devices, to inspect running or installed applications. They may run it before attaching to a target process for further analysis or scripting. They choose it over similar tools because it is explicitly designed for listing processes, a foundational step when interacting with remote systems, as highlighted in the documentation.',
        'sources': ['https://frida.re/docs/frida-ps/', 'https://www.vaadata.com/en/blog/frida-the-tool-dedicated-to-mobile-application-security/'],
    },
    'frida-trace': {
        'scenario': "An analyst reaches for frida-trace when tracing and modifying application behavior dynamically, such as during reverse engineering or security testing, often after copying frida-server to a remote device and before interacting with the target app's methods. They may choose it over similar tools because it allows real-time modification of method outputs and provides detailed tracing capabilities, as demonstrated by altering return values or inspecting method parameters during execution.",
        'sources': ['https://frida.re/docs/frida-trace/', 'https://www.vaadata.com/en/blog/frida-the-tool-dedicated-to-mobile-application-security/'],
    },
    'hashcat': {
        'scenario': 'An analyst reaches for hashcat when dealing with hashes like MD5, using wordlists such as rockyou.txt for brute-force or combination attacks, and runs it after identifying the hash type and preparing input files; they choose it over similar tools due to its GPU-accelerated cracking capabilities and support for advanced attack modes like mask attacks, as demonstrated in the examples.',
        'sources': ['https://github.com/IPIRATEXAPTAIN/htb-academy/blob/main/CrackingPasswordsWithHashcat.md', 'https://hashcat.net/wiki/doku.php?id=frequently_asked_questions'],
    },
    'hayabusa': {
        'scenario': 'An analyst reaches for Hayabusa when generating fast forensics timelines from Windows event logs, either after collecting logs for offline analysis or during live-response investigations; they may run it before importing data into tools like Elastic Stack or Timesketch, as it consolidates events into structured formats and leverages Sigma rules for detection, offering speed and compatibility with enterprise-scale analysis platforms.',
        'sources': ['https://github.com/Yamato-Security/hayabusa'],
    },
    'hivexsh': {
        'scenario': 'When an analyst needs to examine Windows Registry hive files, they use hivexsh after obtaining the hive file (e.g., via virt-cat or guestfish) to navigate and inspect its keys and subkeys, as it is specifically designed for this task and provides interactive shell commands for structured exploration.',
        'sources': ['https://libguestfs.org/hivexsh.1.html', 'https://manpages.ubuntu.com/manpages/xenial/man1/hivexsh.1.html'],
    },
    'hydra': {
        'scenario': 'An analyst reaches for Hydra after enumeration and gathering web-form details from tools like Burp Suite, running it for online brute-force attacks on SSH or web forms; they choose it over similar tools like John the Ripper because Hydra operates online, making it suitable for live targets requiring real-time credential testing.',
        'sources': ['https://crackerfrank.hashnode.dev/cracking-passwords-with-hydra-a-tryhackme-walkthrough', 'https://hackproofhacks.com/blog/password-cracking-with-hydra-hacking-series/', 'https://www.freecodecamp.org/news/how-to-use-hydra-pentesting-tutorial/'],
    },
    'inetsim': {
        'scenario': 'An analyst reaches for inetsim when setting up a malware analysis lab with VirtualBox and Burp, particularly when encountering installation issues like the "apt-key is deprecated" error, which the documentation addresses with specific keyring setup commands. They may run it after resolving dependencies and configuring the lab environment to simulate network services for analyzing C2 traffic.',
        'sources': ['https://blog.christophetd.fr/malware-analysis-lab-with-virtualbox-inetsim-and-burp/'],
    },
    'john': {
        'scenario': "An analyst reaches for John when attempting to crack password hashes, often after preparing a larger wordlist and configuring the tool's settings, as it supports multiple modes like single crack, wordlist with rules, and incremental cracking for thoroughness. They may run `john --show` afterward to display cracked passwords, preferring John over similar tools due to its flexibility in using custom charsets, filters, and incremental modes tailored to specific password patterns.",
        'sources': ['https://www.openwall.com/john/doc/EXAMPLES.shtml'],
    },
    'log2timeline.py': {
        'scenario': 'An analyst reaches for log2timeline.py when creating a forensic timeline from disk images or directories, as it extracts timestamps into a Plaso storage file, often preceding psort.py for filtering and sorting. They may use it after acquiring evidence and before analysis, preferring it for its ability to detect partitions and VSS, and for supporting targeted extraction via filter files.',
        'sources': ['https://plaso.readthedocs.io/en/latest/sources/user/Using-log2timeline.html', 'https://www.cyberforensicacademy.com/blog/log2timeline-guide-creating-forensic-timelines'],
    },
    'mactime': {
        'scenario': 'An analyst reaches for mactime after gathering temporal data from file systems, logs, and other sources into a body file using tools like fls, to sort and merge the data into a single timeline. They would run it after collecting and consolidating all temporal data, as it is specifically designed to handle the body file format and create a chronological view, which is critical for event reconstruction.',
        'sources': ['https://github.com/sleuthkit/sleuthkit/wiki/Timelines'],
    },
    'mergecap': {
        'scenario': 'An analyst reaches for mergecap when merging multiple pcap files captured sequentially into a single file, often running it after capturing or before analysis to consolidate data; they choose it over append mode to maintain correct timestamps and avoid misordering packets, as demonstrated in the documentation.',
        'sources': ['https://osqa-ask.wireshark.org/questions/31113/wireshark-merging-pcap-files/', 'https://osqa-ask.wireshark.org/questions/39951/how-to-simultaneously-filter-and-merge-several-pcap-files/', 'https://wiki.wireshark.org/Tools'],
    },
    'mmls': {
        'scenario': 'An analyst reaches for mmls after verifying the integrity of a disk image using hashing commands like md5sum to obtain details about the partition layout, which is critical before proceeding with further analysis. They run it to confirm the image is a physical disk copy rather than a logical one, ensuring accurate partition information for subsequent steps like fsstat. They choose mmls over similar tools because it specifically provides partition layout details necessary for forensic examination.',
        'sources': ['https://hackernoon.com/getting-started-with-digital-forensics-using-the-sleuth-kit-c34a3wkg'],
    },
    'msodde': {
        'scenario': 'An analyst reaches for msodde when examining Office documents for DDE (Dynamic Data Exchange) or malicious field commands linked to exploitation techniques, often after decrypting password-protected files or alongside tools like olevba for macro analysis. They choose it over similar tools because it specifically filters and extracts DDE-related fields, which are critical for detecting vulnerabilities like those in CSV injection or macro-less code execution mentioned in the documentation.',
        'sources': ['https://github.com/decalage2/oletools/blob/master/oletools/msodde.py', 'https://github.com/decalage2/oletools/wiki/msodde'],
    },
    'msoffcrypto-tool': {
        'scenario': 'An analyst reaches for msoffcrypto-tool when decrypting password-protected or encrypted Microsoft Office files, often after using Oletools to extract initial artifacts, as it specifically handles decryption with passwords, intermediate keys, or private keys generated for escrow, making it preferable over tools like SSView, which focuses on structured storage analysis rather than decryption.',
        'sources': ['https://docs.remnux.org/discover-the-tools/analyze+documents/microsoft+office', 'https://medium.com/@m01z/dissecting-malicious-office-docs-a-quick-guide-3884732804e7'],
    },
    'ngrep': {
        'scenario': 'An analyst reaches for ngrep when searching for specific patterns in network traffic, such as detecting "login" in Telnet sessions, using switches like -w, -i, and -t for precise matching and timestamps; they may run it alongside tcpdump to analyze captured packets, preferring it over tcpdump for its grep-style filtering and intuitive regular expression handling.',
        'sources': ['https://www.admin-magazine.com/Articles/Network-Grep'],
    },
    'nping': {
        'scenario': 'An analyst reaches for nping when they need to send custom network packets for testing or forensic analysis, such as probing specific ports or crafting ICMP requests, often after identifying a target range or before verifying network behavior. They may choose it over similar tools due to its detailed target specification options, support for CIDR and octet ranges, and flexibility in packet crafting, as demonstrated in the examples and documentation.',
        'sources': ['https://nmap.org/book/nping-man.html'],
    },
    'numbers-to-string.py': {
        'scenario': 'An analyst reaches for numbers-to-string.py when processing files containing numeric sequences that need conversion to readable strings, such as ASCII or custom-encoded data; they may run it after extracting numbers from a file or before analyzing the resulting text, and they choose it over similar tools due to its support for custom translation tables, statistical analysis, and binary output handling as described in the documentation.',
        'sources': ['https://github.com/DidierStevens/DidierStevensSuite/blob/master/numbers-to-string.py'],
    },
    'objdump': {
        'scenario': 'An analyst reaches for objdump when examining raw binary files like BIOS dumps or ELF binaries to inspect assembly code, section headers, or memory layouts, often after capturing memory or firmware data; they may use it alongside tools like ndisasm or Ghidra for deeper analysis, preferring objdump for its integration with ELF metadata and ability to display low-level code structures.',
        'sources': ['https://can-ozkan.medium.com/learning-elf-the-foundation-of-linux-binary-analysis-c4f1f8df83e4', 'https://github.com/gl0bal01/intel-codex/blob/main/Security/Analysis/sop-malware-analysis.md', 'https://hacktricks.wiki/en/binary-exploitation/basic-stack-binary-exploitation-methodology/elf-tricks.html'],
    },
    'olebrowse': {
        'scenario': 'An analyst reaches for olebrowse when they need to interactively explore the structure of an OLE file, such as viewing or extracting individual data streams from MS Office documents, as it provides a simple GUI interface for this purpose. They may use it alongside tools like oledir or olemap for structural analysis, but prefer olebrowse for its visual inspection capabilities over command-line alternatives.',
        'sources': ['https://github.com/decalage2/oletools/wiki', 'https://github.com/decalage2/oletools/wiki/olevba'],
    },
    'oledump.py': {
        'scenario': 'An analyst reaches for oledump.py when examining OLE files (e.g., .xls) for embedded VBA macros or obfuscated content, often after extracting a file from a password-protected zip (using the password "infected") to avoid manual extraction. They may run it with options like -m to list streams, -v to decompress macros, or plugins like plugin_http_heuristics.py to extract URLs, preferring it over similar tools due to its ability to analyze zipped files in-place and integrate with YARA for rule-based scanning.',
        'sources': ['https://blog.didierstevens.com/programs/oledump-py/'],
    },
    'olemeta': {
        'scenario': 'An analyst reaches for olemeta when examining OLE files (e.g., MS Office documents) to extract standard metadata properties, often as part of a broader OLE file analysis workflow. They may use it alongside tools like oledir or oletimes for structural or timestamp analysis, choosing olemeta specifically for its focused extraction of standard properties rather than malware-related features.',
        'sources': ['https://cincan.io/blog/2019_12_19_oletools/', 'https://github.com/decalage2/oletools/blob/master/oletools/doc/olemeta.md'],
    },
    'oletimes': {
        'scenario': 'When analyzing OLE files for timestamps, an analyst uses oletimes to extract creation and modification timestamps of all streams and storages, as it provides precise timing data crucial for forensic timelines.',
        'sources': ['https://decalage.info/python/oletools/', 'https://github.com/decalage2/oletools/wiki', 'https://github.com/decalage2/oletools/wiki/oleid'],
    },
    'openssl': {
        'scenario': 'An analyst reaches for openssl when testing SSL/TLS connections to servers (e.g., using s_client to connect to ports like 993 or 995) or generating cryptographic digests (e.g., MD5 or SHA1) for file integrity checks. They may run these commands before verifying server configurations or after obtaining data for forensic analysis, as openssl provides direct command-line tools for these tasks without requiring additional software. They might prefer it over similar tools for its simplicity in quick tests or when specific functions like base64 encoding/decoding are needed.',
        'sources': ['https://www.golinuxcloud.com/openssl-cheatsheet/', 'https://www.madboa.com/geek/openssl/'],
    },
    'pdfid': {
        'scenario': 'An analyst reaches for pdfid when triaging PDF documents to quickly identify potential threats, such as those containing JavaScript or obfuscation, before conducting deeper analysis with a parser; they may run it initially to screen files for suspicious content, preferring it over more complex parsers due to its simplicity and reduced risk of exploitation.',
        'sources': ['https://blog.didierstevens.com/programs/pdf-tools/'],
    },
    'pdfid.py': {
        'scenario': 'An analyst reaches for pdfid.py when triaging PDF documents to quickly identify potential threats like embedded JavaScript or suspicious actions, running it before deeper analysis with a full parser due to its simplicity and effectiveness in scanning for keywords without complex parsing.',
        'sources': ['https://blog.didierstevens.com/programs/pdf-tools/'],
    },
    'photorec': {
        'scenario': 'An analyst reaches for PhotoRec when recovering deleted files from damaged or unbootable disks, disk images, or encrypted partitions, often after using TestDisk to repair partition tables; they run it with parameters like `/log` for logging or specifying raw devices for speed, preferring it over similar tools for its robust support of fragmented file recovery and diverse image formats like .dd, .E01, and split files.',
        'sources': ['https://docslib.org/doc/9154809/photorec-step-by-step', 'https://oneuptime.com/blog/post/2026-01-15-recover-deleted-files-testdisk-ubuntu/view', 'https://www.cgsecurity.org/wiki/PhotoRec_Step_By_Step'],
    },
    'psort.py': {
        'scenario': "An analyst reaches for psort.py after generating a plaso.dump file with log2timeline.py to create a timeline, filter events by tags, or extract time slices; they may run pinfo.py first to inspect the dump's contents, and choose psort over similar tools for its ability to handle complex time-based filtering and tag-based queries directly from the plaso data.",
        'sources': ['https://digitalinvestigator.blogspot.com/2026/07/super-timeline-analysis-with.html', 'https://github.com/log2timeline/plaso/blob/main/docs/sources/user/Using-psort.md', 'https://nullsec.us/supertimeline-quick-reference/'],
    },
    'pyxswf': {
        'scenario': 'An analyst reaches for pyxswf when examining files like MS Office documents or RTF files suspected of containing embedded Flash (SWF) objects, particularly when SWF streams are fragmented within OLE structures or encoded in hexadecimal within RTF; they may run it after initial file inspection to extract SWF content for further analysis, preferring it over similar tools due to its specific handling of OLE fragmentation and RTF hex-encoded SWF extraction.',
        'sources': ['https://github.com/decalage2/oletools/wiki', 'https://github.com/decalage2/oletools/wiki/oleid', 'https://github.com/decalage2/oletools/wiki/olevba'],
    },
    'r2': {
        'scenario': 'An analyst reaches for r2 when examining stripped or complex binaries to analyze code structure, often running commands like `aa` or `aaa` to identify symbols, entry points, and function trees, as it provides detailed opcode-level insights and customizable analysis loops via its API or scripts, which may offer more precision than default tools.',
        'sources': ['https://book.rada.re/analysis/code_analysis.html', 'https://r2wiki.readthedocs.io/en/latest/tools/radare2/'],
    },
    'rabin2': {
        'scenario': 'An analyst reaches for rabin2 when examining binary files to extract structured information about ELF/PE/MZ/CLASS files, often after extracting them from disk images or PCAPs, as it provides detailed insights into binary structure and security features (e.g., `rabin2 -I` for security checks or `rabin2 -z` for strings) that may be more straightforward or comprehensive than alternatives like `readelf` or `checksec`.',
        'sources': ['https://gist.github.com/52617365/95baed8b731c3effdad04b1d6ccf4831', 'https://github.com/Adamkadaban/CTFs'],
    },
    'radare2': {
        'scenario': "An analyst reaches for radare2 when analyzing a binary to understand its structure, find exploits, or debug code, often running `radare2 <binary file>` to start, followed by `aaa` to analyze the binary's executable sections and calls. They may choose it for its detailed disassembly and navigation capabilities, as highlighted by the emphasis on commands like `aaa` and `afl` for exploring code flow and functions.",
        'sources': ['https://kindawingingit.medium.com/radare2-an-introduction-d6762dceeac5'],
    },
    'radiff2': {
        'scenario': 'An analyst reaches for radiff2 when comparing two binaries to identify byte-level differences, such as when examining modified or cracked versions of a file; they may run it after obtaining the binaries to analyze changes or similarities, using options like -s for similarity metrics or -c to count differences, as it provides precise offsets and matching function data that other tools might not explicitly detail.',
        'sources': ['https://book.rada.re/tools/radiff2/binary_diffing.html'],
    },
    'rafind2': {
        'scenario': 'When an analyst needs to search for specific strings, hex patterns, or zero-terminated strings within a binary file, they use rafind2 to quickly locate offsets, then feed those results to radare2 for contextual analysis. They choose it over similar tools because it provides minimal, precise output that integrates seamlessly with radare2 commands for deeper inspection, and supports efficient workflows like counting results or displaying hex dumps.',
        'sources': ['https://book.rada.re/tools/rafind2/intro.html'],
    },
    'rahash2': {
        'scenario': 'An analyst reaches for rahash2 when they need to compute hash values for files or text strings, often using the -s option for strings or -a all to apply multiple algorithms simultaneously; they may run it after acquiring evidence to verify integrity or before submitting files for analysis, preferring it over similar tools for its ability to handle multiple algorithms in one command and its integration with radare for further forensic processing.',
        'sources': ['https://book.rada.re/tools/rahash2/rahash_tool.html'],
    },
    'rasm2': {
        'scenario': "An analyst reaches for rasm2 when they need to disassemble binary or hex data into human-readable assembly instructions, such as converting a hex value like '90' to 'nop' or analyzing bytecode. They may use it after obtaining a binary file or hex dump, often in conjunction with radare2 commands like `pd` or `pD` for deeper analysis. They choose it for its direct integration with radare2 and ability to handle both hexpair and binary inputs efficiently.",
        'sources': ['https://book.rada.re/tools/rasm2/disassemble.html'],
    },
    'readelf': {
        'scenario': "An analyst reaches for readelf when examining stripped binaries or analyzing ELF headers to identify architecture, sections, or security features like CET; they may run it after using strings or before deeper disassembly to understand the binary's structure and protections, preferring it over similar tools for its precise ELF-specific insights into headers, sections, and dynamic symbols.",
        'sources': ['https://hacktricks.wiki/en/binary-exploitation/basic-stack-binary-exploitation-methodology/elf-tricks.html', 'https://intezer.com/blog/elf-malware-analysis-101-initial-analysis/', 'https://w00tsec.blogspot.com/2015/02/firmware-forensics-diffs-timelines-elfs.html'],
    },
    'regfinfo': {
        'scenario': "An analyst reaches for regfinfo when examining Windows NT Registry Files (REGF), such as NTUSER.DAT, to retrieve information about the registry's structure and contents. They might run it after extracting the registry file from a disk image or before using other tools that require the key and value hierarchy, as it provides structured output options like bodyfile and verbose diagnostics.",
        'sources': ['https://manpages.debian.org/unstable/libregf-utils/regfinfo.1.en.html'],
    },
    'regfmount': {
        'scenario': 'An analyst reaches for regfmount when examining Windows registry hive files to explore their structure and contents, often after extracting the hive from a disk image or virtual machine; they may run commands like `ls` and `cat` on the mounted directory to inspect keys and values, preferring it over similar tools for its ability to present registry data as a navigable file system with editable text files.',
        'sources': ['https://miloserdov.org/?p=5448'],
    },
    'regipy-dump': {
        'scenario': 'An analyst reaches for regipy-dump when they need to extract and analyze the contents of a registry hive, often after ensuring the hive is clean or applying transaction logs, and before running plugins or comparisons; they may use it to generate a JSON or timeline output for further examination, as it handles checksum validation and transaction logs during parsing.',
        'sources': ['https://github.com/mkorman90/regipy'],
    },
    'regipy-parse-header': {
        'scenario': "An analyst reaches for regipy-parse-header when examining the header of a registry hive file to quickly retrieve metadata such as sequence numbers and modification times, often running it before deeper analysis of the hive's contents. They may choose it because the Rust backend significantly reduces parsing time compared to the default Python parser, though the Python version remains the default if the Rust backend is not installed.",
        'sources': ['https://github.com/mkorman90/regipy'],
    },
    'regipy-plugins-run': {
        'scenario': 'An analyst reaches for regipy-plugins-run after dumping a registry hive to disk, as it automatically detects the hive type and executes relevant plugins for analysis, offering efficiency over manual plugin selection or alternative tools that lack automatic hive-type detection.',
        'sources': ['https://github.com/mkorman90/regipy'],
    },
    'regripper': {
        'scenario': 'An analyst reaches for RegRipper when examining registry hive files to quickly extract and decode data using pre-canned plugins, often after extracting the hive from a forensic image or system; they may run it alongside manual registry analysis to validate findings, as it automates complex data extraction tasks like decoding ROT-13 or translating binary values, which would be time-consuming manually.',
        'sources': ['https://www.sans.org/blog/regripper-ripping-registries-with-ease'],
    },
    'reordercap': {
        'scenario': 'An analyst uses reordercap when packets in a capture file are out of chronological order, running it after capturing or extracting the file to reorder packets by timestamp; they avoid using the same input and output file to prevent malformation, and prefer it over manual sorting or other tools because it automatically detects file formats and compression.',
        'sources': ['https://manpages.debian.org/testing/wireshark-common/reordercap.1.en.html', 'https://tshark.dev/edit/reordercap/'],
    },
    'rip.pl': {
        'scenario': 'An analyst reaches for rip.pl when parsing Windows registry hives to extract forensic artifacts, often after extracting the hive files from a disk image or memory dump, and may list plugins first with perl rip.pl -l to determine which analysis to perform; they choose it because it is pre-installed on the SIFT workstation and supports a large number of plugins for detailed registry analysis.',
        'sources': ['https://fwhibbit.es/en/windows-registry-prepare-the-coffeemaker', 'https://linuxconfig.org/how-to-install-regripper-registry-data-extraction-tool-on-linux', 'https://www.sans.org/blog/regripper-ripping-registries-with-ease'],
    },
    'scalpel': {
        'scenario': 'When an analyst needs to recover files from a disk image or raw device without relying on filesystem structure, they use Scalpel after imaging the drive, as it is filesystem-independent and can extract files from multiple formats. They may choose it over similar tools like Foremost because it is a faster, rewritten version designed for both digital forensics and file recovery.',
        'sources': ['https://www.kali.org/tools/scalpel/'],
    },
    'sha256sum': {
        'scenario': 'An analyst uses sha256sum to verify file integrity after detecting content changes, running it after appending data to confirm checksum mismatches, and preferring it over MD5/SHA-1 for stronger tamper protection and over sha512sum for a balance between security and efficiency.',
        'sources': ['https://penguin-gym-linux.com/en/articles/tutorials/checksum-md5-sha256'],
    },
    'sigtool': {
        'scenario': 'An analyst reaches for sigtool when investigating false positives detected by ClamAV, running it after obtaining a signature name from scan reports or logs to unpack the database and search for the specific signature; they use it over other methods because it directly facilitates identifying and analyzing signatures linked to false positives.',
        'sources': ['https://docs.clamav.net/manual/Usage/SignatureManagement.html'],
    },
    'ssdeep': {
        'scenario': 'An analyst reaches for ssdeep when comparing files for similarity rather than exact matches, running commands like -r to generate fuzzy hashes and -x or -k to compare signatures, as it is a mainstream tool used by NIST and can detect partial overlaps between files.',
        'sources': ['https://dfir.science/2017/07/How-To-Fuzzy-Hashing-with-SSDEEP-(similarity-matching).html', 'https://ssdeep-project.github.io/ssdeep/usage.html'],
    },
    'tcpflow': {
        'scenario': 'An analyst reaches for tcpflow after capturing network traffic with tools like tcpdump, when they need to reconstruct and analyze TCP data streams in files for easier forensic examination; they may run tcpflow on stored pcap files to extract and organize data, preferring it over Wireshark for its ability to save reconstructed flows into conventional files, simplifying further analysis with standard tools.',
        'sources': ['https://forensics.wiki/tcpflow/', 'https://www.systutorials.com/docs/linux/man/1-tcpflow/'],
    },
    'tcpxtract': {
        'scenario': 'When an analyst needs to extract files from network traffic, they use tcpxtract on pcap capture files or live traffic, as it supports 26 file formats and allows custom configurations via its config file. They may run it after capturing traffic with tools that generate pcap files, preferring it over similar tools due to its flexibility in adding new formats and reliance on file signatures for accurate extraction.',
        'sources': ['https://www.freshports.org/net/tcpxtract/'],
    },
    'testdisk': {
        'scenario': 'An analyst reaches for TestDisk when recovering lost partitions or repairing filesystems on physical devices, running it with administrative or root privileges after ensuring access rights; they choose it over similar tools because it specifically handles partition recovery and filesystem repair, unlike PhotoRec, which focuses on file recovery from unallocated space.',
        'sources': ['https://www.cgsecurity.org/wiki/PhotoRec', 'https://www.cgsecurity.org/wiki/TestDisk_Step_By_Step'],
    },
    'tshark': {
        'scenario': 'An analyst reaches for tshark when capturing or analyzing network traffic from the command line, often after setting up capture filters (e.g., `tshark -f !arp`) or before generating statistics (e.g., `tshark -z io,stat`). They may prefer it over GUI tools for scripting, automation, or when working with large captures that require efficient, non-interactive processing.',
        'sources': ['https://docsislab.wordpress.com/packet-capture/wireshark-command-line/', 'https://www.wireshark.org/docs/wsug_html_chunked/AppTools.html'],
    },
    'tsk_gettimes': {
        'scenario': 'An analyst uses tsk_gettimes after imaging a disk to extract metadata from all file systems, generating a body file for mactime to create a timeline. They may run it before using mactime to automate metadata collection from multiple file systems, choosing it over manual fls commands for efficiency.',
        'sources': ['https://github.com/sleuthkit/sleuthkit/wiki/Body-file', 'https://github.com/sleuthkit/sleuthkit/wiki/Timelines', 'https://github.com/sleuthkit/sleuthkit/wiki/tsk_gettimes'],
    },
    'tsk_recover': {
        'scenario': 'When an analyst needs to recover files from a disk image, they use tsk_recover after ensuring sufficient storage space in the destination folder. They run it following the creation of the image, as it is specifically designed for recovering files from disk images.',
        'sources': ['https://github.com/sleuthkit/sleuthkit/wiki/Body-file', 'https://github.com/sleuthkit/sleuthkit/wiki/Timelines', 'https://hackernoon.com/getting-started-with-digital-forensics-using-the-sleuth-kit-c34a3wkg'],
    },
    'upx': {
        'scenario': 'An analyst reaches for UPX when encountering a sample with .UPX0/.UPX1 sections, running `upx -d` to quickly unpack it before analyzing the decrypted code, as it is straightforward and automated compared to manual unpacking or tools like Unipacker that require emulation for more complex packers.',
        'sources': ['https://inventivehq.com/blog/malware-unpacking-guide'],
    },
    'vol': {
        'scenario': "An analyst reaches for vol when examining memory dumps to detect malicious activity, such as unusual processes or command-line arguments; they may first run plugins like `windows.pslist` or `windows.pstree` to establish context before using `windows.cmdline` or `windows.handles` for deeper analysis, as the tool's use of symbol tables ensures accurate parsing of memory structures over guesswork.",
        'sources': ['https://hivesecurity.gitlab.io/blog/memory-forensics-volatility-attack-detect/', 'https://www.dfirhive.com/post/windows-memory-and-process-analysis-volatility3-walkthrough'],
    },
    'volshell': {
        'scenario': 'An analyst reaches for volshell when they need to interactively run plugins or execute custom scripts on a memory image, often after loading the image to extract or analyze specific data. They may use it to generate TreeGrid objects for structured data access or run snippets via rs for quick tasks, preferring it over writing full plugins due to its flexibility and direct framework access.',
        'sources': ['https://github.com/volatilityfoundation/volatility3/blob/develop/doc/source/volshell.rst', 'https://volatility3.readthedocs.io/en/latest/volshell.html'],
    },
    'xlmdeobfuscator': {
        'scenario': 'An analyst reaches for xlmdeobfuscator when examining obfuscated XLM macros in xls, xlsm, or xlsb files, often using it as a Python library with parameters like `process_file` to extract and deobfuscate macros; they may run it after extracting the files or before analyzing the deobfuscated code, preferring it over similar tools due to its ability to function without MS Excel and its integration into projects like CAPE Sandbox and IntelOwl.',
        'sources': ['https://github.com/DissectMalware/XLMMacroDeobfuscator/blob/master/README.md', 'https://github.com/dissectmalware/xlmmacrodeobfuscator'],
    },
    'xortool': {
        'scenario': 'An analyst reaches for xortool when dealing with XOR-encrypted data, particularly when the key length is unknown or longer than default limits, and runs it after initial attempts to guess the key fail, using flags like -m, -l, or -c to refine results; they choose it over similar tools because it automates key-length analysis, filters plaintexts by character sets (e.g., Base64), and handles multi-byte keys with adjustable parameters.',
        'sources': ['https://github.com/hellman/xortool', 'https://github.com/hellman/xortool/blob/master/README.md', 'https://www.doyler.net/security-not-included/basic-xortool-usage'],
    },
    'yara': {
        'scenario': 'An analyst reaches for YARA when they need to detect specific malware or file patterns using Boolean conditions and tags, running it after collecting files from an incident or system, as it allows efficient filtering and organization of rules through metadata and tags.',
        'sources': ['https://www.eccouncil.org/cybersecurity-exchange/ethical-hacking/mastering-yara-rules-a-complete-guide-with-use-cases-syntax-and-real-world-examples/', 'https://www.picussecurity.com/resource/glossary/what-is-a-yara-rule', 'https://yara.readthedocs.io/en/stable/writingrules.html'],
    },
}

RESEARCHED_FLAGS: dict[str, dict] = {
    'AppCompatCacheParser': {
        '--csv': 'An analyst would use the --csv flag when parsing the ShimCache from the SYSTEM hive to generate CSV output for analyzing execution evidence, such as identifying unusual or first-time executions.',
        '--csvf': 'An analyst would use the --csvf flag when parsing the ShimCache from the SYSTEM hive to generate a CSV-formatted output file for further analysis.',
    },
    'MFTECmd': {
        '--csvf': 'An analyst would use the --csvf flag when specifying a custom filename for the CSV output file generated by MFTECmd during the analysis of an $MFT file.',
        '-f': 'An analyst would use the -f flag when specifying the path to the Master File Table ($MFT) file, such as when processing a mounted disk image or a local NTFS drive to extract file system metadata.',
    },
    'PECmd': {
        '--csv': 'An analyst would use the --csv flag when processing an entire prefetch directory to generate a structured CSV report for detailed analysis of execution timestamps and file activity.',
        '-f': 'An analyst would use the -f flag when examining a specific prefetch file to extract detailed execution information, such as timestamps and context about a suspicious executable like Mimikatz.',
        '-k': 'An analyst would use the -k flag when performing one-off analysis to quickly highlight and identify known-bad folders or files by searching for specific keywords in the output.',
    },
    'RECmd': {
        '--csv': 'An analyst would use the --csv flag when batch-processing registry hives against the community ruleset to generate structured CSV output for forensic analysis of persistence mechanisms, user activity, and system configuration details.',
        '--csvf': 'An analyst would use the --csvf flag when processing registry hives with RECmd to generate a CSV output file for further analysis or documentation during a forensic investigation.',
        '-d': 'An analyst would use the -d flag with RECmd when batch-processing hives against a community ruleset to extract forensic values like RunOnce persistence or user activity from the registry.',
        '-f': 'An analyst would use the -f flag when processing a single registry hive file against a specific rule file to extract forensic artifacts.',
    },
    'SrumECmd': {
        '-f': 'An analyst would use the -f flag with SrumECmd when extracting per-app network usage data from the SRUDB.dat file to investigate network activity over the last 30-60 days.',
    },
    'WxTCmd': {
        '--csv': 'An analyst would use the --csv flag with WxTCmd when parsing the Windows 10 Timeline database to export the results into a CSV file for structured analysis of application execution times and user activity.',
        '-f': 'An analyst would use the -f flag with WxTCmd when processing the Windows 10 Timeline database file (ActivitiesCache.db) to extract and save application usage data as a CSV for forensic analysis.',
    },
    'aeskeyfind': {
        '-t': 'An analyst would use the -t flag when examining a memory image with potential bit errors due to memory decay, allowing the tool to tolerate a specified number of discrepancies in candidate key schedules to improve the chances of recovering valid AES keys.',
        '-v': 'An analyst would use the -v flag when examining memory images to obtain detailed verbose output, including extended keys and constraints on the rows of the key schedule, to aid in forensic analysis.',
    },
    'affcat': {
        '-S': 'An analyst would use the -S flag when examining specific 512-byte sectors of a disk image to analyze or extract data from a known sector location.',
        '-p': 'An analyst would use the -p flag when needing to extract or examine a specific data page number from a disk image without processing the entire file.',
        '-s': 'An analyst would use the -s flag when they need to quickly list the segment names of an AFF file without processing its full contents.',
    },
    'affinfo': {
        '-a': 'An analyst would use the -a flag when they need to print all segments of an AFF file, including data segments that are normally suppressed.',
        '-b': 'An analyst would use the -b flag when examining an AFF file to identify and count bad blocks within each segment during a forensic investigation.',
    },
    'bdeinfo': {
        '-o': "An analyst would use the -o flag with bdeinfo when specifying the correct byte offset for a BitLocker-encrypted volume in a disk image, after confirming the volume's presence through hexdump analysis or partition layout checks.",
        '-p': 'An analyst would use the -p flag when providing a password to access a BitLocker-encrypted volume during forensic examination.',
        '-r': 'An analyst would use the -r flag when providing a recovery password to access a BitLocker Drive Encrypted volume.',
        '-s': 'An analyst would use the -s flag when providing a file containing a startup key to unlock a BitLocker-encrypted volume.',
        '-v': 'An analyst would use the -v flag when they need detailed error, verbose, or debug output during the analysis of a BitLocker Drive Encrypted volume.',
    },
    'binwalk': {
        '-E': 'An analyst would use the -E flag when analyzing entropy to detect encrypted or compressed sections within a firmware image.',
        '-e': 'An analyst would use the -e flag when automatically extracting embedded files and file systems from a firmware image during firmware reverse engineering or investigation.',
    },
    'bulk_extractor': {
        '-R': 'An analyst would use the -R flag when needing to recursively scan and extract buried evidence from compressed files like ZIP, GZIP, or PDF archives.',
        '-o': 'An analyst would use the -o flag when they need to specify a custom output directory to save the extracted artifacts generated by bulk_extractor.',
    },
    'capa': {
        '--quiet': 'An analyst would use the --quiet flag when they want to disable all output from capa except for error messages.',
        '--rules': 'An analyst would use the --rules flag when they need to apply a custom set of rules for analyzing a binary instead of the default embedded rules.',
        '--tag': "An analyst would use the --tag flag when they need to filter the identified capabilities based on specific values in the rule's metadata fields.",
        '-f': 'An analyst would use the `-f` flag when analyzing 32-bit shellcode to specify the format for capa to process the sample correctly.',
        '-vv': 'When an analyst needs to verify the exact locations within a binary where capa identified capabilities to trust the results and guide further analysis with tools like IDA Pro.',
    },
    'capinfos': {
        '-T': 'An analyst would use the -T flag when generating a table-style report to organize and export capture file information in a structured format, such as for importing into spreadsheet applications or further analysis.',
        '-n': 'An analyst would use the -n flag when examining a capture file to determine the number of resolved IPv4 and IPv6 addresses present.',
    },
    'chainsaw': {
        '--json': 'An analyst would use the --json flag when they need to output search or analysis results in a structured, machine-readable JSON format for further processing or integration with other tools.',
        '--mapping': 'An analyst would use the --mapping flag when applying third-party detection rules to event logs, as the mapping file specifies which log fields to use for rule matching.',
        '-i': 'An analyst would use the -i flag when searching for a string in event logs where the case of the letters in the pattern may vary, such as when looking for "mimikatz" in logs where it might appear as "MIMIKATZ" or "mimikatz".',
        '-r': 'An analyst would use the -r flag when they need to include additional custom or third-party rules alongside Sigma rules to enhance detection logic during a hunt through event logs.',
        '-s': 'An analyst would use the -s flag when incorporating Sigma rules into the hunting process to apply third-party detection logic during log analysis.',
        '-t': 'An analyst would use the -t flag when searching for specific event log entries by defining precise tau expressions, such as identifying events by their System EventID in EVTX files.',
    },
    'clamscan': {
        '--exclude-dir': 'An analyst would use the --exclude-dir flag when scanning a system to skip over directories like /proc, /sys, and /dev that contain non-file system data and are not relevant to virus scanning.',
        '--infected': 'An analyst would use the --infected flag when scanning directories or files to quickly identify and isolate only the infected items without displaying clean files, as demonstrated in the examples of showing infected files during recursive scans or automated upload checks.',
        '--max-filesize': 'An analyst would use the --max-filesize flag when scanning directories containing large files to skip scanning files exceeding a specified size, such as 100MB, to avoid unnecessary processing.',
        '--recursive': 'An analyst would use the --recursive flag when scanning a directory and needing to include all subdirectories to ensure every file is checked.',
    },
    'dumpcap': {
        '--autostop': 'An analyst would use the --autostop flag when they need to automatically halt packet capture after a specified duration, upon reaching a certain number of files, or when a capture file reaches a defined size limit.',
        '-w': 'An analyst would use the -w flag when capturing network traffic to disk for later analysis, particularly when managing large volumes of data through ring buffers, size-based file rotation, or time-based segmentation to ensure efficient storage and focused investigation.',
    },
    'esedbexport': {
        '-t': 'An analyst would use the -t flag when extracting data from the NTDS (Active Directory) database file (ntds.dit) using the esedbexport tool in a Docker container.',
    },
    'esedbinfo': {
        '-v': "An analyst would use the -v flag when needing detailed verbose output about an ESE Database File's structure and contents, such as page size, table counts, and column details.",
    },
    'evtxexport': {
        '-S': 'An analyst would use the -S flag when exporting event logs from a mounted volume and needing to include the SOFTWARE registry file to resolve software-specific information referenced in the event data.',
        '-f': 'An analyst would use the -f flag when exporting event records from an EVTX file in a specific format, such as XML, to ensure the data is structured for analysis or integration with other tools.',
        '-l': 'An analyst would use the -l flag when specifying the path to a particular EVTX log file to be processed by evtxexport.',
        '-p': 'An analyst would use the -p flag when specifying the path to a mounted file system or volume containing Windows event logs and registry files for extraction.',
        '-r': 'An analyst would use the -r flag when specifying the directory containing the SYSTEM and SOFTWARE registry files to properly parse event log data from a mounted Windows volume.',
        '-s': 'An analyst would use the -s flag when specifying the path to the SYSTEM registry file to export event log data that requires registry information for proper interpretation.',
        '-v': "An analyst would use the -v flag when they need detailed error, verbose, or debug output printed to stderr during the processing of EVTX files to troubleshoot issues or understand the tool's operation.",
    },
    'evtxinfo': {
        '-c': 'An analyst would use the -c flag when the ASCII strings in the EVTX file are encoded using a codepage different from the default (windows-1252).',
    },
    'ewfmount': {
        '-f': 'An analyst would use the -f flag when mounting a logical evidence file (such as a L01 or Lx01 file) to access metadata about loose files or directories rather than a disk image.',
    },
    'floss': {
        '--no': 'An analyst would use the --no flag when they want to exclude the extraction of static strings from a binary, such as when focusing on other types of obfuscated strings.',
        '--only': 'An analyst would use the --only flag when they want to extract only specific types of strings, such as stack or tight strings, from a malware binary to focus on obfuscated or language-specific data.',
    },
    'fls': {
        '-b': 'An analyst would use the -b flag with fls when generating a body file to create a timeline of file system events.',
        '-d': 'An analyst would use the -d flag with fls when examining a disk image to identify and list deleted files by their inode numbers for potential recovery.',
        '-f': 'An analyst would use the -f flag when specifying the file system type for non-Windows partitions, such as OpenBSD, to ensure fls correctly interprets the directory structure and file metadata.',
        '-m': "An analyst would use the '-m' flag with 'fls' when gathering allocated file data from each partition of a disk image to create a timeline, as described in the TSK documentation.",
        '-o': 'An analyst would use the -o flag when specifying the starting sector offset of a partition in a disk image to process that specific partition with fls.',
        '-p': 'An analyst would use the -p flag with fls when generating timelines to list files with full paths.',
        '-r': "An analyst would use the '-r' flag with 'fls' when recursively gathering all files from a file system to create a comprehensive timeline of file system activity, as required for processing each partition in a disk image.",
        '-s': "An analyst would use the '-s' flag with 'fls' when adjusting the system's time skew to align timestamps in the body file with those of other servers.",
    },
    'foremost': {
        '-d': 'An analyst would use the -d flag when examining UNIX file systems to enable indirect block detection for more thorough file recovery.',
        '-i': 'An analyst would use the `-i` flag when processing a disk image file, such as one generated by `dd`, to specify the input file for forensic carving.',
        '-t': 'An analyst would use the -t flag when specifying particular file types to recover from a disk image during a forensic investigation.',
    },
    'freshclam': {
        '--checks': "An analyst would use the --checks flag to specify a custom number of daily database update checks when the default of 12 checks per day is insufficient for their system's needs.",
        '--daemon': 'An analyst would use the --daemon flag when configuring freshclam to run continuously in the background to automatically check for and download virus database updates at regular intervals without manual intervention.',
        '--datadir': 'An analyst would use the --datadir flag when they need to install the new ClamAV database in a specific directory that is writable, already exists, and is an absolute path, rather than the default location.',
        '--log': 'An analyst would use the --log flag when they need to direct the output of the freshclam update process to a specific file for record-keeping or troubleshooting.',
        '--quiet': 'An analyst would use the --quiet flag when automating ClamAV database updates via scripts or cron jobs to suppress output and check exit codes for success or failure without generating unnecessary log entries.',
        '-d': 'An analyst would use the -d flag when they need freshclam to run continuously in the background to periodically check for and download virus database updates without manual intervention.',
        '-v': 'An analyst would use the -v flag when needing detailed output to monitor the ClamAV database update process, such as verifying download progress and confirming successful updates.',
    },
    'frida': {
        '--file': 'When an analyst needs to specify the executable file for Frida to monitor and unpack during runtime analysis.',
        '-N': 'When an analyst needs to inject a script into a specific Android application to modify its behavior, such as bypassing validation or decrypting a flag, they would use the -N flag to target the application by name.',
        '-U': 'When an analyst needs to attach Frida to a target application running on a connected Android device via USB to intercept logs, decrypt data, or hook methods during dynamic instrumentation.',
        '-f': 'An analyst would use the -f flag when needing to inject a script at the start of a target process to bypass security mechanisms like SSL pinning or anti-root protection as the application launches.',
        '-l': "An analyst would use the -l flag when injecting a JavaScript script to modify an application's behavior, such as decrypting obfuscated strings or bypassing security mechanisms like SSL pinning.",
        '-p': 'When an analyst needs to inject a JS script into an already running target process on a USB-connected device by specifying its process ID (PID) instead of launching the application anew.',
    },
    'frida-ps': {
        '-D': 'An analyst would use the -D flag when they need to list processes on a specific device by its ID, such as when targeting a particular connected device during a mobile pentest.',
        '-U': 'An analyst would use the -U flag when connecting to a device via USB to list its running processes or installed applications during a mobile forensic investigation.',
    },
    'frida-trace': {
        '--decorate': 'An analyst would use the --decorate flag when tracing functions that exist in multiple modules to distinguish their logs by adding the module name to the trace output.',
        '-I': 'An analyst would use the -I flag when they need to trace all functions within a specific module, such as to broadly monitor activity in a particular library without specifying individual functions.',
        '-N': 'When the target application is already running and the analyst needs to trace functions using its identifier.',
        '-O': "An analyst would use the -O flag when dealing with a large number of command line options that exceed the operating system's maximum command line length, allowing them to pass options via text files.",
        '-P': 'An analyst would use the `-P` flag when tracing multiple functions and needing to dynamically control handler behavior, such as conditionally printing the process ID based on a JSON parameter passed via the command line.',
        '-S': 'An analyst would use the -S flag when they need to initialize a frida-trace session by executing custom JavaScript code files to set up the environment, share functions, or add data to the global "state" object before tracing begins.',
        '-U': 'An analyst would use the -U flag when tracing an application running on a remote Android device connected via USB from their host machine.',
        '-a': "An analyst would use the -a flag when tracing unexported functions in a module whose names are not available, requiring the use of an absolute offset to identify the function's entry point.",
        '-f': 'An analyst would use the -f flag when launching a specific application on a mobile device to trace its API calls, such as monitoring crypto functions in Snapchat or Java methods in YouTube.',
        '-i': 'An analyst would use the -i flag when they need to trace specific functions or modules, such as monitoring particular API calls or methods in a target process.',
        '-p': "An analyst would use the -p flag when tracing functions in a specific process by its process ID, such as monitoring a Windows application's memory-related calls in msvcrt.dll.",
        '-x': 'An analyst would use the -x flag when they need to exclude specific functions from being traced after including an entire module or a set of functions matching a pattern.',
    },
    'fsstat': {
        '-o': "An analyst would use the -o flag with fsstat when examining the file system's data structures, such as the $MFT in NTFS, after determining the correct offset from the partition layout using mmls.",
    },
    'hashcat': {
        '--custom-charset1': 'An analyst would use the --custom-charset1 flag when defining a custom character set (e.g., ?l?d) to reference in a mask with ?1, such as in a hashcat mask file line like "?l?d,?l?l?l?l?1" to specify a combination of lowercase letters and digits for password cracking.',
        '--outfile-format': 'An analyst would use the --outfile-format flag when they need to specify a custom output format for cracked hashes, such as saving results in plain text instead of the default hash[:salt] format.',
        '--session': 'An analyst would use the --session flag when resuming an interrupted hashcat session to continue cracking from the last checkpointed position.',
        '--show': 'An analyst would use the --show flag to display previously cracked hashes stored in the potfile when verifying results or avoiding redundant cracking efforts.',
        '--stdout': 'An analyst would use the --stdout flag when generating custom wordlists by specifying mask patterns to create targeted combinations of characters for cracking hashes.',
        '-D': 'An analyst would use the -D flag when they need to specify whether to use the CPU, GPU, or both for hash cracking based on available hardware resources.',
        '-a': 'An analyst would use the -a flag when performing a combination attack to generate password combinations from two separate wordlists.',
        '-b': 'An analyst would use the -b flag when benchmarking a hash mode to estimate raw speed on their hardware before initiating a cracking job.',
        '-d': 'An analyst would use the -d flag when specifying a particular GPU device in a multi-GPU setup where hashcat encounters mapping errors due to identical or similarly identified devices, requiring manual selection to bypass temperature or fan control issues.',
        '-g': 'An analyst would use the -g flag when encountering errors related to excessive rule usage, such as clEnqueueCopyBuffer() -30 or cuStreamSynchronize() 702, to reduce the number of rules and resolve the issue.',
        '-m': 'An analyst would use the -m flag when specifying the hash type (e.g., MD5, SHA-256) to ensure Hashcat correctly interprets the hash format during cracking attempts.',
        '-o': "An analyst would use the -o flag when they need to specify the output file path for storing cracked hashes, such as in the example where 'cracked.txt' is used.",
        '-r': 'An analyst would use the -r flag when applying custom or built-in rule sets to a wordlist to generate password variations during cracking attacks, as demonstrated in the examples involving rules/best64.rule and modifying rules to append specific strings like years to passwords.',
        '-w': 'An analyst would use the -w flag when optimizing Hashcat performance on a dedicated cracking rig with a GPU not driving a display, specifically setting -w 4 for maximum workload intensity.',
    },
    'istat': {
        '-b': "An analyst would use the -b flag when examining a deleted directory's inode with a size of 0 to force the display of block addresses and recover file names from the directory's data blocks.",
        '-f': "An analyst would use the -f flag with istat when examining a deleted file's inode on an ext2 file system to retrieve detailed metadata and block information, as demonstrated with inode 2139 in the /root/able2/able2.part2.dd disk image.",
        '-o': "An analyst would use the -o flag with istat when examining metadata of a specific inode to retrieve detailed information about a file's properties and timestamps from a disk image or partition.",
    },
    'john': {
        '--external': 'An analyst would use the --external flag when generating a custom charset file with specific word filters to consider simpler passwords, as demonstrated in the example with --external=filter_alpha.',
        '--format': 'An analyst would use the --format flag when cracking hashes from specific sources like NTDS.dit or /etc/shadow, or when the hash type requires a specific format identifier such as NT or raw-md5 to ensure John the Ripper correctly interprets the hash structure.',
        '--groups': 'An analyst would use the --groups flag when checking for cracked accounts in specific privileged groups, such as those with group IDs 0 or 1, to identify compromised administrative or high-privilege user accounts.',
        '--incremental': 'An analyst would use the --incremental flag when the wordlist has been exhausted and the hash remains uncracked, particularly for short passwords (5-7 characters) where incremental brute-force is feasible.',
        '--make-charset': 'An analyst would use the --make-charset flag when generating a custom character set file based on character frequencies from a password file containing many already cracked passwords or multiple password files from the same organization or country.',
        '--restore': 'An analyst would use the --restore flag when resuming an interrupted session to continue cracking passwords from where it left off.',
        '--rules': 'An analyst would use the --rules flag when applying word mangling rules to a wordlist to generate variations of passwords for cracking, as demonstrated in examples like "john --wordlist=all.lst --rules mypasswd" and similar commands in the documentation.',
        '--session': 'An analyst would use the --session flag when running multiple parallel cracking sessions or resuming an interrupted session to avoid conflicts and ensure proper restoration from a saved session state.',
        '--shells': 'An analyst would use the --shells flag when excluding accounts with disabled shells from the cracked password report.',
        '--show': 'An analyst would use the --show flag after successfully cracking passwords to display the cracked credentials in a human-readable format for review or documentation.',
        '--single': 'An analyst would use the --single flag when auditing Linux system passwords to quickly identify weak passwords in hash files during the initial phase of a security assessment.',
        '--status': 'An analyst would use the --status flag to check the status of a running or interrupted John session, such as when monitoring progress or resuming a paused cracking process.',
        '--stdout': "An analyst would use the --stdout flag when processing the output of John's password cracking through the 'unique' utility to eliminate duplicate candidate passwords, as demonstrated in the examples where mangled passwords are piped into 'unique' for deduplication.",
        '--users': 'An analyst would use the --users flag when checking if cracked accounts correspond to specific UIDs, such as root (UID 0), or when isolating specific usernames like "root" in the output.',
        '--wordlist': 'An analyst would use the --wordlist flag when attempting to crack password hashes by feeding John the Ripper a file of potential passwords, such as the rockyou.txt wordlist, to compare against the target hash file.',
    },
    'log2timeline.py': {
        '--file-filter': 'An analyst would use the --file-filter flag when processing a full disk image directly to specify individual files or paths for analysis, avoiding the need to create a separate triage collection.',
        '--info': 'An analyst would use the --info flag when they need to check the list of supported plugins, parsers, and output modules available in log2timeline.py.',
        '--logfile': 'An analyst would use the --logfile flag when they need to redirect all log messages from log2timeline.py to a file for detailed debugging or record-keeping during processing.',
        '--partitions': 'An analyst would use the --partitions flag when processing a disk image with multiple partitions and needing to specify a particular partition number to avoid interactive prompts during the analysis.',
        '--storage-file': 'An analyst would use the --storage-file flag when processing a storage media image to specify the output file where the extracted timeline events will be stored.',
        '--timezone': "When analyzing loose files, a triage collection, or when the system's time zone cannot be auto-detected, an analyst would use the --timezone flag to explicitly specify the source system's time zone.",
        '-d': 'An analyst would use the -d flag when coupled with --logfile to obtain more detailed debug information during the processing of a storage media image.',
    },
    'mactime': {
        '-b': 'An analyst would use the -b flag when processing a body file to generate a timeline of file activity based on timestamps extracted from the file system.',
        '-i': 'An analyst would use the -i flag when creating an index summary file to import into a spreadsheet for graphing suspicious behavior, such as when analyzing file activity hits per day or hour.',
        '-z': 'An analyst would use the -z flag when the time zone of the data in the body file differs from their local time zone to ensure accurate timestamp interpretation in the timeline.',
    },
    'md5sum': {
        '--check': 'An analyst would use the --check flag when verifying if files have changed by comparing their current state to stored hash values, such as after modifying a file or during automated integrity checks.',
        '--ignore-missing': 'An analyst would use the --ignore-missing flag when verifying checksums of files that may be intentionally absent, to avoid warnings about missing files and focus on verification failures.',
        '--quiet': 'An analyst would use the --quiet flag when checking multiple files to display only the modified files, filtering out unchanged ones during verification.',
        '--status': 'An analyst would use the --status flag when running md5sum in a script to check file integrity and need the command to return a status code (0 for no changes, 1 for mismatches) without producing any output.',
        '--strict': 'An analyst would use the --strict flag when verifying checksum files to ensure they are properly formatted and to have the tool exit with a non-zero status if any hash lines are invalid.',
        '--tag': 'An analyst would use the --tag flag when they need to display the MD5 hash in BSD-style format, as demonstrated in the examples where it formats the output as "MD5 (filename) = hashvalue".',
        '--warn': 'An analyst would use the --warn flag when verifying hash values in a checksum file to detect and alert on improperly formatted or incorrect hash entries during validation.',
        '-w': 'An analyst would use the -w flag when verifying a hash file to identify which line contains an improperly formatted MD5 checksum.',
    },
    'mergecap': {
        '-F': 'An analyst would use the -F flag when they need to specify a particular output format for the merged capture file, such as when the default pcapng format is not suitable or when compatibility with specific tools requires a different format.',
        '-I': 'When merging multiple capture files that have compatible Interface Description Blocks (IDBs) to ensure they are merged correctly rather than duplicated.',
        '-a': 'An analyst would use the -a flag when they need to concatenate input files in the order they are provided, without reordering packets based on timestamps.',
        '-w': 'An analyst would use the -w flag with mergecap when they need to aggregate and consolidate multiple packet capture files into a single output file for further analysis or sharing with a colleague.',
    },
    'mmls': {
        '-o': "An analyst would use the -o flag when analyzing an embedded filesystem by specifying its sector offset, obtained from mmls output, to correctly reference files within a partition that isn't the primary boot volume.",
    },
    'mraptor': {
        '--zip': 'When an analyst needs to scan a file contained within a password-protected ZIP archive, such as "malicious_file.xls" with the password "infected".',
        '-r': 'An analyst would use the -r flag when scanning multiple files across subdirectories to check for suspicious macro behaviors recursively.',
        '-z': 'An analyst would use the -z flag when examining a password-protected zip archive containing files to be analyzed by mraptor.',
    },
    'msodde': {
        '-a': 'An analyst would use the -a flag when examining a Word document to extract all field commands for comprehensive analysis, as demonstrated in the example "Scan a Word document, extracting all fields: msodde -a file.doc."',
        '-d': 'An analyst would use the -d flag when analyzing OpenXML files to filter specific field commands during the detection of DDE links.',
        '-f': 'When analyzing OpenXML files (e.g., docx) to filter specific field commands, an analyst would use the -f flag with msodde.',
        '-l': "An analyst would use the -l flag to adjust the logging level when analyzing MS Office files for DDE links, allowing more detailed or less verbose output depending on the investigation's needs.",
        '-p': 'An analyst would use the -p flag when analyzing encrypted Office files (e.g., .docx or .rtf) to attempt decryption using a provided password in order to extract and analyze DDE links.',
    },
    'ngrep': {
        '-IO': 'An analyst would use the -IO flag when processing a saved pcap_dump file to apply network grep searches on previously captured packet data.',
    },
    'nmap': {
        '--datadir': 'An analyst would use the --datadir flag when needing to specify a custom location for Nmap data files, such as when scripts or configuration files are stored outside the default directories.',
        '--script-args-file': 'An analyst would use the --script-args-file flag when they need to specify multiple script arguments in a file rather than on the command line, allowing for easier management of complex or repeated argument sets.',
        '--script-trace': 'An analyst would use the --script-trace flag when executing specific scripts to monitor and analyze all incoming and outgoing communication between the scripts and the target system, such as when troubleshooting script behavior or inspecting detailed protocol interactions.',
        '--script-updatedb': 'An analyst would use the --script-updatedb flag when they have added, removed, or modified the categories of NSE scripts in the default scripts directory, requiring the script database to be updated.',
        '-iR': "An analyst would use the -iR flag when they need to choose random targets for scanning, as indicated by the documentation's description of the option.",
        '-sC': 'An analyst would use the -sC flag when conducting a scan to automatically execute the most common NSE scripts for quick vulnerability and service enumeration without manually specifying individual scripts.',
    },
    'nping': {
        '--dest-port': 'An analyst would use the --dest-port flag when testing connectivity to a specific service on a target host, such as verifying HTTPS availability on port 443.',
        '--tcp': 'An analyst would use the --tcp flag when sending TCP packets to specific ports as part of network testing or scanning, such as in the example where it is used with --flags rst to send a reset packet to port 80.',
        '-p': 'An analyst would use the -p flag when testing specific TCP ports on a target host, such as checking if a web server is listening on port 80.',
    },
    'ntfs-3g': {
        '-o': 'An analyst would use the -o flag when mounting NTFS partitions from disk images to apply specific options like read-only access, show system files, handle stream interfaces, or specify sector-based offsets for proper forensic examination.',
    },
    'objdump': {
        '--disassemble': 'An analyst would use the --disassemble flag when examining a raw binary file or analyzing specific symbols in an ELF file to inspect their assembly code.',
        '-EB': 'An analyst would use the -EB flag when disassembling a binary that uses big-endian byte ordering to ensure correct interpretation of the data.',
        '-EL': 'An analyst would use the -EL flag when processing a binary file that uses little-endian byte order to ensure correct interpretation of its data.',
        '-e': 'An analyst would use the -e flag when combining disassembly with debug information to analyze programs with debugging tags.',
        '-i': 'An analyst would use the -i flag when needing to check the supported object formats and architectures by objdump.',
    },
    'oledir': {
        '--zip': 'An analyst would use the --zip flag when processing a password-protected zip archive containing OLE files that need to be extracted and analyzed.',
        '--zipfname': 'An analyst would use the --zipfname flag when examining a zip archive to specify particular files within it for processing by oledir.',
        '-f': 'An analyst would use the -f flag when extracting specific files from a zip archive that is contained within an OLE file.',
        '-r': 'An analyst would use the -r flag when they need to recursively search for OLE files in all subdirectories of a given directory.',
        '-z': 'An analyst would use the -z flag when extracting OLE file entries from a password-protected ZIP archive to analyze its contents.',
    },
    'oledump.py': {
        '--cut': "An analyst would use the --cut flag when they need to extract a specific section of a stream's content for focused analysis.",
        '-f': 'An analyst would use the -f flag when examining files like AutoCAD .dwg files to locate embedded OLE objects such as VBA macros by scanning for the OLE MAGIC sequence (D0CF11E0).',
        '-i': 'An analyst would use the -i flag when examining OLE files to display additional details about modules, such as their sizes and potential structure, aiding in the analysis of embedded components like VBA projects.',
        '-p': 'An analyst would use the -p flag when analyzing a malicious Office document to extract hidden data, such as URLs, by applying specific plugins like plugin_http_heuristics or plugin_dridex.',
        '-q': "An analyst would use the -q flag when examining a file with the HTTP Heuristics plugin to filter out oledump's own output and focus on extracting URLs like http://???.???.???.??:8080/stat/lld.php.",
    },
    'olevba': {
        '--decode': 'An analyst would use the --decode flag when examining a document to reveal obfuscated strings by displaying them in decoded form.',
        '--reveal': "An analyst would use the --reveal flag when examining a file to deobfuscate and display the macro source code's VBA strings in a readable format.",
        '-d': 'An analyst would use the -d flag when performing a detailed analysis of a single file to display all details of the VBA macro examination.',
        '-r': 'An analyst would use the -r flag when scanning a directory structure to recursively process all .doc and .xls files in subfolders.',
        '-z': 'An analyst would use the -z flag when scanning encrypted documents stored in a Zip archive that require a password to access their contents.',
    },
    'pdf-parser': {
        '-w': 'An analyst would use the -w flag when processing PDFs that contain embedded malicious content with complex filters like /ASCIIHexDecode and /FlateDecode, as demonstrated in the example where decompression failed.',
    },
    'pdf-parser.py': {
        '-w': "An analyst would use the -w flag when processing a PDF containing embedded malicious content with complex filters like ASCIIHexDecode/FlateDecode, as demonstrated by the user's attempt to decode a malicious file that resulted in a decompression error.",
    },
    'pinfo.py': {
        '--verbose': 'An analyst would use the --verbose flag when troubleshooting or performing thorough validation of the collection process, or immediately after storage file creation to verify successful artifact extraction and document provenance.',
        '-v': 'An analyst would use the -v flag when troubleshooting processing issues, validating the integrity of a storage file, or verifying the completeness of artifact extraction after creating a Plaso storage file.',
    },
    'psort.py': {
        '--data': 'An analyst would use the --data flag when they need to specify a custom location for filter files or databases, such as when using a non-default winevt-rc.db file.',
        '--output-time-zone': 'An analyst would use the --output-time-zone flag when they need to adjust the time zone of the date and time values in the output events to match a specific location or requirement, rather than the default UTC.',
        '--slicer': 'An analyst would use the --slicer flag when filtering specific events but also needing to include surrounding context to better understand the timeline or related activities.',
        '-a': 'An analyst would use the -a flag when processing a storage media file or VSS store where duplicate entries need to be preserved for comprehensive analysis.',
        '-d': 'An analyst would use the -d flag when psort encounters an unexpected exception during runtime to debug the issue by printing the traceback and dropping into pdb.',
    },
    'pyxswf': {
        '-f': 'An analyst would use the -f flag when examining an RTF file containing Flash objects embedded in hexadecimal format to extract and analyze the embedded SWF content.',
        '-o': "An analyst would use the -o flag when examining OLE files like MS Office documents to extract embedded SWF streams that may be fragmented or obfuscated within the file's structure.",
        '-x': 'An analyst would use the -x flag when extracting embedded SWF files from OLE or RTF documents to save them as MD5HASH.swf in the working directory for further analysis.',
    },
    'r2': {
        '-B': 'An analyst would use the -B flag when mapping a binary at a specific address to align its symbols and flags with the physical address, such as when analyzing PIE binaries or raw firmwares.',
        '-P': 'An analyst would use the -P flag when applying a pre-defined rapatch file to a binary and immediately quitting after the patch is applied.',
        '-a': 'An analyst would use the -a flag when specifying the target architecture for analysis, such as when dealing with a fat binary requiring a particular architecture like ppc.',
        '-b': "An analyst would use the -b flag when specifying the bitness (e.g., 32 or 64) of the target binary's architecture during analysis, such as when opening a fat binary with a specific sub-architecture.",
        '-c': 'An analyst would use the -c flag when needing to execute specific radare2 commands directly from the command line without entering the interactive mode, such as quickly extracting data or automating tasks in scripts.',
        '-d': 'An analyst would use the -d flag when debugging a program, attaching to a running process by its PID, or configuring radare2 to handle stdin input during debugging sessions.',
        '-e': 'An analyst would use the -e flag when setting specific configuration variables during radare2 startup, such as disabling color output or enabling cache settings for a binary analysis session.',
        '-s': 'An analyst would use the -s flag when they need to immediately seek to a specific memory address in a binary to start analysis without loading the entire file first.',
    },
    'rabin2': {
        '-B': 'An analyst would use the -B flag when examining a PIE binary to override its base address for accurate symbol and section analysis.',
        '-C': 'An analyst would use the -C flag when creating a binary file (such as ELF, Mach-O, or PE) by specifying code and data hexpairs to reconstruct or analyze the binary structure.',
        '-D': 'An analyst would use the -D flag when needing to demangle symbol names in a binary file to interpret obfuscated or mangled function names.',
        '-K': 'An analyst would use the -K flag when needing to compute a checksum for sections of a binary file using a specified rahash2 algorithm, such as md5, to verify integrity or analyze file components.',
        '-X': 'An analyst would use the -X flag when they need to package extracted files and binaries contained within a file into a fat or zip archive.',
        '-f': 'An analyst would use the -f flag when they need to select and analyze a specific sub-binary within a larger file by specifying its name.',
        '-m': 'An analyst would use the -m flag when examining a binary to retrieve source line references corresponding to a specific memory address.',
        '-n': 'An analyst would use the `-n` flag with `rabin2` to retrieve the offset of a specific symbol, such as when examining the location of a function like `_main` in a binary file.',
    },
    'radiff2': {
        '-A': "An analyst would use the -A flag when they need to automatically run the 'aaa' or 'aaaa' analysis commands on each binary after loading to ensure both files are fully analyzed before performing a differential comparison.",
        '-C': 'When an analyst is unsure whether two binaries are similar and needs to check for matching functions between them.',
        '-O': 'An analyst would use the -O flag when comparing the opcodes of two functions in different binaries to identify differences in their machine code instructions.',
        '-S': 'An analyst would use the -S flag when sorting code diff output by attributes such as name, address, or size to organize and analyze differences between binary files more effectively.',
        '-a': 'An analyst would use the -a flag when specifying the architecture plugin (e.g., x86, arm) to ensure accurate binary analysis during code or graph diffing operations.',
        '-c': 'An analyst would use the -c flag when they need a concrete count of the number of differences between two binaries.',
        '-g': 'An analyst would use the -g flag when comparing the control flow graphs of specific functions between two binaries to visually identify structural or code differences, such as analyzing security updates or infected files.',
        '-s': 'An analyst would use the -s flag when comparing two binaries to quickly determine their overall similarity percentage and distance for a high-level overview of differences.',
        '-t': 'An analyst would use the -t flag when adjusting the similarity threshold for code diffing to filter differences based on a specific percentage match.',
        '-u': "An analyst would use the -u flag when comparing two binaries to output the differences in a unified format similar to the system 'diff' tool.",
    },
    'rafind2': {
        '-R': 'An analyst would use the -R flag when replacing occurrences of a specific string in a file with a new value.',
        '-a': 'An analyst would use the -a flag when searching for patterns in memory or files where alignment to specific byte boundaries is required to ensure valid hits, such as when examining structured data or instruction sequences.',
        '-b': 'An analyst would use the -b flag when specifying the block size for searching through binary data to control the granularity of the search process.',
        '-f': 'An analyst would use the -f flag to start searching from a specific address when analyzing a binary file.',
        '-x': 'An analyst would use the -x flag when searching for specific hexadecimal patterns, such as "909090" or "41.42" with nibble masks, in files or directories to identify binary data matches.',
    },
    'rahash2': {
        '-I': 'An analyst would use the -I flag when specifying a custom initialization vector (IV) for cryptographic operations such as encryption or decryption in algorithms that require it, like AES-CBC.',
        '-S': 'An analyst would use the -S flag when encrypting or decrypting data with a specific key or seed value, such as during symmetric encryption operations with plugins like AES-ECB or Blowfish.',
        '-a': "An analyst would use the -a flag with the value 'all' when they need to compute multiple hash values for a file or string using all available algorithms known to rahash2.",
        '-c': "An analyst would use the -c flag when verifying if a file's computed hash matches a known hash to confirm its integrity or detect modifications.",
        '-t': 'An analyst would use the -t flag when they need to stop hashing at a specific memory address to limit the hash calculation to a particular section of a file or data.',
    },
    'rasm2': {
        '-D': 'An analyst would use the `-D` flag when needing to disassemble hexpair bytes while also viewing the corresponding offset and opcode bytes for detailed analysis.',
        '-L': 'An analyst would use the -L flag when needing to list supported assembly plugins for a specific target architecture to determine which plugins are available for use with rasm2.',
        '-a': 'An analyst would use the -a flag when disassembling code for a specific architecture, such as x86 or Java, to ensure the correct instruction set is used.',
        '-b': 'An analyst would use the `-b` flag when specifying the bitness of the target architecture (e.g., 32 or 64) during disassembly to ensure accurate interpretation of machine code instructions.',
        '-d': 'An analyst would use the `-d` flag when converting hexadecimal opcodes into human-readable assembly instructions to analyze binary data.',
        '-i': 'An analyst would use the -i flag when they need to skip a specific number of bytes in the input buffer to bypass irrelevant data, such as file headers or padding, while disassembling a binary file.',
        '-s': 'An analyst would use the -s flag when they need to specify the assembly syntax (intel or att) for disassembled output.',
    },
    'rax2': {
        '-D': 'An analyst would use the -D flag when decoding a base64 encoded string to retrieve its original binary or textual content.',
        '-F': 'An analyst would use the -F flag when processing hexadecimal data from standard input, such as converting shellcode from a file into another format for analysis.',
        '-K': 'An analyst would use the -K flag when generating a randomart visualization of binary data, such as for creating a visual representation of a hash or hexadecimal value in a forensic report.',
        '-S': 'An analyst would use the -S flag when converting raw binary data into a hexadecimal string representation for analysis or documentation.',
        '-b': 'An analyst would use the -b flag when converting binary data into a string representation for analysis or documentation.',
        '-e': 'An analyst would use the -e flag when converting between different endianness representations, such as swapping byte order in hexadecimal values during data analysis.',
        '-k': 'An analyst would use the -k flag when performing calculations or conversions that require retaining the original numeric base representation of the input values.',
        '-s': 'An analyst would use the -s flag when converting a hexadecimal string into its corresponding raw byte representation for further analysis or processing.',
    },
    'regfinfo': {
        '-B': 'An analyst would use the -B flag when they need to output the key and value hierarchy of a REGF file as a bodyfile for further processing or analysis.',
        '-H': 'An analyst would use the -H flag when examining a Windows NT Registry File to display its key and value hierarchy for forensic analysis.',
        '-c': 'An analyst would use the -c flag when the ASCII strings in the REGF file are encoded using a specific codepage other than the default (windows-1252).',
        '-v': 'An analyst would use the -v flag when they need detailed error or debug information printed to stderr during the analysis of a Windows NT Registry File.',
    },
    'regipy-diff': {
        '-o': 'An analyst would use the -o flag when comparing registry hives to save the resulting differences to a CSV file for further analysis or documentation.',
    },
    'regipy-dump': {
        '-t': 'An analyst would use the -t flag when they need to output a timeline of the registry hive data instead of a JSON file.',
    },
    'regripper': {
        '-c': 'An analyst would use the -c flag when listing all plugins to output the list in CSV format for easier data handling or integration with other tools.',
        '-f': 'An analyst would use the -f flag when specifying the type of registry hive file being parsed, such as system, sam, or ntuser, to ensure RegRipper applies the correct plugin configurations during analysis.',
        '-l': 'An analyst would use the -l flag when they need to list all available plugins to determine which ones to apply during registry analysis.',
        '-p': 'An analyst would use the -p flag when they need to execute a specific plugin module on a registry hive file, such as extracting user-assist data from an NTUSER.DAT file.',
        '-r': 'An analyst would use the -r flag when parsing a specific Windows registry hive file, such as when extracting data from the SYSTEM or SAM hives during an investigation.',
    },
    'reordercap': {
        '-n': 'An analyst would use the -n flag when verifying if a pcap file is already in chronological order to avoid unnecessary processing and output file creation.',
    },
    'rip.pl': {
        '-c': 'An analyst would use the -c flag when exporting the list of available plugins to a CSV file for reference purposes.',
        '-f': 'An analyst would use the -f flag when specifying the type of registry hive file being parsed, such as system, sam, or security, to ensure RegRipper processes the correct hive structure.',
        '-l': 'An analyst would use the -l flag when needing to list all available plugins to determine which ones can be applied to a specific registry hive during an investigation.',
        '-p': "An analyst would use the -p flag when extracting specific registry data, such as details about folders viewed through the 'shellbags' plugin, from a Registry file like UsrClass.dat.",
        '-r': 'An analyst would use the -r flag when processing a specific registry hive file to extract and analyze data during a forensic investigation.',
    },
    'scalpel': {
        '-b': "An analyst would use the -b flag when carving files from a disk image if defined footers aren't discovered within the maximum carve size for a file type.",
        '-c': 'An analyst would use the -c flag when they need to specify a custom configuration file to define or modify the header/footer database used for file carving.',
        '-d': 'An analyst would use the -d flag when needing to generate a comprehensive header/footer database to ensure all footers are discovered, even though it sacrifices performance.',
        '-o': 'An analyst would use the -o flag with scalpel when specifying the output directory for extracted files from a disk image or device file during data carving.',
    },
    'sha256sum': {
        '--check': 'An analyst would use the --check flag when verifying the integrity of files against a known checksum file to identify discrepancies or failed validations without unnecessary output.',
        '-b': 'An analyst would use the `-b` flag when verifying files across different systems or handling files with mixed line endings to ensure consistent binary-mode hashing.',
    },
    'sigtool': {
        '--datadir': 'An analyst would use --datadir when they need to specify a non-default directory as the default database location for all sigtool operations.',
        '--hex-dump': "An analyst would use the --hex-dump flag when needing to generate a hexadecimal representation of a file's contents for detailed forensic examination or signature creation.",
        '--unpack': 'An analyst would use the --unpack flag when investigating a potential false positive by unpacking the virus signature database to locate and examine the specific signature causing the detection.',
    },
    'ssdeep': {
        '-b': 'An analyst would use the -b flag when processing multiple files from different directories to generate fuzzy hashes based only on filenames, ignoring directory paths.',
        '-d': 'An analyst would use the -d flag when comparing multiple files across directories to identify similar or duplicate documents, such as eliminating redundant Microsoft Word files in folders like Incoming, Outgoing, and Trash.',
        '-k': 'An analyst would use the -k flag when comparing computed fuzzy hashes of unknown files against a set of known malicious signatures to identify potential matches.',
        '-l': 'An analyst would use the -l flag when comparing files to have ssdeep output relative filenames instead of absolute paths for easier analysis.',
        '-m': 'An analyst would use the -m flag when comparing files against a precomputed fuzzy hash signature or database to identify matches, such as verifying if a file corresponds to a known hash stored in a file like sig.txt or fuzzy.db.',
        '-p': 'When an analyst needs to make file matches easier to find by displaying each match in both directions (A matches B and B matches A) for clarity.',
        '-r': 'An analyst would use the -r flag when recursively processing files in a directory to generate fuzzy hashes for comparison against known signatures or other file sets.',
        '-s': 'An analyst would use the -s flag when creating a database of fuzzy hashes for later comparison to detect similarities between files, even if they have been slightly modified.',
        '-x': 'An analyst would use the -x flag when comparing multiple sets of generated fuzzy hash signatures against each other to identify potential matches or overlaps between files, such as comparing system directory hashes with known malware hashes.',
    },
    'strings': {
        '--radix': 'An analyst would use the --radix flag when they need to print the memory location of each string in the file, such as to analyze the positions of strings within a binary executable.',
        '-a': 'An analyst would use the -a flag when they need to scan the entire file, including metadata, to ensure no readable text is missed, especially if vital information like error messages is suspected to be outside the main data section.',
        '-d': 'An analyst would use the -d flag when examining a binary file to extract only the strings from its data sections, ignoring other sections like debugging symbols or metadata.',
        '-f': 'An analyst would use the -f flag when processing multiple files to trace which file a particular string originated from.',
        '-t': 'An analyst would use the -t flag when they need to determine the exact location of strings within a binary file for further investigation or correlation with other data.',
    },
    'tcpflow': {
        '-C': 'An analyst would use the -C flag when they need to view flow data in the console without the display of source/destination headers.',
        '-L': 'An analyst would use the -L flag when running multiple instances of tcpflow that output to the same standard output to prevent their outputs from overlapping and corrupting each other.',
        '-R': 'An analyst would use the -R flag when processing a pcap file captured with tcpdump -w to rebuild the flows.',
        '-X': 'An analyst would use the -X flag when generating a DFXML report to document every TCP connection and system details for forensic analysis.',
        '-c': 'An analyst would use the -c flag when they need to print the contents of packets to the console in real-time without storing any captured data to files.',
        '-i': "An analyst would use the -i flag when they need to capture packets from a specific network interface rather than relying on libpcap's default selection.",
        '-l': 'An analyst would use the -l flag when processing multiple pcap files simultaneously with shell globbing, such as analyzing all capture files in a directory at once.',
        '-o': 'An analyst would use the -o flag when they need to specify a particular directory to store the transcript files generated by tcpflow during packet analysis.',
        '-r': 'An analyst would use the -r flag when processing a pcap file to automatically decode and save TCP flows, such as extracting HTTP responses or reconstructing data from network captures.',
        '-w': "An analyst would use the -w flag when they need to capture and save UDP packets that were not processed by tcpflow's default handling.",
    },
    'tcpxtract': {
        '-o': 'An analyst would use the -o flag when performing a live capture from a network interface to specify the output directory for extracted files.',
    },
    'tshark': {
        '-q': 'An analyst would use the -q flag when running tshark with the -z option to generate specific statistics, as shown in examples like "tshark -q -z io,stat,5,ip.addr==255.255.255.255" and "tshark -q -z conv.',
    },
    'upx': {
        '-d': 'An analyst would use the `-d` flag with UPX when encountering a malware sample packed with UPX to automatically unpack it into its original executable form.',
        '-o': 'An analyst would use the -o flag when unpacking a UPX-packed sample to specify the output file name for the unpacked executable, as demonstrated in the example command.',
    },
    'vivbin': {
        '-M': 'An analyst would use the -M flag when running a command-line analysis module that modifies the VivWorkspace and requires saving changes to the workspace.',
    },
    'vshadowinfo': {
        '-a': 'An analyst would use the -a flag when examining allocation information related to a Volume Shadow Snapshot (VSS) volume.',
        '-o': "An analyst would use the -o flag when needing to specify a non-default volume offset in bytes to access a particular section of a VSS volume that isn't starting at the beginning of the source file or device.",
    },
    'xlmdeobfuscator': {
        '--export-json': 'An analyst would use the --export-json flag when they need to save the deobfuscated macro output in a structured JSON format for further analysis or reporting.',
        '--file': 'An analyst would use the --file flag when processing an Excel document (such as .xlsm) to deobfuscate or extract macros from it.',
        '--no-indent': 'An analyst would use the --no-indent flag when they need to extract deobfuscated macros from an Excel document without any formatting indentation to simplify analysis or processing.',
        '--output-formula-format': 'An analyst would use the --output-formula-format flag when they need to deobfuscate macros in Excel documents and want the output to display only the integer-formula representation without any indentation or additional formatting.',
        '--with-ms-excel': 'An analyst would use the --with-ms-excel flag when processing Excel files on Windows and needing to leverage MS Excel for deobfuscation, as the tool first attempts to load the file with MS Excel before falling back to xlrd2.',
        '-x': 'An analyst would use the -x flag when they need to extract macros from Excel documents without performing any deobfuscation.',
    },
    'xortool': {
        '--char': 'An analyst would use the --char flag when they have prior knowledge or suspicion about the most frequent character in the plaintext, aiding xortool in accurately guessing the XOR key.',
        '--hex': "An analyst would use the --hex flag when the input data is hex-encoded, as indicated by the tool's option description.",
        '--key-length': 'An analyst would use the --key-length flag when they have prior knowledge or suspicion about the specific length of the XOR key used in the encrypted data.',
        '--max-keylen': 'When analyzing XOR-encrypted data and the key length is unknown but needs to be limited to a specific maximum for efficiency or based on prior knowledge.',
        '-o': 'An analyst would use the -o flag when brute-forcing possible keys by checking only printable characters to guess the most frequent byte in XOR-encrypted data.',
        '-p': "An analyst would use the -p flag when they have a known plaintext segment to aid in decrypting XOR-encrypted data, as demonstrated in examples where it's paired with encrypted files and brute-force options.",
        '-r': 'An analyst would use the -r flag when adjusting the threshold validity percentage for determining the likelihood of correct key guesses during XOR analysis.',
        '-t': 'When analyzing a Base64-encoded XORed message to filter plaintexts to only those containing valid Base64 characters.',
        '-x': 'An analyst would use the -x flag when processing a hex-encoded file, such as when decrypting data that has been represented in hexadecimal format.',
    },
    'xxd': {
        '-g': 'An analyst would use the -g flag when adjusting the number of bytes per group in a hex dump to improve readability or align with specific data formats, such as when working with little-endian structures.',
        '-i': 'An analyst would use the -i flag when generating a C include file (array) from a binary file to embed the data into a program or for forensic analysis requiring textual representation of binary content.',
        '-l': 'An analyst would use the -l flag when they need to examine a specific number of bytes from a file, such as inspecting the first 64 bytes of a binary to identify its header or a particular segment without processing the entire file.',
        '-r': 'An analyst would use the -r flag with xxd when they need to reconstruct a binary file from a properly formatted hex dump that includes offsets and correct hexadecimal data.',
        '-s': 'An analyst would use the -s flag when needing to start reading or writing from a specific byte offset within a file, such as examining data at a non-zero position or continuing from a previously processed section.',
    },
    'yara': {
        '-v': 'An analyst would use the -v flag when validating the syntax of a YARA rule to ensure it is correctly formatted before testing it against files.',
    },
    'yarac': {
        '--fail-on-warnings': 'An analyst would use the --fail-on-warnings flag when compiling YARA rules to ensure that no warnings are present, enforcing strict rule validation during the compilation process.',
        '--no-warnings': 'An analyst would use the --no-warnings flag when compiling YARA rules into a binary to suppress warnings during compilation, allowing the process to proceed without interruptions when external variables or rule syntax may generate non-critical alerts.',
    },
}

for _cmd, _fl in RESEARCHED_FLAGS.items():
    _w = ENRICHMENT.setdefault(_cmd, {}).setdefault('when', {})
    for _f, _n in _fl.items():
        _w.setdefault(_f, _n)

# Hand-written entries win: a human who wrote a scenario has
# judged it, and a research pass must never overwrite that.
for _cmd, _rec in RESEARCHED.items():
    _e = ENRICHMENT.setdefault(_cmd, {})
    _e.setdefault('scenario', _rec['scenario'])
    _e.setdefault('sources', _rec['sources'])
# --- END researched scenarios ---
