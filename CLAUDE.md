# YoutubeScraper — ytauto + channel knowledge vault

Two things live here:
1. **ytauto** — terminal app (Textual TUI) that scrapes YouTube into a deduped
   SQLite library. Code in `backend/`, run with `./run.sh`, tests:
   `PYTHONPATH=backend venv/bin/python -m pytest backend/tests -q`.
2. **`vault/`** — the knowledge layer for the faceless YouTube channel project
   (an Obsidian vault of plain markdown). **For any channel work, read
   `vault/CLAUDE.md` first** — it holds the three-layer memory rule (SQLite =
   data, vault = knowledge, Notion = decisions), the cross-surface boundary, and
   the session protocol (read Notion log at start; update vault + Notion at end).

One home per fact: numbers → `library.db`; durable prose/facts → `vault/`;
decisions/status → the Notion log. Never duplicate a fact across layers.
