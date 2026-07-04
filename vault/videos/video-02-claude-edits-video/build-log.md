---
summary: Build log for Video #2 — what draft-1 contains, which placeholders MUST become real before publish (Gate-2 "I tested" integrity), and how to iterate.
updated: 2026-07-04
source: the build session 2026-07-04 (studio/videos/video-02-claude-edits-video/)
---

# Video #2 — build log

**Where things live:** `studio/videos/video-02-claude-edits-video/` (symlink from this
repo → ClaudeHyperFrame; the projects stay separate, navigation is unified).
Composition = `storyboard.mjs` (beats) + `build.mjs` (generator) → `index.html`.
Iterate: edit storyboard → `node build.mjs` → `npx hyperframes render . --quality draft`.

## Pipeline state (2026-07-04)
- 7 OBS clips delivered → trimmed (3s off each end; clip-03 phone kept whole) →
  `assets/clips-trimmed/` + purpose-cut `assets/sub/` (pinterest, runbook-scroll,
  prompt-typing, scene-written, kokoro-gen).
- Century excerpts cut from the 1080p master → `assets/excerpts/` (title / 1907 /
  1970 / outro / flawed-title-card.png).
- VO: 50 Kokoro lines (bm_george). Gotchas hit + fixed: `kokoro-onnx` python pkg
  was missing (installed vs SYSTEM python — the shell's venv shadows it); the shared
  audio engine runs all lines in `Promise.all` → 50 parallel model loads exhausted
  RAM → wrote `gen-vo.sh` (serial, resumable, rebuilds audio_meta.json).

## Draft-1 deliberate placeholders — MUST become real before publish ⚠️
1. **S35 bot-scroll clip** — draft shows a text card. Final: cut the real frozen-scroll
   capture from the 2026-07-02 Playwright test (or re-run it and record).
2. **S37–38 title-card fix** — draft shows the flawed frame + a "FIXED" card. Final:
   actually fix the century title-card overlap, re-render that scene, show real
   before/after. ("I tested" integrity — the fix must really happen.)
3. **S27 disclosure toggle** — creator skipped clip-08; draft uses a designed quote
   card. Acceptable for final too (the claim is about OUR upload behavior), but the
   toggle must genuinely be set on upload day.
4. **No BGM in draft-1** — final adds a YT Audio Library track (ducked −18dB, silent
   through the WHERE-IT-BREAKS beats). Creator downloads the track (license-safe).
5. **clip-09/clip-10 never recorded** — S38 uses prompt-typing sub-clip; S23 uses a
   card. Optional to record later; not blocking.

## Known rough edges to review on draft-1
- runbook-scroll.mp4 reused across S03/S06/S16/S17 (replays from 0 each time) — fine
  if it reads okay; else cut distinct sub-ranges.
- clip-04 blind sub-cuts (0–25s typing, 488–516s result) — verify they show what the
  beats claim; adjust ranges in ffmpeg + rebuild.
- Kokoro pronunciation of "HyperFrames", "Mauretania", "DaVinci" — audition lines
  02/10/29; respell in audio_request.json + regenerate single lines if garbled.
