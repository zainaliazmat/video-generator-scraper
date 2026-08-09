---
summary: The durable design system for the TechToolTester channel (@techtooltester) — tokens, type, layout rules, motion, SFX, outro. Earned over video-02's 8 drafts. Copy these into each video's project DESIGN.md so every video inherits the learning. NOT auto-read by build.mjs (yet) — it's the human/author reference of record.
updated: 2026-07-07
source: distilled from studio/videos/video-02-claude-edits-video/build.mjs (draft-3→8, the CURRENT bright grade) + build-log; supersedes the stale dark grade still sitting in that project's DESIGN.md
stage: ADOPTED for the TechToolTester lane — SUPERSEDED BY knowledge/design-finance-blockframe.md for all finance work
---

# DESIGN — TechToolTester (bright grade)

> The channel's visual register: bright, clean, kinetic — the calm, trustworthy
> counterpoint to hype AI channels. Ref boards: creator's SaaSCendx Pinterest.
> This is the channel default; a specific video may override with a documented reason.

**⚠️ Note:** video-02's own `DESIGN.md` still describes the *original dark editorial grade*
(draft-1) — it drifted out of sync when the build pivoted bright at draft-3. This file is
the corrected, current source of truth. When authoring a new video, copy from HERE.

## Format
- 1920×1080 · 30fps · H.264 MP4.

## Background
- BRIGHT white/pastel drifting gradient — coral + blue + lavender glows, slow drift.
- **No grain. No vignette. No black.** (Draft-2's grain fogged all content — deleted.)

## Palette (current bright tokens)
Pull the live values from `build.mjs`; the roles:
| role | use |
|---|---|
| light bg base | the pastel gradient |
| dark ink | primary text (dark on light) |
| ink-soft | secondary text |
| amber accent | rules, chips, highlights, "one to pay for" isolation |
| red | stamps / warnings / ✗ verdicts only |
| green | ✓ verdicts only |
| white mat + blue-tinted shadow | media panels |

## Type
- Display / big numbers / stamps: **Archivo Black** (Google Fonts, `display=block`).
- Code / terminal / labels / chips: **JetBrains Mono**.
- The local machine lacks these — **never rely on a system font stack for display.**

## Layout & components
- **≤60% panel rule** — media is never full-bleed (except cinematic artifact excerpts).
- **Screen recordings:** white mat, soft blue-tinted shadow, **hollow 10px ring** (a filled
  mat paints over the video — see [[../skills/hyperframes_production]] §1).
- **.card** — one idea, ≤2 lines big type + 1 chip.
- **.chip** — mono label, splits on `·`/`—`, pops one piece at a time.
- **.stamp** — Archivo, red, rotated, slams in (`back.out`) for "WHAT THEY SKIP" beats.
- **.verdict** — two-column skip/try, ✓/✗ green/red.
- **.phone-frame** — portrait clips in a bezel+notch mockup, bg dimmed.
- **Artifact excerpts** play FULL-BLEED, no frame (cinematic moments feel cinematic).

## Motion
- **Kinetic type everywhere:** every `.big`/`.sub`/`.rail-line` word scales in one-by-one
  (kSplit → `.kw` spans, GSAP stagger, `back.out`); accent words get a static glow shadow.
- Pattern interrupt every 30–45s (stamp · chip snap · artifact cut · zoom).
- Planned silence after big reveals.
- Zooms: keyframed clip-path inset synced to scale (root videos can't nest — the clip-path
  keeps the zoom inside the panel; sample on the real eased curve — see the skill §1a).

## SFX (real packs, not synthesized)
- Canon set in `studio/library/sfx/`: boom · whoosh · whoosh2 · pop · shimmer · tick
  (48kHz mono, peak −1dB, fades baked).
- `tick` per kinetic word (cap ~8/scene, round-robin in **time** order) · whoosh on media
  scenes · pop on cards · boom on slams · shimmer on glows.
- Track bands 32–35 so same-track sounds never overlap.

## Outro — STANDING RULE
**Every channel video ends with the channel logo + SUBSCRIBE overlay** (logo pop + pulsing
pill over the last scene). Brand assets: `studio/library/brand/`. Applies to HistoryFramesFilm
too (its own brand assets, same rule).

## Related
- [[../skills/hyperframes_production]] — how the contract + QA + motion mechanics work.
- [[channels]] — the two-channel plan.
