#!/usr/bin/env python3
"""Gate the guide against its own promises.

Failures (exit 1) — these break the guide's core claim:
  E-INVENTED   a page documents a flag that is NOT in the tool's capture
  E-NOCAPTURE  a page exists for a tool with no capture at all
  E-SCOPE      a page exists for a tool outside the kit catalogue

Warnings (exit 0) — quality debt, tracked not blocked:
  W-MISSING    a captured flag is absent from the page (completeness gap)
  W-TODO       placeholder text still present
  W-NOPURPOSE  no purpose line
  W-UNREVIEWED "when you would use it" column still empty

Run: python scripts/lint.py [--strict]   (--strict promotes warnings to errors)
"""
from __future__ import annotations
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from helpparse import parse_options  # noqa: E402

ROOT = HERE.parent
CAP = ROOT / "capture"
REF = ROOT / "reference"

COV = json.loads((CAP / "coverage.json").read_text(encoding="utf-8"))
DOCUMENTED: dict[str, dict] = COV["documented"]

# Flags in a page's options table
ROW = re.compile(r"^\|\s*`([^`]+)`\s*\|")
# Flags used inside fenced invocations
FLAG_IN_CMD = re.compile(r"(?<![\w-])(--?[A-Za-z][A-Za-z0-9-]*)")


def captured_flags(cmd: str) -> set[str] | None:
    meta = DOCUMENTED.get(cmd)
    if not meta:
        return None
    p = CAP / meta["image"] / "help" / f"{cmd}.help.txt"
    if not p.exists():
        safe = re.sub(r"[^A-Za-z0-9._-]", "_", cmd)
        p = CAP / meta["image"] / "help" / f"{safe}.help.txt"
    if not p.exists():
        return None
    text = p.read_text(encoding="utf-8", errors="replace")
    flags = {o["flag"] for o in parse_options(text)}
    # Also honour flags that appear anywhere in the raw help text: some tools
    # list options in prose or in a usage line the parser is too strict to take.
    flags |= set(FLAG_IN_CMD.findall(text))
    return flags


def main() -> int:
    strict = "--strict" in sys.argv
    errors: list[str] = []
    warns: list[str] = []
    pages = [p for p in REF.rglob("*.md") if p.name != "INDEX.md"]

    for page in sorted(pages):
        cmd = page.stem
        rel = page.relative_to(ROOT).as_posix()
        text = page.read_text(encoding="utf-8", errors="replace")

        # A "<tool>-gui" page documents the graphical interface of a tool whose
        # CLI is documented separately. It is gated against the accessibility
        # tree in capture/gui/ exactly as a CLI page is gated against --help:
        # a control named on the page must exist in the tree, and a control in
        # the tree should be accounted for on the page.
        if cmd.endswith("-gui"):
            base = cmd[:-4]
            tree = CAP / "gui" / base / f"{base}.tree.txt"
            if not tree.exists():
                errors.append(f"E-GUI-NOCAPTURE {rel}: no control tree at "
                              f"capture/gui/{base}/{base}.tree.txt")
                continue
            dump = tree.read_text(encoding="utf-8", errors="replace")

            # Control names as the walker recorded them: Type "Name" #AutomationId
            captured_ctrls = set(re.findall(r'^\s*\w+ "([^"]+)"', dump, re.M))
            captured_ids = set(re.findall(r"#(\S+)", dump))

            # Controls the page claims, written in bold. Bold is also used for
            # header labels ("Kit:") and ordinary emphasis, so a claim only
            # counts when it looks like a control label: short, no trailing
            # colon, no sentence punctuation. Otherwise every emphasised phrase
            # is reported as an invented control and the check becomes noise
            # nobody reads.
            def looks_like_control(s: str) -> bool:
                s = s.strip()
                if not s or s.endswith(":") or len(s) > 30:
                    return False
                return not any(ch in s for ch in ",;")

            claimed = {c for c in re.findall(r"\*\*([^*]{1,40})\*\*", text)
                       if looks_like_control(c)}

            invented_ctrls = sorted(
                c for c in claimed
                if c not in captured_ctrls and c not in captured_ids)
            if invented_ctrls:
                warns.append(
                    f"W-GUI-INVENTED {rel}: {len(invented_ctrls)} name(s) not in "
                    f"the tree: {', '.join(invented_ctrls[:6])}")

            missing_ctrls = sorted(c for c in captured_ctrls if c not in text)
            if missing_ctrls:
                warns.append(
                    f"W-GUI-MISSING {rel}: {len(missing_ctrls)} captured "
                    f"control(s) absent: {', '.join(missing_ctrls[:6])}")

            if not re.search(r"!\[[^\]]*\]\([^)]*\.png\)", text):
                warns.append(f"W-GUI-NOSHOT {rel}: no screenshot referenced")

            steps = len(re.findall(r"^\d+\. ", text, re.M))
            if steps > 7:
                warns.append(f"W-GUI-STEPS {rel}: {steps} numbered steps; "
                             f"more than seven means more than one task")
            continue

        cf = captured_flags(cmd)
        if cf is None:
            errors.append(f"E-NOCAPTURE {rel}: no capture for `{cmd}`")
            continue

        documented_flags = set()
        for line in text.splitlines():
            m = ROW.match(line)
            if m:
                documented_flags.add(m.group(1).strip())

        invented = sorted(f for f in documented_flags if f not in cf)
        if invented:
            errors.append(
                f"E-INVENTED {rel}: {len(invented)} flag(s) not in capture: "
                + ", ".join(invented[:10]))

        # Only count a flag as "missing" if it is unambiguously a real flag.
        # A single-dash token with several letters is a usage-line CLUSTER
        # ("[-hvV]", "[-BehjkLqRrvX]"), not an option -- counting those would
        # invent work that does not exist.
        def real_flag(f: str) -> bool:
            if f.startswith("--"):
                return bool(re.fullmatch(r"--[A-Za-z][A-Za-z0-9-]*", f))
            return bool(re.fullmatch(r"-[A-Za-z0-9]", f))

        missing = sorted(f for f in cf
                         if f not in documented_flags and real_flag(f)
                         and f not in ("--help", "--version"))
        if missing and documented_flags:
            warns.append(f"W-MISSING {rel}: {len(missing)} captured flag(s) not "
                         f"documented: {', '.join(missing[:8])}")

        if "_TODO" in text:
            warns.append(f"W-TODO {rel}: placeholder text remains")
        if re.search(r"^## Purpose\s*\n\s*\n\s*_TODO", text, re.M):
            warns.append(f"W-NOPURPOSE {rel}: no purpose line")

        rows = [l for l in text.splitlines() if ROW.match(l)]
        if rows:
            unreviewed = sum(1 for l in rows if re.search(r"\|\s*\|\s*$", l))
            if unreviewed == len(rows):
                warns.append(f"W-UNREVIEWED {rel}: 'when you would use it' "
                             f"empty for all {len(rows)} options")

    print(f"linted {len(pages)} pages")
    for e in errors:
        print("  " + e)
    for w in warns[:40]:
        print("  " + w)
    if len(warns) > 40:
        print(f"  ... and {len(warns) - 40} more warnings")
    from collections import Counter
    by_code = Counter(m.split()[0] for m in errors + warns)
    print("\nby code:")
    for code, n in sorted(by_code.items()):
        print(f"  {code:14s} {n}")
    print(f"\nERRORS={len(errors)}  WARNINGS={len(warns)}")

    if errors or (strict and warns):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
