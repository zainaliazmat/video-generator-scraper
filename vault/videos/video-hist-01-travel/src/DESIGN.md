# DESIGN.md — "A Century of Travel"

> HyperFrames reads this file as **brand truth** (precedence: `frame.md` → `design.md` → `DESIGN.md`).
> Treat every value here as a hard constraint. Do not invent a different palette, font, or motion language.

## Concept

A cinematic, vintage **parallax photo slideshow** that tells the history of travel decade by decade.
The feeling: an old documentary title sequence — archival black‑and‑white photographs, giant year
numbers, elegant serif titles, gentle camera drift, film grain, and a slow nostalgic score.
**One‑sentence angle:** _the journey itself was once the destination — and we relive that romance, one era at a time._

## Format

- **Resolution:** 1920 × 1080 (16:9), `data-fps="30"`.
- **Length:** ~4:00 (target 235–245 s). Lock final scene durations to the music/VO.
- **Output:** H.264 MP4. (Optionally also export a 1080×1350 4:5 social cut later.)

## Palette (the "vintage blue‑sepia" grade)

| Token           | Hex / value              | Use                                             |
| --------------- | ------------------------ | ----------------------------------------------- |
| `--paper`       | `#0d0f12`                | base / letterbox / behind everything            |
| `--ink`         | `#f4f1ea`                | primary text (warm off‑white, never pure #fff)  |
| `--ink-soft`    | `rgba(244,241,234,0.82)` | captions / secondary text                       |
| `--band`        | `rgba(15,19,24,0.55)`    | semi‑transparent dark band behind titles        |
| `--grade-wash`  | `rgba(28,40,56,0.18)`    | cool blue‑sepia wash over each photo (multiply) |
| `--accent-warm` | `#c9a86a`                | sparing: small rules, year underline, dividers  |

**Photo grade recipe (apply per image):** `grayscale(1) contrast(1.08) brightness(0.92) sepia(0.12)`
plus the `--grade-wash` layer in `mix-blend-mode: multiply`. Net effect: desaturated, cool shadows,
faint warm midtones. Keep it consistent across every scene so cuts feel like one film.

## Typography (both fonts embed in HyperFrames)

- **YEAR / numerals:** **Archivo Black** (heavy grotesque). Huge — 140–160 px. Letter‑spacing −0.01em.
  Subtle `text-shadow: 0 6px 40px rgba(0,0,0,.55)` for legibility over busy photos.
  _(Acceptable alternates if you prefer: Anton, Montserrat 800. Pick one and stay consistent.)_
- **TITLE:** **Playfair Display** (high‑contrast serif), weight 500–700, 56–66 px, sitting on a
  `--band` rectangle. This is the "The History" look from the reference.
- **CAPTION (one line, optional per scene):** Playfair Display **italic**, 28–32 px, `--ink-soft`.
- Never use Inter / Helvetica / system‑ui / Roboto for display text.

## Layout

- **Left‑aligned, vertically centered** text block. Title‑safe padding **≥ 160 px** left/right
  (use padding on a flex column, never `position:absolute; top:Npx`).
- Order top→bottom: **YEAR** → **TITLE (on band)** → **caption**.
- Title card (first scene) and outro are **centered** instead of left‑aligned.
- Foreground "produced" detailing (do this — it's what separates produced from generic): a thin
  `--accent-warm` rule under the year, a small uppercase kicker (e.g. `EST. 1841` / `№ 03`), and a
  faint **vintage printed‑text / manuscript texture** anchored to the right and bottom edges
  (~8–14% opacity) — this is the recurring overlay visible in the reference.

## Motion language

- **Ken Burns** on every photo: slow `scale 1.0 → 1.12–1.16` + a few % `x`/`y` drift,
  `ease: "sine.inOut"`, lasting the whole scene. Alternate drift direction scene‑to‑scene.
- **Parallax depth:** the photo (near plane) drifts **more** than the text layer (use `xPercent`
  on both, text at ~25–35% of the photo's travel). Keep it subtle — depth, not motion‑sickness.
- **Text entrance:** YEAR rises first (`y:40, opacity:0 → power3.out, 0.7s`), then TITLE (+0.12s),
  then caption (+0.28s). Hold fully visible for the scene's "dwell," then dissolve out.
- **Transitions:** slow **cross‑dissolve** between scenes (~1.0 s opacity crossfade on overlapping
  clips). Optionally borrow one or two `css-dissolve` / `css-light` (gentle white bloom) transitions
  from the catalog for variety at act breaks — but the default is a plain dissolve. No hard cuts,
  no flashy wipes; this is a stately, nostalgic piece.

## Texture overlays (persistent, full‑duration clips on the top tracks)

1. **Film grain** — deterministic only. Use SVG `feTurbulence` (fixed `seed`) desaturated, blended
   `soft-light` at ~6–10% opacity; OR a looping grain `.mp4` overlay (a `<video>`, direct child of
   root). **Never** drive grain with `Math.random()` / `Date.now()`.
2. **Vignette** — CSS radial‑gradient (no asset), darkening to ~0.6 alpha at the corners.
3. **Vintage paper / printed‑text** — a faint aged‑paper or old‑newspaper scan, edge‑anchored,
   low opacity, optionally with very slow parallax drift.

## Audio

- **Music:** one nostalgic cinematic track, ~4:05, slowly building. Mood prompt:
  _"wistful nostalgic orchestral, soft piano and warm strings, gentle swelling, vintage, cinematic, period documentary."_
- **Optional VO:** warm, unhurried documentary narrator. If used, **duck the music** ~‑8 dB under VO.
- **Optional SFX:** very light, period‑appropriate beds keyed to a few scenes (steam hiss, distant
  train, ocean, prop‑plane drone, jet) and a soft whoosh under act‑break transitions. Keep subtle.

## Determinism / render rules (non‑negotiable — HyperFrames contract)

- Exactly **one** `gsap.timeline({ paused: true })` registered on `window.__timelines["<id>"]`.
- No `Date.now()` / `performance.now()` / unseeded `Math.random()` / network fetches at render.
- No `repeat: -1` (use finite counts). Animate only the visual allowlist
  (`x`, `y`, `scale`, `rotation`, `opacity`, `color`, `backgroundColor`, `borderRadius`) — never
  `width` / `height` / `top` / `left` / `display` / `visibility`.
- Root `<div data-composition-id>` is explicitly sized (`position:relative; 1920×1080`); full‑screen
  fills go on a **full‑bleed child** (`position:absolute; inset:0`), never on the root.
- Every `id` unique across the assembled page; `<video>`/`<audio>` are **direct children of the root**.
- Must pass `npx hyperframes lint`, `validate`, and `inspect` with **0 errors** before preview.
