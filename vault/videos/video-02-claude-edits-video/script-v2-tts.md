---
summary: Script v2 — FULL TTS EDITION (Kokoro narrates; creator records zero voice). VO split into numbered segments mapping 1:1 to the project's audio_request.json lines; visuals/pacing carry the energy. Supersedes v1's human-VO delivery.
updated: 2026-07-04
source: v1 + creator decision 2026-07-04 (narration = Kokoro for now; own-voice rule PARKED, not deleted)
---

# VIDEO #2 — "Claude Code Just Edited This Entire Video" — v2 (TTS)

> Target ~15:00 · VO ≈1,800 words in ~46 Kokoro segments (voice: bm_george, speed 0.9 — audition alternates at build) ·
> Creator records ONLY screen clips per [[recording-guide]] — no voice, ever.
> **The twist that makes TTS a strength:** this video about AI-made video is itself fully AI-narrated — and says so in the first 40 seconds. Full self-demonstration; disclosure = the hook, not a liability.

## TTS PACING RULES (replaces the human-delivery system for this video)
- Segments are short (8–16s). The EDIT breathes between them — never wall-to-wall narration.
- Visual pattern interrupt at least every 30–45s (zoom, stamp, verdict card, cut to artifact) — visuals do the vocal-variety job a human voice would.
- Music bed (YT Audio Library, ducked under VO) + planned SILENCE beats: after S14 (the render reveal), after S31 ("stop."), on the verdict card.
- Captions ON (auto or styled) — TTS + captions measurably helps ESL viewers; fits our audience.
- Numbers/names are written the way Kokoro should SAY them. Audition "HyperFrames" first — if garbled, respell as "Hyper Frames" in the lines.
- Gate 2: the altered-content toggle gets set to YES for this video (AI narration presented as narration — we disclose proudly; it's the premise).

## 1. TITLE (unchanged from v1 — study-validated)
★ **Claude Code Just Edited This Entire Video — No Editor, No Timeline (Honest Review)**
(alternates in v1 §1; A/B per v1 §2 thumbnails.)

## 2. THE SCRIPT — numbered VO segments + screen cues
*(Each `S##` becomes one `lines[]` entry in audio_request.json, id = the number.)*

### HOOK — 0:00–0:40
**S01** — "Every frame of the video you are watching was edited by Claude. Not a human. Not Premiere. Not DaVinci. There is no timeline at all — just a text file, and one command."
**[SCREEN]** cold open ON the artifact: 1907 liner scene full-bleed → 1970 Pan-Am 747 scene → smash cut to bare terminal running the render command.
**S02** — "And one more thing. This voice — the one talking to you right now — is not human either. It is a free, open-source AI voice. This entire video is the demo."
**[SCREEN]** waveform overlay pulses with the words "THIS VOICE = AI · FREE" stamped in the video's Archivo style.
**S03** — "By the end, you will have the exact workflow. It is free, and open source. But there is one thing it still cannot do — and nobody making these videos is honest about it. Stay for that."
**[SCREEN]** back to "A Century of Travel" title card; small "8:20" tease chip on "stay for that".

### THE ANSWER, FAST — 0:40–1:45
**S04** — "Here is the whole thing in thirty seconds. I wrote a short brief. Claude Code turned it into a design system, a researched script, and a narrated voiceover."
**[SCREEN]** 5-step montage begins: brief doc → DESIGN.md → script page → waveforms.
**S05** — "Then it wrote every scene of the video as code. H T M L files — the same stuff websites are made of. One render command later, I had a four minute cinematic history documentary, in full ten-eighty P."
**[SCREEN]** scene file → render progress bar → finished frame; "4:00 · 1080p" stat card.
**S06** — "In the next few minutes: the tool, and why it is free. The five step build. The parts that genuinely shocked me. And around the eight minute mark — the part where it breaks. Because you need to know that before you waste a weekend."
**[SCREEN]** roadmap strip with 4 chips lighting up in turn (Simon's roadmap pattern).
**S07** — "And no — there is no affiliate link here. There is not even an affiliate program. Nobody is paying me to say any of this."
**[SCREEN]** "FREE · OPEN SOURCE (Apache 2.0) · NO AFFILIATE EXISTS" card; beat of silence after.

### WHAT THIS ACTUALLY IS — 1:45–3:10
**S08** — "The tool is called HyperFrames. HeyGen open-sourced it in April."
**[SCREEN]** GitHub repo page (recorded clip), star count visible.
**S09** — "Think of it like this. A normal video editor is a live orchestra. You conduct every cut by hand, in real time, on a timeline."
**[SCREEN]** the cluttered-timeline clip (clip-03), chaotic zoom.
**S10** — "HyperFrames is sheet music. You write the score once — this scene starts here, lasts this long, drifts left, fades out — and the renderer plays it perfectly, every single time."
**[SCREEN]** clean scene file beside the rendered scene; `data-start` / `data-duration` highlighted as the words land.
**S11** — "Where the comparison breaks: you do not hear the music while you write it. You preview, adjust, and re-render."
**[SCREEN]** quick preview-reload loop.
**S12** — "And here is why that matters for Claude. Claude cannot drag a playhead. But it is extremely good at writing structured text. Scenes as text turns video editing into something an A I is naturally good at."
**[SCREEN]** split: playhead dragging (dimmed, ✗) vs text streaming into a file (✓).

### THE BUILD — 3:10–8:20 *(each step ends on a mini verdict card)*

**STEP 1 — the brief (3:10–3:55)**
**S13** — "I gave Claude one paragraph. A cinematic, vintage parallax slideshow, telling the history of travel, decade by decade. That is it."
**[SCREEN]** clip-01: the brief being pasted into Claude Code, response streaming.
**S14** — "From that one paragraph it proposed the angle — the journey itself was once the destination — and wrote a full design system before touching a single scene."
**[SCREEN]** DESIGN.md appears; SILENCE BEAT (2s, music swell) on the palette table.

**STEP 2 — the design system (3:55–4:55)**
**S15** — "This file is the reason the result looks produced, instead of A I generated."
**[SCREEN]** clip-02: DESIGN.md slow scroll.
**S16** — "Every color. Every font. The exact photo treatment — grayscale, a little sepia, a cool blue wash. And even the motion rules: every photo gets a slow Ken Burns drift, and the text moves at a third of the photo's speed. That is what creates real parallax depth."
**[SCREEN]** 1883 Orient Express scene frozen; arrows overlay showing photo-vs-text drift speeds.
**S17** — "Claude treats this file as law. Change it once, and the whole video regrades itself. Try doing that in a timeline editor."
**[SCREEN]** palette value edited → three scenes flash re-graded; verdict chip "DESIGN AS LAW ✓".

**STEP 3 — research and script (4:55–5:55)**
**S18** — "For a history piece, the facts are the product. Claude built the timeline first. Thomas Cook's first tour in eighteen forty one. The Suez Canal in eighteen sixty nine. The Orient Express. The great ocean liners. Lindbergh in nineteen twenty seven. The seven forty seven opening the skies in nineteen seventy."
**[SCREEN]** the runbook's verified-timeline table, rows highlighting in sync.
**S19** — "Only then did it write narration to fit. Fourteen voice segments, about a hundred and sixty seconds of speech, each one timed before any visuals existed."
**[SCREEN]** the 14 wav files with durations (file manager clip-10 excerpt).
**S20** — "Audio first, visuals second. That single ordering decision kills the sync problems that eat most editing time."
**[SCREEN]** "AUDIO → THEN → VISUALS" diagram card; verdict chip.

**STEP 4 — the voice (5:55–6:55) — the transparency beat**
**S21** — "Now, the voice. The documentary's narrator is an A I voice — an open source text to speech engine called Kokoro. Free, and it runs on your own computer."
**[SCREEN]** clip-07: Kokoro generating a line, waveform appears.
**S22** — "And as I told you at the start — so is this one. Same engine. I am not hiding the tool behind a human voiceover and pretending. The tool is good enough to narrate its own tutorial. That is the review."
**[SCREEN]** side-by-side waveforms: "documentary VO" / "this VO" — both labeled KOKORO; slow zoom.
**S23** — "One honest rule if you do this on your own channel: YouTube asks you to disclose realistic synthetic media. This video has the toggle set to yes. It costs nothing, and viewers respect it more than they punish it."
**[SCREEN]** clip-08: the actual altered-content toggle being set to YES in Studio.

**STEP 5 — scenes as code + the render (6:55–8:20)**
**S24** — "Now the part that felt like a trick the first time. I asked Claude for each scene in plain English."
**[SCREEN]** clip-04: typing the 1907 scene request.
**S25** — "Nineteen oh seven. The Mauretania. Giant year number. Title on a dark band. Slow drift left. And it just — wrote it. An H T M L file with the photo, the type, and the timing baked in."
**[SCREEN]** the scene file streaming into existence; clip-05 close-up on the timing attributes.
**S26** — "Fourteen scenes later, one command. Twenty minutes on an ordinary laptop. Out comes a seven hundred megabyte, ten-eighty P master. No timeline was ever opened."
**[SCREEN]** clip-06: render command + progress; then the finished 1907 scene playing; SILENCE BEAT (2s) on "734 MB · 1080p · 4:00" card.

### ⚠️ WHERE IT BREAKS — 8:20–10:30 *(the section others skip)*
**S27** — "Now the part of this video that the other videos skip."
**[SCREEN]** hard cut to red stamp "WHAT THEY SKIP"; music drops out.
**S28** — "If you are imagining dropping in your real footage and telling Claude — cut this into a five minute edit — stop."
**[SCREEN]** freeze; 1s silence after "stop."
**S29** — "Independent testing this year tried exactly that. They asked for a five minute cut. They got nine and a half minutes, while the model reported four fifty nine. And eleven out of eleven cuts landed mid sentence."
**[SCREEN]** big numbers graphic: "ASKED 5:00 → GOT 9:38" · "11/11 cuts mid-sentence".
**S30** — "Claude cannot feel a beat, or hear a breath. It edits structure, not footage. And that is exactly why scenes as code works: nothing is ever cut. Motion is written, and rendered perfectly, because it was never eyeballed in the first place."
**[SCREEN]** verdict card: "CUTTING REAL FOOTAGE ✗ / WRITING MOTION ✓".
**S31** — "Second limit. Screen recording real apps. I tried automating that with a browser bot, and the scrolling came out frozen and lurching. Record real screens by hand. Render everything else."
**[SCREEN]** 2s of the frozen-scroll bot capture, labeled "my automation attempt"; then a clean hand-recorded scroll beside it.
**S32** — "And third — look at my own title card. See the caption clipping into the title? Claude shipped that bug, and I did not catch it either."
**[SCREEN]** OUR flawed title card, zoom into the overlap, red circle.
**S33** — "So let us fix it live, with one sentence."
**[SCREEN]** clip-09: the fix prompt typed → re-render → clean title card; before/after wipe. Verdict chip "ITERATION IS THE WORKFLOW".

### 🎁 THE PAYOFF — 10:30–12:00 *(teased at 0:35; the full loop + giveaway)*
**S34** — "Here is the whole pipeline, end to end — because this is the part that still gets me."
**[SCREEN]** timelapse build: each step ~3s, music builds.
**S35** — "One brief. A design system. A researched script. Fourteen A I voice lines. Fourteen scenes as code. One command."
**[SCREEN]** step cards snap in rhythm with each phrase.
**S36** — "Four minutes of cinematic documentary, from an afternoon of iteration, on a laptop, with free, open source tools."
**[SCREEN]** the finished documentary playing wide; let it breathe 3s.
**S37** — "And you do not have to reverse engineer any of it. My design template, the exact prompts, and my build checklist are linked below — free. No email gate. Take them."
**[SCREEN]** giveaway card with the link visible; hold.

### THE HONEST VERDICT — 12:00–13:30
**S38** — "So — should you use this?"
**[SCREEN]** clean verdict frame, music low.
**S39** — "If you make videos from real footage — vlogs, gameplay, interviews — no. Skip it. A timeline editor is still faster than fighting a text file."
**[SCREEN]** left column stamps: "REAL-FOOTAGE CREATORS → SKIP".
**S40** — "But if you make motion graphic content — explainers, documentaries like this one, data stories, faceless channels — this is the closest thing to a cheat code I have tested this year."
**[SCREEN]** right column: "MOTION-GRAPHIC CREATORS → TRY IT TODAY"; 1.5s silence on the full card.
**S41** — "It is free. There is no catch I have found. And remember — I earn nothing if you try it."
**[SCREEN]** "NO AFFILIATE — STILL." chip returns (callback).
**S42** — "My plan: every cinematic video on this channel's sister history channel gets built exactly this way."
**[SCREEN]** 3s teaser strip of A Century of Travel scenes + subtle channel-link lower third.

### CTA + LOOP — 13:30–14:30
**S43** — "Next video, I am going further. A complete faceless video built with an A I stack, start to finish — script, voice, visuals, edit."
**[SCREEN]** next-video placeholder card slides in.
**S44** — "And I will tell you exactly which single tool is worth paying for. Because it is not the one you think."
**[SCREEN]** blurred tool logos with a "?" — open loop.
**S45** — "If honest breakdowns like this are useful, subscribe. One a week. No hype."
**[SCREEN]** subscribe pointer, small and calm.
**S46** — "The full documentary — all four minutes — is linked below. Go watch what a text file can do."
**[SCREEN]** end on the 1841 title card; music resolves; hold 3s.

## 3. FACT-CHECK LIST — unchanged from v1 §5 (re-verify day-of), PLUS:
| Claim | Source | Checked | Day-of |
|---|---|---|---|
| Kokoro runs locally / free (as spoken in S21) | project pipeline (audio_meta.json) + kokoro repo | 2026-07-04 | ☐ |
| Render ≈20 min claim (S26) | re-time on the creator's machine at build | — | ☐ measure real time |

## 4. GATE 2 (adjusted for TTS)
☐ altered-content toggle = **YES** (stated in-video, S23 — consistency between claim and toggle) ☐ material variation: own artifact, own flaw fixed live, own verdicts ✓ ☐ music from YT Audio Library only ☐ every "I tried / I tested" claim really run (bot-scroll clip = our real 2026-07-02 test; the live fix = actually performed at build) ☐ giveaway link live before publish ☐ prices/policy wording re-verified day-of ☐ Notion ≤3 lines.
