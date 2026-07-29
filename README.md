# CyberLab Reference Guide

A field quick-reference for the kit. You open it mid-mission or mid-exercise
when you need a **capability** and do not remember which tool provides it — it
routes you to the tool, the exact command, and **every option, explained**.

---

## Start here

| You are… | Go to |
|---|---|
| Facing a problem — *"I need to carve deleted files"* | [**Capability Index**](reference/INDEX.md) — 46 capabilities |
| Asking what the kit even has | [**Kit Tool List**](catalog/KIT-TOOLS.md) — 1,006 tools, VM → category → tool |
| Wanting a finished page | [`fls`](reference/examine-the-filesystem/fls.md) · [`vol`](reference/memory-forensics/vol.md) · [`yara`](reference/malware-triage-static/yara.md) |
| Carrying it into the field | [**PDF**](CyberLab-Reference-Guide.pdf) — 372 pages |
| Wanting to know how pages are built and why | [**The Format**](docs/FORMAT.md) |

## Where it stands

| | |
|---|---|
| Kit inventory | **1,006** tools, 5 platforms, 54 categories |
| Captured from a real binary | **945** commands |
| Capabilities | **46**, across 10 investigation phases |
| Tool pages | **135**, every one with a complete options table |
| Flags with usage guidance | **153** across 20 reviewed tools |
| Mined invocations | **360** real commands from cyberlab |
| Citations checked | **255** URLs — 245 live |
| Linter | **0 errors**, 269 warnings (tracked debt) |

## What makes this different

Every DFIR quick-reference in the field either organises by tool (so you must
already know the tool) or skips flag documentation. The most complete one in
public circulation states outright that it *"assumes operator familiarity."*

This guide inverts that:

- **Capability-first.** You search by what you need to *do*, not what the binary is called.
- **Options completely listed out** — every flag, with *what it does* and *when you'd use it*.
- **Tools attached to commands**, each tagged with the VM that carries it, so you
  know whether you can run it on the box in front of you.

## Scope is binding

Only tools in [`catalog/kit-tools.json`](catalog/kit-tools.json) may be
documented. It is generated from the kit VMs' own upstream manifests:

| Platform | Tools | Source of truth |
|---|---|---|
| Kali Linux | 403 | `kali-meta` `debian/control` (`kali-tools-*`) |
| REMnux | 268 | `REMnux/docs` discover-the-tools |
| SIFT Workstation | 162 | `teamdfir/sift-saltstack` |
| FLARE-VM | 137 | `mandiant/flare-vm` `config.xml` |
| Security Onion | 36 | kit tracker CSV |

## Every flag is real

Options are **captured from the running binary** (`--help` / man, inside the kit
container), stored raw under [`capture/`](capture/), and enforced by
`scripts/lint.py`: a documented flag absent from a capture is a **build error**.

This answers a measured failure in the predecessor project, where fabricated CLI
flags reached ~44 of 61 modules. Rationale in
[docs/FORMAT.md](docs/FORMAT.md#5-verification-why-the-options-can-be-trusted).

Citations are liveness-checked too — see [capture/SOURCES.md](capture/SOURCES.md).

## Rebuild everything

```bash
python scripts/build_kit_list.py      # kit inventory from upstream manifests
python scripts/candidates.py          # candidate command names
# scripts/probe_container.sh runs inside the kit container on rick
python scripts/merge_coverage.py      # merge probe results -> coverage report
python scripts/mine_cyberlab.py       # candidate invocations (read-only)
python scripts/generate_pages.py      # tool pages (never overwrites hand-written)
python scripts/build_index.py         # capability index
python scripts/lint.py                # gate: 0 errors required
python scripts/validate_sources.py    # citation liveness
python scripts/build_pdf.py           # print render
```

## Relationship to cyberlab

Separate repository, deliberately. The
[cyberlab training lab](https://github.com/project-cyberlab/cyberlab) is **on
hold** and receives no changes from this work; it is read-only input for mining.

## Layout

```
catalog/    kit tool list — the binding scope (generated)
reference/  the guide: INDEX.md + one page per tool, grouped by capability
capture/    raw --help/man output, committed as evidence
docs/       FORMAT.md (how pages are built), PLAN.md (roadmap)
scripts/    build, probe, mine, generate, lint, validate, render
```
