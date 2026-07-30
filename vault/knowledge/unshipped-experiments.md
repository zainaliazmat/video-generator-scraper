---
summary: The four HyperFrames projects built for practice and never uploaded (soul-of-coffee, iron-horse-of-the-indus, watercolor-ink-brand-film, dark-truth-social) — what each was, the durable technique each proved, and where its code now lives. Creator decision 2026-07-31 — learning-only, will not ship; studio dirs deleted, code kept text-only in `../../compositions/`.
updated: 2026-07-31
source: the four projects' own DESIGN/runbook/script docs, read before deletion 2026-07-31
---

# Unshipped experiments — what the practice builds taught

Four projects were built in the studio, never uploaded, and retired on **2026-07-31**
(creator: *"other videos are just for learning purposes i wont upload them"*). They were
not wasted: each one proved a technique the shipped work now uses, and two of them are
**reusable templates** rather than videos.

**Where the code lives now:** `compositions/<slug>/` — text-only, git-tracked, complete
(HTML composition + design docs + scripts). The renders, images and audio are gone.
Unlike a shipped video these have **no `vault/videos/<slug>/` note** — a milestone note
records a delivery, and there was none.

| Project | What it was | Kept in `compositions/` |
|---|---|---|
| **watercolor-ink-brand-film** | A **production pack, not a video** — the "Historical Memories" watercolor-ink style specified end to end (pack + copy-paste Claude Code prompts + a working reference scene). Never built as itself. | `PRODUCTION-PACK.md`, `CLAUDE-CODE-PROMPTS.md`, `reference-scene.html`, `scene_still.png` |
| **soul-of-coffee** | The pack above **executed** — a 238 s / 24-scene HistoryFramesFilm brand film, bean-to-cup, VO drafted and imaged, rendered to draft. The furthest-along unshipped piece. | `index.html`, `build-composition.mjs`, `_shared.css`, `SCRIPT-VO-DRAFT.md`, audio JSON |
| **iron-horse-of-the-indus** | A 26-scene / 8:57 vintage archival documentary on the North Western Railway, written as a **client brand film** (the outro carries a `[CLIENT LOGO]` slot). Research → script → storyboard → narration all complete; draft rendered. | `PRODUCTION_RUNBOOK.md`, `DESIGN.md`, `ASSET_SHORTCUTS.md`, `docs/{research,script,storyboard,narration}.md`, `index.html`, `CREDITS.txt` |
| **dark-truth-social** | A 4:00 editorial **motion-graphics** piece (grunge / spray-paint / halftone), Tailwind-v4 + Lottie. The only non-photographic register ever built here. | `DESIGN.md`, `index.html`, `compositions/*.html` (shader wipes), `hyperframes.json` |

## The durable techniques (this is why the four were worth building)

1. **Build ONE scene template perfectly, then mass-produce.** watercolor-ink's stated
   golden rule — *"do not try to build 24 scenes from scratch"* — is what let
   soul-of-coffee reach 24 scenes at all. Every scene is the same machine with different
   content: paper → ink-masked photo that spreads open → watery SVG-displaced edges →
   desaturated base with a full-colour copy bleeding through the same mask → Ken Burns →
   type → grain/vignette → ink-splatter wipe. This is the same instinct the finance lane
   later hard-coded as a shared `blockframe.css` template.
2. **On-screen text stays poetic; facts live in the VO.** soul-of-coffee's review pass
   found the composition already had title + subtitle + one line per scene, so adding
   researched facts on screen would have doubled the text. Only two lines were re-pointed
   to carry a fact. Same rule the finance cuts obey from the other direction.
3. **Not every beat is narrated.** ~20 of 24 scenes carry VO; the rest are deliberately
   music-only, *"and that restraint is what makes the narrated moments land."* Pace
   target: **~2.3 words/sec** so documentary VO breathes.
4. **Uniform-scene arithmetic beats hand-timed scenes.** iron-horse: every body scene is
   21.7 s starting at `14.0 + (k−1)·20.7`, so each begins exactly 1.0 s before the
   previous ends → a clean 1.0 s cross-dissolve everywhere and **zero accumulated drift**,
   with the total falling out as arithmetic (536.8 s). Only the title and outro are
   special-cased. Reach for this whenever scene length isn't dictated by VO.
5. **A sourcing table with one caveat per image.** iron-horse's asset table names, for
   every single scene, the specific mistake available to make: Empress Bridge spans the
   **Sutlej not the Indus**; the Lansdowne frame must not include the 1962 Ayub Bridge;
   the three Quetta routes (1886 Bolan / 1887 Chappar / 1894 Mushkaf) are distinct events;
   Mughalpura is 1904 not the unconfirmed 1912. Generalises [[../videos/video-hist-01-travel/index|the
   date-quibble rule]]: **the caveat belongs next to the search link, not in a reviewer's head.**
6. **Ethical restraint is a spec line, not a vibe.** iron-horse's Partition scenes carry
   written rules — quiet, non-graphic, verify date *and* side, never gore / ghost-train /
   named-massacre, *"when in doubt, the emptier, quieter frame"* — plus a pre-delivery
   checkbox that enforces them. Same shape as the no-revered-faces rule
   ([[depiction-no-prophet-faces]] in memory): put it in the checklist or it doesn't hold.
7. **The critique pass.** soul-of-coffee kept a `critique/` directory with a full proxy
   frame per scene, an all-scenes contact sheet, and **paired before/after stills** for
   each fix (grain, outro trim, text fade). Reviewing a grid instead of a video is what
   makes a grade inconsistency visible — the ancestor of the max-density snapshot pass the
   finance pipeline now runs. Contact sheet after **any** photo swap.
8. **A fourth design register exists and is unused.** dark-truth-social is cream paper
   `#F2EED6` + spray-green `#2E5E1F`, Rubik Spray Paint / Roboto Slab / Space Mono,
   1-bit halftone photos with hand-drawn outlines, kinetic type and orbiting clusters —
   no photography grade at all. Nothing shipped has ever looked like it. If a channel ever
   needs a loud editorial look, the tokens and the shader wipes are already written:
   `compositions/dark-truth-social/DESIGN.md`.

## What was lost on purpose

Renders, scene photography, VO wavs, the critique stills and the Kokoro audio — ~2.2 GB.
Rebuilding any of the four re-pays image sourcing and TTS off the archived docs. That is
the accepted price for projects that were always practice.

Related: [[design-cinematic-history]] · [[design-techtooltester]] ·
[[design-finance-blockframe]] · [[../skills/hyperframes_production]] ·
[[../videos/video-hist-01-travel/index]]
