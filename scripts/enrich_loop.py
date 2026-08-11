#!/usr/bin/env python3
"""Turn retrieved evidence into guidance, and refuse anything not grounded.

The pipeline, per tool or flag:

    retrieve passages showing it in use   (sources.py, cited)
        -> local model compresses one passage to one sentence
        -> GATE, mechanical: grounded? cites a live page? invents nothing?
                             does it state a SCENARIO rather than a definition?
        -> keep the best survivor, with its URL
        -> nothing survived: write a MISS, never a blank

The gate is the only ground truth and the model never self-certifies. That
rule is inherited from the loop that broke without it: cyberlab shipped
fabricated CLI flags across ~44 of 61 modules by trusting generated text.

Output goes to research_output.json, which the build does not read. Promoting
anything into enrichment.py is a separate, deliberate act.

    python scripts/enrich_loop.py --tool pdfid
    python scripts/enrich_loop.py --tools pdfid pdf-parser photorec testdisk
    python scripts/enrich_loop.py --tool fls --flags
"""
from __future__ import annotations
import argparse
import hashlib
import json
import re
from collections import Counter
import sys
import time
from datetime import datetime
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import sources  # noqa: E402
import blind_check  # noqa: E402

ROOT = HERE.parent
OUT = ROOT / "research_output.json"
MISSES = ROOT / "research_misses.json"
REVIEW = ROOT / "research_review.json"
# The append-only history of every verdict. run_forever mirrors here.
LIVE_LOG = ROOT / "research_live.log"

# Both GPUs. Measured: 9-14B models answer this as well as 32B and twice as
# fast, because compressing one retrieved paragraph is near-trivial work.
# Bigger models buy nothing here; more sources do.
WORKERS = [
    ("l3e7-3090", "http://192.168.1.253:11434", "qwen3:14b"),
    ("rick-4090", "http://100.112.76.79:11434", "qwen3:14b"),
]

TOOL_PROMPT = """You are writing for a junior forensic analyst who has never \
used this tool.

TOOL: {tool}

Below are passages from real documentation and walkthroughs showing it in use.

{passages}

Write 2-3 sentences saying WHEN an analyst reaches for this tool: what \
situation brings them here, what they run before or after it, and why they \
would pick it over a similar tool. Use ONLY what the passages state.

If the passages do not support that, reply exactly: INSUFFICIENT

No preamble, no bullet points, just the sentences."""

FLAG_PROMPT = """You are writing for a junior forensic analyst.

TOOL: {tool}
FLAG: {flag}

Below are passages from real documentation and walkthroughs.

{passages}

Write ONE sentence saying WHEN an analyst would use this flag -- the situation, \
not the definition. Use ONLY what the passages state.

If the passages do not say when to use it, reply exactly: INSUFFICIENT

No preamble, just the sentence."""


def ask(base: str, model: str, prompt: str, timeout: int = 300) -> str:
    body = json.dumps({"model": model, "prompt": prompt, "stream": False,
                       "options": {"temperature": 0.1, "num_ctx": 8192}}).encode()
    req = urllib.request.Request(base + "/api/generate", data=body,
                                 headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return json.loads(r.read()).get("response", "").strip()
    except Exception as e:
        return f"__ERROR__ {e}"


# ---------------------------------------------------------------- the gate

STOP = {"the", "a", "an", "of", "to", "and", "or", "in", "on", "for", "with",
        "by", "when", "you", "your", "it", "is", "are", "this", "that", "be",
        "would", "will", "can", "use", "used", "using", "as", "at", "from",
        "analyst", "junior", "forensic", "tool", "flag", "reach", "reaches"}


def _stem(w: str) -> str:
    """Crude suffix stripping, enough to match a plural to its singular.

    Grounding was measured by exact word overlap, so a note saying "disk
    images" against a source saying "disk image" scored the plural as
    ungrounded. Every grounding failure clustered at 37-45% against a 45%
    threshold, and inspecting one showed the missing words were devices,
    drives, filesystems, images -- all present in the sources in the
    singular -- plus ordinary verb forms like ensuring and focuses.

    The threshold was not too strict. The measurement was wrong, and lowering
    the bar to compensate would have weakened the one check that stops a model
    writing from memory instead of from the page.
    """
    # "es" overshoots: devices -> devic while device stays device,
    # so the plural still failed to match its own singular. Plain "s"
    # handles both.
    for suf in ("ing", "ies", "ed", "s"):
        if w.endswith(suf) and len(w) - len(suf) >= 3:
            base = w[: -len(suf)]
            return base + "y" if suf == "ies" else base
    return w


def words(s: str) -> set[str]:
    return {_stem(w) for w in re.findall(r"[a-z0-9]+", s.lower())
            if w not in STOP and len(w) > 2}


# A note has to say WHEN, which means naming a trigger, a position in a
# workflow, a choice against something else, or a consequence. A sentence
# with none of these is a definition wearing a "when you need to" hat --
# the exact defect this whole exercise exists to remove.
SCENARIO = (
    r"\bafter\b", r"\bbefore\b", r"\bonce\b", r"\bthen\b", r"\bnext\b",
    r"\bfeeds?\b", r"\bfollow(?:s|ed|ing)?\b", r"\bstep\b", r"\bfirst\b",
    r"\bwhen\b", r"\bif\b", r"\bwhere\b", r"\bsuspect", r"\bflagg?ed\b",
    r"\bnon-?zero\b", r"\bfail(?:s|ed|ing)?\b", r"\bmalformed\b",
    r"\bunlike\b", r"\binstead\b", r"\brather than\b", r"\bwhereas\b",
    r"\bcannot\b", r"\bdoes not\b", r"\bwithout\b", r"\bso that\b",
    r"\bbecause\b", r"\bin order to\b", r"\botherwise\b", r"\bevidence\b",
    r"\btimeline\b", r"\bcorrelat", r"\btriage\b", r"\bconfirm",
)

HEDGE = re.compile(r"\b(may be used|can be used|is used to|allows you to|"
                   r"this option|this flag|typically|generally|as needed|"
                   r"if desired|various|etc\.|in summary|note that)\b", re.I)


# The model talking about its own inputs instead of the tool.
#
# "The passages do not explicitly compare it to similar tools." "...as the
# passages caution against its general use." "...as described in the
# passages." The model is handed retrieved passages and sometimes writes
# about them rather than from them, and the result reads as an answer while
# telling the analyst nothing: a junior analyst has never seen these
# passages and never will.
#
# Two such notes are live in the guide right now (mactime, evtxexport),
# which is how this was found -- by reading published output rather than by
# any counter moving.
#
# Deliberately NOT matching a bare "source" or "context". Those are ordinary
# forensic words: "the source system's time zone", "preparing the source and
# destination media". Both were false positives on the first draft of this
# pattern, and rejecting them would have thrown away two correct notes.
META = re.compile(
    r"\b(?:the|these|those|above|given|provided|supplied)\s+"
    r"(?:passages?|excerpts?|snippets?)\b"
    r"|\bpassages?\s+(?:show|shows|state|states|caution|cautions|indicate|"
    r"indicates|mention|mentions|do not|does not)\b"
    r"|\bin the context of the walkthrough\b", re.I)


def strip_meta(note: str) -> str:
    """Drop whole sentences that talk about the retrieved passages.

    Removing the sentence rather than rejecting the note, because the leak
    is almost always one trailing clause bolted onto guidance that is
    otherwise correct and cited. Rejecting would discard the good part to
    punish the scaffolding.

    Mechanical, not a rewrite. Asking a model to fix its own note reopens
    exactly the door this project closed: text that no longer corresponds to
    any retrieved passage. Cutting a sentence cannot invent anything.
    """
    kept: list[str] = []
    for part in re.split(r"(?<=[.!?])\s+", note.strip()):
        m = META.search(part)
        if not m:
            kept.append(part)
            continue
        # Usually the leak is a trailing clause bolted onto real guidance --
        # "...when monitoring a downloads directory, as the passages caution
        # against its general use." Cutting at the comma keeps the answer and
        # loses only the aside. Dropping the whole sentence would have thrown
        # away the guidance to punish the clause, which is what the first
        # version of this did to clamscan --remove and yara.
        cut = part.rfind(",", 0, m.start())
        trimmed = part[:cut].strip() if cut > 0 else ""
        if len(trimmed) >= 40 and not META.search(trimmed):
            kept.append(trimmed.rstrip(",;: ") + ".")
    return " ".join(kept).strip()


# ------------------------------------------------- the directionality check
#
# The failure this exists for: a local model produced six fluent, grounded,
# correctly-cited notes, the mechanical gate passed all six, and two of them
# had the workflow BACKWARDS.
#
#   "pdfid ... often running it before or after using pdf-parser"
#   "mraptor ... run it after olevba to confirm macro presence"
#
# pdfid always runs first -- it is the ten-second count that decides whether
# pdf-parser is worth opening. mraptor is the fast triage verdict that runs
# BEFORE olevba's deep analysis. Both notes invert the order.
#
# Nothing in a grounded-and-cited check can catch a reversed arrow. Each note
# was assembled from passages that legitimately mention both tools; the model
# guessed the direction between them. For a junior analyst -- the entire
# audience -- a reversed workflow is worse than no guidance, because it reads
# as authoritative and sends them down the expensive path first.
#
# So an ordering claim is treated as a CLAIM, requiring support in the
# passages, rather than as prose.


# Orderings established once, by hand, after checking the sources.
#
# The corroboration check looks for a cue sitting next to the second tool
# name. Real pipelines are not written that way: the Sleuth Kit wiki links
# fls to mactime through the body file they share, never with the word
# "then". So a correct and thoroughly documented ordering was sent to review
# every single round, for both tools, forever.
#
# Re-deriving the same fact from prose on every pass and failing every time
# is not rigour, it is a treadmill. These are verified once and recorded, and
# the reviewer tier is exactly where that judgement belongs.
VERIFIED_ORDER: set[tuple[str, str]] = {
    ("fls", "mactime"),          # fls -m writes the body file mactime sorts
    ("ils", "mactime"),          # same, for inode-level output
    ("tsk_gettimes", "mactime"),
    ("pdfid", "pdf-parser"),     # count first, parse only if it is non-zero
    ("pdfid.py", "pdf-parser.py"),
    ("oleid", "olevba"),         # triage the document, then read the macros
    ("mraptor", "olevba"),       # fast verdict, then deep analysis
    ("log2timeline.py", "psort.py"),   # collect, then sort and filter
    ("dd", "foremost"),          # image the disk, then carve the image
    ("dc3dd", "foremost"),
    ("dd", "scalpel"),
    ("testdisk", "photorec"),    # repair the filesystem, else carve past it
    ("ewfacquire", "ewfexport"),
    ("volatility3", "strings"),
}

_ORDER_BEFORE = (r"before", r"prior to", r"ahead of", r"feeds? (?:in)?to",
                 r"then (?:run|use)", r"followed by")
_ORDER_AFTER = (r"after", r"following", r"once you(?:'ve| have)",
                r"subsequent to")

# An ordering claim hedged both ways states nothing and hides an error --
# which is exactly how the pdfid note slipped through.
_HEDGED_ORDER = re.compile(
    r"\b(?:before or after|after or before|either before or after)\b", re.I)


# Tool names that are also ordinary English. `file`, `strings` and `sort` are
# real tools in the catalogue, so "recover files", "the file system" and
# "strings of text" were being read as workflow claims about them. Any tool
# whose name is a common word has to be excluded from the ordering universe
# or the check fires constantly on plain prose.
_COMMON_WORD_TOOLS = {
    "file", "files", "strings", "sort", "find", "date", "time", "tree",
    "top", "test", "info", "list", "stat", "split", "join", "head", "tail",
    "diff", "patch", "make", "man", "who", "size", "base64", "expand",
    "install", "link", "true", "false", "yes", "print", "read", "seq",
}


def _known_tools() -> set[str]:
    try:
        cov = json.loads((ROOT / "capture" / "coverage.json")
                         .read_text(encoding="utf-8"))
        return {t for t in cov["documented"]
                if len(t) > 2 and t.lower() not in _COMMON_WORD_TOOLS}
    except Exception:
        return set()


def ordering_claims(note: str, subject: str,
                    universe: set[str]) -> list[tuple[str, str]]:
    """Ordering assertions in the note, as (runs_first, runs_second) pairs.

    Only pairs where the OTHER tool is one we know about, so ordinary English
    ("after scanning") is not mistaken for a workflow claim.
    """
    claims: list[tuple[str, str]] = []
    others = {t for t in universe
              if t.lower() != subject.lower()
              and re.search(r"(?<![\w./-])" + re.escape(t) + r"(?![\w-])",
                            note, re.I)}
    for other in others:
        for pat in _ORDER_AFTER:
            # "<subject> ... after ... <other>"  => other runs first
            if re.search(pat + r"[^.;]{0,60}?" + re.escape(other), note, re.I):
                claims.append((other, subject))
        for pat in _ORDER_BEFORE:
            if re.search(pat + r"[^.;]{0,60}?" + re.escape(other), note, re.I):
                claims.append((subject, other))
    return list(dict.fromkeys(claims))


def ordering_support(claim: tuple[str, str], evidence: list[dict]) -> int:
    """+1 if the passages back this order, -1 if they contradict it, 0 if silent.

    The cue must sit immediately before the second tool's name. Scanning a
    whole 320-character span for the word "after" matched prose that had
    nothing to do with the two tools, and turned a correct claim
    (pdfid before pdf-parser) into a reported contradiction.
    """
    first, second = claim
    fpat = r"(?<![\w./-])" + re.escape(first) + r"(?![\w-])"
    spat = r"(?<![\w./-])" + re.escape(second) + r"(?![\w-])"
    before_cue = re.compile(r"(?:" + "|".join(_ORDER_BEFORE) +
                            r"|then|next|first)[^.;]{0,24}$", re.I)
    after_cue = re.compile(r"(?:" + "|".join(_ORDER_AFTER) +
                           r")[^.;]{0,24}$", re.I)
    votes = 0
    for e in evidence:
        text = e["passage"]
        for fm in re.finditer(fpat, text, re.I):
            for sm in re.finditer(spat, text[fm.end():fm.end() + 320], re.I):
                lead = text[fm.end():fm.end() + sm.start()]
                if before_cue.search(lead):
                    votes += 1
                elif after_cue.search(lead):
                    votes -= 1
                break
    return 1 if votes > 0 else (-1 if votes < 0 else 0)


def check_direction(note: str, subject: str,
                    evidence: list[dict]) -> tuple[str, str]:
    """Classify an ordering claim. Returns (verdict, reason).

    verdict is "ok", "reject" or "review".

    A mechanical check cannot adjudicate what it cannot verify, and pretending
    otherwise produces false negatives -- three correct notes were rejected
    here for asserting orders the retrieved passages simply did not spell out.
    Silence is not disproof. That is the same error as concluding no source
    exists because a search came up empty.

    So:
      contradicted by a source -> reject, this is a real signal of error
      unsupported              -> review, a human-level judgement is required
      hedged both ways         -> reject, it states nothing and hides an error
    """
    if _HEDGED_ORDER.search(note):
        return "reject", "hedges the order both ways ('before or after')"
    claims = ordering_claims(note, subject, _known_tools())
    unsupported = []
    for claim in claims:
        if claim in VERIFIED_ORDER:
            continue                      # settled; no need to re-derive it
        if (claim[1], claim[0]) in VERIFIED_ORDER:
            return "reject", (f"claims {claim[0]} -> {claim[1]}, but that "
                              f"pipeline runs the other way round")
        support = ordering_support(claim, evidence)
        if support < 0:
            return "reject", f"sources contradict the order {claim[0]} -> {claim[1]}"
        if support == 0:
            unsupported.append(f"{claim[0]} -> {claim[1]}")
    if unsupported:
        return "review", ("asserts an order no source states: "
                          + "; ".join(unsupported[:2]))
    return "ok", "ordering corroborated"


_FLAG_TOKEN = re.compile(r"(?<![\w-])(--?[A-Za-z][\w-]*)")


def wrong_flag(note: str, flag: str | None) -> str | None:
    """Another flag of the SAME tool that this note is really about.

    Written as its own function for the same reason misattributed() was: a
    check buried in gate() can be read, compiled, and never fire.

    Replayed over every recorded flag note before being adopted. It fires
    once, on nping -c, whose note describes --icmp throughout and never
    mentions -c, and it costs no accepted note. A rule that cheap is worth
    having even for one case, because the failure it catches is invisible --
    the note is fluent, grounded, correctly cited and about the right tool.
    """
    if not flag:
        return None
    named = set(_FLAG_TOKEN.findall(note or ""))
    if not named or flag in named:
        return None
    # -c and --count are the same option spelled two ways, and a note may
    # legitimately use the long form. Only a genuinely different letter
    # counts as a different flag.
    other = [f for f in named if f.lstrip("-")[:1] != flag.lstrip("-")[:1]]
    return other[0] if other else None


def misattributed(note: str, tool: str, flag: str | None) -> str | None:
    """The other tool this note hangs the flag on, if it does.

    The model writes from the passage it was handed, and passages show
    several tools at once. So it produced "use the -m flag with fls" on the
    ils page and again on mactime, and for diec -t it described `docker build
    -t` after reading a Dockerfile. Each is fluent, grounded in a real
    passage, and about the wrong program. For a junior analyst that is worse
    than silence: the flag often exists on both tools and means something
    different on each.

    Written as its own function because the check embedded in gate() could be
    read, compiled and still not fire, and a rule that cannot be tested in
    isolation cannot be trusted to be protecting anything.
    """
    if not flag:
        return None
    low = note.lower()
    for other in _known_tools():
        if other.lower() == tool.lower():
            continue
        if other.lower() not in low:
            continue
        for pat in (rf"{re.escape(flag.lower())}[^.;]{{0,40}}with[^.;]{{0,15}}{re.escape(other.lower())}",
                    rf"{re.escape(other.lower())}[^.;]{{0,15}}{re.escape(flag.lower())}",
                    rf"with[^.;]{{0,10}}{re.escape(other.lower())}"):
            if re.search(pat, low):
                return other
    return None


def gate(note: str, evidence: list[dict], tool: str,
         real_flags: set[str] | None,
         flag: str | None = None) -> tuple[bool, str]:
    """Mechanical checks only. No model gets a vote here."""
    note = " ".join(note.split())
    if not note or note.startswith("__ERROR__"):
        return False, "model error"
    if note.strip().upper().startswith("INSUFFICIENT"):
        return False, "model declined: passages did not support it"
    if len(note) < 40:
        return False, "too short to carry a scenario"
    if len(note) > 700:
        return False, "too long"
    if HEDGE.search(note):
        return False, "hedged filler"
    if not any(re.search(p, note, re.I) for p in SCENARIO):
        return False, "states no trigger, position, choice or consequence"

    # Grounded: the note's content words must come from the passages it was
    # given. This is what stops the model reaching into its own memory.
    pool = words(" ".join(e["passage"] for e in evidence))
    nw = words(note)
    if nw:
        overlap = len(nw & pool) / len(nw)
        if overlap < 0.45:
            return False, f"not grounded in the sources ({overlap:.0%} overlap)"

    # A flag note must be about the tool whose flag it is.
    #
    # The model writes from the passage it was given, and passages often show
    # several tools. So it produced "use the -m flag with fls" on the ils
    # page, the same on mactime, and for diec -t it described docker build -t
    # after reading a Dockerfile. Each is fluent, grounded in a real passage
    # and about the wrong program -- which for a junior analyst is worse than
    # silence, because the flag exists on both tools and means different
    # things.
    bad = misattributed(note, tool, flag)
    if bad:
        return False, f"attributes {flag} to {bad}, not to {tool}"

    # The same fault one level in: the right tool, the wrong flag.
    #
    # nping -c came back describing --icmp. misattributed() looks for other
    # TOOLS and sees nothing wrong, because nothing is wrong at that level --
    # the note is about nping. It is simply about a different option, and a
    # reader would take the sentence as the meaning of -c.
    #
    # A cross-reference is fine and common: "-c together with -a" names both.
    # What is rejected is naming ONLY some other flag.
    other = wrong_flag(note, flag)
    if other:
        return False, (f"describes {other}, never {flag}; the scenario "
                       f"belongs to a different option of the same tool")

    # ...and the quieter form of the same fault, where the note borrows
    # another tool's option semantics without ever naming it.
    #
    # scalpel is a fork of foremost and names it in its own man page, so a
    # scalpel option block passes the proximity test on a foremost query.
    # The loop reported that `foremost -b` carves files whose footers are
    # missing -- true of scalpel's -b; foremost's -b sets the block size.
    # Nothing in the note gives that away, so the check has to look at where
    # the evidence came from rather than at what the note says.
    #
    # Two outcomes, because the two failures are different. A flag the tool
    # does not have is a fabrication and is rejected. A flag it does have,
    # documented here from someone else's synopsis, is a note that may well
    # be right and cannot be confirmed from this evidence -- that is a human
    # judgement, so it goes to review. Replayed over 154 recorded flag
    # records this fires 11 times, reproducing both hand-caught
    # misattributions (mactime -m, ils -m, each lifted from an fls synopsis)
    # and costing one accepted note, which it sends to review rather than
    # discards.
    if flag and evidence:
        owners = [sources.option_owner(e["passage"], flag, tool, _known_tools())
                  for e in evidence]
        foreign = next((o for o in owners if o), None)
        if foreign and not any(o is None for o in owners):
            if real_flags and flag not in real_flags:
                return False, (f"every passage documents {flag} under "
                               f"{foreign}'s synopsis, and {tool} has no {flag}")
            return False, ("NEEDS-REVIEW: evidence for " + flag + " comes from "
                           f"{foreign}'s synopsis, not {tool}'s")

    # An ordering claim is a claim, not prose. Two of the first six notes
    # this loop produced had the workflow backwards while passing every
    # other check.
    verdict, why_dir = check_direction(note, tool, evidence)
    if verdict == "reject":
        return False, why_dir
    if verdict == "review":
        return False, "NEEDS-REVIEW: " + why_dir

    # Never name a flag the tool does not have. This is the cardinal error --
    # it is how the previous loop shipped `clamscan --yaravars`.
    if real_flags is not None:
        named = set(re.findall(r"(?<![\w-])(--?[A-Za-z][A-Za-z0-9-]*)", note))
        bogus = [f for f in named if f not in real_flags]
        if bogus:
            return False, f"names flags absent from the capture: {bogus[:3]}"
    return True, "ok"


def capture_flags(tool: str) -> set[str] | None:
    cov = json.loads((ROOT / "capture" / "coverage.json").read_text(encoding="utf-8"))
    meta = cov["documented"].get(tool)
    if not meta:
        return None
    safe = re.sub(r"[^A-Za-z0-9._-]", "_", tool)
    for name in (f"{tool}.help.txt", f"{safe}.help.txt"):
        p = ROOT / "capture" / meta["image"] / "help" / name
        if p.exists():
            text = p.read_text(encoding="utf-8", errors="replace")
            return set(re.findall(r"(?<![\w-])(--?[A-Za-z][A-Za-z0-9-]*)", text))
    return None


def render(evidence: list[dict], budget: int = 5000) -> str:
    out, used = [], 0
    for e in evidence[:6]:
        chunk = f"[{e['url']}]\n{e['passage']}\n"
        if used + len(chunk) > budget:
            break
        out.append(chunk)
        used += len(chunk)
    return "\n".join(out)


def work_one(tool: str, flag: str | None, worker) -> dict:
    name, base, model = worker
    ev = sources.evidence_for(tool, flag)
    if not ev:
        return {"tool": tool, "flag": flag, "status": "miss",
                "why": "no passages found showing it in use",
                "sources_tried": 0}
    prompt = (FLAG_PROMPT if flag else TOOL_PROMPT).format(
        tool=tool, flag=flag or "", passages=render(ev))
    t0 = time.time()
    note = ask(base, model, prompt)
    # Cut any sentence that talks about the retrieved passages before
    # anything judges or stores the note, so what the gate sees is exactly
    # what would be published. See strip_meta().
    if not note.startswith("__ERROR__"):
        note = strip_meta(note)
    # Check invented flags on EVERY note, not only flag-level ones.
    #
    # This passed `None` for tool-level notes, which disabled the check that
    # exists to stop the single failure this project was built around. Since
    # flag-level work has never run, the check had protected nothing at all --
    # and it showed: a clamscan note recommended `--memory`, which clamscan
    # does not have. That is `clamscan --yaravars` again, the exact fabricated
    # flag that ran through 44 of 61 modules in the previous project.
    #
    # A tool-level note that names a flag is making a claim about that flag,
    # and it gets checked like any other.
    ok, why = gate(note, ev, tool, capture_flags(tool), flag)

    # Blind verification, only for notes the mechanical gate approved. The
    # gate sees the note and the evidence together and is therefore prone to
    # confirmation bias (MARCH, arXiv 2603.24579) -- it approved two inverted
    # workflows. This re-derives the claims from the sources alone.
    blind = None
    if ok:
        blind = blind_check.verify(note, ev)
        if blind["verdict"] == "reject":
            ok, why = False, "blind check: " + blind["reason"]
        elif blind["verdict"] == "review":
            ok, why = False, "NEEDS-REVIEW: blind check: " + blind["reason"]
    rec = {
        "tool": tool, "flag": flag,
        "status": "kept" if ok else "rejected",
        "why": why,
        "note": " ".join(note.split())[:700],
        "citations": sorted({e["url"] for e in ev[:4]}),
        "top_score": ev[0]["score"],
        "sources_tried": len({e["url"] for e in ev}),
        "worker": name, "seconds": round(time.time() - t0, 1),
        "blind": blind,
    }
    if not ok:
        # Three distinct outcomes, and collapsing them loses the point.
        # A miss is an open question, a rejection is a caught error, and a
        # review is a claim only a human-level pass can settle.
        if why.startswith("NEEDS-REVIEW"):
            rec["status"] = "review"
            rec["why"] = why[len("NEEDS-REVIEW: "):]
        elif "declined" in why or "no passages" in why:
            rec["status"] = "miss"
        else:
            rec["status"] = "rejected"
    return rec




# Flags nobody needs a scenario for. --help and --version are not analytical
# choices, and documenting when to use --help is the kind of filler that made
# the guide feel auto-populated in the first place.
_NOT_WORTH_IT = {"--help", "-h", "--version", "-V", "--usage", "-?"}

# Tested and rejected: excluding output-file flags (-o, --output, --csv, --json)
# on the theory that they are plumbing which can only restate itself.
#
# Measured across every reviewed flag note: output-ish flags were accepted 62%
# of the time, everything else 63%. Indistinguishable. The good ones say
# something real -- regipy-dump -t chooses timeline output over a raw dump,
# which decides whether the result drops straight into a timeline tool, and
# regipy-diff -o names CSV because a hive diff is only useful once you can
# sort it. The bad ones restate the flag, exactly as bad notes about any other
# flag do.
#
# The lesson is about the shape of the note, not the shape of the flag, and
# the gate already tests for that. Left here so the plausible-sounding
# exclusion does not get added again on instinct.


# A short and long spelling declared together on one help line:
#     -c, --check              read checksums from the FILEs and check them
#     -i <interface>, --interface <interface>
#     -D, --list-interfaces    print list of interfaces and exit
#
# Sharing a line is the tool's own statement that these are one option --
# stronger evidence than two entries that happen to have the same wording.
_PAIR = re.compile(r"(?<![\w-])(-[A-Za-z])\b[^,\n]{0,20},\s*(--[\w-]+)")


def _twin(tool: str, flag: str) -> str | None:
    """The other spelling of this option, if the help declares one."""
    txt = _help_text(tool)
    for m in _PAIR.finditer(txt):
        short, long = m.group(1), m.group(2)
        if flag == short:
            return long
        if flag == long:
            return short
    return None


def _help_text(tool: str) -> str:
    try:
        cov = json.loads((ROOT / "capture" / "coverage.json")
                         .read_text(encoding="utf-8"))
    except Exception:
        return ""
    meta = cov["documented"].get(tool)
    if not meta:
        return ""
    safe = re.sub(r"[^A-Za-z0-9._-]", "_", tool)
    for name in (f"{tool}.help.txt", f"{safe}.help.txt"):
        p = ROOT / "capture" / meta["image"] / "help" / name
        if p.exists():
            return p.read_text(encoding="utf-8", errors="replace")
    return ""


def rank_flags(tool: str, limit: int) -> list[str]:
    """The flags worth researching, most-used first.

    Taking them alphabetically was actively perverse: for fls it selected
    --help, -B, -D, -F, -P, -S, -V and -a, skipping -m, -r and -s -- the three
    already proven to have evidence and the only three that change what an
    analyst does. Nothing found sources, and the run looked like the flag path
    did not work.

    Rank by how often a flag actually appears in the tool's own corpus
    instead. A flag people write walkthroughs about is both the one worth
    documenting and the one that will have a passage to ground it, so the same
    signal serves both ends.
    """
    real = capture_flags(tool) or set()
    if not real:
        return []

    # Skip flags that already have an answer.
    #
    # Measured: 42 of 54 flag notes produced so far -- 78% -- were for flags
    # that already carried hand-written guidance, and the hand-written version
    # was better every time. "Decompress, the only flag you normally want in
    # analysis" beats a sentence about automatically unpacking a sample, and
    # "Partition offset in sectors, from mmls" beats a paragraph around it.
    #
    # So the loop was spending most of its flag budget, and most of the review
    # time, re-answering solved questions -- while 2,300 cells sat empty. The
    # empty ones are the entire point.
    try:
        from enrichment import ENRICHMENT
        answered = set((ENRICHMENT.get(tool) or {}).get("when", {}))
    except Exception:
        answered = set()

    # ...and flags whose TWIN already has one.
    #
    # generate_pages mirrors guidance across a short and long spelling that
    # share an identical captured description, because they are one option
    # and whichever spelling a reader looks up should give them an answer.
    # rank_flags could not see that -- the mirroring happens at render time
    # -- so it kept researching --check while -c was answered and the row was
    # already filled. sha256sum -c was one such attempt, published nothing
    # new, and had to be rejected as redundant rather than wrong.
    #
    # Measured before adopting: the captured help holds 655 short/long pairs;
    # 118 of 991 answered options have both spellings answered, and 49 of 706
    # recorded flag attempts went to an option whose twin was already done.
    # That is 7% of the flag budget spent on questions with an answer.
    #
    # This excludes on the basis of a MEASUREMENT -- does this option already
    # have an answer -- not a judgement about whether a note is any good, so
    # it cannot over-reject the way the classifiers in DISPROVEN did.
    answered |= {t for f in answered if (t := _twin(tool, f))}
    real = real - answered
    corpus = sources.corpus_for(tool)
    text = " ".join(p["text"] for p in corpus)
    counts: dict[str, int] = {}
    for f in real:
        if f in _NOT_WORTH_IT or len(f) < 2:
            continue
        n = len(re.findall(r"(?<![\w-])" + re.escape(f) + r"(?![\w-])", text))
        if n:
            counts[f] = n
    ordered = sorted(counts, key=lambda f: (-counts[f], f))
    return ordered[:limit]


def tools_needing_work(limit: int, skip: set[str]) -> list[str]:
    """Tools with a page and no tool-level guidance yet.

    Ordered by whether the tool sits next to a confusable neighbour, because
    that is where a junior analyst makes the wrong call -- not by which page
    has the most blank cells, which put hashcat first purely for having 143
    options nobody has to choose between.
    """
    NEIGHBOURS = [
        "pdfid", "pdf-parser", "pdf-parser.py", "pdfid.py",
        "photorec", "testdisk", "foremost", "scalpel", "bulk_extractor",
        "dd", "dc3dd", "dcfldd", "ewfacquire", "guymager",
        "oleid", "olevba", "mraptor", "oleobj", "rtfobj", "msodde",
        "die", "diec", "upx", "binwalk",
        "fls", "mactime", "icat", "ils", "istat", "mmls", "fsstat",
        "tsk_recover", "tsk_gettimes", "img_stat",
        "vol", "volatility3", "log2timeline.py", "psort.py",
        "tshark", "capinfos", "editcap", "mergecap", "dumpcap",
        "chainsaw", "hayabusa", "evtxexport", "yara", "clamscan",
        "ssdeep", "exiftool", "hashcat", "john", "radare2", "frida",
    ]
    cov = json.loads((ROOT / "capture" / "coverage.json").read_text(encoding="utf-8"))
    have = set(cov["documented"])

    # Only tools the guide actually claims to cover.
    #
    # Falling back to every captured binary had the loop researching 2to3,
    # addpart, addr2line and adduser -- base OS utilities that are not analyst
    # tools and that this guide already decided not to document. Watching a
    # live round was the only way to see it; the counters just showed misses.
    #
    # The taxonomy is the list of tools with a page, which is the same set
    # that has somewhere for an answer to go.
    try:
        from taxonomy import TAXONOMY
        mapped = {c for _ph, caps in TAXONOMY.items() for _cap, cmds in caps
                  for c in cmds}
    except Exception:
        mapped = set()

    # Drop what the guide has already decided not to document.
    #
    # OUT_OF_SCOPE excludes curl, grep, less, stat and wget from page
    # generation, but they remained in the taxonomy, so the loop kept
    # researching them and I kept rejecting the results by hand -- curl came
    # back describing web application pentesting, grep came back describing
    # grep. That is manual work created by an inconsistency between two lists
    # that should agree, and budget spent on tools with nowhere to put an
    # answer.
    try:
        from generate_pages import OUT_OF_SCOPE
    except Exception:
        OUT_OF_SCOPE = set()
    pool = ((have & mapped) or have) - OUT_OF_SCOPE

    ordered = [t for t in NEIGHBOURS if t in pool and t not in skip]
    if len(ordered) < limit:
        ordered += sorted(t for t in pool
                          if t not in set(NEIGHBOURS) and t not in skip)
    return ordered[:limit]


def already_done() -> set[str]:
    done: set[str] = set()
    for f in (OUT, REVIEW, MISSES):
        try:
            done |= {r["tool"] for r in json.loads(f.read_text(encoding="utf-8"))
                     if not r.get("flag")}
        except Exception:
            pass
    return done


def flush(results: list[dict], review: list[dict], misses: list[dict],
          replace: bool = False) -> None:
    """Persist all three buckets, merged with what is already on disk.

    Called after every tool rather than once at the end of the run. A round
    covers thirty tools and their flags and takes upwards of forty minutes,
    and until this existed none of it reached disk until the last one
    finished: a round forty-two minutes in held twenty-four verified KEPT
    notes in memory alone, with the record files still showing the state from
    before it started. Any crash, restart or kill discarded the lot, and the
    log would still show KEPT for every one of them.

    REVIEW was worse than fragile: it was read, merged, deduplicated and then
    never written at all. research_review.json did not exist, and every note
    a mechanical check could not settle -- sixty-five of them, including
    everything the option_owner guard deliberately routed to review rather
    than reject -- was silently dropped. The bucket meant for the judgements
    most needing a human was the one bucket that threw them away.

    Merging on every call is what makes it safe to call repeatedly: each
    write reconciles against the file, so the result is the same whether it
    ran once or thirty times.
    """
    for f, new in ((OUT, results), (REVIEW, review), (MISSES, misses)):
        merged = list(new)
        if not replace:
            try:
                merged = json.loads(f.read_text(encoding="utf-8")) + merged
            except Exception:
                pass
            # Deduplicate on (tool, flag), keeping the best-evidenced attempt.
            #
            # Rounds revisit tools deliberately -- a later pass has better
            # seeds and a warmer cache -- but appending every attempt meant
            # fls -s appeared six times and the file reported 95 flag notes
            # when it held roughly a third that many distinct ones. Inflated
            # counts are worse than useless: they make the loop look more
            # productive than it is, which is the number I would have used to
            # decide it was working.
            best: dict[tuple, dict] = {}
            for rec in merged:
                key = (rec.get("tool"), rec.get("flag"))
                cur = best.get(key)
                if cur is None or (rec.get("top_score", -99) >
                                   cur.get("top_score", -99)):
                    best[key] = rec
            merged = list(best.values())
        f.write_text(json.dumps(merged, indent=2), encoding="utf-8")


BARREN = ROOT / "research_barren.json"


def barren_tools() -> dict[str, int]:
    """Tools that have never produced anything, and the seed count when so.

    Left to itself the rotation is fair, and fairness is the problem: a tool
    with no corpus misses every round and its attempt count rises in step
    with everyone else's, so it is picked again forever. vdbbin, vivbin, xxd
    and yarac had each been attempted 196 times without once producing a
    note, and 23 such tools were consuming 19% of every attempt the loop
    made.

    Skipping them is only safe because the skip is tied to the seed count.
    This project is not allowed to conclude a tool has no sources -- and it
    is not concluding that here. It is recording that the sources it
    currently has yield nothing, and the moment the tool is seeded the count
    changes and the tool becomes eligible again on its own.

    Note what is NOT used as the trigger: a run of misses alone. A tool can
    miss because search was suspended, which says nothing about the tool.
    The condition is a long run of attempts where every single one missed.
    """
    try:
        return json.loads(BARREN.read_text(encoding="utf-8"))
    except Exception:
        return {}


def seed_fp(tool: str) -> str:
    """A fingerprint of the exact sources this tool currently has.

    The barren record needs to answer "have its sources changed since we set
    it aside", and a COUNT cannot: swapping one bad seed for a good one
    leaves the count identical, and unrelated attempts accumulating in the
    log made an attempt-count comparison drift until it re-trapped two tools
    that had 29 and 30 passages between them.

    Hashing the URLs answers the question directly and is immune to both.
    """
    try:
        seeds = json.loads((ROOT / "catalog" / "seed-urls.json")
                           .read_text(encoding="utf-8"))
    except Exception:
        return ""
    urls = sorted(seeds.get(tool, ()))
    return hashlib.sha1("\n".join(urls).encode()).hexdigest()[:12]


def seed_counts() -> dict[str, int]:
    try:
        seeds = json.loads((ROOT / "catalog" / "seed-urls.json")
                           .read_text(encoding="utf-8"))
    except Exception:
        return {}
    return {k: len(v) for k, v in seeds.items() if not k.startswith("_")}


def refresh_barren(min_attempts: int = 8) -> dict[str, int]:
    """Recompute the barren list from the log, and write it."""
    outcomes: dict[str, list[str]] = {}
    try:
        txt = LIVE_LOG.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return {}
    for verdict, tool in re.findall(
            r"(KEPT|MISS|REJECTED|REVIEW)\s+(\S+)\s\s", txt):
        outcomes.setdefault(tool, []).append(verdict)
    seeds = seed_counts()
    prev = barren_tools()
    out: dict[str, dict] = {}
    for tool, v in outcomes.items():
        if len(v) < min_attempts or not all(x == "MISS" for x in v):
            continue
        old = prev.get(tool) if isinstance(prev.get(tool), dict) else None
        fp = seed_fp(tool)
        if old and old.get("fp") != fp:
            # Its sources changed since it was set aside. Every line in the
            # log predates the change, so none of it says anything about the
            # new sources. Record the change and the attempt count AT the
            # change, and leave the tool eligible.
            #
            # Two failures are being avoided at once here, and each is the
            # other's mirror. Comparing attempt counts alone drifted, because
            # attempts accumulate from unrelated rounds until the difference
            # crosses the threshold -- that re-trapped rasm2 and rahash2
            # while they held 29 and 30 passages. Comparing fingerprints
            # alone never re-traps at all, because the stored fingerprint
            # stays stale forever and the tool grinds on unbounded.
            #
            # The fingerprint says WHEN the sources changed; the counter,
            # rebased at that moment, says how many real retries have
            # happened since. Neither works without the other.
            out[tool] = {"seeds": seeds.get(tool, 0), "attempts": len(v),
                         "fp": fp, "eligible": True}
            continue
        if old and old.get("eligible"):
            if len(v) - old.get("attempts", 0) < min_attempts:
                out[tool] = dict(old)      # still serving its retry window
                continue
        out[tool] = {"seeds": seeds.get(tool, 0), "attempts": len(v),
                     "fp": fp}
    BARREN.write_text(json.dumps(out, indent=2, sort_keys=True),
                      encoding="utf-8")
    return out


def still_barren() -> set[str]:
    """Barren tools whose sources have not changed since they were recorded.

    Changed, not merely grown. Replacing a seed that yielded nothing with one
    that might is exactly the intervention worth retrying for, and it leaves
    the count where it was.
    """
    seeds = seed_counts()
    out = set()
    for t, rec in barren_tools().items():
        if not isinstance(rec, dict):
            rec = {"seeds": rec}
        if rec.get("eligible"):
            continue                # inside its retry window after a reseed
        fp = rec.get("fp")
        if fp is not None:
            if seed_fp(t) == fp:
                out.add(t)
        elif seeds.get(t, 0) <= rec.get("seeds", 0):
            out.add(t)          # older records, before fingerprints existed
    return out


def attempt_counts() -> Counter:
    """How many times each tool has actually been attempted, from the log.

    Not from the three record files. Those deduplicate on (tool, flag) and
    keep the best-evidenced attempt, which is right for reporting and makes
    them useless for counting: a tool ground eight times appears at most once
    per file. That deduplication is exactly why the repeat-grinding was
    invisible in the JSON while the log showed scalpel rejected eight times
    with the same reason.

    The log is append-only and every verdict lands in it, so it is the only
    complete record of what was attempted.
    """
    n: Counter = Counter()
    try:
        txt = LIVE_LOG.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return n
    for tool, _whole, flag in re.findall(
            r"(?:KEPT|MISS|REJECTED|REVIEW)\s+(\S+)(\s+(-{1,2}\S+))?\s\s", txt):
        if not flag:
            n[tool] += 1
    return n


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--tool")
    ap.add_argument("--tools", nargs="*")
    ap.add_argument("--flags", action="store_true",
                    help="also work this tool's captured flags")
    ap.add_argument("--limit-flags", type=int, default=12)
    ap.add_argument("--auto", type=int, default=0,
                    help="pick this many tools that still need work")
    # Accumulating is the default. It used to require --append, and a manual
    # single-tool run without the flag silently destroyed the accumulated
    # record of five rounds -- misses went from 93 to 8 with no warning.
    # Losing history by omitting an option is a trap, not a feature; the
    # destructive path should be the one you have to ask for.
    ap.add_argument("--replace", action="store_true",
                    help="discard previous results instead of accumulating")
    a = ap.parse_args()

    tools = a.tools or ([a.tool] if a.tool else [])
    if a.auto:
        seen = set() if a.replace else already_done()
        tools = tools_needing_work(a.auto, seen)
        if not tools:
            # Everything attempted at least once. Start over rather than
            # exiting: the user's instruction is to iterate forever and
            # repeats are fine, and a second attempt is genuinely different --
            # better seeds, a warmer cache, search engines recovered from
            # whatever suspended them last time.
            #
            # Returning nothing here made run_forever spin: enrich_loop exited
            # in under a second, the runner immediately started another round,
            # and it did that 5,600 times while appearing healthy.
            # Least-attempted first, not the top of the list again.
            #
            # This restart used to call tools_needing_work(a.auto, set()),
            # which returns the first N in NEIGHBOURS order -- the same
            # thirty tools on every pass, forever. Measured over 462
            # recorded verdicts: 121 distinct targets, 341 repeat attempts,
            # 74% of all output. pdfid, pdf-parser, pdf-parser.py, pdfid.py,
            # photorec, testdisk, foremost and scalpel -- the first eight
            # entries of NEIGHBOURS -- had been attempted eight times each,
            # and scalpel returned exactly the same rejection all eight
            # times. Meanwhile the tail of the pool was never reached at
            # all, which is why seeding tools kept producing nothing: the
            # seeds were fine and the tools were never picked again.
            #
            # Rounds completed, verdicts accumulated and the log grew the
            # whole time. Same shape as every other failure here: a fallback
            # that looks like progress while covering the same ground.
            counts = attempt_counts()
            refresh_barren()
            skip = still_barren()
            order = {t: i for i, t in enumerate(
                tools_needing_work(10 ** 6, set())) if t not in skip}
            tools = sorted(order, key=lambda t: (counts.get(t, 0), order[t]))[:a.auto]
            if skip:
                print(f"skipping {len(skip)} tools that have never produced a "
                      f"note from their current sources; seeding any of them "
                      f"makes it eligible again", flush=True)
            print(f"all tools attempted; next pass takes the least-attempted "
                  f"{len(tools)} (lowest count {min(counts.get(t, 0) for t in tools) if tools else 0})")
        print(f"auto-selected {len(tools)} tools: {', '.join(tools[:10])}"
              f"{' ...' if len(tools) > 10 else ''}")
    if not tools:
        print("pass --tool or --tools")
        return 1

    kept, results, misses, review = 0, [], [], []
    for i, tool in enumerate(tools):
        worker = WORKERS[i % len(WORKERS)]
        jobs: list[str | None] = [None]
        if a.flags:
            jobs += rank_flags(tool, a.limit_flags)
        for flag in jobs:
            rec = work_one(tool, flag, worker)
            label = f"{tool}{' ' + flag if flag else ''}"
            # Timestamp every verdict. Without one there is no way to tell
            # whether a line came from the round in flight or from a round
            # that started before the last fix, and a pass can outlive
            # several code changes. That ambiguity cost real time.
            ts = datetime.now().strftime("%H:%M:%S")
            if rec["status"] == "kept":
                kept += 1
                results.append(rec)
                print(f"{ts}  KEPT     {label:28s} {rec['note'][:80]}", flush=True)
            elif rec["status"] == "review":
                review.append(rec)
                print(f"{ts}  REVIEW   {label:28s} {rec['why'][:60]}", flush=True)
            else:
                misses.append(rec)
                print(f"{ts}  {rec['status'].upper():8s} {label:28s} {rec['why'][:60]}", flush=True)

        # Persist after each tool, not at the end of the run. See flush().
        #
        # The lists keep accumulating rather than being cleared. Clearing
        # would be the obvious way to avoid rewriting the same records, and
        # it breaks --replace: that mode does not merge with the file, so
        # each flush would overwrite it with only the latest tool's work.
        # Rewriting a few hundred small records costs nothing.
        flush(results, review, misses, a.replace)

    flush(results, review, misses, a.replace)
    print(f"\nkept {kept}, not kept {len(misses)}")
    print(f"  -> {OUT.name} (the build does not read this)")
    print(f"  -> {REVIEW.name} (claims a mechanical check cannot settle)")
    print(f"  -> {MISSES.name} (open questions, not verdicts)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
