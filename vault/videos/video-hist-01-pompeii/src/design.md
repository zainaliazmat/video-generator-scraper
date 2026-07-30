# DESIGN — Pompeii Ka Akhri Din (HyperFrames build sheet)

*Generated build copy 2026-07-13. Canonical rationale lives in the vault
(`vault/videos/video-hist-01-pompeii/DESIGN.md`). This file = the look + the hard render rules the
HyperFrames build must obey, with the real asset filenames in this folder.*

## Format
- **1920×1080**, `data-fps=30`, **~21 min** (target 20:00–21:30), H.264 MP4.
- Lock each scene's duration to the VO line it carries (see `frame.md`). Times there are VO-driven approximations.

## The 3 visual layers (every scene is exactly ONE — the grade separates them)
| Layer | What | Grade (CSS-ish) | Files |
|---|---|---|---|
| **① RECON** (life) | AI photoreal reconstructions | full warm colour, cinematic, film-grain | `S1..S9-*.jpeg` (this folder) |
| **② EVIDENCE** (truth) | real ruins/casts/frescoes/manuscripts | **desaturate**: `grayscale(.35) contrast(1.05) brightness(.96)` + slight cool/blue wash | `_evidence/EV-*.jpg` |
| **③ CARD** (facts) | parchment motion-graphic cards + chip | aged parchment, warm, minimal | built in HyperFrames — see `cards` spec |

**Signature edit — the recon→evidence match cut** (1.0 s cross-dissolve, identical framing):
- seg 14: `S3-14B_loaves-cooling` → `_evidence/EV-14C_carbonised-bread`
- seg 52 / 64: `S1-03A_horse-groomed` (living) ↔ `_evidence/EV-52B_horse-cast`
That cut IS the thesis — "these people were real."

## Palette (tokens)
`--paper #0d0f12` (letterbox) · `--ink #f4f1ea` (text, never pure #fff) · `--ink-soft rgba(244,241,234,.82)`
· `--parchment #e8dcc0` (card bg) · `--pompeii-red #9c342a` (accent/motif) · `--ash #8a8578` (evidence tint,
silence beats) · `--ember #d8863a` (eruption/firelight — used ONLY from seg 23 on).

## Typography (embed fonts — never system-ui)
- Roman-Urdu kinetic type / captions: clean Latin-script sans (Inter / Mukta, 600–800), legible at 10% size.
- Timestamp chip + labels: same sans, uppercase, tracked.
- Card headlines / Latin quotes: serif (Playfair Display).
- English only in metadata + refs/labels that the script keeps English (dates, verse refs, Latin, SUBSCRIBE).

## Motion grammar (flat still → cinema)
- **Ken Burns** on every RECON still: `scale 1.0 → 1.08–1.14`, few-% drift, `sine.inOut`, alternate direction scene-to-scene.
- **2.5D parallax:** foreground drifts more than background; text/UI travels ~25–35% of image travel.
- **Camera = emotion:** push-in = intimacy/tension · pull-back = scale/aftermath (46A) · tilt-up = mountain & the 33 km column (24A) · **locked/no motion** on silence & peak beats (41A/42, 45A, C-57).
- **Transitions:** ~1.0 s cross-dissolve default; **hard cut to black + 1 beat silence** ONLY at the 3 pattern interrupts (23, 41–42, C-57); soft ember bloom at act breaks after seg 23.

## Recurring UI — timestamp chip
Bottom-left, small, uppercase, tracked, `--ink` on a faint dark band. One component, value changes. Sequence
in `cards` / `frame.md`: `6:00 AM → … → 12:00 PM → 2/3/4 PM → 7 PM → 3 AM → 6:30 AM → AUG 2024 → NOV 2024 → APR 2026`.

## Pattern interrupts & planned silence (do NOT move — retention)
- **23** the blast: silence → full-frame eruption.
- **41–42** dead silence on the pre-dawn lull: hold longer than comfortable (locked `S6-41A`).
- **C-57** DNA reveal: full-screen single fact, no music (Von Restorff).

## Sound
Low drone from seg 05, builds under the morning, drops for tone-shifts (19, 41–42). Blast (23), pumice patter
(27–31), roof cracks (35), surge wash (45). VO = creator's Roman-Urdu; duck music ~-8 dB under VO. Reverent slow
pacing on the ibrah coda (61a–d). Music: cleared / YT Audio Library only.

## ⚠ Continuity / fact rules baked into the assets
- Vesuvius pre-eruption = single tall green cone, ONE summit; **decapitated broken stump** only in `S6-46A`
  (aftermath). Montage mountains (47A/B/C) = calm, no plume.
- Roof collapse (35A) + physics card (C-36) = **pitched tiled** roof, not flat.
- Herculaneum victims = **skeletons** (`EV-39A`), NOT casts. Casts are a Pompeii thing (`EV-51A`).
- Ibrah coda: NO nudity/explicit imagery ever; 61a = empty Lupanar; Qaum-e-Lut = overturned-ruin, not a depiction.

## Determinism / render contract (HyperFrames rejects otherwise — NON-NEGOTIABLE)
One `gsap.timeline({paused:true})` on `window.__timelines["<id>"]`; no `Date.now()` / `performance.now()` /
unseeded `Math.random()` / network at render; no `repeat:-1`; animate ONLY
`x,y,scale,rotation,opacity,color,backgroundColor,borderRadius` (never width/height/top/left/display/visibility);
root explicitly sized; full-screen fills on a full-bleed child; `<video>`/`<audio>` direct children of root.
Pass `hyperframes lint` / `validate` / `inspect` at 0 errors before preview. Build stages: simple render →
motion/texture → VO+music → polish → render.
