---
summary: CEO gate, hi chapter 1, attempt 1 — REWORK, 1 blocker. The editor's three rounds all closed; nothing regressed. The blocker is one the scene-by-scene pass structurally cannot see: s6's three-cell cascade — the chapter's one drawn mechanism and its longest scene — fires 1.4-2.8s AHEAD of the three nouns it counts and finishes 0.2s before the first one is spoken, leaving 5.07s with no event while the voice reads a list the picture already completed. Fix is three numbers. Also rules the two questions escalated here: s7's five rungs (UPHELD §8, no overlay and no re-fetch, binds ch3-7) and the hi cut's tone format (ch1 stands, the invariant is stated).
updated: 2026-08-08
source: renders/DRAFT-ch1.mp4 (1275f/42.500s) + regenerated SHEET/SHEET.json + 18 sampled frames + index.html animation calls + assets/audio.json + measured RMS envelopes of assets/voice/1.2.mp3 and 1.6.mp3 (and en ch1's 1.6.mp3 for comparison) + editor-hi-ch1-styleE-{1,2,3}.md + run.json constraints/chapters.hi.1/chapters.en.1 + storyboard-hi.md §1/§8 + video-studies/passive-income-number.md (hook section) + ceo-en-ch1-1.md
stage: fin-ceo, cut hi, chapter 1, attempt 1
---

# CEO · passive-income-number · hi · chapter 1 · attempt 1
VERDICT: REWORK

**BLOCKERS: 1 · RULINGS: 2 · NOTES: 5**

## Would I keep watching?

For the first twenty-four seconds, yes — and it is the best cold open either cut has
produced. It runs the study's proven twin structure (wake → no alarm → window → money →
one buzz → *you did not get rich, you hit a number*) and **beats both twins to the
withheld noun**: twin A announces at 0:22, twin B names it at 0:45, and s5 lands
«आप एक ख़ास नंबर तक पहुँचे हैं» over a literal enamel **275** at **18.0s**. The payoff
beat is whole — one photograph, one continuous zoom, a legible phone under an opaque ₹
card, and the buzz on «बजता है» at 15.702. Nothing in the first 24s needs knowledge the
video has not given, and there is no figure on screen to be orphaned.

**Where I would leave: 24.76 → 29.83.** Five seconds with no event, on the chapter's
longest scene, while the voice names three things the picture finished naming before it
started. That is finding 1 and it is the blocker. It is also not a taste call — it is
measured below against the voice track, which is the one thing a scene-by-scene pass
cannot check from inside a scene.

The chapter ends correctly: 1.8 withholds the condition and closes on an open loop.

## Findings

| # | scene/span | severity | what | fix |
|---|-----------|----------|------|-----|
| 1 | s6, 21.66–29.83 | **BLOCKER** | **The count runs ahead of the words it counts, then the frame dies for five seconds.** Measured from `1.6.mp3`'s own RMS envelope (four internal pauses at rel 1.65–2.25 / 3.35–3.70 / 4.55–4.85 / 5.75–6.15, VO anchored at 21.909), the line's clauses fall at: «उस नंबर का काम एक ही है» **21.91–23.56** · «आपका बिजली का बिल,» **24.16–25.26** · «आपका राशन» **25.61–26.46** · «और आपका किराया» **26.76–27.66** · «चुपचाप भरते रहना।» **28.06–28.91**. The three cells pop at **22.759 / 23.359 / 23.959** and the three ticks draw at 23.109 / 23.709 / 24.309 — so the bulb lands **1.40s** before बिजली, the sack **2.25s** before राशन, the house **2.80s** before किराया, and **all three, plus all three audible `chip` clicks, are complete 0.20s before the first noun's clause even begins** — two of them fire during a 0.6s silent em-dash. Then the last tick settles at **24.759** and the next event is the s7 cut at **29.825**: **5.07s of an unchanging, fully-resolved frame** while the voice does the actual naming. This converts the chapter's one genuinely additive drawn mechanism — the storyboard's own words, *"the count IS the point"* — into a pre-roll, and it puts the dead stretch at 24–30s, the highest-attrition window in a cold open after the first six. | **Re-anchor each cell to its own clause; it is three numbers.** `pop` cell1 at `S.s6 + 2.50` (24.159), cell2 `+ 3.95` (25.609), cell3 `+ 5.10` (26.759); ticks trail +0.35 → 24.51 / 25.96 / 27.11; move the three `chip` cues in `audio.json` to match the cells. The stagger is no longer uniform (1.45 / 1.15) so `popEach` becomes three `pop()` calls — the shape s8 already uses. Result: six events spread 24.16→27.11 instead of six crammed into 1.55s, the dead tail drops **5.07s → 2.72s**, and that tail now carries «चुपचाप भरते रहना» over the completed row, which is the correct settle. **No new asset, no re-fetch, no layout change, nothing else in the chapter is touched.** |
| 2 | s7 | **RULED — ship as is** | See "The s7 ruling" below. Binds ch3–7. | none |
| 3 | s8 foot, 37.07– | note | `A corpus without its withdrawal rate is a promise, not arithmetic` uses **corpus** and **withdrawal rate** at 0:37 with zero setup — neither word has been spoken or shown — and it **answers the question the VO deliberately refuses to answer** («वो शर्त, जिसके बिना कोई भी नंबर सिर्फ़ एक वादा है»). The chapter's closing open loop is narrowed on screen at the moment the voice opens it. The VO carries the beat and this is 26px, so it costs little — but it is the one place the picture argues with the line. | **Free ride on finding 1's render, take it or leave it — it does not gate the next pass.** Either drop the foot (the kicker + stmt + stamp already land the verdict) or replace it with something the viewer already has, e.g. `Every number in this video ships with the rate behind it`. |
| 4 | s3/s4, 8.37–17.99 | note (carried) | Two tea services on one table, in a hook whose whole premise is that **nothing asks of you**. It reads faintly as two people. Compounds the already-accepted European-café finding rather than adding a new one. | none — unfixable in this chapter, and the file is right on every count that matters. **⚠ The live obligation stands: re-read s80's chai-glass callback against this exact file before ch7 is briefed.** |
| 5 | s1, 0.00–4.22 | note | I boosted it: the frame reads clearly as an unmade bed at dawn — duvet, pillow, a pale window. It is dark, and the kicker only arrives at 0.25, but the subject reads and the line is a real hook. The editor's KEEP (restoring the phone would make s1/s3/s4 three dark-phone-on-a-surface frames) is right. | none |
| 6 | s7, 31.6–35.17 | note | 3.5s tail with no event after the stmt settles. I am recording it and **not fixing it**, because every available fix contradicts the ruling I just made two rows up. The ken push into the stairwell is thematically the climb and 5.3s is inside tolerance. | none |
| 7 | whole chapter | note | **It does not read flat and it does not read like a template.** Ground moves 45.7 → 54.4 → 46.7 → 47.9 → 48.3 → **37.7** → 44.6 → 49.6; archetypes alternate A/D/A/A/A/D/B/A with real content on both D's; the drawn art is carrying an idea in both places it appears. s5's enamel **275** under «One specific number» is the frame I would put in front of anyone as proof this is not a generic finance video — it is a better answer to that beat than the en cut's bullseye. | none |

## The s7 ruling — decided once, binds ch3–7

**Uphold storyboard §8. No drawn rungs on s7, and no re-fetch either.** The editor's
recommendation is correct and I am adding the reason it is correct at full strength:

1. **There is no honesty gap to close.** `FIVE RUNGS` is a claim about the *video's
   structure*, stated in the kicker and in the VO. Nothing on screen asserts the
   photograph contains five of anything, and no viewer counts treads in 5.3s.
2. **An overlay would be actively worse than neutral.** I brightness-boosted the frame:
   the stairwell shows roughly **a dozen** treads. Outlining five of twelve would make
   the mismatch *visible* and read as a diagram pasted onto a photograph — the rule-8
   depictive defect §8 refuses by name for 4.10's "three drawn rungs".
3. **The re-fetch is the wrong trade.** The staircase returns at s21, s40, s61 and s79 as
   five different statements. Locking the family to a five-tread frame constrains four
   future scenes to buy a count nobody is counting.

**The rule ch3–7 inherit:** the staircase is the ladder's *metaphor*, never its *inventory*.
Where a count matters it lives in the VO and the kicker, or in a drawn mechanism over an
object the photograph does **not** already contain — s6's sack is the model. Do not raise
this a fourth time.

## The tone ruling — for the hi cut

**ch1 stands exactly as measured (weighted 46.1, opens 45.7, closes 49.6, arc +3.9) and is
not to be flattened, re-graded or touched for tonal reasons in this or any later pass.**
The editor is right that its shape is correct, and the band deletion strengthened it: the
trough (s6, 37.7) is the longest-held and most substantive frame, the peak (s2, 54.4) is a
4.1s throwaway, and the payoff beat now rises instead of dipping.

**The invariant, stated once so both cuts stop rediscovering it from opposite ends:**
ground temperature is assigned by **argumentative weight, not by mood**. In any chapter,
the darkest longest-held frame must be that chapter's most substantive beat, and the
brightest must not be its emptiest. ch1 satisfies this. hi ch2 **inverts** it — brightest
longest-held is a blank notebook page, darkest is the hero corpus — and that, not its
48.0 weighted average, is what is wrong with it. Brightening ch2 without un-inverting it
would fix the number and leave the defect.

**Carried to the ch2 gate:** the −6.4 step from ch1's close (49.6) into ch2's open (43.5)
is inside ch1's grammar but points the wrong way — ch1 climbs, ch2 opens darker and then
goes flat. ch2's open should sit **at or above 49.6**, and ch2 owes the 124s opening its
arc. The en cut reached the same instruction independently (`ceo-en-ch1-1.md` note 2).

## Honesty

Clean. No figure on screen in the chapter, so both rate asserts are vacuously satisfied and
`no_return_promise` / `withdrawal_rate_on_screen` / `derived_income_carries_assumption` have
nothing to bite on. `₹ • • • •` names no amount — it says *money arrived* and refuses to say
how much, which is the right shape. No "retire early", no return implied, no institution or
place implied. The one numeral on screen is a house-number plaque. `hi_currency_framing`
holds — no "dividend" in any form, and the on-screen text is English/Hinglish over Devanagari
VO as the register requires. I would be comfortable if either twin's author watched this.

The one thing I would want the creator to know: **s3/s4 is a European café tea service in an
INR cut.** It asserts no country after the grade and I am accepting it, but I am not going to
pretend it is an Indian chai glass, and it must not book-end the video.

## Regressions vs editor pass

**None.** I checked the two expensive fixes from the encode, not from the construction
argument. `#s3-bg` and `#s4-bg` are one file under one chained ken and the joint reads as a
crop, not a cut — at 14.0s there is one headline and one table. The phone is readable under
the ₹ card at 16.9s with the card's own edge clear of it, so the round-2 band deletion held
and nothing floated back onto nothing. s6's `.band` is intact and still stepping its lower
half back behind the icon row; the deletion did not reach it. s8's stamp and s5's plaque are
untouched. Nothing the editor fixed came back.

## Note for the pipeline, not for this chapter

`popEach(S.sN + 1.10, …, 0.45)` is a **fixed offset that ignores the voice track**, and it is
the root cause of finding 1. I measured en ch1's s6 the same way: its cells complete at 27.551
against a first list-clause starting at 27.701, i.e. the same defect, milder (dead tail 2.9s
against hi's 5.07s). **I am not reopening a locked chapter** — but I am not propagating the
default either. Every remaining chapter in both cuts has a "what X buys" beat with this exact
cascade shape, so the cheapest place this is ever fixed is now: **derive cascade offsets from
the line's measured clause boundaries** (a 0.05s RMS envelope with a −26 dB gate found them in
one pass on both cuts) rather than from a constant. Per the standing rule, that is a default to
correct in the build, not a gate to add.
