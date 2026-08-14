---
summary: First SHIPPED video on the HistoryFramesFilm (cinematic-history) channel — "A Century of Travel". The delivered milestone + the durable learnings future history videos start FROM, not from scratch.
updated: 2026-07-31
source: `src/` in this folder (production runbook, DESIGN.md, composition, thumbnail) — archived out of studio/videos/a-century-of-travel/ on 2026-07-31
url: https://www.youtube.com/watch?v=qyBqfJGwnEI
status: DELIVERED — scheduled to publish 2026-07-11 02:00 PKT (≈ prior-evening US primetime, ~5pm ET)
---

# Video HIST-01 — "A Century of Travel" (DELIVERED · milestone)

**The channel's first finished, uploaded, scheduled video.** This note is the
milestone marker: everything below is what the *next* history video begins from.
The heavy assets (700 MB render, frame PNGs, caches) were removed post-delivery
per the [[CLAUDE#post-delivery-cleanup]] rule — the video lives on YouTube; the
knowledge lives here.

- **URL:** https://www.youtube.com/watch?v=qyBqfJGwnEI
- **Channel:** HistoryFramesFilm (@historyframesfilm) — the cinematic-history lane ([[../../knowledge/niches/cinematic-history]]).
- **Publish:** scheduled 2026-07-11 02:00 PKT (≈ prior-evening US primetime).
- **Working title:** "The Golden Age of Travel: From Ocean Liners to Jets" (final title/description set on YouTube; titles+desc in English per `english-titles-descriptions` (Claude memory)).
- **Format:** compressed-entire-history — 4:04, 14 scenes, 1841→today. (Note: the niche note had *locked* Pompeii day-in-the-life first; in reality the **compressed-history format shipped first**. [[../video-hist-01-pompeii/index]] remains a drafted, not-yet-shipped day-in-the-life piece.)
- **Style:** vintage B&W parallax history slideshow (Ken Burns + film grain + blue-sepia grade + serif titles), built with HyperFrames + Claude Code.
- **Core idea / tagline:** crossing the world went from *weeks* to *hours* — "how the world learned to wander."

## The reusable artifacts (start future history videos here)
- [[production-runbook]] — the **staged-prompt production playbook** (Prompt 0 → 1 → 2 → 2A/2B → 3). This pipeline shipped a finished 4-min film end-to-end. Copy it; swap topic/assets.
- [[asset-sourcing]] — public-domain sourcing workflow (Library of Congress, Wikimedia Commons, NYPL) — the one thing the pipeline can't do for you.
- [[../../knowledge/design-cinematic-history]] — the durable design system (blue-sepia grade, Archivo Black + Playfair Display, motion language). Copy into each new history video's `DESIGN.md`, exactly like [[../../knowledge/design-techtooltester]] does for the AI-tools channel.
- Thumbnail (kept): `src/THUMBNAIL-a-century-weeks-vs-hours.png` + editable Canva `DAHO62hSEPA`.

## Verified timeline (the script spine — reuse for any "history of X" compressed piece)
1841 first organized tour (Thomas Cook) · 1869 Suez Canal · 1883 Orient Express ·
1897 gilded transatlantic liners · 1907 Mauretania (~4.5-day crossing, record ~30 yrs) ·
1912 grandest liners (Titanic handled *soberly*, not spectacle) · 1927 Lindbergh solo ·
1936 Queen Mary · 1939 Pan Am Clippers · 1952 de Havilland Comet (first jet airliner;
some sources say 1953 — verify vs the sourced image) · 1970 Boeing 747 · today.
> Date-quibble rule: sanity-check each on-screen year against the caption of the photo you actually source — it's the one thing a viewer/client notices.

## Learnings this video PROVED (durable — the growth baseline)
1. **Thumbnail aesthetic is DECOUPLED from video aesthetic.** The film is deliberately muted/vintage (retention); the thumbnail is loud, saturated, liner-vs-jet lightning (click). Confirms *energy beats authenticity* a 2nd time (video-02 was 1st) → logged in [[../../knowledge/best-practices#Thumbnails]].
2. **Thumbnail must state the SUBJECT, not just the payoff.** "WEEKS→HOURS" alone didn't say *what* the video was; adding "180 YEARS OF TRAVEL" made the topic read at a glance. Rule: top line = subject+scale, main line = payoff.
3. **The staged-prompt HyperFrames pipeline works** — a simple-first Stage 1 (renders end-to-end with placeholders) → motion/texture → audio → polish gets to a deliverable film reliably. Always keep a watchable version at every stage.
4. **Public-domain archival sourcing is the human critical path** (6–8 of 13 photos is enough to start; placeholders cover the rest).
5. **Determinism is non-negotiable for HyperFrames render** (one paused timeline, no Math.random/Date.now, visual allowlist only) — see runbook §6 / design note.

## Next history video should be BETTER from here
Don't restart. Reuse the runbook + design system; improve on: (a) apply a stronger
hook in the first 0:15 (per [[../../knowledge/best-practices#Hooks]] — ordinary-life
cold open + dramatic irony from the Pompeii study), (b) add the Islamic/religious POV
angle where a topic authentically carries one (`islamic-pov-in-stories`, Claude memory), (c) measure
CTR/AVD once live and feed it back into [[../../knowledge/best-practices]].

## Published + archived (2026-07-31)

**State: LIVE on YouTube · source archived · studio dir deleted.**

| Cut | Channel | URL | Thumbnail |
|---|---|---|---|
| single (EN) | @historyframesfilm | https://www.youtube.com/watch?v=qyBqfJGwnEI | `src/THUMBNAIL-a-century-weeks-vs-hours.png` |

**Source: `src/`** — `index.html` (the whole 14-scene composition), `DESIGN.md`,
`PRODUCTION_RUNBOOK.md`, `ASSET_SHORTCUTS.md`, the audio request/meta JSON, the
`scenes/s05-1907/` sub-composition and the shipped thumbnail PNG. Both
`studio/videos/a-century-of-travel` and its text mirror `compositions/a-century-of-travel`
are **deleted** — the mirror existed only until this video went through the
finished-video rule ([[../../CLAUDE]]).

**Re-render is not free**, and this one is thinner than the finance archives: the render,
the 12 voice WAVs, the score and 8 of the 13 archival photos were already removed at
delivery (2026-07-10) and the `assets` symlink into `studio/library/projects/` is dangling —
that library is gone. A rebuild re-sources the public-domain photos off
[[asset-sourcing]] and re-cuts the VO. Only `s05_1907_mauretania.jpg` survives, inside
the scene sub-composition.
