# fin-storyboard — passive-income-number · en · attempt 1

**Date:** 2026-08-07 · **Tier:** MEDIUM · **Architecture:** `blockframe-9` + the chapter
archetype layer · **Result:** ok

## Wrote

- `vault/videos/passive-income-number/storyboard-en.md`
- `studio/videos/passive-income-number-en/assets/img/manifest.json` (79 entries)

## Read

`vault/CLAUDE.md` · `run.json` (constraints block) · `script-en.md` **as it stands now**
(the three fin-audit VO rewrites at 5.6 / 6.7 / 6.8 are in the file and were storyboarded from,
not from the pre-audit text) · `timing.json` (78 lines, 497.809s) ·
`knowledge/design-finance-blockframe.md` · `knowledge/design-chapter-archetypes.md` ·
`tools/scaffold/assets/chapter-design.css` · `tools/format.json` · `tools/audio/kit.json` ·
`vault/templates/storyboard-template-finance.md` · `japanese-money-methods/storyboard-en.md`
(shape only) · `japanese-money-methods/src/en-ch2/chapter.json` (the spec shape fin-build
consumes) · `assets/lottie/index.json` · `assets/icons/`.

**Not read, deliberately:** `storyboard-hi.md` (being written in parallel; the orchestrator's
instruction was that this is a US cut, not a mirror) and `design-techtooltester.md` (the wrong
system).

## The four non-negotiables

1. **`arch` / `ground` / `art` on all 78 scenes** — §9, three dedicated columns plus `ctr`.
   Sequences written out and read as a rhythm in §4b; three held runs declared with the
   argument each one serves.
2. **`has-photo` + a real `.bg` on all 78** — 78 bg slots, 0 photo-free frames, `CALMEST`
   marked on the six densest.
3. **No rail** — stated in the header, in §4a and in the §9 row checks. No chapter title, no
   counter, no slide number. The `measure-lab` reads `THE LADDER`, never a rung count, for the
   same reason.
4. **Timing verbatim** — every `start`/`dur` copied from `timing.json`; the row check
   reconciles the last scene to 497.809. Nothing re-timed to make a layout work.

## THE ONE RULE — what I did beyond preserving it

fin-audit had already verified all fourteen corpus frames carry their rate. I did not just
copy them forward; I made the rate **structurally undroppable**:

- On all fourteen, the rate is a **`.sub` 40px element in the scene's role colour** (`sN-rate`),
  not a 26px `--muted` foot. Three of the fourteen carry it inside the focal string instead
  (s19, s40, s56) and are marked as such.
- The rate and the number **share one cue** with a 0.12s internal stagger — *a number without
  its rate is not a number*, so they arrive together. This also solves the 0.8s spacing
  problem that a separate rate cue would have created.
- §6 is a standalone table of all fourteen with the exact rate string, plus three build guards,
  including an element budget that hits exactly 6 on the five rung frames and therefore
  **forbids adding anything else to a rate frame** — no icon, no Lottie, no chip.

## The two peaks (§7)

Deliberately different devices, so peak 2 cannot read as a footnote:

- **Peak 1 (s39/s40, $1.5M at 4.0%)** — continuity. The only place in the cut where **both
  halves of the formula land on one continuous zoom** (vault door, `plateKen` 1.00→1.10→1.24).
  `withdrawal_rate_on_screen` turned into a camera move.
- **Peak 2 (s55, $5,555,556 at 1.08%)** — rupture. A shove into it, the two coldest grounds in
  the video, the emptiest photograph, a `hero`, and **no measure bar** because it is off the
  ladder's scale. Paid a second time at s74, where the completed ladder is drawn and one bar
  runs off the right edge of the frame.
- The cut's **one `.mega`** is neither: it is `ABOUT 1%` at s52. In a video arguing that the
  rate is the whole answer, the rate is the one enormous number and the corpus follows it.
  Also the only choice that cannot overflow — `$5,555,556` at `.arch-b .mega`'s 300px measures
  ~1,520px against `.centred`'s 1500px max-width and would have been clipped.

## The ladder climbs even though housing is rung 3

The monthly figures do not ascend (BLS housing $2,189 < the $5,000 hero) — the **corpus**
figures do, so I drew those instead. One `.measure` component, **one scale, 920px =
$1,963,375**, on six frames: 119 → 156 → 308 → 703 → 920 px. Every one of those is already a
rate frame, so the bar never appears without `AT 4.0%` beside it. The scale is stated as an
arithmetic pair (gotcha 7) and the component is **forbidden at any other scale** — which is
why s55 has no bar at all and the overrun is drawn once, at s74.

## Decisions worth carrying forward

- **6 drawn layers, 0 icons, 0 Lotties.** All five of the script's Lottie candidates were
  declined with a reason each (§8): three are the rule-8 depictive failure against their own
  photograph, two are better as static SVG proportions tied arithmetically to the measure
  ladder. The five library icons all depict what their frame already shows.
- **8 of 78 scenes are non-centred.** That is the honest outcome of a photo-led cut and the
  archetype note predicts it in as many words; the variance is carried by the photograph, the
  ground arc, the focal class, the ladder, the 6 drawn layers, 3 cascades, 3 holds, 2 shoves
  and 18 SFX cues — not by adding layouts for their own sake.
- **`bed-tension`**, because this video's argument is a cost.
- **18 SFX cues, one per 27.7s**, closest pair 6.38s. Seven declared dry beats, including the
  largest number in the video ($7,271,759) and the last 23 seconds before the CTA.
- **One declared ground exception:** s54/s55 run cold on `--warn` scenes. The drop is a
  temperature event before it is a number. Declared so a later pass cannot "fix" it.

## Four background overrides against the script's own `img:` cues

s3, s7, s43, s52 all asked for a lit screen as the background. The design doc's *"never a
phone-screen photo as a background"* rule has shipped violated three times; these cues would
have made it four. Replaced with screen-down / from-behind / turned-away / printed
equivalents that keep the keyword match. Recorded as divergence D9 — the hi cut has to apply
the rule against its own cues, not copy this list.

## Flags for the next stage (none blocking)

1. **`format.json chapter_design` does not exist.** My brief and `fin-build.md` §1a both name
   it as the constants home; `grep` finds no such key anywhere in `tools/`. I took the
   constants from `chapter-design.css` (what renders) and restated the four plate rects in
   §12 so fin-build does not guess. Adding the key is a between-runs edit to `tools/`, which
   this stage may not write.
2. **The script's handoff §6 undercounts the hold pairs** — it says two (1.2→1.3, 6.7→6.8),
   but 4.3's own `img:` cue says "ONE continuous zoom from 4.2". I honoured all three; the
   per-line cue is the more specific home. Not an invention.
3. **`/` is banned cut-wide.** Handoff §8 lists six absent glyphs and replaces the solidus
   with `DIVIDED BY`, which implies `/` is not in the 97-codepoint subset — yet the script's
   own cues use `$5,000 / MONTH` and `$5,000/mo`. Both rewritten (§4) with the reason. Verify
   against a dumped `subset.txt` at build.
4. **s72/s73 need one photograph with five crates of increasing size.** Fallback query and a
   fallback plan are in §12; the drawn bars carry the count either way, which is why both
   scenes are `art: fwd`.

## Divergence list

11 rows (§10), led by **D0: the chapter maps cannot align** — hi runs `1.1 … 7.8` (seven
chapters, per `run.json budget._spend_log`), this cut runs `1.1 … 6.13` (six), so `sN` indices
diverge from s8 and never re-converge. Element *part* names are ported so a fix still travels
(D1); `-rate` is new here and should be back-ported to hi if that cut carries corpus frames.
Stated plainly in §10 that the list is derived from the scripts, `run.json` and the shared
design system rather than from reading `storyboard-hi.md`.

## Counts

**78 scenes** · **82 image slots** (78 bg + 4 cut-ins) · **79 files** (s3/s40/s73 re-use their
hold partner) · 14 rate frames · 6 measure bars · 6 drawn layers · 3 cascades · 3 holds ·
2 shoves · 18 SFX cues · 1 bed · 1 `.mega` · 1 `--pop` · longest scene 8.323s (< 9.0) ·
last scene ends 497.809 = `timing.json` total.
