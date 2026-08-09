---
summary: The storyboard SPEC template — the cheap, creator-reviewable artifact that gets signed off (Gate ②) BEFORE build.mjs runs. Copy to the video project, fill, get sign-off, then mirror into storyboard.mjs. Convention from HeyGen's own hyperframes-launch-video STORYBOARD.md.
updated: 2026-07-07
stage: ADOPTED — template
---

# STORYBOARD — <video title>

**Project:** `studio/videos/<slug>/` · **Script:** `script-vN.md` · **Design:** [[../knowledge/design-techtooltester]] (+ project `DESIGN.md`)
**Runtime target:** <mm:ss> · **VO:** <creator Urdu | Kokoro bm_george> · **Grade:** bright

## Global guardrails (from DESIGN)
- ≤60% media panels · hollow ring mats · kinetic type · bright bg · logo+SUBSCRIBE outro.
- Pattern interrupt every 30–45s. Planned silence after big reveals. Cinematic excerpts full-bleed.

## Beats
One row per VO line. Motion in GSAP terms so it maps straight to code. Keep this in sync with `storyboard.mjs`.

| VO | Concept / mood | Visual (media / card) | Motion | SFX | Transition | ~t |
|----|----------------|-----------------------|--------|-----|------------|----|
| 01 | hook — open the loop | | pop / back.out | whoosh | — | 0:00 |
| 02 | | | | | | |
| … | | | | | | |

## Master timing table
| section | beats | ~duration |
|---|---|---|
| Hook | 01–04 | |
| … | | |
| Outro (logo + SUBSCRIBE) | last | |

## Deliberate placeholders (must become real before publish)
- <e.g. S35 real capture, S37–38 real fix — the "I tested" integrity rule>

## Sign-off
- [ ] Creator approved this spec (Gate ②) — date: __
- [ ] Mirrored into `storyboard.mjs`
