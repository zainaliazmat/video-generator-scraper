---
summary: fin-package credit-history · hi · attempt 1 · STATUS ok. New HyperFrames project studio/videos/credit-history-thumbs (3 hi variants, check clean 29/29 AA), publish pack written with real chapter times from timing.json and 15 autocomplete-verified tags from a fresh 2026-07-29 gl=in/hl=hi pull. ⛔ Hard finding — this is the 6th consecutive blockframe-9 on @cashguruguides, the exact thing the good-debt-vs-bad-debt pack said must not happen.
updated: 2026-07-29
source: own tools/autocomplete.py pulls (2026-07-29, gl=in hl=hi, 24 seeds incl. 4 empties) · own sqlite read of library.db (0 lane rows / 1,124 total) · studio/videos/credit-history-hi/assets/voice/timing.json · studio/videos/credit-history-hi/index.html (on-screen feet #s3f/#s4f/#s5f/#s7f/#s8free) · vault/videos/{good-debt-vs-bad-debt,pay-yourself-first,needs-vs-wants,50-30-20-rule}/ packs + milestone notes
---

# fin-package — credit-history · hi · attempt 1

**Result: `STATUS: ok`.**

## Artifacts

- `vault/videos/credit-history/youtube-metadata-hi.md`
- `studio/videos/credit-history-thumbs/thumbnail-hi-v1.png` · `-v2.png` · `-v3.png` (1280×720)
- `studio/videos/credit-history-thumbs/index.html` (+ `package.json`, `meta.json`, `assets/`)

## Thumbnails

New project `studio/videos/credit-history-thumbs/`, one section per variant, exported
with `npx hyperframes@0.7.66 snapshot --at 1,3,5 --no-end` and copied to the contract
filenames. Backgrounds are the video's **own** scene photos (`s1.jpg` archive shelves,
`s7.jpg` blueprint, `s3.jpg` ledger) under the design-finance-blockframe grade — no new
images, no cross-video reuse.

| | Idea | Focal / accent | Numerals |
|---|---|---|---|
| **v1 (rec.)** | `EK MISSED EMI` → red mega **36 MAHINE**, with the 36-cell payment-history grid (6×6, one red) beside it | red / green | 36 · 3 (s5) |
| v2 | `SCORE KAM` → `EXTRA BYAJ` → red mega **₹4.5 LAKH** | red / amber | 4.5 · 30 · 3.3 (s7) |
| v3 | `KITNA HONA CHAHIYE?` → `CIBIL SCORE` → green mega **700+** over a 300→900 gauge | green / red | 700 · 300 · 900 · 750 (s3) |

- `npm run check`: **0 lint · 0 runtime · 0 layout · 0 motion · 29/29 WCAG AA**.
- Legibility assert (largest line ≥40% of width at 320×180): **~59% · ~58% · ~47%** — all pass.
- **Numeral discipline holds**: every numeral on all three is on screen in the render
  and in `script-hi.md` (`#s3g1` "700+ = GENERALLY GOOD", `#s3g2` "750+ = BEST PRICING",
  s5's 36-month grid, s7's `EXTRA INTEREST ₹3.3 to 4.5 lakh` on the ₹30,00,000 model).
- **No dollar glyph** in the thumbs project or the pack (verified by whole-file scan; the
  hi cut treats it as a hard fail).
- ≤12 chars per line, ≤2 big lines per variant, one focal + one accent each.

Two check failures fixed in-flight, both real: `p.gridcap` had no stacking context and
the layout checker correctly called it occluded by the scrim; and the v3 gauge split was
at 62% when the true 700 mark on a 300–900 scale is 66.7% — a thumbnail numeral has to be
geometrically honest too. Also corrected the Hindi gender agreement on v1's sub
(*aapke* → *aapki* credit report).

## Search evidence

`tools/autocomplete.py`, 24 seeds, gl=in hl=hi, 2026-07-29. Three seeds (`credit score`,
`credit history`, `credit report`) first failed on a transient `Network is unreachable`
and were **re-fetched successfully** — recorded rather than silently dropped.

Deepest verified clusters: `cibil score kitna hona chahiye` (with loan / credit-card /
personal-loan children), `cibil score kaise badhaye` (7 children incl. a Devanagari
variant), `cibil score kharab hai …` (a large distress cluster), `cibil score kya hota
hai` / `cibil kya hota hai` (the definition lane, top-10 on the bare seeds).

**Four empties, all recorded in the pack and all load-bearing:**
`emi miss hone par cibil` → NO SUGGESTIONS · `cibil score 300 se 900` → NO SUGGESTIONS ·
`home loan interest rate cibil score` → only two loose neighbours · `auto pay` → returns
**only "how to cancel autopay"** strings. The last one is the most useful negative result
in this run: **s6's action step is the opposite of what India actually searches for**, so
auto-pay can be the content but can never be the title.

**Competitor scoreboard: `library.db` is empty for this lane** — verified directly, 0 of
1,124 rows match cibil / credit score / credit history / credit report / loan / credit.
No scrape was run (it stays the orchestrator's owed step, same as the last two runs). The
only competitor signal is `cibil score kaise badhaye **kuldeep singhania**` — a named
creator attached to the how-to lane, the same shape as Warikoo on `credit card trap`.

## Title

Recommended: **CIBIL Score Kya Hota Hai? Ek Missed EMI = 36 Mahine** (51 chars) — leads
verbatim with the verified top-of-funnel string, then the hero shock; pairs with v1.
Four alternates in the pack, each named against the cluster it titles into, including one
(#5, the `cibil score kharab hai` lead) that is offered **and argued against** because
that cluster wants "how do I still get a loan", which this video does not answer.

Held the pattern from the 50-30-20 and good-debt packs: **title the demand cluster, not
the internal name.** The internal name is "credit history"; India spells the demand
"CIBIL score".

## Gate 2

- **Altered-content disclosure: "No".** Synthetic narration (ElevenLabs Harsh) but no
  realistic synthetic media presented as real — motion graphics over licensed stock. No
  on-screen disclosure required or present. Narrator is a voice, not a persona; no
  lender/card/product pick; no bank named anywhere (s7's foot is worded to avoid it).
- **⛔ Channel sameness — 6th consecutive blockframe-9 on @cashguruguides.** 50-30-20 →
  emergency-fund → needs-vs-wants → pay-yourself-first → good-debt-vs-bad-debt → this.
  The good-debt pack *and* its milestone note both wrote that a 6th would be "an
  indefensible template run" and that escalation had to happen **before the next cut was
  scripted**. It didn't. **The finding worth escalating is not the sameness — it is that
  the previous flag changed nothing.** Publishing this cut is still defensible; scripting
  a 7th on the same architecture is not. Concrete break options are listed in the pack.
- Recording gap noted: only pay-yourself-first has a confirmed upload URL in the vault,
  so the count above is the *production* sequence. Either reading (5th or 6th live)
  crosses the line, but the ambiguity is avoidable — record upload dates in the milestone
  notes.

## Findings owed / not fixed here

1. **`chosen:` has now gone unfilled three uploads running** (pay-yourself-first,
   good-debt hi + en). Until one is filled, the thumbnail loop has zero feedback and every
   sameness argument in these packs is untested theory. Cheapest unfixed gap in the pipeline.
2. **Finance-lane scrape still owed** — `library.db` has never seen this lane.
3. `-en` pack for this slug not written yet (`studio/videos/credit-history-en` exists).

## Commands run

Only the allowlist: `npm run check` and `npx hyperframes@0.7.66 snapshot --at 1,3,5
--no-end` inside `studio/videos/credit-history-thumbs/`, plus `python3
tools/autocomplete.py --q "…" --gl in --hl hi` (24 seeds). No scraper was needed beyond a
read-only sqlite count on `library.db`. File staging used `cp` (font, gsap, grain, three
scene photos) and `mkdir`; edits to `index.html` and the pack were file writes. No git.
