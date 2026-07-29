# DESIGN.md — "Claude Code Just Edited This Entire Video"

> Brand truth for the video-02 composition. Tutorial/workshop register: dark,
> crisp, editorial — the calm counterpoint to hype AI channels. The embedded
> "A Century of Travel" excerpts keep their own vintage grade untouched.

## Format
- 1920×1080 · 30fps · target ~14:30–15:00 · H.264 MP4.
- Narration: Kokoro `bm_george` @0.9 (same voice as the documentary — deliberate; S26 makes it the point).

## Palette
| token | value | use |
|---|---|---|
| `--bg` | `#0b0d10` | base behind everything |
| `--ink` | `#f2efe9` | primary text |
| `--ink-soft` | `rgba(242,239,233,.72)` | secondary |
| `--amber` | `#e0a458` | accent: rules, chips, highlights (echoes century's `--accent-warm`) |
| `--red` | `#c8442c` | stamps / warnings only |
| `--green` | `#4d9d6a` | ✓ verdicts only |
| `--panel` | `#12151a` | cards / screen frames |
| `--line` | `rgba(242,239,233,.14)` | hairlines |

## Type
- Display / stamps / big numbers: **Archivo Black** (compiler-bundled), tight, uppercase for stamps.
- Body / captions: **Inter**-fallback system stack is FORBIDDEN for display; body uses Playfair Display only inside artifact-referencing moments; general UI text = Archivo Black (short) or the mono.
- Code / terminal / labels: `"JetBrains Mono", ui-monospace, monospace`.

## Layout & components
- **.screen-frame** — screen recordings sit in a 1620px rounded (18px) panel, 1px `--line` border, deep shadow; slight 1.00→1.03 scale drift over the scene (life, not distraction).
- **.card** — centered statements; one idea per card; max 2 lines big type + 1 chip.
- **.chip** — small amber-bordered mono label (`FREE · OPEN SOURCE`, `~5 HOURS`).
- **.stamp** — Archivo, `--red`, rotated −4°, slams in (back.out), for "WHAT THEY SKIP".
- **.verdict** — two-column skip/try card; ✓/✗ in `--green`/`--red`.
- **.phone-frame** — clip-03 (portrait) in a centered phone mockup, bg dimmed.
- Artifact excerpts play FULL-BLEED, no frame — the cinematic moments must feel cinematic.

## Motion
- Default: 0.5s opacity fades between scenes (black base makes sequential fades read as dissolves).
- Cards: rise 24px + fade (power3.out, 0.6s). Stamps: scale 1.4→1 + slam (back.out(2)).
- Screen frames: continuous micro Ken Burns (scale to 1.03, sine.inOut, full scene).
- Planned SILENCE: extra pad after the render reveal (S30), after "stop." (S32), on the verdict card (S45).
- Pattern interrupt at least every 30–45s (stamp, chip snap, artifact cut, zoom).

## Audio
- VO on track 31, volume 1. BGM: none in draft-1 (YT Audio Library track added at a later pass, ducked −18dB under VO, out entirely during the WHERE-IT-BREAKS silences).

## Compliance (Gate 2)
- Music only from YT Audio Library. Altered-content toggle = YES at upload (AI narration is the premise, stated in S27). Every "I tried/tested" claim is real (bot-scroll clip = the 2026-07-02 test; the title-card fix really performed before final render).
