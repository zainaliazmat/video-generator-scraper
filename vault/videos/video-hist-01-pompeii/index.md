---
summary: Pompeii Ka Akhri Din (Roman-Urdu history video, 19:56) — ✅ **LIVE on @historyframesfilm 2026-07-31** as "Pompeii City History in Urdu Hindi — The Last Day of the Lost City" (youtu.be/XaIuExXBW9Q); source archived to `src/`, studio dir deleted. Learnings distilled to skills/workflows (per-line TTS rule, chapter-wise production, music sourcing).
updated: 2026-07-31
source: HyperFrames build, archived to `src/` in this folder 2026-07-31
---

# Pompeii Ka Akhri Din — build status

Roman-Urdu faceless history video, ~21 min target. Built in the local HyperFrames
studio. Design/script/storyboard notes in this folder; the buildable copies
(index.html, frame.md, design.md, storyboard.md, build.py, assemble.py) live in
`src/`.

## How the film is assembled — `build.py` (source of truth)
The full composition is **generated**, not hand-written. `src/build.py`
holds the entire EDL (104 scenes) + ~23 card/overlay fragments and emits a static,
deterministic `index.html`. Re-run `python3 build.py` after editing the EDL. Reuses the
Hook's proven determinism contract (one paused gsap timeline on `window.__timelines["main"]`,
transform/opacity only).

### VO sync = SEGMENT-level (build.py `# --- VO RELOCK` block)
build.py no longer trusts frame.md's guessed scene durs. For each chapter it: (1) predicts
where each **script segment**'s narration ends from its Roman-Urdu char length (`WEIGHTS`,
frozen from [[script-v1-urdu]]); (2) **snaps that boundary to a real silence pause** detected
in the actual VO clip via `ffmpeg silencedetect` — so dramatic `[pause]`/`[long pause]` beats
are honoured; (3) splits each segment's audio span across its scenes by their frame.md ratios.
A per-scene `SEG` list maps scene→segment (hand-verified vs storyboard; CH7/8/10 callbacks +
the collapsed CH6–10 blocks reconciled). Chapter spans still equal their VO clip length exactly
(each scene's `dur` = its wall-clock share **+ its trailing dissolve**), so the 10 VO clips stay
back-to-back. `MIN_SPAN["23"]` holds the blast interrupt (char-count can't see its silent beat).
This replaced the old chapter-granular relock that only locked chapter *starts* and let scenes
drift against the voice inside a chapter (the "visuals lag the voice" bug the creator flagged
2026-07-17). Future upgrade if any beat still drifts: `hyperframes transcribe` gives word-level
timestamps for true forced alignment.

## Scripts
- [[script-v1-urdu]] — **canonical** Roman-Urdu VO (approved, has fact-check table + loop ledger).
- [[script-v1-nastaliq]] — one-off Nastaliq (Noto Nastaliq Urdu) rendering of the VO for
  on-screen/read-aloud in Urdu script (creator req 2026-07-14). Roman stays canonical.

## Milestones
- **2026-07-14 — Hook (CH1) rendered, silent draft-1.** 14 scenes, 50.0s.
  Render: `studio/videos/pompeii-ka-akhri-din/pompeii-hook-draft-1080p.mp4`.
- **2026-07-14 — FULL 10-chapter silent visual draft assembled.** All 104 scenes
  (CH1–CH10) + 23 motion-graphic cards. **10:38.0** @ 1920×1080 30fps (~19,140 frames).
  Warm colour cinematic recon; evidence layer desaturated+cool; parchment/dark cards;
  timestamp-chip spine (`6:00 AM`→…→`APR 2026`, hidden across the 1700-year gap + ibrah);
  3 pattern interrupts (blast BLK, pre-dawn silence BLK, DNA reveal BLK) + white-wash
  peak. `hyperframes check` = **0 errors, 8/8 WCAG-AA**. Render:
  `studio/videos/pompeii-ka-akhri-din/pompeii-full-draft-1080p.mp4`.
- **2026-07-16 — VO Ch6–10 generated (Pipeline B) → FIRST DRAFT WITH AUDIO.** All five
  remaining chapters (segs 31–65) transliterated to Devanagari + inline-Urdu z/f/q words +
  v3 emotion tags, generated on `eleven_v3` (Vikram S, seed 42); CH10 Islamic coda
  theology-verified vs [[religious-dimension]]. Engine text logged in [[script-v1-devanagari-tts]].
  All 10 clips copied to `assets/audio/`; **total VO 19:55**. `build.py` extended to
  ffprobe-measure each clip and **relock** each chapter's scene durs so its span == its VO
  length (chapter cuts land on VO starts); emits 10 VO `<audio>` + a self-made low **drone
  bed** (ducked to silence for the pre-dawn hush) as `#root` children; **gsap vendored
  locally** (`assets/gsap.min.js`) because the CDN is unreachable in the render env.
  `hyperframes lint` = **0 errors** (7 pre-existing warnings). Rendered 1920×1080 30fps
  (draft quality, 35,873 frames, ~55 min wall-clock) →
  `studio/videos/pompeii-ka-akhri-din/pompeii-full-draft-v2-audio-1080p.mp4`
  (**665 MB · 19:55.8 · h264 + AAC stereo**). Spot-checked: audio is real speech across all
  10 chapters (mean −19…−21 dB); frames render clean at hook/Ch6/Ch10-ibrah(18+ redaction)/outro;
  timestamp chips + cards intact.
- **2026-07-17 — SEGMENT-LEVEL VO SYNC (fix: visuals lagged the voice).** Creator watched the
  v2 draft and flagged that the voice ran ahead of the visuals from the hook onward (e.g. hook
  line 1 is 0:00–0:07 of speech but its visuals held to ~0:11). Root cause: the v2 relock only
  locked each *chapter's* span to its VO; inside a chapter, scene durs were frame.md guesses scaled
  proportionally, so they drifted off the narration. Rewrote the `build.py` relock to sync at
  **segment** granularity — predict each segment's end from its Roman-Urdu char length, snap to a
  real silence pause in the VO (`ffmpeg silencedetect`), split each segment's span across its scenes
  by frame.md ratios (see the build.py section above). Hook seg-02 visual now starts at **6.8s** (was
  ~11s). Chapter spans unchanged (all 10 within ±4 ms of their VO clip), total still 19:55.8;
  `hyperframes lint` = 0 errors (same 7 warnings). Re-rendered 1080p/30fps draft →
  `pompeii-full-draft-v3-synced-1080p.mp4`. **Still owed: a human proof-WATCH** (Claude can't hear
  audio, so sync is verified by construction — boundaries sit on real audio pauses — not by ear).

- **2026-07-17 — FINAL ASSEMBLED: `pompeii-ka-akhri-din-FINAL-1080p.mp4`** (736 MB · 19:56 ·
  h264+AAC · faststart). `assemble.py` (in the studio dir, re-runnable) concats the 10 chapter
  renders (stream-copy) and mixes the music bed: CH1–4 Teller of the Tales →4s xfade→ Virtutes
  Instrumenti · CH5–7 Long Note Two (ducked to −91 dB during the pre-dawn hush) · CH8–9
  Promises to Keep · CH10 silence (Islamic coda). Each track gain-staged from its measured
  mean loudness to a −33 dB bed (~15 dB under VO) — a flat volume=0.10 had left the bed
  inaudible (~−55 dB), caught by rendering the bed to `bed-check.wav` and probing windows.
  Tafsir-verify reminder removed from C-61b (CH10 re-rendered, frame-verified clean).

- **2026-07-18 — THUMBNAIL FINAL + YT metadata.** Creator rejected the v1–v4 clickbait style
  (red box / outline sans); rebuilt in the video's own design system (Playfair + ember kicker,
  rule now in [[../../knowledge/design-cinematic-history]] → Thumbnails). Final:
  `thumbnails/THUMBNAIL-pompeii-last-morning.png` (creator-picked base image, kept in
  `Pompie Assets/pompeii-thumb-base-man.jpeg`); all other variants deleted. Titles /
  description (real ffprobe'd chapter timestamps) / tags: [[youtube-metadata]].

- **2026-07-18 — ✅ VIDEO FINALIZED (creator sign-off) + cleanup + learnings distilled.**
  Creator declared the video complete. Kept: `pompeii-ka-akhri-din-FINAL-1080p.mp4`
  (verified h264+AAC, 19:56, 736 MB), the final thumbnail, all text/source (build.py,
  assemble.py, index.html, VO audio, scene assets). Deleted the 15 other renders
  (~3.9 GB: hook draft, 3 full drafts, joined-nomusic, ch1–10 chapter renders).
  **Learnings promoted out of this project:**
  - Per-line TTS + ≥0.5 s join pauses → timeline by construction (creator rule) →
    [[../../workflows/voiceover-tts]] Rule 0.
  - Chapter-by-chapter build→proof→re-render→concat workflow (creator rule) →
    [[../../skills/hyperframes_production]] §5c.
  - Music sourcing (Incompetech yes / Pixabay dead end) + measured gain-staging with
    bed-check verification → [[../../skills/hyperframes_production]] §5d.
  - Thumbnail style scoping (energy in the image, type in the design system) →
    [[../../knowledge/design-cinematic-history]] Thumbnails + [[../../knowledge/best-practices]].
  - Title/tag research method (autocomplete + competitor scrape) →
    [[../../knowledge/best-practices]] Packaging; data in [[youtube-metadata]].

## Pending / notes for final
*(2026-07-18: video FINALIZED by creator — items below are closed by sign-off except where marked
OPEN. Chapter renders are deleted; a re-fix now means re-rendering from build.py.)*
- **OPEN — upload to YouTube** with [[youtube-metadata]] (title/desc/tags/thumbnail ready);
  record URL + publish date here, then run the post-delivery cleanup protocol (vault CLAUDE.md)
  for the remaining heavy assets (VO audio, scene images, snapshots).
- **OPEN — CC-BY music credit line** must ship in the description (already baked into
  [[youtube-metadata]]); evidence-still credits per `CREDITS-evidence.md` if required.
- **Timeline review → chapter-by-chapter rebuild (2026-07-17).** Creator proof-watched v3,
  fixed CH1's segment times directly in [[timeline-v3]] (segs 02–07 → 7.0/14.5/25.5/37.5/49.0/61.5s).
  build.py now: (a) `FIX_START` — creator-locked boundaries override predict+snap; (b)
  `--chapter N` builds one chapter standalone (clock from 0, own VO clip, no lead-in transition).
  **ALL 10 chapters rendered on the creator-fixed timeline** (draft quality, h264+AAC 1080p30):
  `pompeii-ch{1..10}-fixed-timeline-1080p.mp4`, total 19:55.9 — sums to the full VO. FIX_START
  now locks every segment boundary in all chapters (creator's global v3-draft timestamps
  converted to chapter-local audio offsets; the doc's CH3/CH9 chapter-head rows had chained
  drift and were ignored — flagged to creator, esp. CH9 seg 55 @ 18.5s local). Next: creator
  proof-watches the 10 chapter drafts → any per-chapter re-fix is one FIX_START number + a
  ~3-7 min re-render of just that chapter → final join by ffmpeg concat (chapter boundaries
  are hard cuts) + SFX pass + final-quality render.
- **Proof-listen owed (human/ear pass)** — the VO text is correct *by construction* (Pipeline B),
  but no one has audibly checked z/f/q/gh/kh words or the CH10 Islamic terms. Claude cannot hear
  audio; a listen pass + short re-gen of any mispronounced chapter is the next step before ship.
- **Background music: 6 candidates downloaded (2026-07-17)** in `assets/audio/music-candidates/`
  from Incompetech (Kevin MacLeod, **CC-BY 4.0 — needs one credit line in the YT description**:
  "Music: Kevin MacLeod (incompetech.com), licensed under CC BY 4.0"). Slots: CH1–4 Teller of the
  Tales / Virtutes Instrumenti · CH5–7 Stay the Course / Long Note Two · CH8–9 Promises to Keep /
  Despair and Triumph · CH10 no music (Islamic coda — drone fades, VO bare). Creator listens,
  picks one per slot → wire as `<audio>` elements in build.py (vol ~0.08, duck for silence beats)
  + re-render. (Pixabay was abandoned: no music API — audio endpoint 403s — and the site is
  Cloudflare-walled against scraping.)
- **Rich SFX deferred** — draft ships with VO + a self-made ambient drone bed only. The design's
  distinct hits (blast, roof-collapse, pyroclastic roar, pumice patter) need cleared library SFX
  (YouTube Audio Library / Pixabay) — a download+mix pass that needs the creator. The two big
  pattern-interrupt silences are honoured (VO has baked `[long pause]`s; drone ducks to 0 at s65).
- **Ch1–3 VO are pre-B renders** (kept as-is by creator decision) — they still read z-words in
  Devanagari; a back-fix to Pipeline B is optional polish, not a blocker.
- **Before ship:** remove the on-screen "⚠ verse wording — tafsir-verify" reminder on
  card C-61b (kept in the draft on purpose so the creator verifies C-61b/C-61c wording
  vs an authoritative Urdu tafsir per the Islamic-POV rule); credit + rights-check the
  press evidence stills (EV-54A/56A/60A/61A) per `CREDITS-evidence.md`.
- **Known cosmetic nits (draft-acceptable):** the C-08/C-38 maps are stylised label
  cards, not relief maps; one big single-file composition trips HyperFrames' file-size /
  track-density style warnings (could split into per-chapter sub-comps later).

## Published + archived (2026-07-31)

**State: LIVE on YouTube · source archived · studio dir deleted.**

| Cut | Channel | URL | Thumbnail |
|---|---|---|---|
| single (Roman-Urdu) | @historyframesfilm | https://youtu.be/XaIuExXBW9Q | `src/THUMBNAIL-pompeii-last-morning.png` |

Shipped title: **"Pompeii City History in Urdu Hindi — The Last Day of the Lost City"**.
**It shipped on channel B, not on the pending Urdu channel C** — the Urdu-first history
lane that [[../../knowledge/channels]] §C describes never got its own channel, so the
Urdu cut went out on HistoryFramesFilm alongside the English «A Century of Travel».

**Source: `src/`** — `build.py` (the generator that IS the film: 104-scene EDL + the VO
relock), `assemble.py`, `index.html` (its 1.4 MB output), `frame.md`, `design.md`,
`storyboard.md`, `INDEX.md`, `CREDITS-evidence.md`, `concat-list.txt` and the shipped
thumbnail. `studio/videos/pompeii-ka-akhri-din` and its `compositions/` text mirror are
**deleted** per the finished-video rule ([[../../CLAUDE]]).

**Re-render is not free:** the 736 MB master, the 10 chapter VO clips, the ambient drone
bed and every scene image are gone — `assets` was a symlink into `studio/library/projects/`,
which no longer exists. `build.py` + the storyboard + [[image-prompts]] are what a rebuild
starts from, and it re-pays the TTS and the image generations.

Still owed: the CC-BY music credit line in the YouTube description (Kevin MacLeod /
incompetech, if a music slot shipped) · analytics after 28 days.
