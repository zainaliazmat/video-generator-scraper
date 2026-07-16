# MAP.md — Project Cartography (2026-07-17)

Project root: `/home/zain-ali/Documents/YoutubeScraper` — total working-tree size **1.6 GB** (excluding the `studio` symlink target). Two distinct things live here: a Python YouTube-scraper terminal app (`ytauto`, code in `backend/`) and a faceless-YouTube-channel knowledge/production project (markdown vault + media assets + research downloads).

---

## 1. Directory Map

Top-level, sorted by size (`du -sh`):

| Path | Size | Contents |
|------|------|----------|
| `studio/` → symlink | (0 B local; target 8.0 GB) | Symlink to `/home/zain-ali/Documents/ClaudeHyperFrame` (outside this repo). |
| `research/` | 813 MB | Downloaded YouTube reference videos/frames/subtitles for study. 6 keyword/pick subtrees. |
| `venv/` | 376 MB | Python virtualenv (Python 3.12). Not tracked. |
| `Pompie Assets/` | 357 MB | Image assets for the Pompeii video (JPEG/JPG scene + evidence stills). |
| `assets/` | 26 MB | `tts-samples/` — 27 generated `.mp3` voiceover samples. |
| `.git/` | 19 MB | Git repository. |
| `history/` | 896 KB | 4 dated `.tsv` scrape snapshots (Compare feature input). |
| `.gstack/` | 872 KB | QA/browse tooling output: 6 screenshot PNGs + `browse-startup-error.log`. Perms `drwx------`. |
| `vault/` | 688 KB | Obsidian markdown knowledge vault (the channel's "knowledge home"). |
| `backend/` | 512 KB | Python source for the scraper + Textual TUI + tests. |
| `__pycache__/` | 88 KB | Root-level bytecode cache (7 `.pyc`). |
| `tools/` | 52 KB | `tts/` (ElevenLabs script) + `prompt-runner/` (browser extension). |
| `.pytest_cache/` | 36 KB | Pytest cache. |
| `docs/` | 20 KB | One spec: `superpowers/specs/2026-07-04-ytauto-tui-design.md`. |

Root-level loose files: `library.db` (1.18 MB SQLite), `CLAUDE.md`, `README.txt`, `PRODUCTION_RUNBOOK.md`, `NICHE_RESEARCH_2026-07.md`, `run.sh`, `ytauto`, `.env`, `.env.example`, `.gitignore`.

File-extension histogram (excluding `.git`, `venv`, `studio`, `research`, `Pompie Assets`): 48 `.md`, 34 `.pyc`, 27 `.mp3`, 26 `.py`, 6 `.png`, 6 `.json`, 4 `.tsv`, 2 `.js`, 2 `.txt`, 1 each `.tcss`/`.css`/`.sh`/`.db`/`.log`/`.env`.

**Largest single files:** `research/f2n9Nbt_jMk/pick-1-f2n9Nbt_jMk/video.mp4` (258.6 MB), `research/.../pick-2-f4ixJQLwAUE/video.mp4` (156.6 MB), `research/wj39QiFqCQg/pick-3-NP4RrJCYFGs/video.mp4` (126.9 MB). Largest image: `Pompie Assets/AllScenes-Final/_evidence/EV-18B_amphitheatre-ruins.jpg` (9.4 MB).

---

## 2. Age Distribution

Mtime histogram (files excluding `.git`, `venv`, `studio`), relative to 2026-07-17:

| Bucket | Count |
|--------|-------|
| ≤ 7 days | 174 |
| 8–30 days | 763 |
| 1–6 months | 0 |
| 6–12 months | 0 |
| > 1 year | 0 |

Entire project is **≤ ~18 days old** (all activity June 30 – July 17, 2026).

- **Newest meaningful files:** `vault/videos/video-hist-01-pompeii/script-v1-devanagari-tts.md` and `.../index.md` (2026-07-17 01:38); TTS mp3s in `assets/tts-samples/` up to 2026-07-16 06:16.
- **Oldest files:** `__pycache__/analyze.cpython-312.pyc` (2026-06-30 21:22), `.pytest_cache` and `.gstack` artifacts (2026-07-01). Oldest source-adjacent activity aligns with the initial commit (2026-07-01).

---

## 3. Version Control

- **Current branch:** `audit/2026-07-17`. Other local branch: `master`.
- **Remotes:** `git remote -v` returns **empty** — no remotes configured. Repo is local-only.
- **Commits:** 39 total, all in **2026-07**. First: `2026-07-01 00:58` "Initial commit: YouTube content-research CLI + Voyara Signal web-app design spec". Last: `2026-07-05 04:29` "docs(vault): video-02 draft-4 …". Commit activity is concentrated July 1–5; no commits since July 5 despite heavy file changes through July 17.
- **Tracked files:** 55 total (`git ls-files`).
- **Uncommitted state:** 23 modified + 1 deleted tracked file (all under `vault/` plus root `.gitignore`, `CLAUDE.md`), and ~15 untracked entries. Untracked notables: `.env.example`, `NICHE_RESEARCH_2026-07.md`, `PRODUCTION_RUNBOOK.md`, `Pompie Assets/`, `tools/`, several new `vault/` knowledge/video/workflow markdown files (e.g. `vault/videos/video-hist-01-pompeii/`, `video-hist-01-travel/`, `vault/workflows/voiceover-tts.md`).
- **.gitignore excludes:** `venv/`, `__pycache__/`, `*.pyc/*.pyo`, `youtube_results.tsv`, `youtube_results_analysis.xlsx`, `youtube_content_ideas.md`, `history/`, `library.db`, `*.zip`, `.pytest_cache/`, `.env`, `assets/tts-samples/*.mp3`, `.DS_Store`, `*.swp`, `vault/.obsidian/`, `.gstack/`, `research/`, `studio`.
- **Large/important dirs NOT tracked by git** (working tree vs `git ls-files`): `research/` (813 MB, 0 tracked), `Pompie Assets/` (357 MB, 0 tracked), `venv/` (376 MB), `assets/` (26 MB), `history/` (896 KB), `tools/` (52 KB), `.gstack/`, `studio`, and root `library.db` (0 tracked). Only `vault/` (22 tracked of ~40 files) and `docs/` (1 file) plus root markdown/scripts and `backend/` are under version control.

---

## 4. Data Stores

- **`/home/zain-ali/Documents/YoutubeScraper/library.db`** — SQLite, 1,208,320 bytes (1.18 MB), mtime 2026-07-07. Git-ignored.
  - Table **`videos`**: **1,124 rows**. 24 columns: `video_id, keyword, title, channel, channel_url, channel_id, subscribers, channel_verified, views, likes, comments, duration, duration_sec, upload_date, tags, categories, language, channel_description, channel_tags, video_url, thumbnail, first_seen, last_seen, times_seen`.
  - No other database files exist in the tree. (Inspected via Python `sqlite3`; the `sqlite3` CLI is not installed.)
- **TSV snapshots** in `history/`: `youtube_results_2026-07-04.tsv`, `web_youtube_results_2026-07-01.tsv`, `web_youtube_results_2026-07-04.tsv`, and a diff TSV — these are the Compare-feature data snapshots.

---

## 5. Boundaries (things living / referenced outside this folder)

- **`studio` symlink → `/home/zain-ali/Documents/ClaudeHyperFrame`** (8.0 GB target directory outside this repo; the video-production "studio").
- **Claude memory dir:** `/home/zain-ali/.claude/projects/-home-zain-ali-Documents-YoutubeScraper/` — 212 MB total; ~30 session `.jsonl` transcripts (largest 34 MB, 30 MB, 29 MB) plus per-session subfolders. Contains a curated `memory/` subdir with named notes (files, names only): `english-titles-descriptions.md`, `islamic-pov-in-stories.md`, `MEMORY.md`, `post-delivery-cleanup-protocol.md`, `scene-image-prompt-rules.md`, `short-report-preference.md`, `thumbnail-canva-template.md`, `tts-voiceover-pipeline.md`, `two-home-memory-architecture.md`, `urdu-scripts-roman-urdu.md`.
- **External services referenced in docs (`PRODUCTION_RUNBOOK.md`, `vault/`):** HeyGen **HyperFrames** (HTML-to-video framework; `npx hyperframes …` CLI), HeyGen audio/SFX library, **ElevenLabs** TTS (API key consumer), local **Kokoro** TTS, Pixabay Music / Uppbeat / Free Music Archive / freesound.org (music/SFX sources), **Canva** (thumbnail template, per memory note), **Notion** (a deleted template `vault/templates/notion-log-entry.md`), YouTube (scrape source via `yt-dlp`).
- **Connectors surfaced to this session (auth required, unused):** Gmail, Google Calendar, Google Drive, HyperFrames by HeyGen, vidIQ. MCP tools for Canva, Notion, Slack, Atlassian, Figma are available but not invoked.
- No hardcoded remote hosts/API endpoints found in tracked configs beyond the above; only reference URL is python.org install link in `run.sh`.

---

## 6. Self-Documentation

| Path | Size | Last modified | Covers |
|------|------|---------------|--------|
| `CLAUDE.md` | 797 B | 2026-07-10 | Repo overview: ytauto vs vault, the "two-home memory" rule (numbers→`library.db`, prose→`vault/`), how to run/test. |
| `README.txt` | 6.49 KB | 2026-07-04 | End-user guide to `ytauto`: Scrape/Compare/Predict tasks, output files, quick start. |
| `PRODUCTION_RUNBOOK.md` | 27.2 KB | 2026-07-04 | Step-by-step prompt playbook for building a vintage-parallax slideshow video with HyperFrames (setup, composition, music, TTS/voiceover, QA, render). |
| `NICHE_RESEARCH_2026-07.md` | 20.6 KB | 2026-07-10 | Niche/market research notes for the channel (July 2026). |
| `vault/CLAUDE.md` | 3.46 KB | 2026-07-10 | Vault operating rules: two-home memory, session start/end protocol for channel work. |
| `vault/index.md` | 5.13 KB | 2026-07-16 | Table-of-contents / map of the knowledge vault (links to skills, workflows, knowledge). |
| `docs/superpowers/specs/2026-07-04-ytauto-tui-design.md` | 5.14 KB | 2026-07-04 | Design spec for the ytauto Textual TUI. |
| `tools/prompt-runner/README.md` | 3.44 KB | 2026-07-12 | Docs for the `prompt-runner` browser extension. |
| `backend/requirements.txt` | 358 B | 2026-07-04 | Dependency manifest (see §7). |

Plus ~40 vault markdown docs organized as `knowledge/` (best-practices, channels, monetization, niches, scraping-playbook, video-studies, design notes, urdu-script-style), `skills/` (hyperframes_production, long_form_scripting, youtube_channel_skill), `templates/` (script, storyboard, video-study), `workflows/` (video-study, voiceover-tts), and `videos/` (video-01, video-02-claude-edits-video, video-hist-01-pompeii, video-hist-01-travel — each with scripts, build-logs, storyboards, design docs).

---

## 7. Code Inventory

- **Language:** Python 3.12 (scraper + TUI); JavaScript (browser extension); Bash (launchers).
- **Location:** `backend/` (26 `.py`, 2,577 total lines counting tests). Key modules: `youtube_scraper.py` (468 L — the scraper core), `study.py` (214 L), `ideas.py` (199 L — AI prediction via claude-agent-sdk), `analyze.py` (194 L), `library.py` (124 L — SQLite layer), `history.py` (104 L). TUI in `backend/tui/` (Textual): `app.py`, `run_screen.py`, `predict_screen.py`, `scrape_screen.py`, `library_screen.py`, `diff_screen.py`, `inputs.py`, `sources.py`, `ytauto.tcss` (styles), `__main__.py`.
- **Tests:** yes — `backend/tests/` with 8 test modules (`test_library.py` 132 L, `test_tui_smoke.py` 66 L, `test_predict.py`, `test_run_scrape.py`, `test_study.py`, `test_inputs.py`, `test_sources.py`) + `conftest.py`. Run: `PYTHONPATH=backend venv/bin/python -m pytest backend/tests -q`. (Pytest cache shows additional past test names not present as source: test_app, test_jobs, test_serialize, test_tsv_sources, test_predict_endpoint.)
- **Entry points:** `run.sh` (2.18 KB — one-command venv-setup + TUI launcher, `--update`/`--fast` aware), `ytauto` (787 B — symlinkable PATH shim that delegates to `run.sh`).
- **Other tools:** `tools/tts/elevenlabs_tts.py` (166 L — ElevenLabs voiceover generation); `tools/prompt-runner/` — a browser extension (`manifest.json`, `content.js`, `background.js`, README).
- **Dependency manifest** (`backend/requirements.txt`): `yt-dlp>=2025.1.1`, `claude-agent-sdk>=0.2.0` (AI prediction, runs via Claude Code CLI), `textual>=0.60` (TUI), `pytest>=8.0`, `pytest-asyncio>=0.23` (test-only). No `package.json`; the browser extension has only `manifest.json`.

---

## 8. Media / Asset Inventory

- **`Pompie Assets/`** (357 MB, 120 files): `AllScenes-Final/` with `_extras/` and `_evidence/` subdirs. Formats: **88 `.jpeg`, 25 `.jpg`, 2 `.mp4`, 5 `.md`**. Naming pattern: scene IDs like `S3-18B_amphitheatre.jpeg`, `S7-47A_shepherd-plain.jpeg`, and evidence stills `EV-18B_amphitheatre-ruins.jpg`, `EV-51A-boxer_man-covering-face.jpg`.
- **`assets/tts-samples/`** (26 MB, 27 `.mp3`): generated voiceover clips. Naming: `pompeii-ch<N>-<range>-B-v3.mp3`, `pompeii-hook-01-07-v3.mp3`, voice tests `ztest-A-vikramS.mp3` / `ztest-B-harsh.mp3` / `ztest-C-ranbir.mp3`, language tests `kanwan-urdu-vs-hindi.mp3`, `pompeii-l03-05-hindi-v3tagged.mp3` (Hindi/Urdu/Nastaliq TTS iterations).
- **`research/`** (813 MB): downloaded reference material — **596 `.jpg` (frames), 22 `.vtt` (subtitles), 12 `.txt`, 10 `.mp4`, 5 `.md`**. Organized by YouTube video ID / keyword with `pick-N-<id>/video.mp4` subfolders and a `faceless/` (top/mid/low) + `own-a-century-of-travel/frames/` set.
- **Project-wide media counts:** 27 `.mp3` (26 MB, all in `assets/`), 12 `.mp4` (10 in `research/`, 2 in `Pompie Assets/`), 6 `.png` (all in `.gstack/qa-reports/screenshots/`), ~700+ JPEG/JPG images (mostly `research/` + `Pompie Assets/`).

---

## Couldn't inspect

- **`sqlite3` CLI not installed** — DB read instead via Python `sqlite3` (succeeded; table + row + column facts above are complete).
- **`studio/`** — symlink to `/home/zain-ali/Documents/ClaudeHyperFrame` (8.0 GB), outside repo scope; not traversed per read-only/boundary limits (only existence, target, and size noted).
- **`.gstack/` internals** — directory perms are `drwx------`; file listing succeeded (7 files), individual PNG/log contents not opened.
- **Memory `.jsonl` session transcripts** (`~/.claude/projects/…`) — listed by name/size only; contents not read (may contain conversational secrets); the `memory/` subdir notes listed by filename only.
- **`.env`** (164 B) — defines variable **`ELEVENLABS_API_KEY`** (value NOT read/printed). `.env.example` (107 B) defines the same name as a placeholder.
- Binary media (mp3/mp4/jpg/png/db) catalogued by count/size/name only; not decoded.
