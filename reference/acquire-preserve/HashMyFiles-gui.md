<!-- generated-by: scripts/generate_gui_pages.py -->
# HashMyFiles (GUI)

**Capability:** acquire preserve  **Window:** `HashMyFiles`  **Version:** —
**Captured:** `C:\Tools\HashMyFiles\HashMyFiles.exe` on 2026-08-02 — control tree in [`capture/gui/HashMyFiles/HashMyFiles.tree.txt`](../../capture/gui/HashMyFiles/HashMyFiles.tree.txt)

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Hash a set of files — MD5, SHA-1, SHA-256 and CRC32 — and show them in one sortable list. Sorting by hash collapses duplicates across directories instantly, which is what makes it a triage tool rather than a hashing utility.

## Window

![HashMyFiles main window](../../capture/gui/HashMyFiles/HashMyFiles.png)

## Controls

The window exposes 1 further named controls: **0 file(s)**. The full tree, with every automation id, is in [the capture](../../capture/gui/HashMyFiles/HashMyFiles.tree.txt).

## Using it

1. Drag files, or a folder, onto the window.
2. Read the count in the status pane to confirm everything you expected was taken — it is the only feedback that files were missed.
3. Sort by hash to group identical files; duplicates across directories collapse immediately.
4. Copy the hashes out for the report, or save them as the record of what was collected.

## Gotchas

- Hashing here is for triage and deduplication. It is not acquisition — an image's hash of record comes from the acquisition tool that made it.
- It follows what you dropped and nothing more. A folder dropped without recursion silently hashes only the top level.
