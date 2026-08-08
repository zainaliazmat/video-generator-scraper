# CEO · japanese-money-methods · en · chapter 5 · attempt 2
VERDICT: REWORK

## Would I keep watching?
Mostly yes — and the rebuild is a real jump. The three-scene ten-cell hold
(8.2–27.3s) is the best-looking run in the video so far, the money frames now
argue *for* their lines instead of against them, and 62.2% no longer sits on a
photograph of people correcting a table in red pen. The `.measure-lab` strike-
through is gone in this encode: at 31.0s "MOVED OUT ON DAY ONE" sits clean above
its own bar, filled to 0.20. The `$200` count-up fires (`$126` at 66.5s), so the
3.6s dead gap is closed.

**The timestamp I would leave at is ~44s.** From 34.5s to 57.3s the chapter goes
completely still: s52, s53, s54 are three consecutive one-line statement cards
over three dark photos, same geometry, same 76px type, same pace, no drawn art,
nothing on screen changing for 23 seconds — a quarter of the chapter. s53 is the
worst of it because it is the *palest idea* of the three (an abstract instruction
about account plumbing) sitting on the *darkest, least legible* picture. That is
where a phone gets flipped, and it lands right before the two number cards that
are the chapter's payoff.

The strip is not flat on temperature — neutral → green food → green money → red
(month-end zero) → green → neutral → amber (62.2%) → green → red (the honest
part) → amber. The coldest and hottest beats land on the two turns, correctly.
The flatness is **archetype**: 8 of 12 scenes are `art-off`, 61 of 88 seconds
carry no drawn art at all. Everything after s51 has collapsed to one layout.

## Findings
| # | scene/span | severity | what | fix |
|---|-----------|----------|------|-----|
| 1 | s52–s54 (34.5–57.3s) | blocker | 23s of three identical statement-over-photo cards with nothing moving. The editor's blocker #6 (s53 is a PROCESS beat on a flat photo, `format.json → reach_for_it_when`) was **not** closed by this rebuild — the image was re-sourced, `art-off` was left in place. | Give s53 the art the editor already specified: inline SVG in the s48–s50 idiom (`art-forward art-lift`, fund role) — two separated containers, one arrow leaving the left and landing in the right, repeating a second time to say *every month*. It asserts separation + recurrence, which is exactly what the line names and the photo cannot say. One scene of art breaks the whole 23s run; do not add layouts to s52 or s54. |
| 2 | s55 (56.8–65.4s) | should-fix | `62.2%` at 240px under the kicker "JAPAN'S OWN FIGURE" — the frame never says *62.2% of what*. The only label is `average propensity to consume` in the 18px foot, which is jargon. In a video whose whole thesis is that Japan's **saving** number travels because it sells, a lone 62.2% invites the viewer to read a spend rate as a saving rate — the precise misread this video exists to correct. | Copy-only, same render: kicker → `JAPAN SPENDS` (or foot's first clause promoted to a sub-line, "of take-home pay — spent"). -hi has the same ambiguity; worth carrying back, but this is not a parity gap. |
| 3 | s47 (0–8.6s) | should-fix | The chapter opens on a very dark mood shot of an elderly couple walking away, under the flattest possible head: "An old Okinawan habit, Confucian in origin." That is a dictionary entry. The actual hook is in the VO and nowhere on screen — *"it has nothing to do with money at first."* | Copy-only: move the hook onto the card. Head → "It has nothing to do with money. At first." with `HARA HACHI BU` staying as kicker. Leave the photo (editor's call stands, and the honesty foot is good). |
| 4 | s58 (80.4–88.0s) | note | The chapter-out is "Not saving. Accounting." — a real loop, and correct. But the cliffhanger the VO actually lands ("written by a woman over a hundred years ago") never appears, and s58 is the only scene in the chapter with no foot at all: 7.7s of two static lines. | Add a foot: `written by a woman, over a hundred years ago`. Free, and it is the strongest reason to watch chapter 6. |
| 5 | s53 | note | Head rags badly — "A separate account. Not the one the card / touches." leaves "touches" orphaned on a centred second line. | Falls out naturally if the stack is re-laid for finding 1. |

## Regressions vs editor pass
**None.** Every item the editor called is either fixed or correctly unchanged:
s50 now reads money-on-a-counter and the food→money transfer holds; s52 is the
open empty wallet; s55 is the Japanese apartment block at dusk (the invented-
source-document failure is gone, and it is the right frame because the figure is
Japan's); s56 is a single bill beside a stack, arguing *start smaller*; s48/s49
no longer blow out or fight the grade; s57 is the night road; s58 is ledgers.
Both figures render at `mega` 240px. The ten-cell hold and the 0.20 measure fill
are intact and firing — untouched, as instructed. The `.measure-lab` overlap the
editor could not prove is proven fixed by this encode.

The one carry-over is editor finding #6, which was never actioned. That is not a
regression, but it is the only thing standing between this chapter and SHIP.

## Honesty
Clean, and this is the best-sourced chapter in the cut. 62.2% traces to
facts-staging J4 (HARD, Statistics Bureau FIES 2024 Table I-2-2) and its foot
refuses the cross-country comparison. $800/$3,200 is labelled "an arithmetic
split, not a statistic" — that footnote is exactly right and I want more of it.
$200 is labelled 5% of the same worked example. s47 pre-emptively refuses every
calorie and lifespan figure in circulation. s53 refuses to name a bank, app or
fund. I would be comfortable if the Statistics Bureau's own author watched this.
