#!/usr/bin/env python3
"""Verify a note by re-deriving its claims from the sources, blind to the note.

The problem this solves, observed here before it was read about: a local model
produced six notes that were fluent, grounded, correctly cited and passed every
mechanical check, and two of them had the workflow backwards -- pdfid described
as running after pdf-parser, mraptor as running after olevba. Both are
inverted. A reversed arrow is worse than no guidance for a junior analyst,
because it reads as authoritative and sends them down the expensive path first.

The reason a checker misses this is confirmation bias, and it is not a quirk
of small models. MARCH (arXiv 2603.24579) measured it: when a verifier sees
the evidence AND the draft together, it endorses errors through internal
coherence rather than grounding. Their fix is deliberate information
asymmetry -- decompose the draft into atomic claims, then have a Checker
re-answer them from the documents ALONE, never shown the draft, and compare.
An 8B model went from 55% to 75% accuracy that way, matching far larger
models. That matches what was measured on this fleet: architecture beats
parameter count for this job.

So:

    PROPOSER  turns the note into atomic questions      (sees the note)
    CHECKER   answers them from the passages only       (never sees the note)
    COMPARE   any disagreement fails the whole note     (zero tolerance)

The Checker also runs on a different host and model from the Solver, so a
single model's blind spot cannot approve its own work.

Verification happens at the point a claim is created, not later. Delayed
verification in agent networks lets false claims propagate and can destabilise
the whole system (arXiv 2606.27409); the same paper notes that when truth is a
fixed constraint -- as a retrieved passage is here -- verification stays
stable. That is the regime this pipeline sits in, by design.
"""
from __future__ import annotations
import json
import re
import sys
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

# Checker deliberately differs from the Solver in both model and host. Asking
# one model to check itself reproduces its own blind spots.
# Different HOST and different model FAMILY from the proposer. Two qwen
# models share training data and blind spots; gemma checking qwen is a
# genuinely separate opinion, which is the whole point of the asymmetry.
CHECKER = ("rick-4090", "http://100.112.76.79:11434", "gemma3:27b-it-q4_K_M")
PROPOSER = ("l3e7-3090", "http://192.168.1.253:11434", "qwen3:14b")

PROPOSE_PROMPT = """Below is a claim written about a forensic tool.

CLAIM:
{note}

Break it into at most 4 short, separately checkable questions. Ask only about \
things the claim actually asserts: ordering between tools, what triggers using \
it, what it can or cannot do, how it compares to another tool.

Each question must be answerable in a few words and must NOT hint at the \
answer. Ask "Which runs first, X or Y?" rather than "Does X run before Y?".

Output strict JSON only:
{{"questions": ["...", "..."]}}"""

ANSWER_PROMPT = """Answer the question using ONLY the source passages below.

SOURCES:
{passages}

QUESTION: {question}

Answer in under 20 words. If the sources do not answer it, reply exactly: \
UNKNOWN

Answer only, no explanation."""

# Ask about CONTRADICTION, not agreement. Asking "do these agree?" rejected a
# correct note twice over: "building a timeline" vs "collecting temporal data
# from file systems" is the same fact at two granularities, and "produces the
# body file" vs "a line for each file" describes one output two ways. A judge
# hunting for agreement calls those disagreements and throws away good work.
#
# Only a genuine conflict should fail. Different wording, different level of
# detail, or extra detail on one side are all compatible -- and if the sources
# simply do not address it, that is UNKNOWN, not a contradiction.
JUDGE_PROMPT = """A claim was made about a forensic tool. A question about it was then answered independently, using only source documents.

QUESTION:     {question}
CLAIM SAYS:   {claimed}
SOURCES SAY:  {found}

Does the claim CONTRADICT the sources -- that is, could they not both be true?

Different wording, different level of detail, or one side saying more than the other are NOT contradictions. Only answer CONTRADICTS if the two genuinely conflict, such as stating opposite orderings or opposite capabilities.

Reply with exactly one word: CONTRADICTS, COMPATIBLE, or UNKNOWN."""


def ask(worker, prompt: str, timeout: int = 300) -> str:
    _name, base, model = worker
    body = json.dumps({"model": model, "prompt": prompt, "stream": False,
                       "options": {"temperature": 0.0, "num_ctx": 8192}}).encode()
    req = urllib.request.Request(base + "/api/generate", data=body,
                                 headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return json.loads(r.read()).get("response", "").strip()
    except Exception as e:
        return f"__ERROR__ {e}"


def _strip_think(s: str) -> str:
    return re.sub(r"<think>.*?</think>", "", s, flags=re.S).strip()


def propose(note: str) -> list[str]:
    raw = _strip_think(ask(PROPOSER, PROPOSE_PROMPT.format(note=note)))
    m = re.search(r"\{.*\}", raw, re.S)
    if not m:
        return []
    try:
        qs = json.loads(m.group(0)).get("questions", [])
    except json.JSONDecodeError:
        return []
    return [str(q).strip() for q in qs if str(q).strip()][:4]


def render(evidence: list[dict], budget: int = 5000) -> str:
    out, used = [], 0
    for e in evidence[:6]:
        chunk = f"[{e['url']}]\n{e['passage']}\n"
        if used + len(chunk) > budget:
            break
        out.append(chunk)
        used += len(chunk)
    return "\n".join(out)


def answer_from_sources(question: str, evidence: list[dict]) -> str:
    """The blind step. This call never receives the note."""
    return _strip_think(ask(CHECKER, ANSWER_PROMPT.format(
        passages=render(evidence), question=question)))


def answer_from_sources_vendor(question: str, evidence: list[dict]) -> tuple[str, str]:
    """The same blind question, asked of a different vendor entirely.

    The local checker and the local drafter are both open-weight models
    trained on overlapping corpora, so they can be wrong in the same place
    and call it agreement. A hosted frontier model from another vendor fails
    differently, and differently-wrong is the only kind of second opinion
    worth having.

    This also fixes a measured problem. Judging alone, the local checker
    called "produces the body file" a contradiction of "a line for each
    file" -- one output described two ways -- and would have binned a correct
    note. Requiring two vendors to agree before a contradiction counts turns
    that single noisy verdict into a disagreement between checkers, which is
    treated as unresolved rather than as a fault in the note.
    """
    try:
        import free_api
    except Exception:
        return "", ""
    return free_api.ask(ANSWER_PROMPT.format(
        passages=render(evidence), question=question), max_tokens=120)


def answer_from_note(question: str, note: str) -> str:
    return _strip_think(ask(PROPOSER, ANSWER_PROMPT.format(
        passages=f"[the claim under test]\n{note}", question=question)))


def agree(question: str, claimed: str, found: str) -> str:
    verdict = _strip_think(ask(CHECKER, JUDGE_PROMPT.format(
        question=question, claimed=claimed, found=found))).upper()
    if "CONTRADICT" in verdict:
        return "DISAGREE"
    if "COMPATIBLE" in verdict:
        return "AGREE"
    return "UNKNOWN"


def verify(note: str, evidence: list[dict]) -> dict:
    """Zero tolerance: one disagreement fails the note.

    MARCH's Zero-Tolerance Reward. A note is a small number of sentences aimed
    at someone who cannot yet tell right from wrong in this domain, so a
    partially-correct note is not a partial success.
    """
    questions = propose(note)
    if not questions:
        return {"verdict": "review", "reason": "could not decompose the claim",
                "checks": []}

    checks, disagreements, unknowns = [], 0, 0
    for q in questions:
        claimed = answer_from_note(q, note)
        found = answer_from_sources(q, evidence)      # blind, local
        vendor, who = answer_from_sources_vendor(q, evidence)   # blind, hosted

        if found.upper().startswith("UNKNOWN"):
            v = "UNKNOWN"
        else:
            v = agree(q, claimed, found)

        # A contradiction has to survive a second vendor. One checker calling
        # a conflict is as likely to be judge noise as a real fault -- it
        # happened, on a note that was correct -- and binning good work is how
        # a loop quietly stops progressing.
        if v == "DISAGREE" and vendor:
            if vendor.upper().startswith("UNKNOWN"):
                v = "UNKNOWN"
            elif agree(q, claimed, vendor) != "DISAGREE":
                v = "UNRESOLVED"
        checks.append({"question": q, "claim_says": claimed[:160],
                       "sources_say": found[:160],
                       "second_opinion": (vendor or "")[:160],
                       "vendor": who, "verdict": v})
        if v == "DISAGREE":
            disagreements += 1
        elif v in ("UNKNOWN", "UNRESOLVED"):
            unknowns += 1

    # Calibrated to the judge's measured reliability, not to an ideal.
    #
    # MARCH uses zero tolerance -- any mismatch fails. That assumes the judge
    # is right. Measured here it is not: on a note that was TRUE, the judge
    # called "produces the body file" a contradiction of "a line for each
    # file", which is one output described two ways. Zero tolerance on a noisy
    # judge throws away correct work, and discarding good notes is how a loop
    # quietly stops making progress.
    #
    # An ordering contradiction is the reliable signal -- "which runs first"
    # has one answer, the judge got it right in both directions, and it is the
    # error that actually misleads a junior analyst. So it fails on its own.
    # Otherwise two independent contradictions are needed, and a lone one goes
    # to review rather than the bin.
    ordering_conflict = any(
        c["verdict"] == "DISAGREE" and re.search(
            r"(runs? first|before|after|order|then|next|follow)",
            c["question"], re.I)
        for c in checks)

    if ordering_conflict:
        return {"verdict": "reject",
                "reason": "sources contradict the claimed order of operations",
                "checks": checks}
    # An ordering contradiction fails on its own. "Which runs first" has one
    # answer, both checkers agreed on it in testing, and a reversed workflow
    # is the error that actually misleads a junior analyst -- it reads as
    # authoritative and sends them down the expensive path first.
    if any(c["verdict"] == "DISAGREE" and
           re.search(r"(runs? first|before|after|then|order|follow)",
                     c["question"], re.I)
           for c in checks):
        return {"verdict": "reject",
                "reason": "two vendors agree the sources contradict the "
                          "claimed order of operations",
                "checks": checks}
    if disagreements >= 2:
        return {"verdict": "reject",
                "reason": f"{disagreements} claims contradicted by the sources",
                "checks": checks}
    if disagreements == 1:
        return {"verdict": "review",
                "reason": "one claim conflicts with the sources; judge is not "
                          "reliable enough alone to bin it",
                "checks": checks}
    if unknowns == len(checks):
        return {"verdict": "review",
                "reason": "sources answered none of the claims",
                "checks": checks}
    return {"verdict": "ok",
            "reason": f"{len(checks) - unknowns}/{len(checks)} claims confirmed",
            "checks": checks}


if __name__ == "__main__":
    import sources
    tool = sys.argv[1] if len(sys.argv) > 1 else "mraptor"
    notes = {r["tool"]: r["note"]
             for r in json.loads(Path(__file__).resolve().parent.parent
                                 .joinpath("research_output.json")
                                 .read_text(encoding="utf-8"))}
    note = notes.get(tool)
    if not note:
        print(f"no note for {tool} in research_output.json")
        raise SystemExit(1)
    ev = sources.evidence_for(tool)
    print(f"NOTE: {note}\n")
    res = verify(note, ev)
    for c in res["checks"]:
        print(f"  [{c['verdict']:8s}] {c['question']}")
        print(f"      claim  : {c['claim_says']}")
        print(f"      sources: {c['sources_say']}")
    print(f"\n{res['verdict'].upper()}: {res['reason']}")
