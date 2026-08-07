---
summary: fin-storyboard, en cut, attempt 2 — full rebuild of storyboard-en.md against the style-E 81-line script and the re-measured 527.873s timing.json. 81 scenes, 84 image slots, arch/ground/art on every row, all 14 corpus frames carrying #sN-rate, the 10.596s 2.2 breach resolved with a derived crop under one continuous zoom.
updated: 2026-08-08
source: run.json + script-en.md (attempt 2, post-audit) + timing.json (527.873s) + storyboard-hi.md (skeleton port) + design-finance-blockframe / design-chapter-archetypes / design-chapter-sound / stock-photo-sourcing + format.json + kit.json + tools/audio/cues.py
stage: fin-storyboard, cut en, attempt 2
---

# fin-storyboard · en · attempt 2

**STATUS: ok.** Attempt 1 was superseded, not patched — it was numbered `s1…s78` against a
script that no longer exists. Nothing was carried by index; five of its design decisions were
re-derived and kept on their merits (the measure-ladder, the two-peak treatment, the `.mega`
being the RATE, the no-`/` font guard, the four never-a-screen photo overrides).

## What was rebuilt from zero

| | attempt 1 (stale) | attempt 2 |
|---|---|---|
| scenes | 78 (`s1…s78`) | **81** (`s1…s81`), ch1 s1–s8 · ch2 s9–s23 · ch3 s24–s39 · ch4 s40–s52 · ch5 s53–s68 · ch6 s69–s81 |
| runtime | 497.809s | **527.873s**, every `start`/`dur` verbatim from `timing.json` |
| breach | 4.2/4.3 pair | **s10 (2.2) alone, 10.596s** — the cut's only `max_scene_seconds` breach |
| holds | 3 (same-file `plateKen`) | 3, but each second scene is a **derived crop file** — the mechanism this run's hi cut already proved (`scdet` 0.073 at the joint vs 0.184/0.214 either side) |
| drawn art | 6 | **7**, and three of attempt 1's are gone: the tank layers were refused on rule 8 and on the script's own yield/withdrawal-rate ⚠ |
| SFX | 18 hand-authored | **derived** per chapter by `tools/audio/cues.py`, with the four tables this storyboard owns written out as `cues-tables.json` |

## The four §3c non-negotiables

1. **`arch` / `ground` / `art` on all 81 rows** — §7. Sequences written out and read as a
   rhythm; six held runs each justified as one argument. A `centred` rule that is deterministic
   (a scene centres unless a drawn layer, the Lottie stage or a cascade occupies the other side)
   rather than per-scene taste.
2. **`has-photo` + a real `.bg` on all 81** — §10, `photo_free_scene_ratio` 0, no per-scene
   grade override anywhere.
3. **No rail** — stated in §3 and re-stated in §9a, where the measure label was deliberately set
   to `THE LADDER` rather than `RUNG 3 OF 5`: a rung count is a counter, and counters are what
   the no-rail rule removed.
4. **Timing verbatim.** Nothing re-timed. `data-duration = dur + 0.45` on s1–s80, s81 bare, root
   527.873.

## The rule the video is built around

Fourteen corpus/derived frames, each with a real `#sN-rate` element: s21, s22, s27, s31, s41,
s42, s59, s60, s63, s67, s68, s75, s76, s77. Ported the hi cut's mechanism rather than attempt
1's — **the rate arrives at +1.10, before the number lands** (or as a `pulse`d span inside a
fused focal), because "the assumption is on screen first and the number arrives into it" is the
constraint's strongest reading and it costs nothing. §4 also names what the build assert must
**not** fire on: a BLS bill ÷ 12 is not a derived income, and s40's `$5,000 A MONTH` is a chosen
input covered by the marker branch.

## Cut-specific items the orchestrator named

- **2.2 (10.596s)** — resolved inside the scene: `s10.jpg` wide on the tank, `s10b.jpg` a
  tighter crop of the **same source** on the tap, swapping at **+6.324** anchored on *"draw"*,
  one continuous `plateKen` 1.00→1.06→1.16. Framings 6.324 + 4.272 = 10.596. Never a
  self-dissolve back to the same file.
- **6.7 slack (6.296s VO, −24.4%)** — nothing on s75 needs a slow reveal. Its three bars ride
  the three cascade cues (no extra cue), assembly finishes ~+4.0 on a 7.096s scene. Declared:
  **judge s75/s76 from the mp4, not the +2.6s contact sheet**, because an enumeration sheets
  mid-cascade and that is not a defect.
- **The tank** — made a four-frame photographic spine (s10, s46, s47, s57) with *tap position*
  as the only variable, because a drawn tank over a photographed tank is rule 8's named failure.
  Flagged as the cut's one real sourcing risk, with the fallback written into the brief rather
  than discovered at fetch time.
- **Two peaks, two treatments** — peak 1 is continuity (the formula completing across one
  unbroken shot, hottest green in the video); peak 2 is rupture (a shove into it, the three
  coldest grounds, the emptiest photograph, no measure bar because it is off the ladder's
  scale), and it is paid a **second** time at s77 with a bar that leaves the frame.

## Lessons from the hi reviews, applied rather than repeated

- Every one of the 78 manifest queries names the **lighting**, not just the object, against the
  `YHIGH ≥ 110` gate and the ~+40 mean R−B warmth predictor. Two script cues were overridden on
  the **material** rule specifically (a blank index card → a blank **enamel** tag; a key on a
  paper envelope → **brass** on dark slate) because matte paper measured dead twice on hi ch1.
- All seven drawn layers are `art-forward` with solid fills and ≥9px strokes; the hi cut's `.18`
  funnel is cited by name as the thing not to repeat, along with the `!important` opacity that
  makes a per-scene inline `opacity` a no-op.
- The yield mechanism at s49 is drawn **as a fraction** (numerator over a heavy rule, quotient
  separate below) precisely so it cannot read as a rising growth curve, which is what the hi
  cut's funnel did.
- The Lottie banner keeps its `$` glyph with the digits masked — hi ch1 masked the amount
  correctly but dropped the currency, so sound-off it said "a notification arrived" rather than
  "money arrived".

## Divergence list

Thirteen entries (D0–D13) with a reason each, plus an explicit ported list. `storyboard-hi.md`
**was read** this time. The load-bearing ones: the chapter maps cannot align (78/7 vs 81/6, and
they part at s8); the whole dividends argument (s53–s64, s77) has no hi analogue because the
word is banned there; not one anchored fraction ports (Brian ~17.31 c/s vs Amrut ~13.03); the
`$` token list must never imply a conversion. **D9 is a back-port item**: the tank is
load-bearing in both style-E scripts, but the hi storyboard on disk is the style-A one and has
no tank — when hi is re-storyboarded, that is the first thing to take from here.

## Owed / flagged, none blocking

1. Four tank frames are the one sourcing risk (fallback declared in §10).
2. s75/s76 want one five-crate photograph wide enough to crop tight on three (fallback declared).
3. Curly quotes are unverified against the 97-codepoint subset — dump `subset.txt` at build.
4. md5 ledger sweep is fin-assets' to run; no hash may repeat across videos or channels.

**Artifacts:** `vault/videos/passive-income-number/storyboard-en.md` ·
`studio/videos/passive-income-number-en/assets/img/manifest.json` (78 fetched keys; 6 derived
crops deliberately carry no key).
