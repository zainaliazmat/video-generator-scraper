---
summary: hi ch3 attempt 4 — SHIP, 0 blockers. Re-review of a byte-identical encode (DRAFT-ch3.mp4 md5 b14960a9…, SHEET rebuilt and identical at 283,860 B) run entirely off `tools/packs/fin-ceo.md` instead of the 22 KB note. Verdict unchanged and I never opened the note body to reach it. One real pack finding: the slice starts at `> **BOX` and therefore drops the "extends [[design-finance-blockframe]] — that note owns the tokens, the grade, the scrim, the type ladder and the watermark" pointer, and fin-ceo/fin-editor are the two BOX_DIET entries that do not carry design-finance-blockframe at all, so the reviewers' §"does it look like our channel" check has no rule source in the pack and nothing in the pack signals the gap. Second finding: "Rule 8"/"Rule 9" are box ITEMS 5 and 6 while items 8 and 9 are different rules (no-rail, density) — a positional citation collision that the note carries too, but the pack makes load-bearing because it is now the whole read.
updated: 2026-08-09
source: studio/videos/passive-income-number-hi-ch3/renders/DRAFT-ch3.mp4 (9 fresh frames: 0.30, 1.20, 3.00, 12.60, 17.40, 30.00, 41.00, 55.00, 60.80) + rebuilt SHEET.jpg/SHEET.json, tools/packs/fin-ceo.md, tools/pipeline_check.py:1006-1122 (BOX_DIET + write_box_packs), vault/knowledge/design-chapter-archetypes.md l.8-22 (head only, to diff the slice), script-hi.md ch3, storyboard-hi.md §1, logs/editor-hi-ch3-3.md, logs/ceo-hi-ch3-3.md
stage: fin-ceo, cut hi, chapter 3, attempt 4 — PACK REGRESSION TEST, SHIPPED
---

# CEO · passive-income-number · hi · chapter 3 · attempt 4
VERDICT: SHIP

Nothing below holds the chapter. The encode is the one I passed at attempt 3 and I confirmed
that before reviewing rather than after: `DRAFT-ch3.mp4` md5 `b14960a999b599c8fcbedfbcc2a7d0be`,
61.184s, and a freshly built `SHEET.jpg` byte-for-byte the size of the `SHEET-ch3.jpg` from
18:29. So this log is worth reading only for the `## Pack regression` section; the review above
it is the control.

## Would I keep watching?

Yes, and I still cannot name a timestamp I would leave at. I went looking again with fresh
frames rather than re-reading myself.

**First six seconds.** s22 opens on the terracotta gullak yard with no type for ~0.9s, then
`RUNG TWO` / `AT A 3.0% WITHDRAWAL RATE` and a countUp that is mid-flight at 3.00s
(`₹19,86,111`). That is a mood shot with a soft line on paper — and it works here because it is
a chapter *hand-off*, not a cold open: the VO says «अब दूसरी सीढ़ी» over a picture of many
small containers, and the number is visibly moving before the viewer can decide to leave. A
counting number is the cheapest legitimate retention device we have and it is in the first
three seconds.

**Flat stretch.** None that costs anything. Read as a strip the chapter goes warm terracotta →
cool teal abacus ×2 → dark fan → dark meter → **amber desk** → neutral balance → **red cables**
→ desaturated dawn. The ground genuinely moves and its two extremes land on the two places the
argument turns: amber on s27 «दर वही रही» (the rate is the whole thesis) and red on s29 (the
internet inflating it). Archetype rhythm is A · B · B-plate · C · A · B · B-plate · C · A —
nine scenes, two plates, evenly spaced. Two drawn layers in nine scenes is under the box's
density ceiling and the box is explicit that holding an archetype across consecutive scenes is
correct when they are one argument, which s23→s24 are.

**The ending still closes rather than opens.** «Slow is the trustworthy part» over a resting
bullock cart is a full stop. Unchanged from attempt 2, unchanged disposition: it is the right
line and the fix belongs to s31, which must earn the cut in its own first two seconds. Not a
ch3 defect and it does not re-open this chapter.

**Clarity to a first-timer.** The chapter's whole load is one division and it shows the
division rather than asserting it: ₹20,00,000 → ₹60,000 a year → twelve equal cells → ₹5,000 a
month → what ₹5,000 buys. Every figure sits beside a comparison, and s25 is the comparison —
₹5,000 is "the summer electricity bill, all year", which is the line that makes the number mean
something to someone who has never heard of a withdrawal rate.

**Honesty.** Re-checked on the frames, not on report: 20,00,000 × 3.0% = 60,000, ÷12 = 5,000,
the lit cell is 1 of 12 identical cells. `AT A 3.0% WITHDRAWAL RATE` is a first-class 40px sub
on s24, `ILLUSTRATIVE ARITHMETIC` is in frame, `ILLUSTRATIVE` is on s25/s26/s28. No source, no
seal, no institution implied by any photograph. I would be comfortable with the source author
watching this.

## Findings

| # | scene/span | severity | what | fix |
|---|-----------|----------|------|-----|
| 1 | — | note | Everything in `ceo-hi-ch3-3.md` findings 1–4 stands unchanged: s24's proudness rule, `.art-lift` load-bearing on s24, the ~1.2s empty `.huge` slot I do not want filled, and the four carried items (s27 mid-press → s77, ch4 counterfoil must be paper, `storyboard-hi.md` l.859/l.968 five-rung ladder, s28 `corpus-doubles`). | None re-opens ch3. The storyboard rows are still the only one with a deadline: before ch5 briefs assets. |
| 2 | s22 · 0.0–0.9 | note | The only soft spot in the chapter is the type-free opening beat, and it survives on the countUp arriving inside 3s. | None. Recording it because if a future chapter opens the same way *without* a moving number, that is where it fails. |

## Regressions vs editor pass

**None.** The two things the editor verified on attempt 3 — s22's removed crop window and s24's
`divide-by-12` layer — are both intact on this encode: all four s22 edges carry photograph at
0.30, and the twelve cells with the single green one, `ONE MONTH` and `TWELVE EQUAL MONTHS`
resolve cleanly at 17.40. The s23→s24 abacus hold is still one continuous push across 12.60.
Nothing came back.

## Pack regression

I reviewed this chapter with `tools/packs/fin-ceo.md` (2,963 B) as my only design source. **I
did not open `vault/knowledge/design-chapter-archetypes.md` for any review judgement** — I
opened its first 22 lines only to diff the slice against the note, which is this section's job,
not the chapter's. No `OPENED-BODY:` is owed. The box's own routing line
("Reviewing (fin-editor, fin-ceo) needs this box and nothing else") was accurate for me.

**1. What is missing — one thing, and it is structural, not a slicing bug.**

`write_box_packs` starts the slice at the line beginning `> **BOX`. The note's opening
blockquote has three lines *above* that, and they are dropped:

> **Code home:** `tools/scaffold/assets/chapter-design.css` … Where this prose and the file
> disagree, **the file wins**. Constants: `tools/format.json chapter_design`.
> Supersedes nothing in [[design-finance-blockframe]]; it *extends* it. **That note still owns
> the tokens, the grade, the scrim, the type ladder and the watermark.**

For fin-build and fin-storyboard the loss is invisible, because `BOX_DIET` hands them
`design-finance-blockframe` anyway. **fin-ceo and fin-editor are the two entries that do not
get it** — and they are precisely the two stages whose job includes "consistency of grade, type
and pacing with the chapters already locked" and "does any frame look like a generic finance
video". So the pack leaves the reviewers with no rule source for grade, scrim, type ladder or
watermark, *and* it has removed the one sentence that would have told them where those rules
live. Under the old regime I inherited that pointer for free by reading the whole note.

It did not cost me this chapter: I judged grade/type/watermark against locked ch1 and ch2, which
is arguably the better test anyway. But if the fix is cheap I would take either — add
`("design-finance-blockframe", [])` to the `fin-ceo` and `fin-editor` rows of `BOX_DIET`, or,
cheaper, have `_box_of` start the slice at the top of the containing blockquote rather than at
the `> **BOX` line, so the "extends / file wins / constants" preamble travels with every box.
I prefer the second: it is one changed index, it fixes the same loss for all five packs at once,
and it makes the pack self-routing instead of silently narrow.

**2. Do my citations still resolve? Yes on text, and there is a numbering collision.**

- **Rule 8** (drawn art is ADDITIVE, never depictive — must assert a proportion, comparison,
  measurement or count) — present, verbatim, unambiguous. It is what I used to accept s24's
  `divide-by-12` and s28's `corpus-doubles`.
- **Rule 9** (never darken a photograph per scene; darken behind with `.band`, or `.art-lift`
  inside the plate) — present, verbatim, unambiguous, and it is what makes my standing s24
  `.art-lift` finding legible without the body.

**The collision:** Rule 8 is box **item 5** and Rule 9 is box **item 6**, while box **item 8**
is "no rail, ever" and box **item 9** is the density ceiling. Two different rules answer to the
numeral 8 and two to the numeral 9 inside a 2,963 B file. The note carries the same collision,
so the pack did not create it — but the note also carries §"Photographs" at l.141/150 where the
Rule 8 / Rule 9 labels sit in prose that disambiguates them, and **the pack has no body, so the
numeral is now the whole referent.** The concrete risk is not mine, it is fin-build's: an
instruction to "apply rule 9" against a pack whose item 9 is a density ceiling is a plausible
way to ship a darkened photograph or a stripped drawn layer. Cheapest fix is in the note, one
line: make items 5 and 6 read `**Rule 8 (box item 5)**` / `**Rule 9 (box item 6)**`, or drop the
legacy "Rule N" names and let the box numbers be the only numbers. Either way it is a note edit,
which is the right home, and every pack picks it up on the next `doctor`.

**3. Would attempt 3's SHIP change on the pack alone? No.**

Every judgement I made this round came out of box items 1, 3, 5, 6, 7 and 9 — archetype
assignment and holding one across consecutive scenes, ground temperature tracking the argument,
additive art, no per-scene darkening, `.centred` and the "fix flatness with content not layouts"
rule, and the density ceiling. All six were in the pack and all six were sufficient. The pack is
1/7th the bytes and cost me nothing on this chapter. Ship it to the other four agents with the
two edits above — the blockquote-preamble one before it reaches fin-editor, since fin-editor is
the other stage the missing `design-finance-blockframe` pointer lands on.
