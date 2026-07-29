# DESIGN.md — Vintage Archival Documentary (brand truth)

> HyperFrames reads this as brand truth. Every value is a hard constraint. Do not invent a different palette, font, or motion language. Only the "Concept" section changes per topic.

## Concept — The Iron Horse of the Indus
A stately archival history of the North Western Railway — the iron spine the Scinde Railway, the great Indus bridges, the frontier passes and, finally, Pakistan Railways were built upon — told from the 1850s river steamers to the consolidation of 1974. The register is reverent and elegiac: engineering triumph and imperial ambition braided with the human cost of Partition, never spectacle. It should feel like a lost documentary title sequence — grand bridges over the great river, smoke in the Bolan Pass, and a nation carried into being on rails.
**One-sentence angle:** *Before the rails there was only the river — this is how iron came to the valley of the Indus, and the country it helped carry into being.*

## Format
1920×1080 (16:9), data-fps="30". Length ~4:00 (target 235–245s); lock final scene durations to the audio. Output H.264 MP4. (Optional later: a 1080×1350 4:5 social cut.)

## Palette ("vintage blue-sepia" grade)
| Token | Value | Use |
|---|---|---|
| --paper | #0d0f12 | base / letterbox / behind everything |
| --ink | #f4f1ea | primary text (warm off-white, never pure #fff) |
| --ink-soft | rgba(244,241,234,0.82) | captions / secondary |
| --band | rgba(15,19,24,0.55) | dark band behind titles |
| --grade-overlay | rgba(28,40,56,0.18) | cool blue-sepia wash over each photo (multiply) |
| --accent-warm | #c9a86a | sparing: rule under numeral, kicker, dividers |

**Photo grade recipe (every image):** `grayscale(1) contrast(1.08) brightness(0.92) sepia(0.12)` + the wash layer in `mix-blend-mode:multiply`. Keep identical across scenes so cuts feel like one film.

## Typography (both fonts embed)
- NUMERAL / year: Archivo Black, huge 140–160px, letter-spacing −0.01em, subtle text-shadow for legibility.
- TITLE: Playfair Display, 500–700, 56–66px, on a --band rectangle.
- CAPTION (one line, optional): Playfair Display italic, 28–32px, --ink-soft.
- KICKER: Archivo Black, ~22px, uppercase, wide tracking, --accent-warm (e.g. "№ 03" / "EST. 1841").
- Never Inter/Helvetica/system-ui/Roboto for display text.

## Layout
Left-aligned, vertically centered text block, title-safe padding ≥160px (padding on a flex column, never absolute top:Npx). Order top→bottom: KICKER → NUMERAL (+ thin warm rule) → TITLE (on band) → caption. Title card (first scene) and outro are CENTERED with no band. Edge-anchored faint vintage paper texture (right + bottom) at ~8–14% opacity.

## Motion language
- Ken Burns on every photo: scale 1.0 → 1.12–1.16 + a few % x/y drift, sine.inOut, full scene; alternate direction scene to scene.
- Parallax: text travels ~25–35% of the photo's travel (xPercent on both). Subtle — depth, not motion sickness.
- Text entrance: kicker first, then numeral+rule (y:40, opacity:0 → power3.out, 0.7s), then title (+0.12s), then caption (+0.16s), then hold; dissolve out.
- Transitions: slow ~1.0s cross-dissolve on overlapping clips; optional soft white bloom at 2–3 act breaks. No hard cuts, no wipes.

## Texture overlays (persistent full-duration clips, top tracks)
1. Film grain — deterministic only: SVG feTurbulence (FIXED seed), desaturated, soft-light ~6–10% opacity. Never Math.random/Date.now.
2. Vignette — CSS radial-gradient darkening to ~0.6 alpha at corners.
3. Vintage paper — faint aged scan, edge-anchored, low opacity, optional very slow parallax drift.

## Audio
Music: one nostalgic cinematic period track, ~4:05, slowly building. Mood: "wistful nostalgic orchestral, soft piano and warm strings, gentle swell, vintage, period documentary." Optional warm unhurried documentary VO; duck music ~−8 dB under VO. Optional subtle period-appropriate SFX beds + a soft whoosh under act-break transitions.

## Determinism / render rules
One paused timeline on window.__timelines["main"]; no Date.now/performance.now/unseeded random/network; no repeat:-1; animate only the visual allowlist; full-screen fills on a full-bleed child; unique ids; <video>/<audio> direct children of root. Pass lint/validate/inspect with 0 errors before preview.
