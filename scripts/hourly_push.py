#!/usr/bin/env python3
"""Publish reviewed work, rebuild the guide, and push. Every hour.

The point is that the copy on GitHub is never more than an hour behind the
work, so a PDF downloaded at any moment reflects what has actually been
verified rather than whatever was true at the last time someone remembered to
push.

What it will publish is deliberately narrow. `publish.py` only promotes notes
carrying an explicit accept verdict in research_decisions.json, and those
verdicts are written by hand after reading the note. So this can run unattended
without any risk of shipping unreviewed text -- the worst it can do on a quiet
hour is rebuild an unchanged document and commit nothing.

That constraint is the whole reason it is safe to automate. The previous
project automated the step *before* review rather than after, and published 44
modules of fabricated flags.

    python scripts/hourly_push.py            # loop until STOP
    python scripts/hourly_push.py --once
"""
from __future__ import annotations
import argparse
import json
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STOP = ROOT / "STOP"
INTERVAL = 3600


def sh(cmd: list[str], timeout: int = 1800) -> tuple[int, str]:
    try:
        p = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True,
                           encoding="utf-8", errors="replace", timeout=timeout)
        return p.returncode, (p.stdout or "") + (p.stderr or "")
    except subprocess.TimeoutExpired:
        return 124, "timeout"


def stats() -> dict:
    def n(f, key=None):
        try:
            d = json.loads((ROOT / f).read_text(encoding="utf-8"))
            return len(d)
        except Exception:
            return 0
    try:
        dec = json.loads((ROOT / "research_decisions.json").read_text(encoding="utf-8"))
        accepted = sum(1 for v in dec.values() if v.get("verdict") == "accept")
    except Exception:
        dec, accepted = {}, 0
    return {"kept": n("research_output.json"),
            "reviewed": len(dec), "accepted": accepted,
            "misses": n("research_misses.json")}


def once() -> str:
    s = stats()
    sh([sys.executable, "scripts/publish.py"])
    rc, out = sh([sys.executable, "scripts/build_all.py"], timeout=2700)
    if rc != 0:
        return f"build failed, nothing pushed: {out[-300:]}"

    rc, _ = sh(["git", "add", "-A"])
    rc, out = sh(["git", "status", "--porcelain"])
    if not out.strip():
        return "no change this hour"

    msg = (f"Hourly: {s['accepted']} scenarios published of {s['reviewed']} "
           f"reviewed\n\n"
           f"Loop state at {datetime.now().isoformat(timespec='minutes')}: "
           f"{s['kept']} notes kept by the pipeline, {s['reviewed']} reviewed "
           f"by hand, {s['accepted']} accepted into the guide, "
           f"{s['misses']} open questions still queued for another attempt.\n\n"
           f"Only notes with an explicit accept verdict reach a page. A miss "
           f"is a question to revisit, never a claim that no answer exists.\n\n"
           f"Co-Authored-By: Claude Opus 5 (1M context) <noreply@anthropic.com>")
    (ROOT / ".hourly_msg").write_text(msg, encoding="utf-8")
    rc, out = sh(["git", "commit", "-q", "-F", ".hourly_msg"])
    (ROOT / ".hourly_msg").unlink(missing_ok=True)
    if rc != 0:
        return f"commit failed: {out[-200:]}"
    rc, out = sh(["git", "push", "-q", "origin", "main"], timeout=600)
    return ("pushed" if rc == 0 else f"push failed: {out[-200:]}") + \
           f" ({s['accepted']} published)"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--once", action="store_true")
    ap.add_argument("--interval", type=int, default=INTERVAL)
    a = ap.parse_args()
    while True:
        stamp = datetime.now().isoformat(timespec="seconds")
        print(f"[{stamp}] {once()}", flush=True)
        if a.once or STOP.exists():
            return 0
        time.sleep(a.interval)


if __name__ == "__main__":
    raise SystemExit(main())
