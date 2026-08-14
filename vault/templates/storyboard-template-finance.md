---
summary: Storyboard SPEC template for the FINANCE channel (@moneymavens101 $) — dark blockframe, scene-DOM + GSAP cue table, written straight into index.html (no build.mjs). Copy to vault/videos/<slug>/, fill, then build. Forked from storyboard-template.md, which encodes the bright TechToolTester system and does not apply here.
updated: 2026-07-28
source: the shipped needs-vs-wants cut + [[../knowledge/design-finance-blockframe]]
stage: ADOPTED — template for finance cuts
---

# STORYBOARD — <video title> · en cut

**Project:** `studio/videos/<slug>-<cut>/` · **Script:** `script-<cut>.md`
**Design:** [[../knowledge/design-finance-blockframe]] — the **dark** system.
Do **not** use `design-techtooltester` (bright, non-finance) for this format.
**Channel:** @moneymavens101 ($)
**Tier:** <SHORT 9-segment blockframe | MEDIUM 8:30 per-line | LONG >10min per-line>
**Runtime target:** <mm:ss> · **VO:** Brian `nPczCj…`
**Rate:** English ~17.6 chars/s (`tools/format.json`) · **Grade:** dark blockframe

## Colour semantics for THIS video (derived from the thesis — mandatory)

Roles are fixed; meanings are per-video. Fill this in before writing a scene, and
check every coloured element against it. The test: *does any element render in a
colour that argues against the script?*

| Token | This video means | Because |
|---|---|---|
| `--fund` green | | |
| `--warn` red | | |
| `--target` amber | | |
| `--pop` orange | call to action | (fixed) |

## Global guardrails (from the design system)

- Dark `#0d1017` · full-bleed photo under `grayscale(.32) brightness(.62) contrast(1.05)` · four-layer scrim + grain `.05`.
- **One focal element per scene.** Never `.huge` and `.mega` together.
- Reveal spacing **≥0.8s**, except a declared cascade (≤5 items @ 0.6–0.7s). Something on screen by scene start **+0.5s**.
- **≤6 elements** visible at once. **≤3 chips per row, ≤22 chars each** — rows declared explicitly, never left to `flex-wrap`.
- `ken` direction **alternates**, never two pushes in a row. Photo-free scenes get `drift` instead — **no static frame beyond ~2s**.
- **Every scene has a full-bleed bg photo** (creator rule 2026-07-28 — photo-free retired); cut-ins per VO keyword, declared before sourcing.
- Type steps down the ladder (`290 · 112 · 96 · 54 · 46 · 44 · 40 · 32 · 30 · 26`) — never interpolated to fit.
- **No SFX. No logo outro** (neither finance channel has a wordmark yet) — close on `.cta`.

## Scenes

One row per VO segment. Element IDs map straight into `index.html`.

| # | Scene purpose | VO segment | Elements (id · class · copy) | Cue table (offset · helper) | Image slot + query | tint |
|---|---------------|-----------|------------------------------|-----------------------------|--------------------|------|
| s1 | hook — open the loop | h1 | `s1k .kicker` · `s1q .huge` | `+0.40 rise` · `+…` | `s1.jpg` — <query> | red .12 |
| s2 | | h2 | | | `s2.jpg` — <bg query> · cut-ins per VO keyword | |
| … | | | | | | |

**Cue classes.** Mark each cue `anchored` (scales with the clip, lands on its word)
or `fixed` (cascades, arrows, stamp slams — constant regardless of clip length).
Surplus time from a longer clip goes into **holds, never into a cascade**.

## Timing

`scene_duration = 0.4 (VO lead-in) + clip_duration + 1.0 (tail)`
Generated from `timing.json` — never hand-edited. The same numbers live in four
places (`<section>`, the JS `S` map, the `<audio>` row, root `data-duration`);
updating three of four passes every check and ships a broken timeline.

| scene | clip (s) | scene dur | scene start |
|---|---|---|---|
| s1 | | | 0 |
| … | | | |

## `-en` divergence (English cut only)

The `-en` cut is a **US rewrite, not a translation**. List every scene that
deliberately differs from the `-hi` storyboard, with a one-line reason. A `-en`
storyboard with **zero** divergences is a red flag, not a clean port.

| scene | diverges how | why |
|---|---|---|
| | | |

## Deliberate placeholders (must be real before publish)
- <e.g. a stat awaiting a primary source>

## Sign-off
- [ ] Colour semantics table filled and consistent with the script
- [ ] Every number traced to a sourced line
- [ ] No image hash reused from any prior video on either channel
- [ ] Photo-free scenes ≤2, each with `drift`
- [ ] Creator approved (Gate ②) — date: __
