# YoutubeScraper — what this repo is, and how to rebuild it from nothing

If this folder is deleted, everything below can be restored from
`git clone github-zainaliazmat:zainaliazmat/video-generator-scraper.git` plus the
steps in [Rebuild from a fresh clone](#rebuild-from-a-fresh-clone). Read
[What cannot be recovered](#what-cannot-be-recovered) first so you know what you
are and aren't getting back.

For the ytauto app's *user manual* (menus, scrape/compare/predict), see
`README.txt`. This file is about the repo and the rebuild.

---

## The three layers

| Layer | Where | In git? |
|---|---|---|
| **ytauto** — Textual TUI that scrapes YouTube into a deduped SQLite library | `backend/`, `run.sh`, `ytauto` | ✅ yes |
| **vault** — the knowledge layer: decisions, facts, milestone notes, **and the source of every finished video** | `vault/` | ✅ yes |
| **studio** — HyperFrames workspace where videos are *built* | `studio/` | ❌ **no** — gitignored, rebuildable |

Plus `tools/` (the video pipeline: TTS, stock fetch, checks, archive) and
`.claude/agents/fin-*.md` (the `/finance-video` pipeline stages) — both in git.

**The rule that makes this safe:** a video is finished the moment its YouTube URL
exists. `tools/archive_cut.py` then moves its source into
`vault/videos/<slug>/src/` and deletes it from `studio/`. So the only things ever
living *solely* in the untracked `studio/` are videos still in production. Full
rule: `vault/CLAUDE.md` § the finished-video rule.

---

## Rebuild from a fresh clone

Versions this was last known to work on (2026-07-29): Python 3.12.3, Node
v22.18.0, npm 11.6.0, ffmpeg 6.1.1, Google Chrome (at `/usr/bin/google-chrome`).

### 1. Clone

```bash
git clone github-zainaliazmat:zainaliazmat/video-generator-scraper.git YoutubeScraper
cd YoutubeScraper
```

### 2. ytauto (the scraper)

```bash
./run.sh          # creates venv/, installs backend/requirements.txt, launches the TUI
./run.sh --update # same, but refresh yt-dlp first (fixes most YouTube breakages)
```

Tests: `PYTHONPATH=backend venv/bin/python -m pytest backend/tests -q`

### 3. Secrets

```bash
cp .env.example .env
```

Then paste real values for all three keys — `.env` is gitignored, so **these are
never in the clone and cannot be recovered from git**:

| Key | Used by |
|---|---|
| `ELEVENLABS_API_KEY` | `tools/tts/elevenlabs_tts.py` — all voiceover |
| `PIXABAY_API_KEY` | `tools/stock/pixabay_fetch.py` — stock photography |
| `PEXELS_API_KEY` | the Pexels stock provider |

### 4. Video-pipeline Python deps

`run.sh` only installs ytauto's deps. The pipeline needs one more:

```bash
venv/bin/pip install -r tools/requirements.txt
```

That is `faster-whisper`, used by `fin-render` to re-transcribe the finished
master and verify VO placement. Everything else in `tools/` is stdlib only.

### 5. studio — a complete new one

**You do not need to clone the HyperFrames monorepo to build or render a video.**
`hyperframes` is a public npm package; each project pins it as a devDependency
(`tools/scaffold/package.json` pins **0.7.66**; latest on npm was 0.7.82 on
2026-07-29). A project directory + `npm install` is a working studio.

```bash
mkdir -p studio/videos
```

That is the minimum. Then jump to step 6 to populate it.

**Optional — the full monorepo**, only if you want the HyperFrames skills,
registry blocks, or examples:

```bash
git clone https://github.com/heygen-com/hyperframes.git studio
cd studio && npm install
```

The previous studio was at monorepo tag **`v0.7.10`** (`f3d7a1e3`), cloned from
the personal fork `zainaliazmat/ClaudeHyperframe.git` with
`heygen-com/hyperframes` as `upstream`. Its git history was **deliberately
removed on 2026-07-29** — see [Why studio has no git](#why-studio-has-no-git).

Skills are installed with `npx skills add heygen-com/hyperframes` (they land in
`studio/.claude/skills/`).

### 6. Restore a video project

Every finished video's source is in the vault. To rebuild one:

```bash
SLUG=good-debt-vs-bad-debt; CUT=hi
mkdir -p studio/videos/$SLUG-$CUT
cp -r tools/scaffold/. studio/videos/$SLUG-$CUT/        # vendored binaries
cp -r vault/videos/$SLUG/src/$CUT/. studio/videos/$SLUG-$CUT/   # the composition
cd studio/videos/$SLUG-$CUT && npm install
npm run check && npm run render
```

Copy the scaffold **first**, the archive **second** — the archive's own
`package.json` is the authoritative one and must win.

`tools/scaffold/` carries what the archive deliberately drops: the pinned
`package.json` + lockfile, `assets/js/gsap.min.js`, the self-hosted FinanceSans
font, and `assets/img/grain.png`. **Never scaffold from a sibling video** — a
shipped one gets deleted from studio.

**Two project styles, both pinned to hyperframes 0.7.66:**

- `good-debt-vs-bad-debt`, `pay-yourself-first` and anything newer declare
  `"devDependencies": {"hyperframes": "0.7.66"}` — these need `npm install`.
- `50-30-20-rule`, `needs-vs-wants`, `emergency-fund` predate that and instead
  call `npx --yes hyperframes@0.7.66` from their npm scripts — for these
  `npm install` is a no-op and `npm run render` fetches the tool itself.

Either way the version is the same, so a restore is reproducible. New cuts should
use the devDependency form (that is what `tools/scaffold/` gives you).

Videos still in production keep a text-only mirror in `compositions/`.

**What a restore will not give you back:** the generated scene images and the VO
mp3s. Re-running `gen_vo_*.sh` re-pays ElevenLabs; re-sourcing photos re-pays
image gens or stock calls. Two gotchas: `gen_vo_*.sh` hardcodes an absolute `cd`
into the old studio path (repoint it first), and the `.src` image-prompt
convention only starts at `pay-yourself-first` — older videos archived no
prompts. Per-video detail is in each `vault/videos/<slug>/index.md`.

### 7. library.db

Not in git (it is regenerable data, and large). Recreate it by running `./run.sh`
and doing a scrape; it rebuilds as a deduped store, one row per video. Historical
snapshots in `history/` are also untracked and are not recoverable.

---

## What cannot be recovered

Git honestly does not have these. Nothing below is a bug — each was excluded on
purpose — but know the list before you rely on the clone.

| Missing | Size | Get it back by |
|---|---|---|
| `.env` API key **values** | — | Re-issue from ElevenLabs / Pixabay / Pexels |
| `studio/library/` — personal media (fonts, sfx, textures, brand, 1.1 G of `projects/`) | ~1.2 G | Not recoverable. Personal asset collection, never versioned |
| Rendered masters (`renders/*.mp4`) | GBs | The videos are on YouTube. Re-render from archived source |
| Generated scene images + VO mp3s | GBs | Re-pay image gens + ElevenLabs |
| `library.db` + `history/` | ~1 MB + | Re-scrape |
| `node_modules/` | ~1.7 G | `npm install` |
| `venv/` | — | `./run.sh` |
| `research/`, `.gstack/`, `Pompie Assets/` | — | Not recoverable; excluded deliberately |

---

## Why studio has no git

`studio/` used to contain its own `.git` — a clone of a personal fork of
`heygen-com/hyperframes`. It was removed on 2026-07-29 because it was actively
harmful:

- It made `studio/` look version-controlled when the parent repo **gitignores the
  whole directory**, so nothing in it was ever backed up to
  `video-generator-scraper.git`. Every finance video built there sat outside the
  project's history entirely.
- Its local `main` was **ahead 4 / behind 1338** and would never be pushed —
  those 4 commits were video source (soul-of-coffee) plus README and `.gitignore`
  tweaks, not HyperFrames work worth upstreaming.
- Its `.gitignore` had been hand-edited into an allow-list to track composition
  text. The finished-video rule replaces that: source goes to the vault, which is
  actually pushed.

Before removal, all text under `studio/videos/` was harvested into
`compositions/` (in git), and the 4 local commits' unique content — the
soul-of-coffee composition and build script — was confirmed present there.

**Consequence:** treat `studio/` as scratch. Anything in it that matters belongs
in the vault (finished) or `compositions/` (in production).

---

## Day-to-day

```bash
./run.sh                                             # the scraper TUI
/finance-video                                       # topic -> two rendered cuts + packs
tools/archive_cut.py <slug> --hi <url> --en <url>    # retire a finished video
venv/bin/python tools/archive_cut.py --self-check    # verify the archiver
PYTHONPATH=backend venv/bin/python -m pytest backend/tests -q
```

Read `CLAUDE.md` for the layout rules and `vault/CLAUDE.md` before any channel
work — it holds the two-home memory rule and the session protocol.
