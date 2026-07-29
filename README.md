# CyberLab Reference Guide

A field quick-reference for the kit. You open it mid-mission or mid-exercise
when you need a **capability** and do not remember which tool provides it — it
routes you to the tool, the exact command, and **every option, explained**.

> **Status:** format and scope established; worked example proven end to end.
> Content build is next. See [docs/PLAN.md](docs/PLAN.md).

---

## Start here

| You are… | Go to |
|---|---|
| Facing a problem — *"I need to carve deleted files"* | **Capability Index** *(being built — see PLAN)* |
| Asking what the kit even has | [**Kit Tool List**](catalog/KIT-TOOLS.md) — 1,006 tools, VM → category → tool |
| Wanting to know how pages are built and why | [**The Format**](docs/FORMAT.md) |
| Wanting to see a finished page | [**`fls`**](reference/filesystem-analysis/fls.md) — worked example, all 22 options |

## What makes this different

Every DFIR quick-reference in the field — SANS, Jai Minton's, tldr — either
organises by tool (so you must already know the tool) or skips flag
documentation entirely. The best of them states outright that it *"assumes
operator familiarity."*

This guide inverts that:

- **Capability-first.** You search by what you need to *do*.
- **Options completely listed out**, each with *what it does* and *when you'd use it*.
- **Tools attached to commands**, and each tagged with the VM that carries it —
  so you know whether you can run it on the box in front of you.

## Scope is binding

Only tools in [`catalog/kit-tools.json`](catalog/kit-tools.json) may be
documented. That file is generated from the kit VMs' own upstream manifests:

| Platform | Tools | Source of truth |
|---|---|---|
| Kali Linux | 403 | `kali-meta` `debian/control` (`kali-tools-*`) |
| REMnux | 268 | `REMnux/docs` discover-the-tools |
| SIFT Workstation | 162 | `teamdfir/sift-saltstack` |
| FLARE-VM | 137 | `mandiant/flare-vm` `config.xml` |
| Security Onion | 36 | kit tracker CSV |

Regenerate with `python scripts/build_kit_list.py`.

## Every flag is real

Options are **captured from the running binary** (`--help` / man, inside the kit
container), stored raw under [`capture/`](capture/), and checked by a linter.
A flag that cannot be produced from a real binary cannot ship.

This is a direct response to a measured failure in the predecessor project,
where fabricated CLI flags reached roughly 44 of 61 modules. Full rationale in
[docs/FORMAT.md](docs/FORMAT.md#5-verification-why-the-options-can-be-trusted).

## Relationship to cyberlab

Separate repository, deliberately. The
[cyberlab training lab](https://github.com/project-cyberlab/cyberlab) is **on
hold** and receives no changes from this work.

## Layout

```
catalog/    kit tool list — the binding scope (generated)
reference/  the guide itself, one page per tool, grouped by capability
capture/    raw --help/man output, committed as evidence
docs/       FORMAT.md (how pages are built), PLAN.md (roadmap)
scripts/    build_kit_list.py, and the linter
```
