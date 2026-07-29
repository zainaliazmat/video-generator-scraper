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
3. **`studio/videos/`** — HyperFrames projects for videos **still in production**
   (one dir per cut; `studio/` is gitignored and is its own repo, so nothing there
   is backed up). A video with a YouTube URL is finished: `tools/archive_cut.py`
   moves its source to `vault/videos/<slug>/src/{hi,en,thumbs}/` and deletes it
   from studio — see the finished-video rule in `vault/CLAUDE.md`.
   (`compositions/` is the older text-only mirror, now holding history cuts only.)
   The finance channels are produced by
   **`/finance-video`** (agents in `.claude/agents/fin-*.md`, mechanics in
   `tools/`, constants in `tools/format.json`) — human doc:
   `vault/workflows/finance-video.md`.

One home per fact: numbers → `library.db`; everything else durable — prose,
facts, decisions, status — → `vault/`. Never duplicate a fact across layers.
