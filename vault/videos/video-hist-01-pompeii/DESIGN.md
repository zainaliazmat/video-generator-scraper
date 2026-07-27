---
summary: The film-rules / design frame for "Pompeii Ka Akhri Din" — a ~21-min colored cinematic history film built in HyperFrames from ~78 photoreal AI stills (Nano Banana) + real-ruins evidence footage + parchment motion-graphic cards, over the creator's Roman-Urdu VO. This is BRAND TRUTH: HyperFrames reads it as hard constraints. Gate ① — lock before storyboard.
updated: 2026-07-10
source: adapts [[../../knowledge/design-cinematic-history]] (→ COLOR recon, not B&W) + study [[../../knowledge/video-studies/pompeii-last-day]] 3-layer system + proven pipeline [[../video-hist-01-travel/production-runbook]] + prompts [[image-prompts]]
---

# DESIGN — Pompeii Ka Akhri Din (film rules)

**Concept:** a cinematic documentary — you are *inside* the last ordinary day of a real
city. Not a slideshow: photoreal reconstructions breathe with camera motion, the real ruins
cut in as evidence, and parchment cards deliver the facts. The emotion is *dramatic irony* —
we watch ordinary life knowing the ending. Engagement engine = the script's 6 retention loops
+ hour-by-hour clock + the ~70% discovery payoff + the ibrah coda.

**Format:** 1920×1080, `data-fps=30`, **~21 min** (target 20:00–21:30). H.264 MP4.
Lock each scene's duration to the VO line it carries.

## The 3 visual layers (every scene is exactly one — the grade tells them apart)

| Layer | What | Look / grade | Source |
|---|---|---|---|
| **① RECON** (life) | AI photoreal reconstructions of the living city | **full warm colour**, cinematic, film-grain | Nano Banana stills → [[image-prompts]] |
| **② EVIDENCE** (truth) | real ruins, casts, frescoes, manuscripts, excavation photos | **desaturated & cool** — `grayscale(.35) contrast(1.05) brightness(.96)` + slight blue wash; forensic, still | public-domain / Pompeii Sites / museum imagery |
| **③ CARD** (facts) | parchment motion-graphic cards — dates, quotes, diagrams, Quran verses, kinetic Urdu type | aged-parchment texture, warm, minimal | built in HyperFrames (no sourcing) |

The **recon→evidence match cut** is the signature edit (seg 14 bread, 52 horse, 64 horse):
colour living shot dissolves to the desaturated real object at the same framing. That cut *is*
the thesis — "these people were real."

## Palette
| Token | Value | Use |
|---|---|---|
| `--paper` | `#0d0f12` | letterbox / base behind everything |
| `--ink` | `#f4f1ea` | primary text (warm off-white, **never pure #fff**) |
| `--ink-soft` | `rgba(244,241,234,0.82)` | captions / secondary |
| `--parchment` | `#e8dcc0` | card background |
| `--pompeii-red` | `#9c342a` | accent — dado red, card rules, the recurring motif colour |
| `--ash` | `#8a8578` | evidence-layer tint, silence beats |
| `--ember` | `#d8863a` | eruption / firelight accent (used ONLY from seg 23 on) |

## Typography (embed in HyperFrames — never system-ui fallback)
- **Roman-Urdu kinetic type / captions:** a clean readable Latin-script sans (Urdu written in
  Roman per creator rule) — e.g. **Inter / Mukta** weight 600–800. Legible at 10% size.
- **Timestamp chip + labels:** same sans, uppercase, tracked.
- **Card headlines / Latin quotes:** a serif (Playfair Display) for gravity.
- **English titles/description** live off-screen (metadata), always English (creator rule).

## Recurring UI — the timestamp chip (hour-by-hour clock)
Bottom-left chip showing the hour (`6:00 AM` … `12:00 PM` … `APR 2026`). Appears seg 07, ticks
through the day, becomes the spine of the story. Small, tracked, `--ink` on a faint dark band.
(The "How So date-chip" move from the study.)

## Motion language — how a flat AI still becomes cinema
Every still gets motion; the *type* of motion is chosen by the beat's emotion:

- **Ken Burns** on every recon still: `scale 1.0 → 1.08–1.14`, few-% drift, `sine.inOut`, whole
  scene, alternating direction scene-to-scene.
- **2.5D parallax:** treat each still as near/far — foreground drifts MORE than background
  (fake depth). Text/UI travels ~25–35% of the image travel. Subtle — depth, not nausea.
- **Camera = emotion:** slow **push-in** for intimacy/tension (hook, the two victims) · **pull-back**
  for scale/aftermath (seg 46 grey plain) · **tilt-up** for the mountain & the 33 km column (24) ·
  **locked/no motion** on the silence & peak beats (42, 45, 57) — stillness is a tool.
- **Match cuts:** recon↔evidence at identical framing (14, 52, 64) — 1.0 s cross-dissolve.
- **Transitions:** ~1.0 s cross-dissolve default; a **hard cut to black + 1 beat silence** ONLY
  at the 3 pattern interrupts; soft ember bloom at act breaks after seg 23.

## Pattern interrupts & planned silence (retention)
- **23** the blast — silence → full-frame eruption (the jolt).
- **42** dead silence on the pre-dawn lull — hold one beat longer than comfortable.
- **57** the DNA reveal — full-screen single fact, no music (Von Restorff).
- Loops & payoff placement per the script's Loop ledger — do not move them.

## Sound design
- Low drone from seg 05; builds under the morning; drops out for tone-shifts (19, 41–42).
- The blast (23), pumice patter (27–31), roof cracks (35), surge wash (45).
- **VO = creator's Roman-Urdu voice.** Duck music **~-8 dB** under VO. Reverent slow pacing on
  the ibrah coda (61a–61d). Music: cleared / YT Audio Library only.

## Realism & continuity rules for the AI stills (the make-or-break)
1. **Fact-check every scene before prompting** (standing rule — [[image-prompts]]). Everything
   photoreal, never "AI/CGI".
2. **Character consistency:** lock a reference image for each recurring character (the bread man,
   the baker, THE horse, young Pliny, the two Regio-IX victims) and feed it back into Nano Banana
   so faces/wardrobe stay identical across their scenes. Inconsistent faces = the #1 tell.
3. **Time-of-day consistency:** the light must track the clock — golden dawn (6–8am) → flat midday
   (12) → ash-dark (afternoon) → firelit night → grey pre-dawn. Same sun in every scene of an hour.
4. **Film grain over EVERYTHING** (all 3 layers) — a single deterministic grain pass unifies stills
   shot at different times into one film. Vignette + faint paper texture as persistent top tracks.
5. **No anachronisms, no legible modern text, no volcano in frame before seg 05.**

## Dynamic scenes (the one production fork — creator decision)
~8 shots are *motion-native* and a Ken-Burns still may not sell them: **23** blast, **24** rising
column, **37** column collapse, **45** the surge, pyroclastic flow. **Recommended v1:** generate
strong AI stills + carry them with HyperFrames motion, ember particles/ash overlays, and sound
design — cheapest path, ships. **Upgrade option:** run those ~8 stills through an image-to-video
AI (Veo / Kling / Runway) for real motion, drop the clips in as `<video>`. Decide at storyboard.

## Determinism / render contract (non-negotiable — HyperFrames rejects otherwise)
One `gsap.timeline({paused:true})` on `window.__timelines["<id>"]`; no
`Date.now()`/`performance.now()`/unseeded `Math.random()`/network at render; no `repeat:-1`;
animate only `x,y,scale,rotation,opacity,color,backgroundColor,borderRadius` (never
width/height/top/left/display/visibility); root explicitly sized; full-screen fills on a
full-bleed child; `<video>`/`<audio>` direct children of root; pass `hyperframes
lint`/`validate`/`inspect` at 0 errors before preview. Build stages + prompts: reuse
[[../video-hist-01-travel/production-runbook]] §6 (adapt asset names to the 3-layer scheme).
