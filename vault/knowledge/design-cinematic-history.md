---
summary: The durable design system for the HistoryFramesFilm (cinematic-history) channel — vintage blue-sepia parallax slideshow. Copy into each new history video's DESIGN.md. Proven by video HIST-01 "A Century of Travel".
updated: 2026-07-10
source: studio/videos/a-century-of-travel/DESIGN.md (shipped 2026-07-11)
stage: ADOPTED — the standing design system for the cinematic-history lane
---

# Design system — cinematic-history (HistoryFramesFilm)

The history-channel analogue of [[design-techtooltester]]. HyperFrames reads a
per-video `DESIGN.md` as **brand truth** — copy this block into each new history
video's `DESIGN.md` and treat every value as a hard constraint. Proven end-to-end
by [[../videos/video-hist-01-travel/index]].

**Concept:** an old documentary title sequence — archival B&W photos, giant year
numbers, elegant serif titles, gentle camera drift, film grain, slow nostalgic score.
The journey itself was once the destination; we relive that romance one era at a time.

**Format:** 1920×1080, `data-fps=30`, ~4:00 (235–245 s). H.264 MP4. Lock final scene
durations to the music/VO.

## Palette — "vintage blue-sepia" grade
| Token | Value | Use |
|---|---|---|
| `--paper` | `#0d0f12` | base / letterbox / behind everything |
| `--ink` | `#f4f1ea` | primary text (warm off-white, **never pure #fff**) |
| `--ink-soft` | `rgba(244,241,234,0.82)` | captions / secondary text |
| `--band` | `rgba(15,19,24,0.55)` | dark band behind serif titles |
| `--grade-wash` | `rgba(28,40,56,0.18)` | cool blue-sepia wash over each photo (multiply) |
| `--accent-warm` | `#c9a86a` | sparing: year underline, rules, dividers |

**Photo grade (every image, so cuts feel like one film):**
`grayscale(1) contrast(1.08) brightness(0.92) sepia(0.12)` + the `--grade-wash` layer
in `mix-blend-mode: multiply`. Net: desaturated, cool shadows, faint warm midtones.

## Typography (both embed in HyperFrames — never fall back to Inter/Helvetica/system-ui)
- **YEAR / numerals:** **Archivo Black**, huge (140–160 px), letter-spacing −0.01em, `text-shadow: 0 6px 40px rgba(0,0,0,.55)`. (Alternates: Anton / Montserrat 800 — pick one, stay consistent.)
- **TITLE:** **Playfair Display** (high-contrast serif) 500–700, 56–66 px, on a `--band` rectangle.
- **CAPTION (one line):** Playfair Display *italic*, 28–32 px, `--ink-soft`.

## Layout
Left-aligned, vertically-centered text block; title-safe padding ≥160 px (use flex
padding, never `position:absolute; top:Npx`). Order: **YEAR → TITLE (on band) → caption**.
Title card + outro are centered. "Produced" detailing (what separates produced from
generic): thin `--accent-warm` rule under the year, a small uppercase kicker
(`EST. 1841` / `№ 03`), and a faint vintage paper/printed-text texture anchored to the
right+bottom edges (~8–14% opacity).

## Motion language
- **Ken Burns** every photo: `scale 1.0 → 1.12–1.16` + few-% drift, `sine.inOut`, whole scene, alternating direction scene-to-scene.
- **Parallax depth:** photo (near) drifts MORE than text (`xPercent`, text ~25–35% of photo travel). Subtle — depth, not motion-sickness.
- **Text entrance:** YEAR rises first (`y:40, opacity:0 → power3.out, 0.7s`), TITLE +0.12s, caption +0.28s, hold, dissolve.
- **Transitions:** ~1.0 s cross-dissolve; a soft white bloom (`css-light`) only at 2–3 act breaks. No hard cuts, no flashy wipes — stately and nostalgic.

## Texture overlays (persistent, full-duration top tracks)
Film grain — **deterministic** SVG `feTurbulence` (fixed seed), desaturated, `soft-light`
~6–10% (or a looping grain `<video>`, direct child of root; never `Math.random`/`Date.now`).
Vignette — CSS radial-gradient to ~0.6 at corners. Paper — faint aged-paper scan, edge-anchored.

## Audio
Music: one nostalgic cinematic track ~4:05, slowly building — *"wistful nostalgic
orchestral, soft piano + warm strings, gentle swell, vintage, period documentary."*
Optional VO: warm unhurried documentary narrator; **duck music ~-8 dB under VO**.

## Determinism / render contract (non-negotiable — HyperFrames will reject otherwise)
One `gsap.timeline({paused:true})` on `window.__timelines["<id>"]`; no
`Date.now()`/`performance.now()`/unseeded `Math.random()`/network at render; no
`repeat:-1`; animate only `x,y,scale,rotation,opacity,color,backgroundColor,borderRadius`
(never width/height/top/left/display/visibility); root explicitly sized, full-screen
fills on a full-bleed child; `<video>`/`<audio>` direct children of root; pass
`hyperframes lint`/`validate`/`inspect` at 0 errors before preview. Full pipeline: [[../videos/video-hist-01-travel/production-runbook]].

## Thumbnails (rule learned 2026-07-17, Pompeii v1–v4 rejected)
**The thumbnail must live in the video's own design system, not YouTube-clickbait grammar.**
Rejected style: saturated orange/teal AI collage, shocked-face subject, red text box, heavy outline
sans — clashes with the muted film-photo aesthetic of the videos and reads as AI slop.
Working recipe (thumb-v5–v8): full-bleed real frame from the video (or its curated stills) →
dark gradient shade on the text side → Playfair Display title (`--ink #f4f1ea`, 128–168 px at 1280×720)
→ small Inter-800 tracked-uppercase kicker with one `--ember` accent word → optional thin
`--pompeii-red` rule. Split-frame before/after (green pastoral | ash street, red seam, timestamp chips)
is the high-concept variant. Build: plain HTML/CSS + headless Chrome screenshot
(`google-chrome --headless=new --window-size=1280,720 --screenshot`), fonts from the project's
`assets/fonts/`.
