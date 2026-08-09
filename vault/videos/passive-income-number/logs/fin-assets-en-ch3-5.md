---
summary: en ch3 attempt 5 — the CEO's single blocker, s34, could NOT be re-fetched. 19 contact sheets / 111 candidate cells / 5 full-resolution confirmation fetches across BOTH pools, 0 acceptances. The binding constraint is arithmetic: payoff clause 3's p10 ≥ 80 on the composed, graded frame requires a SOURCE 10th-percentile luma of ~133, i.e. a near-full-frame bright page — and every frame in either pool that clears it is a book, a Bible, a headline, a foreign-language page, a brand mark or a table of figures. The one non-book frame that cleared the gate (median 133.1 / p10 110.0) carries `CAZENOVE` and columns of share prices; the one paper frame that cleared it best (146.7 / 125.3) is a GERMAN BIBLE — the family the brief forbids re-opening. Nothing was changed: s34.jpg is byte-identical (md5 b78e3a77…, mtime 2026-08-08 11:18), the manifest is restored to the shipped query, `check assets --chapter 3` still PASSes, md5 dedupe across both cuts is empty. s30 was not touched.
updated: 2026-08-09
source: fin-assets attempt 5, chapter 3, en cut — ceo-en-ch3-1 RULING 1 (blocker), editor-en-ch3-1 finding 2, editor-en-ch3-2 finding 2. Measured on this stage's own reproduction of fin-build's §5 composed-frame chain, re-validated against 7 untouched scenes before it was trusted.
stage: fin-assets, cut en, chapter 3, attempt 5
---

# fin-assets — passive-income-number / en / chapter 3 / attempt 5

**STATUS: fail. Accepted 0 · rejected 111 cells over 19 contact sheets · dropped 0 ·
files changed 0.** Scope was one slot (s34) and one slot only; s30, its feather, its
photograph and every other file in the chapter were never opened for writing.

---

## Ran

1. **Re-validated the measuring instrument before trusting a single number.** Chain:
   cover-crop to 16:9 at the scene's `background-position` (s34 has none, so `center`)
   → the central 86.2% that `.bg { inset:-8% }` shows → the locked grade
   (`grayscale(.32)` chroma-only, `brightness(.62)`, `contrast(1.05)`) → Rec.601
   percentiles. Reproduced against fin-build's §5 table on seven scenes nobody has
   touched (table under **Evidence**); worst deviation 1.3 points, s34 itself exact.
2. **Derived the fetch-time target from the constraint**, rather than fetching and
   hoping. Inverting the grade for a composed p10 of 80:
   `((v·0.62) − 0.5)·1.05 + 0.5 = 80/255` → **v ≈ 133/255**. Payoff clause 3 therefore
   demands a source whose 10th-percentile luma is ~133 — *90% of the visible frame
   brighter than mid-grey*. That is not "a bright photo"; it is a near-full-frame page
   with no dark table, no vignette, no shadow band. This is the constraint that
   decided the attempt, and it was known before sheet 1.
3. **19 contact sheets on 17 distinct query families**, `--candidates 6 --only s34`,
   every sheet Read and every cell judged (ledger under **Evidence**). Both pools:
   18 Pexels sheets, 1 Pixabay sheet.
4. **A per-cell tone pass** from sheet 7 onward — each 512×288 cell sliced, graded and
   percentiled, so a cell that cannot clear p10 ≥ 80 is disqualified before it costs a
   full-resolution fetch. Calibrated against a full fetch on the same candidate:
   cell-estimate 132.4 / 105.8 vs the promoted file's 133.1 / 110.0.
5. **5 full-resolution confirmation fetches** into scratch (never into the slot), on
   the only cells that survived both the sheet and the tone pass.
6. **md5 dedupe across ALL projects**, exactly the prescribed `find` over
   `studio/videos` + `vault/videos` — empty output, no collision anywhere.
7. **`python3 tools/pipeline_check.py check assets --slug passive-income-number
   --cut en --chapter 3` → PASS assets-en**, run last, after the manifest was restored.

## Failed

**The re-fetch failed. The pool cannot supply the frame the ruling specifies.**
Not "did not on this pass" — the two constraints are close to mutually exclusive in
both pools, and the failure is legible in the numbers rather than in taste:

- **p10 ≥ 80 admits only near-full-frame bright paper.** 36 cells were measured cell by
  cell (sheets 15–19, plus 5 promoted to full resolution); **11 of the 36 cleared p10 ≥
  80**, and every one of the 11 is disqualified on subject: 4 Bibles or Bible-adjacent,
  1 titled book (`LOVE WORK`), 1 marketing desk with an Apple keyboard, 1 "your voice
  matters" card, 1 shredded-paper field, 2 the same German museum-catalogue spread, 1
  the financial paper below. The other 75 cells were killed on the sheet by eye —
  legible words, foreign language, a brand, a figure, a face, or a dark ground obvious
  at preview size.
- **Everything the pool sells as "two columns of body text" is a book.** Dictionaries,
  Bibles, novels, typography specimens. The two-column *journal* the ruling names is
  not a stock subject; the pools index moods and objects, and "an academic paper" is
  neither.
- **The pool's non-book documents are contracts.** Signature lines, `Assignment`
  clauses, `INSURANCE POLICY`, `Platinum Credit Card`, divorce papers, forms being
  filled in by identifiable people. The shipped s34 is not an unlucky pick — it is
  what this query family *is*, and its sibling from the same shoot (Pexels 261621)
  came back at sheet 8.
- **The one tone-passing non-book frame is a brand mark and a table of figures.**
  Pexels 12585776, a folded financial paper with a pen on a white boarded table:
  composed **median 133.1 / p10 110.0 / spread 8.9**, better than the shipped frame on
  all three, and a +75.5 step-in from s33. It reads `CAZENOVE` (a UK investment bank)
  and `MANAGED F…` at 1880 px, and the body of the frame is **columns of share prices**
  — a legible brand mark plus figures that read as published statistics, on the frame
  whose foot names a study's methodology. Worse than what ships.
- **The best-measuring paper frame in 111 cells is the forbidden family.** Pexels
  954198, high-key open page: composed **median 146.7 / p10 125.3** — it would be the
  brightest and most legible photograph in the chapter. It is a **German Bible**
  (`Der HERR sagt`, `Volk Israel`, verse numbers, bold section headings). The brief
  names this family as already killed, and I did not re-open it; I record it because
  it is the sharpest available proof of the intersection: *the tone gate and the pools'
  inventory meet exactly on the frames this cut has already rejected.*

**I did not substitute a near-miss**, per the brief. In particular I did not promote
the two candidates a less careful pass would have taken:
- the **fanned book + pen** pair (Pexels 226612 / 226611) that recurred on five
  separate queries — it is the pool's answer to "pen + dense text + bright", and it
  measures **p10 5.3 and 4.7**. It fails clause 3 outright, and it would have made s34
  a *book* three scenes from s37, collapsing the deliberate s33 / s34 / s37
  papers-macro-book distinction into two books.
- the **annotated research paper** (Pexels 8036329 family, hands + highlighter over a
  genuine two-column article) — the closest subject match found anywhere, and it
  measures **median 110.0 / p10 38.1**. Half the required p10.

## Evidence

### Instrument validation (source-side predictions, this stage's own chain)

| scene | fin-build §5 | mine | Δ |
|---|---|---|---|
| s24 (`center bottom`) | 37.7 | 36.9 | −0.8 |
| s25 | 92.0 | 93.2 | +1.2 |
| s28 | 95.7 | 95.8 | +0.1 |
| s33 | 57.8 | 57.6 | −0.2 |
| **s34** | **128.1 / p10 92.1** | **128.3 / p10 92.1** | **+0.2 / 0.0** |
| s35 | 139.2 | 138.3 | −0.9 |
| s37 | 21.6 | 20.8 | −0.8 |

⚠ These are **predictions**. This chapter's encode has come in near half the
source-side figure twice (s31 70.6 → 35.0; s27 97.0 → 42.0) with ranks intact. Every
number in this log is source-side and comparative.

**The bar to beat, restated:** shipped s34 = median 128.3 (#2 of 16) · p10 92.1 (#1) ·
spread 7.8 · step-in +70.7 out of s33 (57.6). A replacement must clear p10 80 *and*
not relocate the chapter's ceiling.

### The 19 sheets — every query, every kill

Pexels unless marked. `n/6` is the cells that actually arrived; the drawn number is the
candidate index, and when a preview fails the survivors shift left, so **position ≠
index on a lossy sheet** (q6 rendered 2–6, q14 rendered 3–6).

| # | query | n/6 | what came back, and why every cell died |
|---|---|---|---|
| 1 | open magazine spread two columns of small text flat lay top down white page | 6 | edge-on magazine (no text); dark book curl; beauty magazine + lipstick; Turkish paper `git başımdan`; display title `rules`; hands on a dark table |
| 2 | two columns of printed text on a white page with a black pen resting on it top down | 6 | Italian (`Virgil Abloh conserva…`) legible; novel + pen, dark vignette; fanned dictionary + pen; typography book `Bold`; German museum catalogue; **blank** ruled notebook (the killed empty-frame shape) |
| 3 | dense paragraphs of small print filling a bright white page with a pen shallow focus | 6 | German columns (dup); finger on a German page; dark hands writing; sparse cyan book; fanned dictionary (dup); English Bible `The ark 37 Bezalel…` |
| 4 | printed research paper with two columns of text on a white desk with a pen top down | 6 | office desk + charts; **hands + highlighter on a real two-column article — 110.0 / 38.1, half the p10**; `your voice matters`; colour chart; `Platinum Credit Card`; handwritten clipboard |
| 5 | macro close up of newspaper columns of small text filling the frame | 6 | `Coronavirus` headline; folded newspaper stack; type specimen `Ee`; Dutch paper; glasses + `ECONOMI` + laptop, dark; `LOVE & HATE / Republicans & Democrats` |
| 6 | magnifying glass lying on the fine print of a printed document close up | **5** | German stamp catalogue with prices; `SALES VOLUME DURING THE WEEK` bar chart; `5 Charts to Display Your Data and Metrics`; `INSURANCE POLICY` + a $100 bill + a toy car; book `INDEX` page of page numbers |
| 7 | printed page of justified paragraphs with a black pen on white paper top down macro | 6 | the pool recycling: German columns / Italian / `absorbed` / Turkish `Unutulan` / fanned dictionary / `Bold` |
| 8 | close up of the small print of a document with a pen shallow depth of field **#6** | 6 | identifiable person filling a form; dark hands signing; **divorce documents + two identifiable faces**; `Hey Siri` (brand); **the shipped shoot's sibling, 261621 — `Assignment` + `SIGNATURE`**; scrabble tiles `AGREEMENT` |
| 9 | black pen in focus resting on a blurred page of small printed text bright white paper | 6 | blurred book page; novel + pen; fanned dictionary; cyan book; `Bold`; maths problem sheet with a geometry diagram + dark band |
| 10 | typed manuscript pages spread on a white table with a pen top down bright | 6 | people + editorial mock-ups ×3; blank paper + pencil; **laptop screen (banned outright)**; handwritten cursive macro |
| 11 | dense small text printed on white paper close up bright **#12** | 6 | dictionary `diversity`; Italian; `A NEW CD-ROM… THE LATEST TYPEF`; German stack; `SUPPORT LOCAL`; typewritten `and the story goes` on a foreign paper |
| 12 | raking light across a page of printed text with a black pen lying on it top down | 6 | novel + pen; Italian; fanned dictionary; `absorbed`; `Bold`; **idiom dictionary + white pen — fetched at full res: `hold one's fire`, `hit the sack`, `hit the books` fully legible, and upside down** |
| 13 | single sheet of typed paper on a white desk photographed from directly above with a pen | 6 | blank sheet + crumpled balls; letterpress `VALUEABLE`; braille; blank + pencil; blank clipboard + person; `BOSS LADY` + an Apple keyboard |
| 14 | reading glasses lying on a page of small printed text bright white paper close up | **4** | glasses on a two-column page **legibly about Apple and Steve Jobs** (a brand and a real person); blurred book; glasses on an orange-edged book; `Bold` |
| 15 | stapled printed report with paragraphs of small text and a pen on a white table close up | 6 | German columns; **financial paper + pen — 133.1 / 110.0, killed for `CAZENOVE` + share-price tables**; office desk + people; typewriter; printout with charts + hands; desk with a doughnut chart |
| 16 | printed page of small text and a pen on a white wooden table soft daylight shallow depth of field | 6 | all books. **cell 3 = 146.7 / 125.3 — the GERMAN BIBLE, forbidden family, not promoted.** cells 5/6 = the pen-on-book pair at **p10 5.3 / 4.7** |
| 17 | flat lay of printed pages of small text with a pen on a white background high key top view | 6 | shredded paper 116.2/97.2 (says *destroyed* document); `your voice matters` 125.0/105.0; braille 110.6/62.8; Bible + calendar 117.9/4.7; Bible on boards 122.4/83.3; titled book `LOVE WORK` 147.3/103.6 |
| 18 | **[pixabay]** two columns of printed text on a page with a pen fine print | 6 | Polish newspaper 85.8/32.5; book 103.3/18.0; book 60.3/9.1; **German legal text with literal `§` clause numbers** 69.8/11.5; glasses on book 84.8/4.7; book + heart string 119.8/59.9. **Whole pool fails p10 ≥ 80** — best cell 59.9 |
| 19 | close up of small print paragraphs on a bright white page no headline **#8** | 6 | dictionary `Dd`; `Coronavirus`; `absorbed`; open Bible (Genesis); book fore-edge; glasses on the Apple/Jobs page. **Best p10 in the sheet: 16.5** |

### Why the third pool was not spent

`@commons` is the rung for **named** things — a building, an institution, a landmark.
The beat here is a texture, not a named thing, and Commons' inventory for it is
*scans*, which are flat, perfectly legible and carry the title, authors and journal
name in the frame — i.e. they fail the ruling's own "no title, no figure, no agency
name" harder than a photograph does, and add a CC BY attribution condition for the
privilege. Recorded so the next attempt does not spend a pass discovering it.

### Standing checks, each actually run

- **md5 dedupe, prescribed form**, `find studio/videos vault/videos \( -path
  '*/final/*.jpg' -o -path '*/assets/img/*.jpg' \)` → **empty**. No collision anywhere
  on either channel (the new `_cand/` sheets are inside the glob and collide with
  nothing either).
- **s34.jpg is untouched**: md5 `b78e3a77a27dcfdcca149d3ca1b5613c`, size 149,190 b,
  mtime **2026-08-08 11:18:21** — the attempt-1 file, never re-picked. `--pick` was
  never run against this manifest.
- **`check assets --chapter 3` → PASS assets-en**, with the flag, so the licence
  assertion reaches `assets-ch3/final/` and not an empty `-en/assets/img/`.
- **CREDITS.txt**: 16 rows, 16 keys, unchanged — nothing was fetched into the slot,
  nothing was hand-placed, so no row could be orphaned.
- **s30 was never opened for writing.** Neither were s26, s27, s31, or any other file.

## Changed

**Nothing that ships.**

- `assets-ch3/final/manifest.json` — s34's query was edited 19 times during the sweep
  and is **restored byte-for-meaning to the shipped query**, read back off
  `s34.jpg.src` rather than retyped: `close up of the small print of a contract
  document with a pen shallow depth of field dark@pexels`. Manifest ↔ `.src` ↔ file
  are consistent, so a later plain `--manifest` run still skips this slot.
- `assets-ch3/final/_cand/s34.jpg` + `s34-q1…q18.jpg` — 19 throwaway contact sheets,
  left in place per protocol (not in the manifest, not shipped, cleaned up
  post-delivery). They are the evidence for the ledger above.
- No image, no `.src`, no `CREDITS.txt` row, no `index.html`, no `build.mjs`.

## Owed

1. **The blocker is still open, and it now has a measured price.** The chapter's
   choices are three, and all three are the CEO's to make, not mine:
   - **Keep the shipped frame.** Cost: `Contractor` / `9. Insurance` / `10. Assignment`
     remain legible at 1080p under a foot naming AAII Journal. Benefit: it is still the
     chapter's most legible photograph (#2 median, #1 p10) and §10's letter is met.
   - **Relax payoff clause 3 for this slot only, to about p10 ≥ 35.** That single
     change opens the pool immediately — the annotated two-column research paper
     (110.0 / 38.1) is a *direct* answer to the ruling's subject, hands and highlighter
     in the same plane, no headings and no clause numbers. It costs the chapter its
     brightest frame and moves the payoff frame from #1 on p10 to roughly #6. I did not
     take it, because clause 3 was given to me as hard.
   - **Change the beat rather than the photograph** — take the citation off *this*
     frame (foot moves to s37, which already carries the Conclusion quote) so the
     picture no longer has to be the document it names. That is fin-script / fin-build
     scope and outside this stage's authority.
2. **The `.src` carries the query alone, deliberately.** The brief asked for the
   predicted median / p10 / p90−p50 in the sidecar; the sidecar is also
   `fetch_one`'s skip-on-same-query token (exact string compare on the whole file), so
   any extra line would make a later plain `--manifest` run re-download and clobber a
   deliberately-chosen pick. All fifteen sibling slots carry the query alone. The
   numbers therefore live here, in the log, which is the one home for them: **shipped
   s34 = 128.3 / 92.1 / 7.8, step-in +70.7.** No file changed, so no new prediction was
   owed.
3. **For whoever fetches paper next, on this cut or the next:** the phrase that
   decides the outcome is not the subject, it is the *tone*. `p10 ≥ 80` after this
   grade means the page must fill the frame; the moment a desk, a table edge or a
   vignette enters, p10 falls to single digits — the pen-on-book pair at 5.3 and 4.7,
   the annotated article at 38.1, the whole Pixabay sheet under 60. Query the light and
   the fill before you query the object.
4. **`--only <slot>` is the right tool for a one-slot re-source** — 19 sheets cost 19
   API searches, not 19 × 16. Recording it because attempt 4's log had to say the same
   thing and the flag is easy to miss.
