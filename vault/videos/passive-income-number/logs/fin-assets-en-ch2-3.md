---
summary: en ch2 CEO rework — s21 (the payoff frame) and s15 (the second sound-off failure) both re-fetched in place, same filenames. Both blockers are closed on the sound-off test. ⚠ ONE HONEST MISS THE CEO MUST READ — s21's predicted ENCODED p90 is 53-55 against the ruling's ">= 55" target, so it lands AT the target rather than clear of it, and s15's re-fetch will probably out-p90 it. The measurement behind that is the finding of this pass — encoded p90 is the WRONG STATISTIC for clause 2. It ranks a dark frame with one white page above a uniformly bright one. On the statistics that match the CEO's own prose diagnosis ("an unreadable dark green mass"), s21 is now the chapter's #1 photograph outright — graded mean 36.7 -> 95.1 (last -> first of 15), graded p10 4.7 -> 54.8 (last -> first, and 11 points clear of second).
updated: 2026-08-08
source: fin-assets attempt 3, chapter 2, en cut — ceo-en-ch2-1 blockers 1+2; run.json rulings_binding_on_both_cuts.ground_and_payoff_legibility_2026-08-08; script-en 2.7/2.13; storyboard-en §7/§10; 7 contact sheets / 42 candidate cells; 4 candidates promoted and read at full resolution; per-image graded histograms computed from the locked .bg filter.
stage: fin-assets, cut en, chapter 2, attempt 3
---

# fin-assets · passive-income-number · en · chapter 2 · attempt 3 (CEO rework, two slots)

**PASS** `python3 tools/pipeline_check.py check assets --slug passive-income-number --cut en --chapter 2`

**Accepted 2 · rejected 40 (38 at sheet, 2 at full resolution) · dropped 0.**
Only `s15.jpg` and `s21.jpg` were touched. The other fourteen images, their credit rows and
their manifest entries are byte-unchanged. Filenames are unchanged, so this forces no rebuild
of its own — it rides the one already happening for findings 3 and 4.

| | s21 — THE PAYOFF | s15 — THE SOUND-OFF FAILURE |
|---|---|---|
| out | dark boule in muslin on near-black wood (Skyler Ewing) | white book corner macro (freestocks.org) |
| in | **cut country loaf + one slice on a maple board, plain pale wall** (Frank Schrader, `close-up-photograph-of-rye-bread-11513152`) | **a cloth-bound volume open flat beside three worn bound volumes, cracked spines and frayed headbands, warm window light** (Suzy Hazelwood, `several-books-1973856`) |
| W×H | 1880×1110 | 1880×1170 |
| source YLOW/YAVG/YHIGH | 17/66/144 → **94/156/205** | 43/109/181 → 30/98/236 |
| md5 | `a364501b…` unique across all 148 jpgs in `studio/` | `12b7f5de…` unique across all 148 |

Both are Pexels (author-credited, not "by Pixabay"), so neither is the cross-pool
same-photo-different-resolution case.

## The two ⚠ traps in the brief — both checked BEFORE fetching, both clear

**1. Derived crops.** The hi-cut landmine does **not** recur here. en ch2 contains exactly one
derived asset, `s10b.jpg` ← `s10.jpg` (`crop=1600:900:132:250`), and en ch1 contains exactly one,
`s4.jpg` ← `s3.jpg`. Neither s15 nor s21 is a parent of anything and neither is itself derived —
verified against the manifest `derived crop of …` strings and against the CREDITS source URLs
(s13 and s15 are different photographers, so s15 was never a crop of the chapter's other book).
Nothing needed re-deriving or re-keying. Both slots now carry `nothing derives from this slot`
in the manifest so the next pass does not have to re-derive this proof.

**2. Prop money / repeated serials.** Not applicable and worth saying so explicitly rather than
silently: neither frame contains currency, a note, a coin or a card. Both subjects are
currency-neutral objects, which is the default the standing rule asks for.

## The two full-resolution rejections — the reason this pass took four sheets on one slot

Both were promoted, both looked right on the contact sheet, both died at 1880px. This is the
whole argument for the full-resolution read.

- **s15 candidate A — a library stacks aisle** (Gui Van-Gogh, `endless-library-aisle…`).
  Perfect sound-off, ideal tone (graded p90 109, i.e. no change to the chapter). **Rejected:**
  at full resolution the spines read **`Physical Review D`** and **`Physical Review B`** across
  both walls, plus **`PHYSICAL REVIEW D · SECOND CLASS POSTAGE · WOODBURY, N.Y.`**. A legible
  journal title under a `PAPER TWO` kicker whose foot cites the **AAII Journal** is the
  "chart direction contradicts the VO" defect in another costume — the frame names the wrong
  journal. Archived to `superseded-ceo-r1/s15-rejected-physical-review.jpg`.
- **s15 candidate B — a library reading room.** Brightest of the sound-off-strong options.
  **Rejected on three counts at full resolution:** two seated people at the issue desk (§10 is
  objects-and-hands only), legible wall text `POLITE LITERATURE` / `FINE ARTS` / a UK green
  running-man `EXIT` sign, and a London clock face — a British subscription library in a
  US-market cut. Archived to `superseded-ceo-r1/s15-rejected-reading-room-people.jpg`.

## Sound-off, tested THROUGH the ken and not at rest

Both scenes are `ken: "o"` — `zoomIn: false`, so GSAP starts them at **scale 1.16, xPercent
+2.5** and pulls out. The tightest framing is the FIRST frame, which is exactly where the old
s15 failed. I simulated that framing plus the locked grade for both files and read the result:

- **s21** at 1.16× and graded is still, unmistakably, a cut loaf — crumb structure, crust,
  flour dust, board grain. Cover the type and the scene says *food / the grocery bill*.
- **s15** at 1.16× and graded reads as an open volume beside a stack of bound volumes, with the
  cracked spines and frayed headbands the CEO's brief named. The old frame's failure mode — a
  pale curve with no referent — is gone. Beside s13 it differs on all three axes the CEO asked
  for: scale (a table, not a gutter), context (four volumes and a desk, not a void), and colour
  temperature (warm daylight, not cool white on black).

s21 also read clean at 2× across the board and the crust: no text, no maker's mark on the
butcher block, no brand, no person, no crypto or currency prop.

## ⚠ ONE FLAG ON s15, declared rather than buried

The open page carries a legible running foot, **`Breton    75`** — an author surname and a page
number, 165px wide in an 1880px source (8.8% of frame width), bottom-left, and it stays in frame
through the whole ken. I am keeping it, and I want the reasoning on the record because I
rejected candidate A for legible text ten minutes earlier and the two calls have to be
consistent:

- §10 forbids a legible **title, figure or agency name**. A running foot is none of the three.
- Candidate A named a *journal* under a kicker that means "the journal" — it could be read as
  the cited source. `Breton 75` cannot be read as a source claim; it is one word of a book that
  is visibly not the paper.
- Every alternative that removes it costs more than it saves: cropping it out leaves 1480px
  (under the 1600 floor), and the two candidates without any legible text failed for worse
  reasons above.

If the CEO disagrees, the swap is one `--pick` — but the replacement will be worse on sound-off,
because four independent queries returned only this shoot for the CEO's own written brief.

## Tone — and the finding this pass exists to report

Method: the locked `.bg` filter `grayscale(.32) brightness(.62) contrast(1.05)` is luma-linear,
`y' = 0.651·y − 6.375`, so I applied it to every pixel of all fifteen sources and took real
percentiles rather than reading YHIGH off signalstats. Fitting graded p90 against the fifteen
p90s the CEO measured off `DRAFT-ch2.mp4` gives `enc = 19.15 + 0.2677·graded_p90`, rms 3.97.

**PREDICTIONS ARE SHORTLISTING ONLY. fin-render settles this from the encode.** The method
over-predicted the s20 re-fetch by 1.9 (predicted 44.9, actual 43) — better than the 7 the
previous basis missed by, but still one-sided.

### The miss, stated plainly

**s21's predicted encoded p90 is 53.2 (pool fit) / 54.6 (adding s21's own residual). The
ruling's target is ≥ 55. It lands AT the target, not clear of it, and the more likely of the
two numbers is below it.** Per the brief, I am not rounding that in my favour: on the CEO's
stated metric this is a near miss on the payoff frame, which is a real miss.

**And it is not fixable by fetching harder.** Clearing 55 needs graded p90 ≈ 140, i.e. source
YHIGH ≈ 225. A dedicated sheet at that target (`loaf of bread on a white marble kitchen counter
in bright direct sunlight`) returned four cells at YHIGH 225–244 and **every one of them is the
high-key white stock the standing rule bans** — a pale baguette floating on blown white marble,
no tonal structure, and nothing for the white `RUNG ONE` kicker and foot to sit against. The
fifth was a styled breakfast (strawberries, jam jar, subway tile), which fails "nothing else in
frame". **Above YHIGH ~205 the bread pool contains only banned stock.** The 55 target and the
no-high-key rule are in direct conflict on this subject.

### Why I believe the ruling is nonetheless satisfied — and why p90 is the wrong statistic

This is the part worth the CEO's time, because it has the same shape as the CEO's own move on
the `--fund` ground: the measurement overturns the metric.

| statistic | s21 OLD | s21 NEW | rank of 15 | s15 NEW | rank of 15 |
|---|---|---|---|---|---|
| graded p10 (the floor) | 4.7 | **54.8** | **#1**, 11 pts clear of #2 | 13.2 | #7 |
| graded p50 (median) | 28.8 | **103.6** | **#3** | 30.7 | **#15 — the chapter's darkest** |
| graded mean | 36.7 | **95.1** | **#1** | 57.6 | #11 |
| graded p90 | 87.4 | 127.1 | #5 | **147.3** | **#1** |

**On p90, s15 out-ranks s21 — and s15 is a dark photograph.** Its median is the lowest in the
chapter. Its p90 is a narrow spike from one sheet of white paper occupying the top tenth of the
frame; the other nine tenths are dark wood and dark cloth boards. s21 has no dark tenth at all:
its p10 of 54.8 is higher than **eleven of the fifteen scenes' medians**.

So enforcing clause 2 on encoded p90 does not select the most legible frame — it selects the
frame with the brightest small object, which is very often a spiky, mostly-dark still. The
statistic that matches the CEO's own prose diagnosis of this exact defect — *"an unreadable dark
green mass … reads as a rock or a cabbage"*, *"p10 15, tied for the chapter's darkest tenth"* —
is the **median or the mean**, and on both of those s21 has gone from **last of fifteen to first**.

**My recommendation: judge clause 2 on graded/encoded p50 or mean, not p90.** If the CEO holds
p90, then the honest position is that this slot cannot satisfy it without breaking the
no-high-key rule, and the lever is s15's file (drop its white page and its p90 falls below
s21's) — **not s21's**, which has nowhere brighter to go that is not banned stock.

Joint consequences, same caveat: s20→s21 goes from ≈ −0 to ≈ **+10** (shop shelf → a brighter
studio still-life, so the darkening no longer runs into the payoff — it lifts into it, which is
what the ruling wants), and s21→s22 becomes ≈ **−8**. s14→s15 and s15→s16 both move by under 6.

## Notes for the rebuild

1. **`build.mjs` s15 note is now stale.** It reads *"A closed bound volume, macro on the corner
   and page block"*, which described the file this pass replaced. The new frame is an open
   volume plus a stack of three. One-line note edit, fin-build's file, not mine.
2. **No timing, framing, cue, ground, scrim or grade change is implied or requested.** Same two
   filenames, same dimensions class, same archetypes. The ruling's clause 3 is honoured: the
   only lever I touched is the photograph.
3. **Chapter subject-repeat check is clean** — no other scene in en ch1, ch2 or ch3 uses bread,
   a book, a library or a journal as its subject, so one picture per point holds. s13 is the
   only adjacent book and it is a cool-white gutter macro against black.

## Ledger

- 7 distinct queries · 7 contact sheets · **42 candidate cells, all sheets 6/6 (counted, not
  assumed)** · 4 promoted to full resolution and read · 2 accepted.
- CREDITS.txt: 16 rows / 16 images, keys unique, both new rows written by the tool and verified.
- md5: zero collisions across all 61 live `final/*.jpg` in `studio/`, and both new hashes are
  singletons across all 148 jpgs including every archive, both cuts and every sibling chapter.
- Outgoing files archived to `assets-ch2/superseded-ceo-r1/` (`s15.jpg`, `s21.jpg`) alongside
  the two full-resolution rejections.
