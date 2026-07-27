---
summary: The production engine — turns a finished script into a rendered HyperFrames video. The HyperFrames contract, the storyboard-as-spec convention, the deliver-and-verify QA loop, the earned design system, and every gotcha distilled from video-02's 8-draft build. Load after long_form_scripting once a script is locked. Canonical (v1, 2026-07-07) — replaces the 2026-07-01 stub.
updated: 2026-07-22
source: distilled from studio/videos/video-02-claude-edits-video/ (8 drafts, 2026-07-04→06) + the HyperFrames contract facts (2026-07-01) + workflow-improvement research (research/workflow-improvement-research-2026-07-07.md) + the Pompeii build (2026-07-13→18: per-line TTS rule, chapter-wise production, music sourcing/mixing)
---

# SKILL — HyperFrames Production (v1)

**Third skill in the pipeline:** business ([[youtube_channel_skill]]) → script ([[long_form_scripting]]) → **production (this skill)**. Load this when a script is locked and it's time to turn it into a rendered video.

**What HyperFrames is:** HeyGen's programmatic HTML/CSS + GSAP → MP4 compositor. You *author* the video as code (a storyboard spec + a generator that emits `index.html`); the renderer captures every frame from headless Chromium. **Deterministic — identical output every run.** It composites the real media you supply (screen recordings, footage, stock, audio); it does not generate media. Apache-2.0, open source. We stay on it (do NOT migrate to Remotion — it's source-available with a paid company license for for-profit teams of 4+; borrow its patterns only).

---

## 0. THE PRODUCTION PIPELINE & GATES (where this fits)

Full stage flow, each stage leaving an **inspectable artifact** so any stage is re-runnable and reviewable on its own (pattern from OpenMontage / MoneyPrinterPlus — see the research note):

| Stage | Artifact | Gate |
|---|---|---|
| research | `research/<slug>/` packet + study note | — |
| script | `script-vN.md` (two-track, delivery-marked) | **① creator reviews script** |
| design | `DESIGN.md` (tokens + motion rules) | — (inherits channel DESIGN) |
| storyboard | `storyboard.mjs` ← from `STORYBOARD.md` | **② creator reviews the storyboard SPEC (cheap) — not a render** |
| voice | `assets/voice-*/NN.wav` + `audio_meta.json` | — |
| build | `index.html` (from `node build.mjs`) | — |
| render | `renders/<slug>_<ts>.mp4` (draft quality first) | **③ qa-render.sh auto-review, THEN creator reviews draft** |
| publish | uploaded video | **④ Gate-2 compliance · ⑤ human approval before publish** |

**The load-bearing lesson from video-02:** we ran 8 draft renders because the creator only had a *rendered video* to react to — there was no cheap spec to approve first. Gate ② (review the `STORYBOARD.md` markdown before building) is where most of those cycles should have died. Always give the creator the cheap artifact to audit before spending a 20–30-minute render.

---

## 1. THE HYPERFRAMES CONTRACT (non-negotiable mechanics)

These are hard rules — break one and the render silently corrupts.

- **Every timed element carries `data-start` / `data-duration` / `data-track-index`.** Two patterns: timeline-driven (a paused GSAP timeline registered on `window.__timelines[id]`) or `class="clip"`. Sub-compositions load via `data-composition-src` on a `<template>`.
- **`<video>` clips must be DIRECT children of the root.** The framework owns their playback; nest a video inside a timed section and it **freezes**. Sections carry only *chrome* (frames, chips, cards) — never the video element itself. (This is why `build.mjs` hoists all videos to root and alternates them across tracks 5/6 so crossfading neighbours don't collide on one track.)
- **Scene chrome stacks ABOVE root videos in DOM order.** So any chrome with a filled background paints over the video area. → **The screen "mat" is a hollow border ring, never a filled box.** (Draft-4's white filled mat rendered every screen recording as a blank white panel. Never give scene chrome a background that covers the video.)
- **Determinism is required:** no `Date.now()`, no `Math.random()`, no network calls at render time. Vary things by index, not randomness. Images need `crossorigin="anonymous"`; fonts `display=block` (or bundled — see §4).
- **Canvas is 1920×1080, 30fps.** Video is `muted`; audio is a separate `<audio>` element.
- **Track bands** (keeps layers from colliding): visuals 0–9 · overlays 10–19 · VO/music 20–29 · SFX 30+. Spread SFX across sub-bands (e.g. 32–35) so same-track sounds never overlap; if you round-robin SFX across tracks, rotate in **time order**, not index order (index rotation collides when stagger groups interleave).
- **Versions drift — pin them** (`hyperframes@0.4.45`, `gsap@3.14.2`) and confirm current syntax via the `/hyperframes` skill. CLI: `dev` / `check` / `render` / `publish`. Docs index: `hyperframes.heygen.com/llms.txt`.

### 1a. The two renderer traps that cost us days (video-02 draft-5)
1. **The renderer seeks with `tl.seek(t, true)` — `suppressEvents = true`.** So GSAP `onUpdate` / callback-based sync **silently no-ops in final renders** (works in preview, breaks in the render). Keep all timeline sync **declarative** — keyframed values, never callbacks.
2. **GSAP `power2` easing is CUBIC, not quadratic.** Knots computed with a quadratic ease lagged ~50px. When you sample an eased curve into keyframes (e.g. a zoom's clip-path inset that must track a nonlinear scale), sample along the *exact* eased curve — clip-path tweened linearly against a nonlinear inset leaks content outside the panel mid-zoom. (Fixed: 24 keyframes sampled on the real eased curve; verified ≤1.6px leak, hidden under the 10px ring.)

---

## 2. THE STORYBOARD-AS-SPEC CONVENTION

**Author the storyboard as a spec, not code first.** Two files:

- **`STORYBOARD.md`** — the human-readable, creator-reviewable spec (Gate ②). One beat per row/block. This is HeyGen's own convention (their launch-video `STORYBOARD.md`) and every serious agentic studio does it. Beat fields:
  `VO cue (line id) · Concept/mood · Visual (what media, what card) · Motion (in GSAP terms: power2.out, back.out, zoom origin) · SFX · Transition · timing`
  Plus a **master timing table** and the global design guardrails up top.
- **`storyboard.mjs`** — the machine spec `build.mjs` consumes. Mirrors the `.md` beats. Video-02's shape (reuse it):
  ```
  Beat: { vo:"01", pre:0.5, pad:0.7, visuals:[V, ...] }   // fracs split a beat
  V shapes:
    { v:"screen",   src, chip?, zoom?, brackets?, frac? }  // 16:9 framed recording (video hoisted to root)
    { v:"phone",    src, chip?, frac? }                     // portrait phone-framed recording
    { v:"artifact", src, chip?, frac? }                     // full-bleed cinematic excerpt
    { v:"image",    src, chip?, ring?, frac? }              // full-bleed still (ring = red flaw ring)
    { v:"card",     html, chip?, anim?, frac? }             // typographic card (anim: fade|pop|slam)
  ```
- **`build.mjs`** turns `storyboard.mjs` + `audio_meta.json` + `audio_request.json` → `index.html`. Iterate: **edit storyboard → `node build.mjs` → `npx hyperframes render . --quality draft`**.

Keep the `.md` and `.mjs` in sync — the `.md` is what the creator signs off; the `.mjs` is what renders. When they drift, the creator is auditing a lie. (See the [[../templates/storyboard-template]].)

---

## 3. THE DELIVER-AND-VERIFY QA LOOP (never trust a render blind)

Every render runs through **`studio/library/scripts/qa-render.sh <render.mp4> <project-dir>`** — the automated post-render self-review (pattern from OpenMontage + the motion-skills deliver-and-verify loop). It checks:
- **ffprobe validation** — duration, resolution, codec sane.
- **Frame extraction at N positions** — pull stills across the timeline; eyeball for black frames, blank panels (the draft-4 white-mat bug), broken overlays. **Trust ffmpeg frame extraction over any puppeteer/preview-harness screenshot** — video `currentTime` seeks race in the harness; extracted frames are ground truth.
- **Audio analysis** — silence detection (a dead VO track) and clipping (peaks > −1 dBTP).
- **Transcribe the finished render's audio** (`ffmpeg -vn` → faster-whisper) and diff the segment start times against the composition's VO `data-start` table. One pass proves the right script *and* the right placement in the actual output — it catches a stale clip, a mis-typed `data-start` and a drifting scene that frame stills cannot. Proven on emergency-fund-en (2026-07-27): all 9 scenes landed within 0.1 s.
- **Structural audits** — every root `<video>` ≥ its scene slot duration (ffprobe each); zero same-track SFX overlaps.

`qa-render.sh` prints a pass/fail report. It runs **before** the creator sees the draft — it catches the mechanical bugs so the creator's attention goes to craft, not to spotting blank panels.

---

## 4. THE DESIGN SYSTEM (earned over 8 drafts — the current grade)

The channel design system lives in **[[../knowledge/design-techtooltester]]** (durable tokens + rules). Per-video, copy those tokens into the project's `DESIGN.md`. Current grade (draft-3→8, ref: creator's SaaSCendx Pinterest boards):

- **Background:** BRIGHT — white/pastel drifting gradient (coral + blue + lavender glows). **No grain, no vignette, no black** (draft-2's grain fogged all content; deleted).
- **Media:** never full-bleed — the **≤60% panel rule**. Screen recordings on white mats with soft blue-tinted shadows; the mat is a **hollow 10px ring** (§1). Cinematic artifact excerpts are the exception — they play full-bleed (the cinematic moments must feel cinematic).
- **Text:** dark ink on light. **Kinetic type everywhere** — every `.big`/`.sub`/`.rail-line` word scales in one-by-one (kSplit → `.kw` spans, GSAP stagger, `back.out`); accent words get a static glow text-shadow; chips split on `·`/`—` and pop individually.
- **Fonts:** Archivo Black (display) + JetBrains Mono (code/labels), loaded from Google Fonts with `display=block` (the local machine lacks them — never rely on a system font stack for display).
- **Motion:** pattern interrupt every 30–45s (stamp, chip snap, artifact cut, zoom). Planned silence after big reveals. Zooms use the keyframed-clip-path technique (§1a) — root videos can't be nested, so a synced clip-path inset keeps the zoom inside the panel.
- **SFX:** real packs (creator's Pixabay downloads in `studio/library/sfx/`), not ffmpeg-synthesized placeholders. Canonical set re-cut to 48kHz mono, peak −1dB, fades baked: boom/whoosh/whoosh2/pop/shimmer/tick. `tick` fires per kinetic word (cap ~8/scene, round-robin in time order); whoosh on media scenes; pop on cards; boom on slams; shimmer on glows.
- **Outro (standing rule):** **every channel video ends with the channel logo + SUBSCRIBE overlay** (logo pop + pulsing pill over the last scene). Brand assets in `studio/library/brand/`.

---

## 5. VOICE — the VO quality chain

Two narration paths (see [[long_form_scripting]] §0 for which is live):

- **Creator-recorded (current, Roman Urdu):** process every clip from the original m4a through the broadcast chain (`process-vo.sh`): HPF 80Hz → afftdn denoise → compressor 3:1 → **de-esser AFTER the compressor** (comp amplifies sibilance) → EQ (−2dB @250Hz mud, +2dB @3.8kHz presence, +1.5dB @10.5kHz air) → **two-pass** linear loudnorm −16 LUFS / −1.5 dBTP (single-pass pumps) → 40ms/120ms edge fades. **Anchor the fade-out with `areverse`** — container duration ≠ decoded length, so start-time-based fades miss the true end. Trim clip tails ~0.5s (recordings end on the last word; the tail peaks up to −3 dBFS → an audible click) then re-fade.
  - **Autotune verdict (researched):** never used on spoken narration — it quantizes to a musical scale and sounds robotic on speech. "Ideal studio Hz" is a myth (male mean F0 ≈ 112Hz is a population stat, not a target). The EQ/comp/de-ess/loudness chain above *is* the studio sound.
- **Kokoro TTS (English, parked default):** `bm_george`. **Do NOT run all lines in one `Promise.all`** — 50 parallel model loads exhaust RAM. Use a serial, resumable `gen-vo.sh` that rebuilds `audio_meta.json`.

### 5a. Word-level caption timestamps (the upgrade — adopt when doing captions next)
Kokoro doesn't emit word timestamps, which is why current captions use proportional chunk timing. Fix:
- **English/TTS:** switch to **Kokoro-FastAPI** ([github.com/remsky/Kokoro-FastAPI](https://github.com/remsky/Kokoro-FastAPI), Apache-2.0) — OpenAI-compatible endpoint that emits **per-word timestamps** and queues requests (also fixes the RAM blowup — `gen-vo.sh` becomes API calls).
- **Creator Urdu VO:** run **faster-whisper forced alignment** on the processed WAVs for word-level Roman-Urdu caption timing. **Test Urdu alignment accuracy hands-on before relying on it.**

**English proven 2026-07-27 (emergency-fund-en).** `faster_whisper` is already
installed on this machine — no download, no service. It gives word-level
timestamps for English straight off an ElevenLabs mp3:

```python
from faster_whisper import WhisperModel
m = WhisperModel("base.en", device="cpu", compute_type="int8")
segs, _ = m.transcribe("assets/voice/en1.mp3", word_timestamps=True)
[(w.start, w.word) for s in segs for w in s.words]
```

Use it whenever a project is **per-scene, not per-line** (§5b is still the rule
for new builds; this is how you retime an existing per-scene project without
rebuilding its audio architecture). Every cue then reads
`scene_start + vo_lead_in + word_time` — the on-screen chip lands on the word
that says it, and the offsets stay readable in the source as
`S.s5 + 6.54  // "FDIC insured"`.

**Do not try to reverse-engineer cue times from `silencedetect`.** Attempted
first on the same job: mapping phrases onto detected gaps holds for a 9-second
read and falls apart on a 20-second one (a comma pause and a sentence pause are
indistinguishable, so phrases silently shift by one gap). Word timestamps cost
one command and are exact.

### 5b. Timeline-by-construction (creator rule 2026-07-18; line granularity hardened 2026-07-22)
Generate VO **one clip per script LINE** — a line = one spoken sentence/clause (~2–8 s of TTS),
**not a paragraph** — so one line = one clip = one scene = one exact timeline anchor. Scene timings
come straight from the clip-duration ledger, never from silence-detection on a monolithic clip.
Join with **tiered gaps** (0.20 s intra-paragraph breath · 0.40 s at a segment boundary · 1.0–3.0 s
only at marked beats — collapse 3 s, hard cut 1.5 s, chapter end 1 s); a flat 0.5 s per line is
wrong at this granularity (details: [[../workflows/voiceover-tts]] Rule 0). **Paragraph granularity
is the trap** (Firaun v1, 2026-07-22): a paragraph → one 1–5 min clip anchored ONCE, so the 3–4
scene images under it split by *guessed weights* and drift off the words (the image/timeline
mismatch). Firaun's 56 paragraphs were re-lined → **307 lines** (`build.py` is now LINE-driven,
old paragraph build kept at `build-v1-paragraph.py`) → 307 clips, 23:05 runtime, timeline correct
by construction. Pompeii's char-weight + `silencedetect` + `FIX_START` relock stack (3 rebuild
rounds) exists only because this rule didn't yet; don't rebuild it.

## 5c. CHAPTER-BY-CHAPTER PRODUCTION (creator rule 2026-07-18 — the standard loop)

**Build, render, and finalize each chapter standalone; assemble the full video only after every
chapter is locked.** Proven on Pompeii (`build.py --chapter N`: own clock from 0, own VO, no
lead-in transition):

1. Build chapter N → draft-render just it (~3–7 min vs ~55 min for the full timeline).
2. Creator proof-watches the chapter → fixes are one number + one cheap re-render. Bugs are
   found and killed per-chapter, not per-20-minute-render.
3. Once ALL chapters are locked → ffmpeg concat (stream-copy, chapter boundaries = hard cuts)
   + music/SFX mix pass (`assemble.py` pattern) → one final-quality render/encode.

Corollaries: design chapter boundaries as hard cuts (a cross-chapter dissolve breaks stream-copy
concat); keep per-chapter VO/audio file mapping 1:1; the full-timeline single build stays useful
only for a final continuity watch.

## 5d. BACKGROUND MUSIC — sourcing + mixing (learned on Pompeii, 2026-07-17)

- **Source that works headless: Incompetech** (Kevin MacLeod) — direct mp3 URLs, CC-BY 4.0,
  needs ONE credit line in the YT description ("Music: Kevin MacLeod (incompetech.com), licensed
  under CC BY 4.0"). **Pixabay is a dead end for agents** (no music API — audio endpoint 403s —
  and the site is Cloudflare-walled). YouTube Audio Library needs the creator's browser.
- Download several candidates per slot; the creator listens and picks (Claude can't hear).
- **Never set bed volume by a flat factor.** A `volume=0.10` guess left the Pompeii bed inaudible
  (~−55 dB). Method: measure each track's mean loudness (`ffmpeg -af volumedetect` / astats),
  gain-stage it to a **~−33 dB bed (~15 dB under VO)**, duck ~−8 dB further under dense VO and to
  silence for planned quiet beats. **Verify by rendering the bed alone to wav (`bed-check.wav`)
  and probing loudness windows** before the full mix.
- Slot music per act, crossfade at act boundaries (~4 s); silence is a valid slot (Pompeii CH10
  Islamic coda runs bare VO by design).

---

## 6. THE PRODUCTION LEARNINGS LEDGER (append here; don't re-learn)

Distilled gotchas — read before building so we don't pay the same tax twice. (New gotchas append here, dated; this is the production analog of [[../knowledge/best-practices]].)

- **2026-07-05** — Renderer `tl.seek(t, true)` suppresses events → `onUpdate` callbacks no-op in renders. Keep sync declarative. (§1a)
- **2026-07-05** — GSAP `power2` is cubic; sample eased curves on the real ease or keyframes lag ~50px. (§1a)
- **2026-07-05** — Scene chrome stacks above root videos; a filled mat paints over the recording. Hollow ring only. (§1)
- **2026-07-04** — Videos nested in a timed section freeze; hoist all `<video>` to root, alternate tracks to allow crossfades. (§1)
- **2026-07-06** — VO fade-out must anchor with `areverse` (container dur ≠ decoded length).
- **2026-07-06** — De-ess AFTER the compressor; two-pass loudnorm (single-pass pumps). (§5)
- **2026-07-04** — Kokoro parallel loads exhaust RAM → serial resumable gen. (§5)
- **2026-07-10** — **The `hyperframes-media` audio engine (`scripts/audio.mjs`) silently fails ALL TTS lines with no HeyGen key** — it calls the CLI with `--provider`, but the published `hyperframes tts` is the Kokoro-only build with NO `--provider` flag → every line reports "TTS failed — omitted", `voices: 0`. Fix: skip the engine, call the CLI per line: `npx hyperframes tts "<text>" --voice bm_george --speed 0.95 --output …`, AND export `HYPERFRAMES_PYTHON=/home/zain-ali/Documents/YT-AGENTS/venv/bin/python3` (has `kokoro-onnx`+`soundfile`; without it the CLI errors "kokoro-onnx not installed"). ffprobe each wav, then hand-place `<audio data-track-index=13>` in index.html with `data-duration ≥` clip length (shorter trims the VO). Proven on soul-of-coffee. (§5)
- **2026-07-02** — Playwright `recordVideo` can't capture smooth in-page scrolling (31/49 frozen frames). Render motion in code or record real screens by hand — never screen-capture a live scroll.
- **Preview harness** (`scratchpad preview.mjs`, puppeteer + `tl.seek` + `video.currentTime`): video frames race — **trust ffmpeg frame extraction over harness screenshots** every time. Needs `executablePath /usr/bin/google-chrome`; poll for `__timelines` rather than `waitForFunction`.
- **2026-07-09** — **`--quality high` on a 12-min video hits the 10-min FFmpeg encode timeout** (libx264 encodes at ~0.48× realtime → ~25 min needed). The render captures all frames, then dies at "Encoding video". Fix: `PRODUCER_ENABLE_CHUNKED_ENCODE=true` (encodes in segments, no single-process timeout) and/or `FFMPEG_ENCODE_TIMEOUT_MS=2400000`. Draft renders (`--quality draft`) encode fast and never hit this. Set these env vars for every high-quality final of a long video.
- **2026-07-09** — **Renders need lots of scratch disk and orphaned `renders/work-*` temp dirs pile up.** A killed/failed render leaves its `work-*` dir (3–4 GB of extracted+captured frames) behind; two of them filled a 234 GB disk and the next render died with **ENOSPC** at 56%. Sweep stale `renders/work-*` before a big render — but **NEVER `rm` a `work-*` dir without confirming no render is live** (a running render keeps `compiled/__hyperframes_video_frames/`; deleting it mid-run kills the render with ENOENT). Confirm liveness by the real process name (`node .../hyperframes` / `npm exec`, NOT a `pgrep "hyperframes render"` which misses them).
- **2026-07-09** — **Background a render as a plain harness task** (or fully detach with `setsid` + a done-marker). A `nohup … &` wrapped inside a short-lived shell gets reaped when the wrapper's process group is cleaned → the render dies early with no error in its log.
- **2026-07-18** — **Per-line TTS + join pauses = timeline by construction** (§5b); never regenerate Pompeii's silencedetect/char-weight relock stack.
- **2026-07-22** — **A "line" is one spoken sentence/clause (~2–8s), NOT a paragraph** (§5b). Firaun v1's 56 paragraphs each became one 1–5 min clip anchored once → the 3–4 scenes under it drifted off the words (image/timeline mismatch). Re-lined → 307 lines = 307 clips = 307 exact anchors (23:05); `build.py` now LINE-driven (`build-v1-paragraph.py` kept). Join with TIERED gaps (0.20/0.40/1.0–3.0s), not a flat 0.5s. Re-lining: SLICE the source, never retype (retyping swaps Urdu↔Devanagari scripts); gate with a byte-for-byte reconstruction check.
- **2026-07-18** — **Chapter-by-chapter build→proof→re-render; concat locked chapters at the end** (§5c). A per-chapter fix is minutes; a full-timeline fix was ~55 min + a 20-min proof-watch.
- **2026-07-17** — **Music: Incompetech works headless (CC-BY, credit line required); Pixabay is agent-hostile; gain-stage the bed from measured loudness (~−33 dB, ~15 dB under VO) and verify with a rendered bed-check.wav** — a flat volume guess shipped an inaudible bed (§5d).
- **2026-07-16** — **Vendor gsap locally** (`assets/gsap.min.js`) — the CDN is unreachable in the render env; a CDN `<script>` = blank frames.
- **2026-07-19** — **`<html dir="rtl">` renders a FULLY BLACK video** (previews fine — a silent failure `hyperframes lint` catches as a hard error). For Urdu/Arabic compositions keep `lang` on `<html>` and scope `direction:rtl` to the text elements; the browser's bidi algorithm shapes them correctly anyway. **Run `lint` before the first render of any RTL composition** — this one is invisible until you watch the output.
- **2026-07-19** — **Word-by-word kinetic type needs the space INSIDE the span.** `<span class="kw">` is `inline-block`, which swallows the whitespace between spans, so Nastaliq words butt together. Emit `word&nbsp;` inside each span. (Joining itself is safe — the split is per *word*, never per letter.)
- **2026-07-19** — **Kill baked-in letterbox/pillarbox bars with a measured static crop on the `<img>`, before the Ken Burns move animates the `.photo` wrapper** — otherwise the bars ride into frame mid-push. Measure, don't guess: `ffmpeg -loop 1 -i x.jpg -vf cropdetect=24:2:0 -frames:v 3 -f null -` → `scale = max(Sw/W, Sh/H)`, `translate = (Sw/2 − (X+W/2), Sh/2 − (Y+H/2))` as a % of the master. Firaun's four: P30a 1.048 · P35b 1.180/+5.47% · P11b 1.255 · P37b 1.193/+3.78%.
- **2026-07-19** — **An era/grade filter can repair an image-audit defect for free.** Firaun's P46b was flagged "in COLOUR but must be 1976 B&W"; the chapter's `grayscale(1)` newsreel grade fixed it in-comp — no re-generation. Check the grade before adding anything to a re-gen worklist.
- **2026-07-19** — **A card carrying an inline cite must NOT also get the corner cite chip** (it renders twice), and a progressive overlay (the 9-signs tally) must arrive **with its first mark**, not at chapter start — an empty frame held for 16 s reads as a broken overlay.
- **2026-07-27** — **Per-scene VO? Get word timestamps, don't guess.** `faster_whisper` (already installed) → `word_timestamps=True` → every cue is `scene_start + 0.4 lead-in + word_time`. `silencedetect` phrase-mapping breaks past ~10 s of speech. (§5a)
- **2026-07-27** — **Verify a render by transcribing its own audio**, not just by eyeballing frames — it proves script *and* placement in one pass. (§3)
- **2026-07-27** — **A swapped stock photo breaks the grade.** The dollar-bill shots that replaced the foreign-coin ones were far brighter than the other 7 photos and made two scenes read as a different video, even under the shared `.bg` filter. Match brightness per image (inline `filter:` override), and re-shoot the contact sheet after any photo swap. Same class of bug as a baked-in letterbox: the asset changed, the grade didn't.
- **2026-07-27** — **`hyperframes check` contrast warnings on rotated stamps over photos are usually false positives** (`#s5stamp 1.52:1` on dark ink over a solid green pill). Extract the frame at the reported timestamp and look before "fixing" it — the fix would have made a legible element worse.
- **2026-07-18** — **Thumbnails are built in the video's own design system, not clickbait grammar** — HTML/CSS + headless Chrome screenshot recipe + the style rule live in [[../knowledge/design-cinematic-history]] → Thumbnails (creator rejected 4 AI-collage/red-box variants first).

---

## 7. COMPLIANCE (Gate 2) — the production checklist

- Music only from the YouTube Audio Library, Incompetech (CC-BY — the credit line in the description is MANDATORY, see §5d), or a cleared pack. BGM ducked ~−18dB under VO, out entirely through the "where it breaks" silences.
- Altered-content toggle = YES only if the final cut contains realistic synthetic media presented as real (AI narration as the *disclosed premise* is fine; human VO alone does not trigger it).
- Every "I tested / I tried" claim is really backed by the footage — the [[long_form_scripting]] integrity rule carries into the edit.
- `qa-render.sh` passed; deliberate placeholders (§ build-log) are all made real before publish.
