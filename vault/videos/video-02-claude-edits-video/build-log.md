---
summary: Build log for Video #2 — COMPLETE & SHIPPED 2026-07-09. Full draft history, the final high-quality render, and the render-ops lessons learned. First channel video taken end-to-end.
updated: 2026-07-09
source: build sessions 2026-07-04 → 2026-07-09 (studio/videos/video-02-claude-edits-video/)
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

- **Draft-5 fixes (2026-07-05) — creator audit-4.** (1) ZOOM OVERFLOW FIX: draft-4's
  zoom clip-path tweened linearly while the required inset is NONLINEAR in scale, so
  zoomed recordings leaked ~50px outside the panel mid-zoom (worst on vo03's
  origin-100% zoom). Fix in build.mjs zoom block: clip follows 24 keyframes sampled
  along the exact eased curve. TWO traps hit: GSAP `power2` = CUBIC not quadratic
  (knots computed with quad ease lagged 50px); and the renderer seeks with
  `tl.seek(t, true)` (suppressEvents) so callback-based fixes (onUpdate) silently
  no-op in final renders — keep zoom sync declarative, never callbacks. Verified
  headless: worst leak 1.56px across all 5 zoom scenes (75 sampled frames), hidden
  under the 10px ring. (2) Real SFX: creator's downloaded Pixabay packs replace the
  ffmpeg-synthesized placeholders — canonical boom/whoosh/whoosh2/pop/shimmer.wav
  re-cut at 48kHz mono, peak −1dB, fade baked (packs kept in library/sfx/<category>/);
  project sfx/ now symlinks to library/sfx; sfx durs bumped (boom 2.5s, whoosh 1.0s,
  pop 0.6s, shimmer 2.0s) and sfx spread across tracks 32–35 to kill overlap.
  (3) Urdu VO experiment: script-v3-urdu.md drafted (50 lines, IDs 1:1 with
  audio_request.json; lines 02/26 adapted for creator's own voice) — awaiting
  creator review before generating anything.

- **Draft-6 (2026-07-06) — creator narration cut (Urdu).** Creator's 47 recorded
  lines (drive-download folder, m4a) replace ALL Kokoro VO: edge-trimmed +
  loudnorm −16 LUFS → `assets/voice-ur/NN.wav` (48kHz mono); audio_meta.json +
  audio_request.json regenerated (captions now Roman-Urdu from script-v3, IDs 1:1).
  Lines 09 (affiliate, removed in script v5), 37, 38 (title-card fix beats —
  creator skipped recording) cut from storyboard. Runtime 9:26 → **12:27** (creator
  reads ~45% longer than Kokoro). Flow-audit fixes: vo02 card "THIS VOICE = AI" →
  "DOCUMENTARY VOICE = AI" and vo26 → "THIS VOICE = MINE / DOC VO = KOKORO" (both
  were false with human narration); vo46 "NO AFFILIATE — STILL." → "100% FREE — NO
  CATCH." (referenced the deleted vo09 card); vo04 chapter promise 9:00 → 8:25;
  orchestra-metaphor chips (CONDUCT/SHEET MUSIC) reworded — metaphor never made it
  into the Urdu script. 6 sub-clips + ex-1907 (vo19 slot → ex-1907-long.mp4) were
  now shorter than their scenes → slowed via setpts to fit (factors 1.17–1.61,
  originals in assets/backup/); zooms retimed (runbook click 6.2→7.2s, pinterest
  settle 5→5.8s); hook icon strikes rescaled to the 18s line-01 read. Verified: all
  21 root videos ≥ scene slots (ffprobe audit), all year/brand/sfx assets present.
  9:38 card vs spoken "9 minute 30" is INTENTIONAL (v2 pattern: spoken approx +
  exact figure on screen; source: cutback.video experiment). ⚠️ S37/38 placeholder
  (title-card before/after) is now fully out of the video — the "shipped bug" gate-2
  item no longer applies. runbook-doc-a at 1.61× slow-mo is the one fit-fix worth
  eyeballing in the draft.

- **Draft-7 (2026-07-06) — VO studio chain + kinetic-type SFX (creator audit-5).**
  (1) CLICK FIX: every VO clip ended with a hard cut (recordings stop right on the
  last word, tail peaks up to −3 dBFS → the "tuck"). All 47 clips reprocessed from
  the original m4a (drive-download folder) through a broadcast VO chain: HPF 80Hz →
  afftdn denoise → compressor 3:1 (de-esser AFTER comp — comp amplifies sibilance) →
  EQ (−2dB @250Hz mud, +2dB @3.8kHz presence, +1.5dB @10.5kHz air) → TWO-PASS linear
  loudnorm −16 LUFS/−1.5 dBTP (single-pass pumps) → 40ms/120ms edge fades (fade-out
  anchored with areverse — container duration ≠ decoded length, st-based fades
  missed). Script: process-vo.sh (project dir); v6 wavs in assets/backup/voice-ur-v1/.
  (2) AUTOTUNE VERDICT (researched): pitch correction is never used on spoken
  narration — it quantizes to a musical scale and sounds robotic on speech; "ideal
  studio Hz" is a myth (male mean F0 ≈ 112Hz is a population stat, not a target).
  Studio sound = the EQ/comp/de-ess/loudness chain above. Applied that instead.
  (3) SFX: tick.wav (cut from humordome soft-ui pop pack, canon spec) fires per
  kinetic word/chip/pipe-span (timed to the GSAP staggers, cap 8/scene), pop per
  polaroid tcard; whoosh 0.12→0.2, card pop 0.16→0.22. 221 SFX total; ticks on own
  track band 36–41 round-robined in TIME order (index rotation collided when
  stagger groups interleaved). Verified: 0 same-track overlaps, all 21 root videos
  still ≥ scene slots after the +44ms/clip duration shift.

- **Draft-8 (2026-07-06) — creator: trim VO tails.** First asked 1.0s, revised to
  **0.5s**: all 47 wavs regenerated from m4a via process-vo.sh, then 0.5s cut off
  each tail (new 120ms fade at the new end). Runtime 12:27 → **12:03**. audio_meta
  regenerated, rebuild, audits clean (videos ≥ slots, 0 sfx overlaps). VO is fully
  regenerable from m4a via process-vo.sh + the atrim step — no extra backup kept.
  RENDERED: `renders/…_2026-07-06_02-54-40.mp4` (227.5 MB, 12:03, 80.7 min render);
  boundary spot-check in the mp4: max sample jump ≤1020/32768 at vo-01/20/47 ends —
  no click.

## ✅ FINAL — SHIPPED (2026-07-09)
Creator called the video complete ("trial test IS the final render"). Rendered a
clean upload master from the current `index.html` (no content changes):
**`renders/FINAL-video-02-claude-edits-video.mp4`** — 472 MB, 1920×1080, h264+aac,
**12:03**, 5.48 Mbps, 57m 20s render (`--quality high`). QA: frame-extracted at
6/200/480/710/721s — hook (artifact panel + Claude glow + Roman-Urdu caption) and
outro (A-Century cross-promo panel + SUBSCRIBE/logo overlay) both render clean; the
outro clip that had failed mid-render is correct. **Cleanup:** all 7 old draft renders
deleted; the project now holds only the source ("final draft") + this one final video.
- **Render-ops lessons paid for here (now in [[../../skills/hyperframes_production]] §6):**
  (1) `--quality high` on a 12-min video overruns FFmpeg's 10-min encode timeout →
  set `PRODUCER_ENABLE_CHUNKED_ENCODE=true` (drafts encode fast, never hit it).
  (2) Renders need lots of scratch disk; orphaned `renders/work-*` dirs (3–4 GB each)
  pile up from killed renders → ENOSPC. Sweep them, but NEVER `rm` one without
  confirming no live render (deleting a running render's frames → ENOENT crash).
  (3) Background a render as a plain harness/`setsid` task — a `nohup`-in-wrapper gets
  reaped and dies early with no error.

## Draft-1 deliberate placeholders — resolved at ship (kept for history) ✅
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
