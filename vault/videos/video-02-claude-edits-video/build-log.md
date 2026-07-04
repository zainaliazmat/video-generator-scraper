---
summary: Build log for Video #2 — what draft-1 contains, which placeholders MUST become real before publish (Gate-2 "I tested" integrity), and how to iterate.
updated: 2026-07-05
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
- **Draft-1 RENDERED (2026-07-04):** all 50/50 VO lines done (gen-vo.sh resumed at
  line 46), build.mjs → 55 scenes / 9:26, draft render (32.5 min) →
  `renders/video-02-claude-edits-video_2026-07-04_22-29-27.mp4` (128 MB).
- **Draft-2 (2026-07-05) — creator audit-1 applied.** New design system in build.mjs:
  living gradient bg (drifting glows + dot grid + grain.png borrowed from
  soul-of-coffee) replaces flat black; ALL media now ≤60% panels (never full-bleed);
  kinetic left text-rail on screen/phone scenes (chip text, staggered); burned-in
  captions from the 50 VO lines (255 chunks, ≤6 words, proportional timing — no
  word-level stamps, Kokoro doesn't emit them); whoosh/pop SFX per scene (synthesized
  in assets/sfx/ via ffmpeg); hook = artifact panel left + animated Claude/Pr/DaVinci
  icon tiles (strike-through on Pr+DaVinci, glow on Claude); phone scene gets CSS
  bezel+notch. Clip fixes: OBS window trimmed off heads of clip-05 (2.0s) + clip-02
  (1.2s) (flashed at 2:06/3:18 of draft-1; originals in assets/backup/);
  runbook-scroll wander cut — new sub/runbook-click.mp4 (8.5–26.5s: settle→click→doc
  opens) + doc-a/b/c distinct ranges for S06/S16/S17 (fixes the replay-from-0 reuse);
  animated zooms into the runbook doc + the Pinterest reference player (GSAP scale
  with synced clip-path inset — root-level videos can't be nested, so clip-path keeps
  the zoom inside the panel; formula in build.mjs zoom block) + bracket highlights.
  Preview harness: scratchpad preview.mjs (puppeteer + tl.seek + video.currentTime;
  NOTE: video seeks race — trust ffmpeg frame extraction over harness screenshots).
- VO: 50 Kokoro lines (bm_george). Gotchas hit + fixed: `kokoro-onnx` python pkg
  was missing (installed vs SYSTEM python — the shell's venv shadows it); the shared
  audio engine runs all lines in `Promise.all` → 50 parallel model loads exhausted
  RAM → wrote `gen-vo.sh` (serial, resumable, rebuilds audio_meta.json).

- **Draft-3 (2026-07-05) — creator audit-2 applied.** Style pivot to the creator's
  Pinterest references (SaasCendx, in `studio/library/reference/pinterest/`): BRIGHT
  white/pastel gradient bg (coral+blue+lavender drifting glows), grain overlay and
  dark vignette DELETED (draft-2's grain was fogging all content), media on white
  mats with soft blue-tinted shadows, dark ink text. Kinetic type everywhere: every
  .big/.sub/.rail-line word scales in one by one (kSplit → .kw spans, GSAP stagger,
  back.out), accent words get static glow text-shadow, chips split on "·" and pop
  individually, pipe/years chips stagger as units. Webfonts (Archivo Black +
  JetBrains Mono) now loaded from Google Fonts — local machine doesn't have them.
  SFX remapped: whoosh (2 alternating variants) only on media scenes, pop on cards,
  boom on slam, shimmer on Claude-glow; all ffmpeg-synthesized — creator to supply
  downloaded packs (see asset request list in session notes). Preview harness lives
  at scratchpad preview.mjs (needs executablePath /usr/bin/google-chrome; poll for
  __timelines instead of waitForFunction; video frames still race — trust ffmpeg).
- **Central asset library (2026-07-05):** `studio/library/` — reference/, sfx/,
  textures/, music/, projects/. `library data/` (repo root) moved into
  reference/pinterest/. Idle projects' assets moved to library/projects/<name>
  with symlinks back at videos/<name>/assets; video-02's assets follow after its
  render finishes. Gitignored in the studio repo. Rules in library/README.md.

- **Draft-4 (2026-07-05) — creator audit-3 applied.** (1) CRITICAL FIX: draft-3's white
  screen-mat was a filled box that painted OVER the root-level videos (scene chrome
  stacks above videos in DOM order) → every screen recording rendered as a blank
  white panel. Mat is now a hollow 10px white border ring — never give scene chrome
  a background that covers the video area. (2) vo21 years card → animated polaroid
  timeline: 6 era stills from a-century-of-travel pop in over their years one by one,
  then float. (3) Channel brand assets in `studio/library/brand/` (techtooltester +
  historyframesfilm logos/banners); **standing rule: every channel video ends with
  the channel logo + SUBSCRIBE overlay** (outro block in build.mjs, logo pop + pulsing
  pill over the last scene).

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
