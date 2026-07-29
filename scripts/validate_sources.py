#!/usr/bin/env python3
"""Liveness-check every URL the guide cites.

The predecessor project shipped citations that looked authoritative and 404'd,
because they were generated rather than fetched. A dead link here is a defect,
so this reports them explicitly and writes a dated record of what was checked.

Network-guarded: if a control URL fails, the whole run is inconclusive and we
report that instead of condemning every link as dead.
"""
from __future__ import annotations
import json
import re
import sys
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTROL = "https://attack.mitre.org/"
TIMEOUT = 12
UA = {"User-Agent": "Mozilla/5.0 (cyberlab-reference-guide link checker)"}

URL_RE = re.compile(r"https?://[^\s)>\]\"'`,]+")

# Not citations. Mined invocations contain example and placeholder URLs
# (RFC 5737 documentation ranges, shell variables, printf templates); checking
# them produces noise that hides real dead links.
NOT_A_CITATION = re.compile(
    r"(\$\{?[A-Za-z_]|%[sd]|127\.0\.0\.1|localhost|0\.0\.0\.0|"
    r"192\.0\.2\.|198\.51\.100\.|203\.0\.113\.|example\.(com|org|net)|"
    r"<[^>]*>|\.\.\.)")


def clean_url(u: str) -> str:
    # Markdown escaping leaks into extracted URLs: github.com/x/ioc\_parser
    return u.rstrip(".,;").replace("\\_", "_").replace("\\-", "-")


def check(url: str) -> tuple[str, int | str]:
    url = url.rstrip(".,;")
    for method in ("HEAD", "GET"):
        try:
            req = urllib.request.Request(url, headers=UA, method=method)
            with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
                return url, r.status
        except urllib.error.HTTPError as e:
            if e.code in (403, 405, 429) and method == "HEAD":
                continue                     # some hosts refuse HEAD; retry as GET
            return url, e.code
        except Exception as e:               # DNS, TLS, timeout
            if method == "GET":
                return url, type(e).__name__
    return url, "unknown"


def collect() -> dict[str, list[str]]:
    """url -> where it was cited."""
    found: dict[str, list[str]] = {}

    kit = json.loads((ROOT / "catalog" / "kit-tools.json").read_text(encoding="utf-8"))
    for vm, cats in kit["kit"].items():
        for _c, entries in cats.items():
            for e in entries:
                u = (e.get("url") or "").strip()
                if u.startswith("http") and not NOT_A_CITATION.search(u):
                    found.setdefault(clean_url(u), []).append(f"catalog:{vm}:{e['tool']}")
    for src in kit.get("sources", {}).values():
        if str(src).startswith("http"):
            found.setdefault(str(src), []).append("catalog:source")

    for md in list((ROOT / "reference").rglob("*.md")) + \
              list((ROOT / "docs").glob("*.md")) + [ROOT / "README.md"]:
        if not md.exists():
            continue
        rel = md.relative_to(ROOT).as_posix()
        for u in URL_RE.findall(md.read_text(encoding="utf-8", errors="replace")):
            if NOT_A_CITATION.search(u):
                continue
            found.setdefault(clean_url(u), []).append(rel)
    return found


def main() -> int:
    urls = collect()
    print(f"checking {len(urls)} distinct URLs...")

    _, ctrl = check(CONTROL)
    if not isinstance(ctrl, int) or ctrl >= 400:
        print(f"CONTROL URL failed ({ctrl}) — network unavailable, "
              f"treating run as INCONCLUSIVE (nothing marked dead).")
        return 0

    with ThreadPoolExecutor(max_workers=12) as pool:
        results = dict(pool.map(check, urls))

    dead = {u: s for u, s in results.items()
            if not isinstance(s, int) or s >= 400}
    ok = len(results) - len(dead)

    lines = [f"# Source Validation", "",
             f"Checked {len(results)} distinct URLs on {date.today().isoformat()}.",
             f"Control (`{CONTROL}`) responded, so this run is conclusive.", "",
             f"- **{ok} live**", f"- **{len(dead)} dead or unreachable**", ""]
    if dead:
        lines += ["## Dead or unreachable", "",
                  "| URL | Status | Cited by |", "|---|---|---|"]
        for u, s in sorted(dead.items()):
            where = ", ".join(sorted(set(urls[u]))[:3])
            lines.append(f"| {u} | {s} | {where} |")
        lines.append("")
        lines += ["A 403 usually means the host blocks automated clients rather "
                  "than the page being gone; those are worth a manual look before "
                  "removing the citation.", ""]
    (ROOT / "capture" / "SOURCES.md").write_text("\n".join(lines), encoding="utf-8")

    print(f"live={ok} dead={len(dead)}")
    for u, s in sorted(dead.items())[:25]:
        print(f"  {s}  {u}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
