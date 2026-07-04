---
summary: Script v2.1 — TTS EDITION, HONEST-WORKFLOW REVISION (creator 2026-07-04 — the video was NOT one-prompt; it's a ~4-5h workflow incl. a 2-3h blueprint discussion. Script now shows the real process; overclaim removed everywhere). Kokoro narrates; creator records zero voice.
updated: 2026-07-04
source: v2 + creator's honesty correction + PRODUCTION_RUNBOOK.md (the real process artifact)
---

# VIDEO #2 — "Claude Code Just Edited This Entire Video" — v2.1 (TTS, honest workflow)

> Target ~15:00 · VO ≈1,850 words in ~50 Kokoro segments (bm_george, speed 0.9 — audition at build) ·
> Creator records ONLY screen clips per [[recording-guide]] — no voice.
> **The premise:** fully AI-narrated video about AI-made video — disclosed in the first 40s.
> **The honesty spine (creator's rule, 2026-07-04):** NEVER say or imply one-prompt. The real
> workflow: reference video → 2–3h blueprint discussion with Claude → download assets →
> step-by-step prompts to Claude Code → one render command. ~4–5 focused hours total.
> That truth is the differentiator — every competitor oversells; we quantify honestly.

## TTS PACING RULES (unchanged from v2)
Segments 8–16s · edit breathes between them · visual interrupt every 30–45s · music bed
(YT Audio Library, ducked) + planned silences (after the render reveal, after "stop.", on
the verdict card) · captions ON · numbers written as SPOKEN · audition "HyperFrames"
(respell "Hyper Frames" if garbled) · altered-content toggle = YES, stated in-video.

## 1. TITLE OPTIONS (Claude-anchored; now honesty-signaled)
1. ★ **Claude Code Edited This Entire Video — Here's the REAL Workflow (Not One Prompt)** — bold claim + the honesty hook in the title itself.
2. How I Made a Cinematic Documentary with Claude Code (Honest 5-Hour Workflow) — search + expectation-set.
3. Claude Code Just Edited This Entire Video — No Editor, No Timeline (Honest Review) — v2 original, still valid.
4. AI Made This Cinematic Video — The Truth About How Long It Really Takes — curiosity via honesty.

## 2. THE SCRIPT — numbered VO segments + screen cues
*(Each `S##` = one `lines[]` entry in audio_request.json.)*

### HOOK — 0:00–0:45
**S01** — "Every frame of the video you are watching was edited by Claude. Not a human. Not Premiere. Not DaVinci. There is no timeline at all. Every scene is a text file, rendered with one command."
**[SCREEN]** cold open ON the artifact: 1907 liner scene → 1970 Pan-Am 747 → smash cut to the bare terminal render command.
**S02** — "And this voice — the one talking to you right now — is not human either. It is a free, open source AI voice. This entire video is the demo."
**[SCREEN]** waveform pulse + "THIS VOICE = AI · FREE" stamp.
**S03** — "But I will tell you upfront what nobody else in these videos will: this was not one magic prompt. It took me about five focused hours, and a real workflow — and I am going to show you every step of it, including the two hours of preparation everyone else cuts out."
**[SCREEN]** quick flash of the PRODUCTION_RUNBOOK scrolling — visibly long and detailed; "~5 HOURS · REAL WORKFLOW" chip.
**S04** — "By the end, you will have that exact workflow. It is free, and open source. And around the nine minute mark: the part where this whole approach breaks. You need that before you spend your weekend."
**[SCREEN]** roadmap strip; "9:00" tease chip.

### THE ANSWER, FAST — 0:45–2:00
**S05** — "Here is the honest shape of it, in forty seconds. Step one: I found a video style I loved — a vintage parallax history slideshow — and saved it as my reference."
**[SCREEN]** clip-01a: the Pinterest reference on screen.
**S06** — "Step two: I spent about two to three hours with Claude — a real back and forth — analyzing that reference: its motion, its typography, its pacing. The output was this: a production runbook. The complete blueprint for the video."
**[SCREEN]** clip-01b: PRODUCTION_RUNBOOK.md slow scroll — the style analysis, the timeline table.
**S07** — "Step three: I downloaded the archival photos the blueprint called for — all public domain — and placed them into the project folders."
**[SCREEN]** clip-10 excerpt: assets folder with the B&W photos.
**S08** — "Step four: I fed the blueprint to Claude Code, step by step — and it wrote the design system, the narration, and every scene as code. Then one render command. Four minutes of cinematic documentary, in ten-eighty P."
**[SCREEN]** montage: prompts → scenes → render bar → finished frame; "4:00 · 1080p" card.
**S09** — "And no — there is no affiliate link here. There is not even an affiliate program. Nobody is paying me to say any of this."
**[SCREEN]** "FREE · OPEN SOURCE · NO AFFILIATE EXISTS" card; beat of silence.

### WHAT THIS ACTUALLY IS — 2:00–3:20
**S10** — "The rendering tool is called HyperFrames. HeyGen open-sourced it in April."
**[SCREEN]** GitHub repo clip, stars visible.
**S11** — "Think of it like this. A normal video editor is a live orchestra. You conduct every cut by hand, in real time, on a timeline."
**[SCREEN]** clip-03: the cluttered timeline, playhead scrubbing.
**S12** — "HyperFrames is sheet music. You write the score once — this scene starts here, lasts this long, drifts left, fades out — and the renderer plays it perfectly, every single time."
**[SCREEN]** clean scene file beside its rendered scene; timing attributes highlighted.
**S13** — "Where the comparison breaks: you do not hear the music while you write it. You preview, adjust, and re-render."
**[SCREEN]** preview-reload loop.
**S14** — "And here is why that matters for Claude. Claude cannot drag a playhead. But it is extremely good at writing structured text. Scenes as text turns video editing into something an AI is naturally good at."
**[SCREEN]** split: playhead (✗) vs text streaming (✓).

### THE BUILD — the real six stages — 3:20–9:00

**STAGE 1 — the blueprint (3:20–4:30) — the part everyone cuts out**
**S15** — "Stage one is the one every other video skips, so let us start there. You do not begin by prompting for a video. You begin with a reference — a real video whose style you want — and a long conversation."
**[SCREEN]** the Pinterest reference again, 3s, then Claude AI chat scrolling.
**S16** — "I gave Claude my reference and we spent two, maybe three hours going back and forth: what makes this style work, which effects are really in it, how each one maps to something HyperFrames can render."
**[SCREEN]** clip-01b continued: runbook's style-analysis section — "Ken Burns", "parallax", "film grain" callouts lighting up.
**S17** — "The output of that conversation is a production runbook. Topic locked. A verified historical timeline. A shot list. An asset list. The blueprint. Honestly? This document is worth more than the render."
**[SCREEN]** runbook's verified-timeline table + asset list; hold; "THE BLUEPRINT" chip.

**STAGE 2 — the design system (4:30–5:20)**
**S18** — "From the blueprint, Claude wrote a design file — and this file is the reason the result looks produced, instead of AI generated."
**[SCREEN]** clip-02: DESIGN.md slow scroll.
**S19** — "Every color. Every font. The exact photo treatment — grayscale, a little sepia, a cool blue wash. And the motion rules: every photo drifts on a slow Ken Burns, and the text moves at a third of the photo's speed. That is real parallax depth."
**[SCREEN]** 1883 Orient Express frozen; drift-speed arrows overlay.
**S20** — "Claude treats this file as law. Change it once, and the whole video regrades itself. Try doing that in a timeline editor."
**[SCREEN]** palette edit → scenes flash re-graded; "DESIGN AS LAW ✓" chip.

**STAGE 3 — research and script (5:20–6:05)**
**S21** — "For a history piece, the facts are the product. The runbook locked the timeline first. Thomas Cook's first tour in eighteen forty one. The Suez Canal in eighteen sixty nine. The Orient Express. The great liners. Lindbergh in nineteen twenty seven. The seven forty seven in nineteen seventy."
**[SCREEN]** timeline table, rows highlighting in sync.
**S22** — "Only then came the narration. Fourteen voice segments, about a hundred and sixty seconds of speech, each timed before any visuals existed. Audio first, visuals second — that ordering kills the sync problems that eat editing time."
**[SCREEN]** the 14 wav files with durations; "AUDIO → THEN → VISUALS" card.

**STAGE 4 — the assets (6:05–6:40) — honest work, not magic**
**S23** — "Stage four is manual, and I will not pretend otherwise: I downloaded every archival photograph on the blueprint's list myself. They are public domain — old enough that copyright has expired — which also keeps the video safe to monetize."
**[SCREEN]** clip-10: assets folder browse — the B&W photos appearing one by one.
**S24** — "Budget maybe forty five minutes for this. Good source hunting is what separates a cinematic result from a stock-photo slideshow."
**[SCREEN]** split: a stunning archival shot vs a generic stock image; "45 MIN · WORTH IT" chip.

**STAGE 5 — the voice (6:40–7:30) — the transparency beat**
**S25** — "The documentary's narrator is an AI voice — an open source text to speech engine called Kokoro. Free, and it runs on your own computer."
**[SCREEN]** clip-07: Kokoro generating a line; waveform appears.
**S26** — "And as I told you at the start — so is this one. Same engine. I am not hiding the tool behind a human voiceover and pretending. The tool is good enough to narrate its own tutorial. That is the review."
**[SCREEN]** side-by-side waveforms both labeled KOKORO; slow zoom.
**S27** — "One honest rule if you do this on your own channel: YouTube asks you to disclose realistic synthetic media. This video has that toggle set to yes. It costs nothing, and viewers respect it more than they punish it."
**[SCREEN]** clip-08: the altered-content toggle clicked to YES.

**STAGE 6 — scenes as code, then the render (7:30–9:00)**
**S28** — "Now the part that felt like a trick the first time. Scene by scene, I prompted Claude Code in plain English — one prompt per scene, straight from the blueprint."
**[SCREEN]** clip-04: typing the 1907 scene request.
**S29** — "Nineteen oh seven. The Mauretania. Giant year number. Title on a dark band. Slow drift left. And it just — wrote it. An H T M L file with the photo, the type, and the timing baked in."
**[SCREEN]** scene file streaming in; clip-05: timing attributes close-up.
**S30** — "Fourteen scenes. Fourteen prompts. Then one command. About twenty minutes of rendering on an ordinary laptop, and out comes a seven hundred megabyte, ten-eighty P master. No timeline was ever opened."
**[SCREEN]** clip-06: render start → finish; the finished 1907 scene playing; SILENCE BEAT on "734 MB · 1080p · 4:00" card.

### ⚠️ WHERE IT BREAKS — 9:00–11:00
**S31** — "Now the part of this video that the other videos skip."
**[SCREEN]** red stamp "WHAT THEY SKIP"; music out.
**S32** — "If you are imagining dropping in your real footage and telling Claude — cut this into a five minute edit — stop."
**[SCREEN]** freeze; 1s silence.
**S33** — "Independent testing this year tried exactly that. They asked for a five minute cut. They got nine and a half minutes, while the model reported four fifty nine. Eleven out of eleven cuts landed mid sentence."
**[SCREEN]** "ASKED 5:00 → GOT 9:38" · "11/11 mid-sentence" graphic.
**S34** — "Claude cannot feel a beat, or hear a breath. It edits structure, not footage. That is exactly why scenes as code works: nothing is ever cut. Motion is written, and rendered perfectly, because it was never eyeballed in the first place."
**[SCREEN]** verdict card: "CUTTING REAL FOOTAGE ✗ / WRITING MOTION ✓".
**S35** — "Second limit: screen recording real apps. I tried automating that with a browser bot, and the scrolling came out frozen and lurching. Record real screens by hand. Render everything else."
**[SCREEN]** 2s frozen-scroll bot capture labeled "my automation attempt" vs a clean hand recording.
**S36** — "Third — and be honest with yourself about this one — the workflow has a learning curve. My five hours came after I already knew the tools. Your first video will take longer. Budget a full day, and treat it as learning, not losing."
**[SCREEN]** "FIRST VIDEO = BUDGET A DAY" card, plain and calm.
**S37** — "And fourth — look at my own title card. See the caption clipping into the title? Claude shipped that bug, and I did not catch it either."
**[SCREEN]** OUR flawed title card; zoom; red circle.
**S38** — "So let us fix it live, with one sentence."
**[SCREEN]** clip-09: fix prompt → re-render → clean card; before/after wipe; "ITERATION IS THE WORKFLOW" chip.

### 🎁 THE PAYOFF — 11:00–12:30
**S39** — "Here is the whole pipeline, end to end — because seeing it honestly, all at once, is the part that still gets me."
**[SCREEN]** timelapse build, music building.
**S40** — "One reference video. One long conversation that becomes a blueprint. An asset folder. Fourteen voice lines. Fourteen scene prompts. One render command."
**[SCREEN]** stage cards snapping in rhythm with each phrase.
**S41** — "About five hours of honest work — and I could not have made this in a timeline editor at all. I am not an editor. That is the point."
**[SCREEN]** the finished documentary playing wide; breathe 3s.
**S42** — "And you do not have to reverse engineer any of it. My production runbook template, the design file, and the exact scene prompts are linked below — free. No email gate. Take them."
**[SCREEN]** giveaway card, link visible; hold.

### THE HONEST VERDICT — 12:30–13:55
**S43** — "So — should you use this?"
**[SCREEN]** clean verdict frame, music low.
**S44** — "If you make videos from real footage — vlogs, gameplay, interviews — no. Skip it. A timeline editor is still faster than fighting a text file."
**[SCREEN]** "REAL-FOOTAGE CREATORS → SKIP" column stamps.
**S45** — "But if you make motion graphic content — explainers, documentaries like this one, data stories, faceless channels — this is the most capable free tool I have tested this year. Just come to it with a blueprint, not a wish."
**[SCREEN]** "MOTION-GRAPHIC CREATORS → TRY IT" column; 1.5s silence on the full card.
**S46** — "It is free. There is no catch I have found. And remember — I earn nothing if you try it."
**[SCREEN]** "NO AFFILIATE — STILL." callback chip.
**S47** — "My plan: every cinematic video on this channel's sister history channel gets built exactly this way — blueprint first, every time."
**[SCREEN]** 3s Century-of-Travel teaser strip + channel lower-third.

### CTA + LOOP — 13:55–14:50
**S48** — "Next video, I am going further: a complete faceless video built with an AI stack, start to finish — script, voice, visuals, edit."
**[SCREEN]** next-video card slides in.
**S49** — "And I will tell you exactly which single tool is worth paying for — because it is not the one you think. If honest breakdowns like this are useful, subscribe. One a week. No hype."
**[SCREEN]** blurred tool logos + "?" open loop; calm subscribe pointer.
**S50** — "The full documentary — all four minutes — is linked below. Go watch what a blueprint and a text file can do."
**[SCREEN]** end on the 1841 title card; music resolves; hold 3s.

## 3. FACT-CHECK LIST (verify + RE-DATE day-of)
| Claim | Source | Checked | Day-of |
|---|---|---|---|
| Total build ≈4–5 focused hours incl. 2–3h blueprint discussion (S03/S16/S41) | creator's real timeline, 2026-07 (this correction) | 2026-07-04 | ☐ creator confirms the numbers feel right |
| Archival photos public domain (S23) | runbook asset list sources | 2026-07-04 | ☐ spot-check 3 photos' provenance |
| HyperFrames open-source, Apache 2.0, free | GitHub + hyperframes.heygen.com | 2026-07-04 | ☐ |
| Open-sourced April 2026 | cutback.video | 2026-07-04 | ☐ |
| Frame-precise cutting fails (5:00→578s reported 299.32; 11/11 mid-sentence) | cutback.video experiment 2026 | 2026-07-04 | ☐ ("independent testing") |
| Bot scroll capture freezes (own test) | our Playwright test 2026-07-02 | 2026-07-04 | — own data |
| Kokoro free/open, local | project pipeline + kokoro repo | 2026-07-04 | ☐ |
| Render ≈20 min; master ≈734MB 1080p 4:00 | project renders/ | 2026-07-04 | ☐ re-time at build |
| YouTube disclosure policy wording | YouTube Help (Gate 2) | — | ☐ MUST verify day-of |
| Historical dates (1841/1869/1907/1927/1970) | runbook verified-timeline | 2026-07-04 | ☐ vs sourced photos |

## 4. GATE 2 (TTS edition)
☐ toggle = YES (S27 consistency) ☐ material variation: own artifact + own blueprint + flaw fixed live ✓ ☐ YT Audio Library music only ☐ every "I tried/tested" really happened (bot clip = real 2026-07-02 test; live fix performed at build; hours = creator-confirmed) ☐ giveaway (runbook template + DESIGN + prompts) live before publish ☐ Notion ≤3 lines.
