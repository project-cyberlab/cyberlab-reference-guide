#!/usr/bin/env python3
"""Audit the guide for garbage that got in by automation.

The linter checks that documented flags exist in a capture. It says nothing
about whether the surrounding text is sane, and several fields are populated by
running commands and keeping whatever came back. That is how the guide ended up
publishing `fls: invalid option -- '-'` as the opening line of a synopsis and
`/data/version is not a valid directory!` as a version number.

This pass looks for output that is obviously not what the field is meant to
hold. It is a linter for plausibility rather than for evidence.

Run: python scripts/audit.py [--fix]
"""
from __future__ import annotations
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REF = ROOT / "reference"
CAP = ROOT / "capture"
KIT = ROOT / "catalog" / "KIT-TOOLS.md"

# Text that means the command rejected us, not that it described itself.
ERROR_NOISE = re.compile(
    r"(invalid option|invalid argument|unrecognized option|unknown option|"
    r"is not a valid|command not found|no such file|illegal option|"
    r"Try '.*--help'|usage: .*\[-)", re.I)

# A version should be a version. These are the shapes that are not.
BAD_VERSION = re.compile(
    r"(not a valid|calling Getopt|invalid|error|usage|Traceback|"
    r"^\s*$|^-|^/)", re.I)


def audit_versions() -> list[str]:
    out = []
    for f in sorted(CAP.rglob("*.help.txt")):
        head = f.read_text(encoding="utf-8", errors="replace").splitlines()[:6]
        for line in head:
            if not line.startswith("# version:"):
                continue
            v = line.split(":", 1)[1].strip()
            if not v:
                continue
            if BAD_VERSION.search(v) or len(v) > 60:
                out.append(f"BAD-VERSION {f.name}: {v[:70]}")
    return out


def audit_capture_noise() -> list[str]:
    out = []
    for f in sorted(CAP.rglob("*.help.txt")):
        text = f.read_text(encoding="utf-8", errors="replace")
        body = text.split("#---", 1)[-1].strip().splitlines()
        for line in body[:3]:
            if ERROR_NOISE.search(line):
                out.append(f"CAPTURE-NOISE {f.name}: {line.strip()[:70]}")
                break
    return out


def audit_pages() -> list[str]:
    out = []
    for p in sorted(REF.rglob("*.md")):
        if p.name == "INDEX.md":
            continue
        text = p.read_text(encoding="utf-8", errors="replace")
        rel = p.relative_to(ROOT).as_posix()

        m = re.search(r"## Synopsis\s*\n+```\n(.*?)\n```", text, re.S)
        if m and ERROR_NOISE.search(m.group(1)):
            out.append(f"SYNOPSIS-NOISE {rel}: {m.group(1).strip().splitlines()[0][:60]}")

        m = re.search(r"## Purpose\s*\n+(.+)", text)
        if m:
            purpose = m.group(1).strip()
            if ERROR_NOISE.search(purpose):
                out.append(f"PURPOSE-NOISE {rel}: {purpose[:60]}")
            elif len(purpose) < 12 and not purpose.startswith("_TODO"):
                out.append(f"PURPOSE-THIN {rel}: {purpose[:40]}")

        for m in re.finditer(r"^\|\s*`([^`]+)`\s*\|([^|]*)\|([^|]*)\|", text, re.M):
            desc = m.group(3).strip()
            if ERROR_NOISE.search(desc):
                out.append(f"OPTION-NOISE {rel}: `{m.group(1)}` -> {desc[:50]}")
                break

        if re.search(r"\*\*Version:\*\*\s*\S{45,}", text):
            out.append(f"VERSION-LONG {rel}: version string over 45 chars")

        # The Argument column holds a placeholder name. A sentence fragment,
        # an unbalanced bracket or a stray English word means the flag parser
        # grabbed part of the description instead.
        for m in re.finditer(r"^\|\s*`([^`]+)`\s*\|\s*([^|]*?)\s*\|", text, re.M):
            arg = m.group(2).strip()
            if not arg or arg == "—":
                continue
            if arg.count("[") != arg.count("]") or arg.count("<") != arg.count(">"):
                out.append(f"ARG-BRACKETS {rel}: `{m.group(1)}` -> {arg[:30]}")
            elif arg.endswith((".", ",", ";", ":")):
                out.append(f"ARG-PUNCT {rel}: `{m.group(1)}` -> {arg[:30]}")
            elif arg.lower() in ("the", "a", "an", "of", "to", "and", "or",
                                 "is", "for", "with", "in", "on"):
                out.append(f"ARG-STRAY {rel}: `{m.group(1)}` -> {arg[:30]}")
            elif len(arg) > 30:
                out.append(f"ARG-LONG {rel}: `{m.group(1)}` -> {arg[:30]}")
    return out


def audit_unexplained_sections() -> list[str]:
    """Flag sections that are a bare table with nothing saying why they exist.

    Every complaint about this guide reading as a data dump has had the same
    shape: a heading, then straight into rows. The AutomationId column, the
    179-row control tables, the scan-engine list. The rows were often correct
    and still useless, because a reader cannot tell what question the table
    answers or when they would need it.

    One sentence of lead-in is the difference. It is a low bar and it is worth
    enforcing, because the failure mode is not writing something wrong -- it is
    filling a field because the field was there.
    """
    out = []
    # A handful of sections are self-evident from their title and do not need
    # a sentence to justify a table.
    # Matched on the leading word so that "Options -- complete" and
    # "Options (common)" count as the same self-evident section.
    OBVIOUS = {"options", "flags", "synopsis", "gotchas", "sources",
               "see", "common", "related"}
    heading = re.compile(r"^(#{2,4})\s+(.+?)\s*$")
    for p in sorted(REF.rglob("*.md")):
        if p.name == "INDEX.md":
            continue
        rel = p.relative_to(ROOT).as_posix()
        lines = p.read_text(encoding="utf-8", errors="replace").splitlines()
        # Fence-aware, because a `#` inside a code block is a shell comment
        # and not a heading. The cyberlab loop learned this the expensive way:
        # fence-blind section parsing mis-read 12 of 38 modules.
        in_fence = False
        for i, line in enumerate(lines):
            if line.lstrip().startswith("```"):
                in_fence = not in_fence
                continue
            if in_fence:
                continue
            m = heading.match(line)
            if not m:
                continue
            first = re.split(r"[\s(]", m.group(2).strip().lower())[0]
            if first in OBVIOUS:
                continue
            # Look at the first non-blank line under the heading.
            for nxt in lines[i + 1:]:
                if not nxt.strip():
                    continue
                if nxt.lstrip().startswith("|"):
                    out.append(f"SECTION-UNEXPLAINED {rel}: '{m.group(2)}' "
                               f"opens straight into a table")
                break
    return out


def audit_kit_list() -> list[str]:
    out = []
    if not KIT.exists():
        return out
    for i, line in enumerate(KIT.read_text(encoding="utf-8").splitlines(), 1):
        if not line.startswith("| ") or line.startswith("| Tool"):
            continue
        cells = line.split("|")
        if len(cells) < 5:
            continue
        tool, purpose = cells[1].strip(), cells[3].strip()
        if not tool:
            out.append(f"KIT-NOTOOL line {i}: row with no tool name")
        if purpose and ERROR_NOISE.search(purpose):
            out.append(f"KIT-PURPOSE-NOISE line {i}: {purpose[:60]}")
    return out


def main() -> int:
    groups = {
        "capture versions": audit_versions(),
        "capture bodies": audit_capture_noise(),
        "pages": audit_pages(),
        "unexplained sections": audit_unexplained_sections(),
        "kit list": audit_kit_list(),
    }
    total = sum(len(v) for v in groups.values())
    for name, items in groups.items():
        print(f"--- {name}: {len(items)}")
        for it in items[:12]:
            print(f"    {it}")
        if len(items) > 12:
            print(f"    ... and {len(items) - 12} more")
    print()
    print(f"AUDIT FINDINGS: {total}")
    return 1 if "--strict" in sys.argv and total else 0


if __name__ == "__main__":
    raise SystemExit(main())
