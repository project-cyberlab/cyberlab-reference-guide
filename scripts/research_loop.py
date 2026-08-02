#!/usr/bin/env python3
"""Draft the judgement layer with a local model, then validate every word of it.

The guide needs a "when you would use it" note for ~2,300 more option rows and
a real purpose for ~60 more tools. That is too much to write by hand and far
too much to trust a model with unchecked -- an unvalidated model writing
plausible command guidance is precisely the cyberlab failure, reproduced at
machine speed.

So the loop is: evidence in, draft out, validate hard, keep what survives.

    1. pick a tool that needs work
    2. build a prompt containing ONLY its captured --help text
    3. ask a local model for the missing notes, one line per flag
    4. reject anything that mentions a flag not in that capture, restates the
       captured description, exceeds a sentence or two, or hedges
    5. write survivors to enrichment_draft.py for review

Nothing this produces reaches a page until it is moved into enrichment.py.
The draft file is quarantine, not output.

Local first because it is free and private: rick's 4090 and l3e7's 3090 both
run ollama. Falls back to an API key only when asked.

usage:
    python scripts/research_loop.py --list
    python scripts/research_loop.py --tool fls [--model mistral-small3.2:24b-instruct-2506-q4_K_M]
    python scripts/research_loop.py --batch 10
"""
from __future__ import annotations
import argparse
import json
import os
import re
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CAP = ROOT / "capture"
REF = ROOT / "reference"
DRAFT = ROOT / "scripts" / "enrichment_draft.py"

# l3e7 is the thinking box. Port 11434 is the ollama default -- this
# pointed at 11435 and silently failed every call, which is why the
# loop shipped without ever having been run.
OLLAMA = os.environ.get("OLLAMA_HOST", "http://192.168.1.253:11434")
DEFAULT_MODEL = os.environ.get("RESEARCH_MODEL",
                               "mistral-small3.2:24b-instruct-2506-q4_K_M")

PROMPT = """You are documenting a digital-forensics command-line tool for an \
analyst who has never used it.

Below is the tool's own --help output. This is the ONLY source you may use. \
Do not use knowledge of other tools. Do not mention any flag that does not \
appear below.

TOOL: {cmd}

--- captured help ---
{help}
--- end ---

For each flag listed, write ONE short sentence saying WHEN an analyst would \
reach for it. Not what it does -- the help already says that -- but why and \
in what situation. If you cannot say something useful and specific about a \
flag, omit it entirely; an omission is fine and a vague line is not.

Output strict JSON only, no prose around it:
{{"when": {{"-x": "sentence", "--long": "sentence"}}}}
"""


def captured(cmd: str) -> tuple[str, set[str]] | None:
    cov = json.loads((CAP / "coverage.json").read_text(encoding="utf-8"))
    meta = cov["documented"].get(cmd)
    if not meta:
        return None
    safe = re.sub(r"[^A-Za-z0-9._-]", "_", cmd)
    for name in (f"{cmd}.help.txt", f"{safe}.help.txt"):
        p = CAP / meta["image"] / "help" / name
        if p.exists():
            text = p.read_text(encoding="utf-8", errors="replace")
            flags = set(re.findall(r"(?<![\w-])(--?[A-Za-z][A-Za-z0-9-]*)", text))
            return text, flags
    return None


def needs_work() -> list[tuple[int, str, Path]]:
    """Pages with option rows and no guidance, worst first."""
    out = []
    row = re.compile(r"^\|\s*`([^`]+)`\s*\|")
    for p in REF.rglob("*.md"):
        if p.name == "INDEX.md" or p.stem.endswith("-gui"):
            continue
        empty = total = 0
        for line in p.read_text(encoding="utf-8", errors="replace").splitlines():
            if not row.match(line):
                continue
            total += 1
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if not (len(cells) >= 4 and cells[-1]):
                empty += 1
        if empty:
            out.append((empty, p.stem, p))
    out.sort(reverse=True)
    return out


def ask(model: str, prompt: str) -> str:
    body = json.dumps({
        "model": model,
        "prompt": prompt,
        "stream": False,
        "options": {"temperature": 0.2, "num_ctx": 8192},
    }).encode()
    req = urllib.request.Request(f"{OLLAMA}/api/generate", data=body,
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=600) as r:
        return json.loads(r.read()).get("response", "")


HEDGE = re.compile(r"\b(may be used|can be used|is used to|allows you to|"
                   r"this option|use this|typically|generally|as needed|"
                   r"if desired|various|etc\.)\b", re.I)


def flag_desc(help_text: str, flag: str) -> str:
    """The captured description sitting next to this flag in the help output."""
    lines = help_text.splitlines()
    for i, line in enumerate(lines):
        s = line.strip()
        if not s.startswith("-"):
            continue
        head = re.split(r"\s{2,}", s, 1)
        if flag not in re.findall(r"(?<![\w-])(--?[A-Za-z][A-Za-z0-9-]*)", head[0]):
            continue
        if len(head) > 1 and head[1].strip():
            return head[1].strip()
        # optparse and argparse both wrap: when a flag takes an argument the
        # spec fills the line and the description lands on the next one,
        # indented further. Without this the guard silently sees no
        # description and waves the paraphrase through -- which is exactly
        # what happened on pdf-parser.
        indent = len(line) - len(line.lstrip())
        for nxt in lines[i + 1:]:
            if not nxt.strip():
                break
            if len(nxt) - len(nxt.lstrip()) > indent:
                return nxt.strip()
            break
    return ""


def validate(draft: dict, cmd: str, help_text: str, real_flags: set[str]) -> tuple[dict, list[str]]:
    """Keep only notes that are grounded, specific and short."""
    kept, rejected = {}, []
    described = {ln.strip().lower() for ln in help_text.splitlines()}
    for flag, note in (draft.get("when") or {}).items():
        note = " ".join(str(note).split())
        if flag not in real_flags:
            rejected.append(f"{flag}: not in capture")
            continue
        if not note or len(note) < 15:
            rejected.append(f"{flag}: too short")
            continue
        if len(note) > 240:
            rejected.append(f"{flag}: too long")
            continue
        if HEDGE.search(note):
            rejected.append(f"{flag}: hedged/filler")
            continue
        if note.strip().lower() in described:
            rejected.append(f"{flag}: restates the help text")
            continue
        # The subtler restatement, and the one that actually got through:
        # take the flag's own description, prepend "When you need to", submit.
        # "-o: select indirect object by id" becomes "When you need to focus on
        # specific indirect objects by their IDs" -- which fills the column and
        # tells a junior analyst nothing they could not read one cell to the
        # left. Compare content words against the captured description for this
        # specific flag and refuse a paraphrase.
        desc = flag_desc(help_text, flag)
        if desc:
            stop = {"the", "a", "an", "of", "to", "and", "or", "in", "on",
                    "for", "with", "by", "when", "you", "your", "need",
                    "want", "are", "is", "it", "this", "that", "their",
                    "specific", "use", "using", "from", "at", "as", "be"}
            def words(s):
                return {w for w in re.findall(r"[a-z]+", s.lower())
                        if w not in stop and len(w) > 2}
            nw, dw = words(note), words(desc)
            if nw and len(nw & dw) / len(nw) >= 0.45:
                rejected.append(f"{flag}: paraphrases its own description")
                continue
        # A note naming a flag that does not exist is the cardinal error.
        bogus = [f for f in re.findall(r"(?<![\w-])(--?[A-Za-z][A-Za-z0-9-]*)", note)
                 if f not in real_flags]
        if bogus:
            rejected.append(f"{flag}: invents {bogus[:3]}")
            continue
        kept[flag] = note
    return kept, rejected


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--tool")
    ap.add_argument("--batch", type=int, default=0)
    ap.add_argument("--model", default=DEFAULT_MODEL)
    a = ap.parse_args()

    work = needs_work()
    if a.list:
        print(f"{len(work)} pages need guidance, worst first:")
        for empty, stem, _ in work[:30]:
            print(f"  {empty:4d} empty  {stem}")
        return 0

    targets = ([a.tool] if a.tool
               else [s for _, s, _ in work[:a.batch]] if a.batch
               else [])
    if not targets:
        print("nothing to do; pass --tool or --batch")
        return 1

    results: dict[str, dict] = {}
    for cmd in targets:
        cap = captured(cmd)
        if not cap:
            print(f"  {cmd}: no capture, skipped")
            continue
        help_text, real_flags = cap
        print(f"  {cmd}: asking {a.model} ({len(real_flags)} real flags)")
        try:
            raw = ask(a.model, PROMPT.format(cmd=cmd, help=help_text[:12000]))
        except Exception as e:
            print(f"    model call failed: {e}")
            continue
        m = re.search(r"\{.*\}", raw, re.S)
        if not m:
            print("    no JSON in response")
            continue
        try:
            draft = json.loads(m.group(0))
        except json.JSONDecodeError:
            print("    response was not valid JSON")
            continue
        kept, rejected = validate(draft, cmd, help_text, real_flags)
        print(f"    kept {len(kept)}, rejected {len(rejected)}")
        for r in rejected[:4]:
            print(f"      - {r}")
        if kept:
            results[cmd] = kept

    if not results:
        print("nothing survived validation")
        return 0

    header = ('"""Model-drafted guidance awaiting review.\n\n'
              "NOT loaded by the build. Every line here was written by a local\n"
              "model from a tool's captured help and survived validation, which\n"
              "means it is grounded and specific -- not that it is correct.\n"
              "Read it, fix it, move it into enrichment.py.\n"
              '"""\n\nDRAFT = ')
    existing = {}
    if DRAFT.exists():
        try:
            ns: dict = {}
            exec(DRAFT.read_text(encoding="utf-8"), ns)
            existing = ns.get("DRAFT", {})
        except Exception:
            pass
    existing.update(results)
    DRAFT.write_text(header + json.dumps(existing, indent=4) + "\n", encoding="utf-8")
    print(f"\nwrote {sum(len(v) for v in existing.values())} notes across "
          f"{len(existing)} tools to {DRAFT.relative_to(ROOT)}")
    print("review before moving into enrichment.py -- the build does not read it")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
