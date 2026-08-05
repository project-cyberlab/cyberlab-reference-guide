<!-- generated-by: scripts/generate_gui_pages.py -->
# HashMyFiles (GUI)

| | |
|---|---|
| **Capability** | acquire preserve |
| **Window title** | HashMyFiles |
| **Captured from** | `C:\Tools\HashMyFiles\HashMyFiles.exe` on 2026-08-02 — control tree in [`capture/gui/HashMyFiles/HashMyFiles.tree.txt`](../../capture/gui/HashMyFiles/HashMyFiles.tree.txt) |

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Hash a set of files — MD5, SHA-1, SHA-256 and CRC32 — and show them in one sortable list. Sorting by hash collapses duplicates across directories instantly, which is what makes it a triage tool rather than a hashing utility.

## When you'd reach for this

Reach for HashMyFiles when you have a folder of files and the question is which of them are the same. It hashes a set at once and shows MD5, SHA-1, SHA-256 and CRC32 in one sortable list.

Sorting by hash is what makes it a triage tool rather than a hashing utility: identical files collapse together immediately, so the same payload dropped under six names across four directories is obvious at a glance. Command-line hashing gives you the same numbers and leaves you to spot the duplicates yourself.

For verifying a single acquisition against its recorded hash, `sha256sum` is the simpler answer.

**Sources:** <https://www.nirsoft.net/utils/hash_my_files.html>

## Controls

The parts of this window you will actually touch, read from the application's own accessibility tree rather than from a screenshot. The full node list is in [`capture/gui/HashMyFiles/HashMyFiles.tree.txt`](../../capture/gui/HashMyFiles/HashMyFiles.tree.txt).

The window exposes 1 further named controls: **0 file(s)**. The full tree, with every automation id, is in [the capture](../../capture/gui/HashMyFiles/HashMyFiles.tree.txt).

## Using it

1. Drag files, or a folder, onto the window.
2. Read the count in the status pane to confirm everything you expected was taken — it is the only feedback that files were missed.
3. Sort by hash to group identical files; duplicates across directories collapse immediately.
4. Copy the hashes out for the report, or save them as the record of what was collected.

## Gotchas

- Hashing here is for triage and deduplication. It is not acquisition — an image's hash of record comes from the acquisition tool that made it.
- It follows what you dropped and nothing more. A folder dropped without recursion silently hashes only the top level.
