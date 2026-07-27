# YoutubeScraper — ytauto + channel knowledge vault

Two things live here:
1. **ytauto** — terminal app (Textual TUI) that scrapes YouTube into a deduped
   SQLite library. Code in `backend/`, run with `./run.sh`, tests:
   `PYTHONPATH=backend venv/bin/python -m pytest backend/tests -q`.
2. **`vault/`** — the knowledge layer for the faceless YouTube channel project
   (an Obsidian vault of plain markdown). **For any channel work, read
   `vault/CLAUDE.md` first** — it holds the two-home memory rule (SQLite = data,
   vault = knowledge + decisions) and the session protocol (read the vault at
   start; update it at end).

One home per fact: numbers → `library.db`; everything else durable — prose,
facts, decisions, status — → `vault/`. Never duplicate a fact across layers.
