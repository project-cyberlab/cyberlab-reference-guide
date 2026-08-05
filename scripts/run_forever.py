#!/usr/bin/env python3
"""Run research passes back to back, assessing after each, until told to stop.

The loop kept stalling between passes because it needed a human to start the
next one. That is not a loop, it is a queue of manual jobs. This drives
itself: pass, assess, retry what was written off unfairly, pass again.

Stopping: delete nothing, touch a file. `STOP` in the repo root ends the run
cleanly after the pass in flight, so a long pass is never killed mid-tool and
half its work thrown away.

What it deliberately does NOT do is publish. Promoting a note into the guide
needs a judgement call about whether it serves a junior analyst, and the whole
design rests on that judgement being made by something that can make it. A
runner that published its own output would be the previous project again.

    python scripts/run_forever.py            # until STOP appears
    python scripts/run_forever.py --rounds 4
"""
from __future__ import annotations
import argparse
import json
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
STOP = ROOT / "STOP"
LOG = ROOT / "research_runlog.jsonl"
# Stable path for the human-readable stream. Rotating this per
# restart orphaned three watchdogs, each of which then reported a
# healthy loop as dead.
LIVE = ROOT / "research_live.log"

BATCH = 25


def run(cmd: list[str], timeout: int) -> str:
    """Run a pass, echoing its output live.

    This used to capture and print only when the pass finished, which meant a
    round in progress showed nothing at all -- so the only thing left to watch
    was the round counter. A counter going up looks identical whether the loop
    is researching tools or dying instantly on a bad argument, and it did the
    latter 5,649 times without anyone noticing.

    Streaming makes a stalled or failing pass obvious within seconds instead
    of at the end of a round that may take an hour.
    """
    lines: list[str] = []
    try:
        proc = subprocess.Popen(
            [sys.executable, "-u"] + cmd, cwd=ROOT,
            stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
            text=True, encoding="utf-8", errors="replace", bufsize=1)
    except Exception as e:
        return f"__ERROR__ {e}"
    deadline = time.time() + timeout
    try:
        for line in proc.stdout:              # type: ignore[union-attr]
            print(line.rstrip(), flush=True)
            with LIVE.open("a", encoding="utf-8") as _fh:
                _fh.write(line)
            lines.append(line)
            if time.time() > deadline:
                proc.kill()
                return "__TIMEOUT__"
        proc.wait(timeout=30)
    except Exception:
        try:
            proc.kill()
        except Exception:
            pass
    return "".join(lines)


def counts() -> dict:
    out = {}
    for name, f in (("kept", "research_output.json"),
                    ("review", "research_review.json"),
                    ("miss", "research_misses.json")):
        try:
            out[name] = len(json.loads((ROOT / f).read_text(encoding="utf-8")))
        except Exception:
            out[name] = 0
    return out


def search_is_up() -> bool:
    """Is the search backend actually answering?

    A miss recorded while every upstream engine was suspended is not evidence
    of anything, and retrying it while they are still suspended just
    reproduces the same non-answer. Ask before requeueing.
    """
    try:
        sys.path.insert(0, str(HERE))
        import sources
        return bool(sources._search_once("forensics timeline"))
    except Exception:
        return False


def retry_unfair_misses() -> int:
    """Re-queue misses caused by the search being throttled, not by absence.

    A pass once wrote off 39 tools as having no sources while every upstream
    engine was suspended. Those verdicts were manufactured by rate limiting,
    and leaving them in place would bake a false "nothing exists" into the
    record -- the one conclusion this project may not draw. So a tool that
    missed for want of sources gets another attempt on a later pass, when the
    engines have recovered.
    """
    f = ROOT / "research_misses.json"
    try:
        misses = json.loads(f.read_text(encoding="utf-8"))
    except Exception:
        return 0
    keep, requeued = [], 0
    for m in misses:
        if "no passages found" in (m.get("why") or ""):
            requeued += 1          # dropped from the miss list, so --append
            continue               # will pick the tool up again
        keep.append(m)
    if requeued:
        f.write_text(json.dumps(keep, indent=2), encoding="utf-8")
    return requeued


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--rounds", type=int, default=0, help="0 = until STOP")
    ap.add_argument("--batch", type=int, default=BATCH)
    a = ap.parse_args()

    rnd = 0
    while True:
        if STOP.exists():
            print("STOP present; finishing.")
            return 0
        if a.rounds and rnd >= a.rounds:
            print(f"completed {rnd} rounds.")
            return 0
        rnd += 1
        started = datetime.now().isoformat(timespec="seconds")
        before = counts()

        # Every few rounds, give the unfairly-missed tools another go rather
        # than only ever reaching for untouched ones.
        # Requeue when search RECOVERS, not on a round counter.
        #
        # Every third round was the wrong trigger: during the outage it kept
        # returning misses to a queue that could not serve them, so they
        # missed again for the same reason and came back round. The signal
        # that matters is search working again, because that is the moment
        # those verdicts become retryable rather than merely unfair.
        requeued = retry_unfair_misses() if search_is_up() else 0

        print(f"\n=== round {rnd} at {started} "
              f"(requeued {requeued} throttled misses) ===", flush=True)
        # Alternate tool-level and flag-level rounds. The flag column is
        # 3,166 rows and was never once attempted; tool scenarios alone can
        # never fill it. Repeating a tool is fine -- a later pass has better
        # seeds, a warmer cache and recovered search engines, so a second look
        # is not wasted work.
        cmd = ["scripts/enrich_loop.py", "--auto", str(a.batch)]
        if rnd % 2 == 0:
            cmd += ["--flags", "--limit-flags", "6"]
        out = run(cmd, timeout=10800)

        assess = run(["scripts/loop_assess.py"], timeout=1800)
        print(assess[-1500:], flush=True)

        after = counts()
        with LOG.open("a", encoding="utf-8") as fh:
            fh.write(json.dumps({
                "round": rnd, "started": started,
                "finished": datetime.now().isoformat(timespec="seconds"),
                "before": before, "after": after,
                "requeued": requeued,
                "gained_kept": after["kept"] - before["kept"],
            }) + "\n")

        if out == "__TIMEOUT__":
            print("pass timed out; pausing before the next round", flush=True)
            time.sleep(120)

        # A round that finishes almost instantly did no work -- it means the
        # pass exited early rather than researched anything. Spinning on that
        # burns CPU and fills the log with rounds that gained nothing, which
        # is what 5,600 one-second rounds looked like from the outside:
        # perfectly healthy.
        elapsed = (datetime.now() -
                   datetime.fromisoformat(started)).total_seconds()
        if elapsed < 20:
            print(f"round finished in {elapsed:.0f}s -- nothing to do; "
                  f"backing off", flush=True)
            time.sleep(300)


if __name__ == "__main__":
    raise SystemExit(main())
