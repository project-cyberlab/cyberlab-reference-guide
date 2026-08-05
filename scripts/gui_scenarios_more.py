"""More hand-written GUI scenarios: PE analysis, documents, and utilities.

Split from gui_scenarios.py only to keep each file readable. Same rules: every
entry is a human judgement written after research, every entry cites what it
was written from, and none of it comes from the research loop -- because each
answers "why this tool rather than the one beside it", which is a comparison
no single retrieved passage contains.
"""
from __future__ import annotations

SCENARIOS: dict[str, dict] = {

    "CFF-Explorer": {
        "scenario": (
            "Reach for CFF Explorer when you need to read the PE itself "
            "rather than ask a signature database what built it. It parses "
            "every structure - headers, sections, imports, exports, resources "
            "- with a hex editor alongside, so it answers questions no "
            "signature can.\n\n"
            "Two reads carry most of the weight on a first pass. The **import "
            "table** bounds what the binary is able to do: no network imports "
            "means it is not calling home in that form. And the gap between a "
            "section's **VirtualSize and SizeOfRawData** is the classic "
            "packing tell - a section occupying far more memory than disk "
            "unpacks itself at runtime. A packed sample often imports almost "
            "nothing beyond LoadLibrary and GetProcAddress, because it "
            "resolves everything else after unpacking; an import table that "
            "short is itself the finding.\n\n"
            "Where PE Detective answers *what produced this*, CFF Explorer "
            "answers *what it is made of* - and it still works when no "
            "signature matches at all."
        ),
        "sources": [
            "https://tech-zealots.com/malware-analysis/pe-portable-executable-structure-malware-analysis-part-2/",
            "https://ccdcoe.org/uploads/2020/07/Malware-Reverse-Engineering-Handbook-final.pdf",
        ],
    },

    "PE-Detective": {
        "scenario": (
            "Reach for PE Detective to answer *what built this* before "
            "committing to unpacking. It matches the binary against a "
            "signature database of compilers, linkers and packers - a few "
            "seconds of work that can save an hour spent unpacking the wrong "
            "way.\n\n"
            "Tick **Deep Scan**. The default pass inspects the entry point "
            "only, so any packer that relocates the entry point is missed, "
            "and that is most of the ones worth detecting. Prefer **All "
            "Matches** over **Best Match** while triaging: disagreement "
            "between signatures tells you an identification is shaky, and a "
            "single best match hides exactly that.\n\n"
            "A clean result is not an all-clear. Signatures only recognise "
            "what someone has already catalogued, so a custom or modified "
            "packer shows nothing at all. That is the moment to open CFF "
            "Explorer and read the section sizes and imports yourself."
        ),
        "sources": [
            "https://www.eyehatemalwares.com/malware-analysis/static-analysis/ma-peid/",
            "https://ccdcoe.org/uploads/2020/07/Malware-Reverse-Engineering-Handbook-final.pdf",
        ],
    },

    "Signature-Explorer": {
        "scenario": (
            "Reach for Signature Explorer after a sample comes back "
            "unidentified and you have worked out by hand what packed it. It "
            "edits the signature database that PE Detective and CFF Explorer "
            "both read, so your identification becomes automatic for the next "
            "sample in the same family.\n\n"
            "That is its entire reason to exist - it analyses nothing. It is "
            "the step that turns one analyst's finding into detection the "
            "rest of the team gets for free, and the reason a signature "
            "database is worth maintaining rather than only consuming."
        ),
        "sources": [
            "https://www.eyehatemalwares.com/malware-analysis/static-analysis/ma-peid/",
        ],
    },

    "PDFStreamDumper": {
        "scenario": (
            "Reach for PDFStreamDumper when `pdfid` has flagged a PDF - a "
            "non-zero `/JS`, `/OpenAction` or `/Launch` count - and you need "
            "to read what is actually inside those objects. It enumerates "
            "every object and stream and applies the filters, so compressed "
            "and hex-encoded content becomes readable instead of noise.\n\n"
            "It occupies the same point in the workflow as `pdf-parser`, and "
            "the choice between them is browsing versus scripting. Use this "
            "when you are exploring an unfamiliar document and want to click "
            "through its object graph; use `pdf-parser` when you already know "
            "what you are extracting, or need the extraction repeatable.\n\n"
            "Treat any JavaScript it shows you as hostile input to be read, "
            "never executed."
        ),
        "sources": ["https://blog.didierstevens.com/programs/pdf-tools/"],
    },

    "OffVis": {
        "scenario": (
            "Reach for OffVis on **legacy** Office files - `.doc`, `.xls`, "
            "`.ppt` - not the modern XML formats. Those older formats are a "
            "chain of length-prefixed records, and the classic Office "
            "exploits work by lying in a length or pointer field so the "
            "parser walks off the end of a buffer.\n\n"
            "It shows three linked views: the raw bytes, the record structure "
            "Microsoft's own parser derives from them, and where parsing "
            "failed. Selecting a record highlights the bytes it came from, so "
            "a field claiming 4000 bytes inside a 200-byte record becomes "
            "visible rather than inferred - which is precisely what `strings` "
            "or a hex editor cannot show you.\n\n"
            "For macro-bearing documents reach for `olevba` instead. This is "
            "for structural corruption, not for reading VBA."
        ),
        "sources": [
            "https://learn.microsoft.com/en-us/security-updates/securitybulletins/2010/ms10-087",
        ],
    },

    "HashMyFiles": {
        "scenario": (
            "Reach for HashMyFiles when you have a folder of files and the "
            "question is which of them are the same. It hashes a set at once "
            "and shows MD5, SHA-1, SHA-256 and CRC32 in one sortable list.\n\n"
            "Sorting by hash is what makes it a triage tool rather than a "
            "hashing utility: identical files collapse together immediately, "
            "so the same payload dropped under six names across four "
            "directories is obvious at a glance. Command-line hashing gives "
            "you the same numbers and leaves you to spot the duplicates "
            "yourself.\n\n"
            "For verifying a single acquisition against its recorded hash, "
            "`sha256sum` is the simpler answer."
        ),
        "sources": ["https://www.nirsoft.net/utils/hash_my_files.html"],
    },

    "CryptoTester": {
        "scenario": (
            "Reach for CryptoTester when you have a blob you believe is "
            "encoded or encrypted - a configuration block, a C2 address, part "
            "of a dropper - and you are working out how. It applies XOR, "
            "block ciphers, hashes and conversions interactively and shows "
            "entropy alongside, so you can judge whether a candidate result "
            "is plausible plaintext rather than guessing.\n\n"
            "It is built for guess-and-check, which is the honest shape of "
            "this work: you rarely know the scheme in advance. Once you do, "
            "scripting the transform is faster and repeatable - this is the "
            "tool for the part before that."
        ),
        "sources": ["https://www.nextron-systems.com/cryptotester/"],
    },

    "AccessEnum": {
        "scenario": (
            "Reach for AccessEnum when the question is *who can write where*. "
            "It walks a directory tree or registry branch and lists the "
            "effective permissions on each, which is the practical way to "
            "find a weak ACL without checking paths one at a time.\n\n"
            "Sorting by permission is the point: the outlier surfaces "
            "immediately - the world-writable directory under Program Files "
            "that lets an unprivileged user replace a binary a service runs "
            "as SYSTEM. That is a privilege-escalation path and a persistence "
            "mechanism at once, so it matters when hunting and when "
            "hardening.\n\n"
            "It reports what the permissions *are*. Whether they are wrong is "
            "your judgement, not the tool's."
        ),
        "sources": [
            "https://learn.microsoft.com/en-us/sysinternals/downloads/accessenum",
        ],
    },
}
