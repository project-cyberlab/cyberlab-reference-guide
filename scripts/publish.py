#!/usr/bin/env python3
"""Promote verified research into the guide, with its citations.

Until now nothing the loop produced could reach a page. That was deliberate
while the pipeline was unproven -- the previous project published generated
text directly and shipped fabricated CLI flags across 44 of 61 modules -- but
a quarantine with no exit is just a slower way of producing nothing.

This is the exit, and it is narrow on purpose:

  * only records the loop KEPT, meaning they survived the mechanical gate,
    the directionality check and blind verification
  * only records carrying at least one citation
  * every published note keeps its sources, printed on the page, so a reader
    can check the claim rather than trust it
  * writing to enrichment.py is a separate deliberate act, run by a human,
    never a side effect of a research pass

What lands on the page is a "When you'd reach for this" section under Purpose
-- the tool-level scenario. That is the shape the user asked for: not a table
cell, but a few sentences saying what situation brings you here, what runs
before and after, and why this tool rather than the one beside it.

    python scripts/publish.py --dry-run     # show what would be written
    python scripts/publish.py               # write it
"""
from __future__ import annotations
import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
KEPT = ROOT / "research_output.json"
TARGET = ROOT / "scripts" / "enrichment.py"

BEGIN = "# --- BEGIN researched scenarios (scripts/publish.py) ---"
END = "# --- END researched scenarios ---"


DECISIONS = ROOT / "research_decisions.json"


def load_kept() -> list[dict]:
    """Only what survived the loop AND was explicitly accepted on review.

    A mechanical threshold cannot stand in for the review. Measured on pass
    two: foremost scored 2 on passage quality and was good; mraptor scored 5
    and led with a niche feature while burying the tool's actual job. Score
    and source count predict neither. So the review verdict is recorded per
    tool in research_decisions.json and nothing publishes without one --
    silence is not consent, because an unreviewed note is exactly what the
    previous project shipped 44 modules of.
    """
    try:
        recs = json.loads(KEPT.read_text(encoding="utf-8"))
    except Exception:
        return [], {}
    try:
        decisions = json.loads(DECISIONS.read_text(encoding="utf-8"))
    except Exception:
        decisions = {}

    out, unreviewed, flags = [], [], {}
    for r in recs:
        if r.get("flag"):
            # Flag notes fill the "When you would use it" column -- the one
            # the whole project is about. They were being skipped here, so 41
            # verified answers sat in quarantine with no route to a page while
            # the column stayed at 26%.
            #
            # Keyed by tool and flag, and rejected verdicts are honoured the
            # same way as for tool notes.
            key = f"{r['tool']} {r['flag']}"
            d = decisions.get(key)
            # Require an explicit accept, exactly as tool notes do.
            #
            # This published on the ABSENCE of a verdict, which is backwards
            # and shipped a fabrication within one iteration: `diec -t` went
            # live saying it tags a Docker image, because the model had read a
            # Dockerfile and described `docker build -t`. Silence is not
            # consent. It is the precise mechanism that put 44 modules of
            # invented flags into the previous project, reproduced here by me
            # in a single commit.
            if not d:
                unreviewed.append(key)
                continue
            if d.get("verdict") != "accept":
                continue
            note = " ".join((r.get("note") or "").split())
            if len(note) < 30 or not r.get("citations"):
                continue
            flags.setdefault(r["tool"], {})[r["flag"]] = note
            continue
        if r.get("status") != "kept":
            continue
        if not r.get("citations"):
            continue                       # uncited means uncheckable
        note = " ".join((r.get("note") or "").split())
        if len(note) < 60:
            continue
        d = decisions.get(r["tool"])
        if not d:
            unreviewed.append(r["tool"])
            continue
        if d.get("verdict") != "accept":
            continue
        # "An analyst reaches for this tool when..." reads as boilerplate on a
        # page that is already about that tool. Name it, so a reader landing
        # mid-document knows what they are reading about.
        note = re.sub(r"\bthis tool\b", r["tool"], note, count=1)
        out.append({"tool": r["tool"], "note": note,
                    "citations": r["citations"][:3]})
    if unreviewed:
        print(f"held back, awaiting review: {', '.join(sorted(unreviewed))}\n")
    return out, flags


def render_block(records: list[dict], flagnotes: dict) -> str:
    lines = [BEGIN,
             "#",
             "# Generated by scripts/publish.py from research the loop verified:",
             "# retrieved from real documentation and walkthroughs, checked",
             "# against the sources blind to the draft, and cited. Do not edit",
             "# by hand -- rerun publish.py. Anything hand-written belongs in",
             "# ENRICHMENT above, which always wins over this block.",
             "RESEARCHED: dict[str, dict] = {"]
    for r in sorted(records, key=lambda x: x["tool"]):
        lines.append(f"    {r['tool']!r}: {{")
        lines.append(f"        'scenario': {r['note']!r},")
        lines.append(f"        'sources': {r['citations']!r},")
        lines.append("    },")
    lines.append("}")
    lines.append("")
    # The flag column. Keyed tool -> flag -> note, merged into ENRICHMENT's
    # existing "when" dict so a hand-written note for one flag is never lost
    # because research produced one for another flag on the same tool.
    lines.append("RESEARCHED_FLAGS: dict[str, dict] = {")
    for tool in sorted(flagnotes):
        lines.append(f"    {tool!r}: {{")
        for fl in sorted(flagnotes[tool]):
            lines.append(f"        {fl!r}: {flagnotes[tool][fl]!r},")
        lines.append("    },")
    lines.append("}")
    lines.append("")
    lines.append("for _cmd, _fl in RESEARCHED_FLAGS.items():")
    lines.append("    _w = ENRICHMENT.setdefault(_cmd, {}).setdefault('when', {})")
    lines.append("    for _f, _n in _fl.items():")
    lines.append("        _w.setdefault(_f, _n)")
    lines.append("")
    lines.append("# Hand-written entries win: a human who wrote a scenario has")
    lines.append("# judged it, and a research pass must never overwrite that.")
    lines.append("for _cmd, _rec in RESEARCHED.items():")
    lines.append("    _e = ENRICHMENT.setdefault(_cmd, {})")
    lines.append("    _e.setdefault('scenario', _rec['scenario'])")
    lines.append("    _e.setdefault('sources', _rec['sources'])")
    lines.append(END)
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()

    records, flagnotes = load_kept()
    if not records and not flagnotes:
        print("nothing verified to publish")
        return 0

    print(f"{len(records)} verified scenarios ready:\n")
    for r in records:
        print(f"  {r['tool']}")
        print(f"    {r['note'][:150]}")
        print(f"    cites {len(r['citations'])}: "
              f"{r['citations'][0].split('//')[-1][:60]}")
    if a.dry_run:
        print("\n(dry run, nothing written)")
        return 0

    text = TARGET.read_text(encoding="utf-8")
    block = render_block(records, flagnotes)
    if BEGIN in text:
        text = re.sub(re.escape(BEGIN) + r".*?" + re.escape(END),
                      block, text, flags=re.S)
    else:
        text = text.rstrip() + "\n\n\n" + block + "\n"
    TARGET.write_text(text, encoding="utf-8")
    print(f"\nwrote {len(records)} scenarios into {TARGET.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
