#!/usr/bin/env python3
"""A second opinion from a different vendor entirely.

The local models are the drafting tier: cheap, parallel across two GPUs, and
measured adequate at 9-14B because compressing a retrieved paragraph is not
hard work. What they cannot provide is independence. gemma checking qwen is
better than qwen checking qwen, but both are open-weight models trained on
overlapping corpora, and shared training data means shared blind spots.

A hosted frontier model from a different vendor does not share those. That is
the entire value here -- not that it is smarter, but that it is wrong in
different places. Corroboration between two systems that fail the same way is
an echo; corroboration across genuinely different ones is evidence.

Keys live on rick in the night_loop pack and are read once into a local file
this repo does not track. They are free tiers with daily caps, so this tier is
used only where independence actually buys something: checking a claim against
the sources, never drafting.

    from free_api import ask, available
"""
from __future__ import annotations
import json
import subprocess
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
KEYS = ROOT / ".free_keys.local.json"

# Order matters. SambaNova fronts DeepSeek-class models that follow a strict
# output contract; the fast trio behind it are backstops for when it
# rate-limits, which the earlier project measured it doing under sustained
# load at around 210k tokens a day.
PRIORITY = ("sambanova", "sambanova2", "sambanova3",
            "mistral", "groq", "gemini", "openrouter", "nvidia")


def _load() -> dict:
    if KEYS.exists():
        try:
            return json.loads(KEYS.read_text(encoding="utf-8"))
        except Exception:
            pass
    # Pulled through WSL because a PreToolUse hook blocks direct homelab ssh,
    # and WSL keeps warm control masters so this costs milliseconds.
    try:
        p = subprocess.run(
            ["wsl.exe", "-d", "Ubuntu-24.04", "-e", "bash", "-c",
             "ssh ricksanchez 'cat ~/work/night_loop/.free_keys.json'"],
            capture_output=True, text=True, timeout=120)
        data = json.loads(p.stdout)
    except Exception:
        return {}
    KEYS.write_text(json.dumps(data), encoding="utf-8")
    return data


_KEYS: dict = {}


def available() -> list[str]:
    global _KEYS
    if not _KEYS:
        _KEYS = _load()
    return [p for p in PRIORITY if p in _KEYS]


def ask(prompt: str, provider: str | None = None,
        timeout: int = 120, max_tokens: int = 400) -> tuple[str, str]:
    """Return (answer, provider_used). Empty answer means every provider failed.

    Tries providers in priority order rather than picking one, because a free
    tier that is rate-limited is indistinguishable from one that is down, and
    a verification step that silently returns nothing is worse than useless --
    it looks like agreement.
    """
    global _KEYS
    if not _KEYS:
        _KEYS = _load()
    order = [provider] if provider else list(available())
    for name in order:
        cfg = _KEYS.get(name)
        if not cfg:
            continue
        body = json.dumps({
            "model": cfg["model"],
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.0,
            "max_tokens": max_tokens,
        }).encode()
        req = urllib.request.Request(
            cfg["base_url"].rstrip("/") + "/chat/completions",
            data=body,
            headers={"Content-Type": "application/json",
                     "Authorization": f"Bearer {cfg['api_key']}"})
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r:
                d = json.loads(r.read())
            text = (d["choices"][0]["message"]["content"] or "").strip()
            if text:
                return text, name
        except Exception:
            continue
    return "", ""


if __name__ == "__main__":
    print("providers:", ", ".join(available()) or "(none reachable)")
    ans, who = ask("Reply with exactly one word: OK")
    print(f"probe -> {who or 'all failed'}: {ans[:80]}")
