# CEO · japanese-money-methods · en · chapter 6 · attempt 2
VERDICT: REWORK

## Would I keep watching?

Through 34s, yes. **I would leave at 0:48 (s66).**

Not because s66 is a repeat — it isn't, and that was the call I was asked to make.
The crop is real (`auto 260% @ 86%/55%` against a full bleed), the subject changes
from "spread of bills + document" to one portrait, and the tint drops from red to
neutral. Sampled at 43.5 / 46.5 / 48.5 / 51.0 it reads as a matched zoom, which is
the creator's own continuous-zoom rule working. **s65/s66 passes.**

I would leave at 0:48 because it is the *third consecutive scene with nothing on it
but a sentence*. s64, s65, s66, s67 are four `arch-a has-photo art-off` scenes back to
back — **33.8s → 62.9s, 29 seconds, 28% of the chapter** — same centred stack, same
dark desk, no drawn layer, no number, no comparison. Nine of fifteen scenes in this
chapter are that archetype; the four in a row are where it becomes visible. The
measured ground confirms it: luminance across all fifteen scenes sits in a 27–43
band on 0–255, and inside the flat run it moves 26.9 → 37.0 → 37.4 → 33.6. Nothing
changes but the words.

The worse fact is *which* scene sits in the middle of it. The chapter's Von Restorff
beat — the one the script marks as "the whole differentiator", at 69.4% of the video —
is s65, and s65 is one of the four bare ones.

Temperature itself is fine and I am not asking for more of it: warm swings −13.4 (s63)
to +8.3 (s73), and the two hot beats do land on turns (s65 red, s73 amber). The
problem is not the grade. It is that three scenes have nothing to hold.

**The ending is acceptable.** 6.15 closes on a statistic rather than a question, but
the statistic *is* the tension and ch7 opens on "there is a fourth one". I would not
spend a render on that.

## Findings

| # | scene/span | severity | what | fix |
|---|-----------|----------|------|-----|
| 1 | s65 (40.98–48.68) | blocker | The frame carries **no antecedent and no "four"**. Built markup is `stmt` + `foot` only — the storyboard's `head: THE FOUR CATEGORIES` was never built, and `RAIL OFF` took the rail with it. On screen at 42.4s a first-time viewer reads *"These came later. They are the version that travelled west."* over a photo of dollar bills. **What came later?** Nothing in frame says four, says categories, or names needs/wants/culture/unexpected. Sound-off, at 1.5× on a phone, the video's single differentiating claim is invisible. The new photograph fixed the ground (real surface, no black cut-out) but did not fix the assertion. | Give s65 something real to hold: restore the head `THE FOUR CATEGORIES`, and put the four names on the frame as a four-row list in `--warn` (the `s68` list geometry already exists in this chapter and is proven). That is a markup + cue edit, not a fetch. It fixes the clarity blocker **and** breaks the flat run at its exact centre. |
| 2 | s73 (97.3–104.3) | blocker | Closing frame of the chapter states `4 IN 10` in amber with `63% of adults could cover…` directly beneath it. Two numbers that read as disagreeing, on the last frame, requiring the viewer to compute 100−63 to reconcile them. This is a number without a comparison — it is a number *against* a comparison. | Text edit only, no art: reword the foot so both numbers sit on the same side — e.g. *"63% of adults could cover a $400 emergency with cash or its equivalent; the rest — about 4 in 10 — could not. Federal Reserve SHED 2025, fielded Oct 2025, released 13 May 2026."* `facts-staging.md` U5 already writes the fact this way ("63% (2025) → ~4 in 10 cannot"), so this is a wording fix, not a new claim. |
| 3 | s72 (90.0–97.8) | should-fix | **Editor #10, handed back and still open.** The picture is unchanged — a mechanic under a car on a lift — and `OVER 20%` in red now sits centred on it. The line's second half (a card balance at over 20% a year) has no picture at all, and the composite invites a misread: a big red 20% over a car repair reads as *the repair* costing 20%. The kicker and foot resolve it only for someone who reads the foot, which nobody does at 1.5×. Additionally the `--warn` tint measures +1.8 warm here against s65's +7.8 — the red beat barely registers as one. | As the editor asked: one frame carrying both halves (a hand holding a card over a printed repair invoice), or split `data-framings` — framing 1 the garage, framing 2 the card. |
| 4 | s64 (33.8–41.4) | should-fix | Second-cheapest place to break the flat run, and it has a real thing to assert. *"Saving is decided before spending, not after."* is an **ordering claim** and the frame states it only in words. It is also the run's darkest scene (L=26.9) with a two-element stack and first cue at 34.1s. | Two labelled chips in sequence — `SAVE` lit first, `SPEND` second — asserting the order. Do **not** reuse s71's opposed-arrow device; this is a sequence, not an opposition. |
| 5 | s61 (13.6–20.2) | should-fix | The frame contradicts itself in text. Head: *"Every year since. **Four wartime years missing**."* Foot: *"Over a hundred years of **continuous publication**…"*. A viewer reading both in six seconds is told the run is unbroken and broken. The drawn layer resolves it (the gap renders in `--warn`) but the type does not, and type is what gets read. | Foot → "Over a hundred years in print — the publisher marked the 120th in 2025." Drops "continuous"; the claim survives intact and matches `facts-staging.md` line 108. |
| 6 | s73 (97.3+) | should-fix | **Editor #12, handed back and still open.** A share beat with no drawn art, in a chapter that has four working drawn layers. `.measure` / `.measure-fill` exist in `assets/chapter-design.css` and are used nowhere in either cut. If #2 is done as a text fix, this stays open as the better version of the same fix. | The editor's spec stands: one bar, `COULD COVER $400 IN CASH`, fill to 63%, remaining 37% dark under the `4 IN 10`. Lower priority than #1 — one of #2 or #6, not both. |
| 7 | s59 (0.0–7.5) | note | Chapter opens on a very dark frame (L=36.5) where the ruled ledger — the object the chapter is named after — is barely separable from the bokeh behind it. The cue ladder is correct (head 0.3, stmt 1.1) so the line lands in time; the picture is what is soft. Ships as is. | none — do not spend a fetch. If s59 is ever retouched, lift the ledger, not the whole frame. |
| 8 | s60 | note | Not the Commons portrait or the *Fujin no Tomo* cover that was asked for — it is a period Japanese document in hand. But it no longer asserts the wrong place (the Latin letterpress is gone), it is Japanese, it is period-plausible, and it does not overclaim. Good enough. | none |

## Regressions vs editor pass

**None.** Everything the editor caught that was addressed, stayed fixed:

- s72's cue order is genuinely repaired — head 90.295 → num 91.095 → foot 91.895, ≥0.8s ladder intact. The footnote no longer precedes its number.
- s65/s66 is no longer one picture serving two points (see above).
- s59, s61, s64, s67 took the -hi photographs; s67's planner page now says "start of the month", which was the whole point of that line.
- s70 is an actual face-down phone beside a notebook. Landed.
- s73 is the empty wallet. It states the shortfall, and it is a strictly better picture than the shopping bags.
- All four drawn layers (s61, s63, s68, s71) still fire and still finish inside their scenes. Not re-litigated, spot-checked only.

Two editor findings were **not addressed rather than regressed** — #10 (s72's picture)
and #12 (s73's measure bar). They are carried above as findings 3 and 6.

## Honesty

Clean, with one exception already logged as #5. Every on-screen figure traces:
`OVER 20%` → G.19 May 2026 22.15% (foot carries period and release date, and the
"price evidence, not a recommendation" line is doing real work); `4 IN 10` → SHED 2025
U5; `1904` and `120th in 2025` → publisher primary. s65's foot is the most important
sentence in the chapter for our credibility — *"no Japanese primary attributes them to
Hani Motoko or to 1904"* — and it is correctly hedged. **The problem with s65 is not
that it overclaims; it is that the honest claim is unreadable.** If Fujin no Tomo Sha
watched this chapter they would have no complaint about what we said. They would not
be able to tell what we said.
