---
summary: ONE CHANGE — s5's drawn layer. §7 amended `art: off → ticks`, `ctr: Y → N`; three .icon marks (bulb/sack/house) each taking a tick in sequence at +2.30/+2.95/+3.60. Timing untouched, check passes 0 errors, cues.py reproduces the 7 cues exactly but does NOT leave the file unchanged (it emits 7 inert `_dry` stubs that crash mix.py).
updated: 2026-08-07
source: fin-build attempt 3, chapter 1, hi cut. Clears editor round-2 blocker #1.
---

# fin-build — passive-income-number / hi / chapter 1 / attempt 3

**Scope: s5's drawn layer, and nothing else.** No timing touched, no photograph
touched, no other scene touched. `s5.jpg` is the same file (the incumbent jars,
YHIGH 160, R−B +61.8), `assets-ch1/` was not opened for writing, and s1–s4/s6/s7
are byte-identical to the build fin-editor reviewed at round 2.

## What changed

| file | change |
|---|---|
| `studio/videos/passive-income-number-hi-ch1/build.mjs` | SCENES row 1.5 → `art: "ticks"`, `ctr: false`, `brule: 336`. New `MARKS` table + `TICK_LEN`. `scene()` emits the band/brule for any art scene (not just `lottie`) and a `.v-ticks` row for `ticks`. New `.v-ticks` / `.v-tickcell` in the inline `<style>`. New s5 motion block. |
| `…/index.html` | regenerated. Only s5's `<section>`, the two `.v-` rules and the s5 motion block differ. |
| `assets/icons/light-bulb.svg`, `grain-sack.svg`, `house-door.svg` | **new library files** — colourless, classless, `i-*` ids, `viewBox 0 0 100 100`, matching the five that were already there. The next video inherits them. |
| `vault/videos/passive-income-number/storyboard-hi.md` | §7 row 5 (`art`/`ctr`), the row-check counts (71→70 centred, 7→8 with something on the other side), a ★ amendment note under §7, and §8's icon subsection rewritten to cover s5 + s68 (`off` 73→72, heading `1 icon`→`2 icon scenes`). |

## The design decision, and why it is this shape

**`.icon`, not `.art`.** The task's warning about `art_opacity` (ch2's funnel
invisible at `.18`, fixed at `.3016`) does not apply here and that is deliberate:
`.has-photo .art { opacity: .30 !important }` scopes to `.art`, while
`blockframe.css`'s `.icon` strokes in `currentColor` at **full** opacity. The
whole floor problem is designed out rather than tuned around. This is also what
`vector_art.icon_first` asks for — inline `<svg class="icon">` + `draw()`, no
player, no fetch, no Lottie spent (ch1 keeps 3 of its 4 slots free).

**`ctr: Y → N` follows `art: off → ticks`.** `.centred` exists because `.art-off`
empties the archetype's other side; s5 is archetype D and now has its mechanism
back, so it takes D's geometry exactly as s3 already does in this chapter —
left-aligned stack at the top, `.band`, `.brule`, art owning the bottom
two-thirds. This is the system's own rule applied, not a second decision.

**Rule 8 holds, and the sack is why.** The assertion is a COUNT (three
obligations) being PAID (the verb) — `vector_art.reach_for_it_when` on the
merits. The one place a depictive collision was possible is the ration mark: the
photograph *is* jars of grain, so the middle glyph is a tied **sack**, the
category rather than the object. The editor's spec said "a jar/sack"; sack is
the half that does not re-draw the still.

**Rule 9 holds.** The photograph is not darkened per scene. `.band` darkens
behind the marks, which is the sanctioned mechanism and what s3 already uses.

**No role colour.** §7's focal column says `—` for s5, so the marks are plain
`.icon` on `--ink`. Green ticks would have asserted `fund` on a scene that has
not earned it.

## The sequence — the ticks do not land together

The whole point of the fix, so it is timed explicitly. All offsets are read off
`S.s5`; nothing here re-times anything.

| +offset | abs | what |
|---|---|---|
| 0.15 | 17.273 | `fill("#s5-br")` — D's rule draws in under the type |
| 0.30 | 17.423 | kicker (ladder variant A) |
| 1.10 | 18.223 | statement |
| **1.90** | 19.023 | `fade("#s5-ticks")` — the row arrives **whole**: three glyphs and three EMPTY boxes. This is the COUNT, stated at once |
| **2.30** | 19.423 | `draw("#s5-tick1")` 0.45 s — electricity |
| **2.95** | 20.073 | `draw("#s5-tick2")` — ration |
| **3.60** | 20.723 | `draw("#s5-tick3")` — rent |
| 4.05 | 21.173 | last tick complete; the finished checklist holds **2.13 s** before the dissolve |

0.65 s apart: no two read as simultaneous, and all three are struck well before
the scene ends. They sit under the line's **second** clause — VO 1.5 runs
17.373 s +5.381 s and «चुपचाप भरता रहता है» is roughly its back half — so the
photograph and the type name the three subjects and the ticks answer them.
`chapter_sheet.py`'s +2.6 s sample lands mid-tick-one, which is an honest
in-progress frame, not the half-built-mechanism defect the gotcha warns about.

Geometry: `.v-ticks` is absolutely positioned into archetype D's `.p-d` band
(0,424,1920,656) exactly as `.v-lstage` is on 1.3 — 220 px glyph over a 130 px
checkbox, 376 px tall from y496, so it clears the watermark box (y956+) and sits
at x390–1530, well inside the 150 px safe padding. Not `blockframe`'s `.row`:
that is a child of `.stack`, which D hangs at the TOP of the frame.

## Snapshot pass — 14 frames, TWO batches, every one looked at

One `-o` per batch, never reused.

- **`snapshots/qa/b1` — 7 frames, all reviewed.** Each scene at its last cue:
  1.10 / 5.061 / 12.00 / 13.427 / **21.20** / 24.404 / 31.046. Every `.stack`
  inside the safe area, nothing overflowing, watermark present on all seven.
  s5 at 21.2 s: all three glyphs legible, all three ticked, the type clearing
  the brule at y336.
- **`snapshots/qa/b2` — 7 frames, all reviewed.** s5's own ladder: 17.42 /
  18.30 / 19.50 / 19.723 / 19.95 / 20.60 / 23.20. Confirmed visually that the
  ticks land **one at a time**: 19.50 three empty boxes · 19.723 tick 1
  drawing · 19.95 tick 1 only · 20.60 ticks 1+2 · 23.20 all three.

The CLI's `Navigation timeout of 10000 ms exceeded` was wrapped in a
retry-until-success loop; both batches succeeded on the first attempt this run.

## `hyperframes check` — PASSED, 0 errors

```
Lint      0 error(s), 1 warning(s), 2 info(s)
Runtime   0 errors, 0 warnings
Layout    0 error(s), 0 warning(s), 9 info(s)
Motion    0 errors, 0 warnings
Contrast  10/10 text checks pass WCAG AA
```

Nothing new appeared and **no design token was edited**. The one warning
(`timeline_track_too_dense`) and the infos (`#sN-bg` `container_overflow` — the
`inset:-8%` ken window, by design; `pointer-events:none` on `.grain`) are the
same set the round-2 build carried; `format.json known_benign` is empty by
design and stays empty.

Composition duration **35.745 s**, unchanged. 7 scenes, unchanged starts and
durations, overlap 0.45 s on every joint, tracks alternating 1/2/1/2/1/2/1,
`#root` still carries `cut-hi`. `build.mjs`'s own asserts (gap-per-joint against
`timing.json`, track alternation, last scene lands on the chapter root) all pass
— they are what would have thrown if this touched a timing.

## Audio — 7 cues, and a finding you should act on

Ran `python3 tools/audio/cues.py studio/videos/passive-income-number-hi-ch1
--write` as instructed. **The drawn art changed the count by zero**, as
expected: `dry` covers s1–s7, so a `draw()` on `#s5-tick1` cannot produce a
content cue, and `cues.py`'s framing-swap rule only matches `#sN-bg\d`.

**It reproduces the seven cues exactly** — same names, same times, same order:

```
3.961 transition · 9.776 transition · 10.676 buzz · 12.327 transition
17.123 transition · 23.304 transition · 29.146 transition
```

**But it does NOT leave the file unchanged, and the difference is not cosmetic.**
Alongside the prose deltas (`_comment`, `_density`, the buzz rationale string) it
appends **seven inert `{"_dry": "sN is DRY — …"}` objects into `sfx[]`**.
`tools/audio/mix.py` line 86 does `c['name']` with no guard, so:

```
KeyError: 'name'   # mix.py cannot consume cues.py's own output when `dry` is set
```

Verified by replaying that loop against the written file. So `cues.py --write` is
now correct about *sound* and produces a plan the mixer crashes on — a smaller
bug than the one it fixed, but a real one, and it will bite every chapter that
declares a `dry` list (ch5's s41/s42/s45, ch6's s63/s69/s70). Per the
fix-defaults rule the home is `cues.py` (emit the notes under a top-level
`_dry_notes` key, not as `sfx` entries), with a `if "name" not in c: continue`
guard in `mix.py` as the belt. **I did not edit `tools/` — that is outside this
stage.** `assets/audio.json` was restored by re-running `build.mjs` and is
byte-identical to the shipping file (md5 `1741a3e137260b11eea94cfcfac04c2c`).

## System gaps found (reported, not improvised)

1. **`cues.py` / `mix.py` contract mismatch** — above. The only one that can
   break a render.
2. Carried from attempt 1, still open: `.arch-b .foot`/`.huge`'s 900 px caps are
   not released by `.scene.centred`, patched here as `.v-footwide`. The real fix
   is one rule in `chapter-design.css`.

Nothing was missing from the motion vocabulary — `fade` and `draw` are exactly
the two helpers this needed.
