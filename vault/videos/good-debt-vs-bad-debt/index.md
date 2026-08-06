---
summary: Milestone note for «Good Debt vs Bad Debt — the minimum-payment trap» pair (Hindi/₹ 3:15 · US/$ 2:59) — both cuts rendered, MASTER QA PASS, committed 2026-07-28/29; **LIVE on YouTube 2026-07-29** (hi youtu.be/f-doI5d0NRk · en youtu.be/gC2QlQiLqhw); source archived to `src/`, studio dir deleted. Thumbnail chosen: v2 both cuts. Owed — lane scrape · analytics after 28 days. ⛔ HARD flag: 5th consecutive blockframe-9 on BOTH channels — **SUPERSEDED 2026-07-30: blockframe-9 was reviewed against twelve alternatives and chosen; it is now locked in `tools/format.json`. See [[../../knowledge/design-finance-blockframe]] §0. Do not act on the "MUST change architecture" instruction below.**
updated: 2026-07-29
source: run.json + the fin-render / fin-build / fin-assets / fin-package logs in logs/ (the /finance-video pipeline)
---

# Good Debt vs Bad Debt — milestone note

Run 2026-07-28→29, `/finance-video` pipeline. Topic: the credit-card
minimum-payment trap, framed as good debt vs bad debt. fin-research was **rescued**
(missing study note, library empty for this lane); fin-script-hi took **attempt 2**
(currency-check trap, below); both fin-render cuts landed on **attempt 3** (frame-gate
re-source + orchestrator-owned encode). Budget: **18 of 30 ElevenLabs calls** (9 VO
clips per cut); **144 Pixabay calls** (hi 48 + 30 frame-gate re-source, en 66).

## The two cuts

| | Hindi / India (@cashguruguides) | US / English (@moneymavens101) |
|---|---|---|
| Master *(deleted on archive — now on YouTube)* | was `…-hi/renders/FINAL-1080p-hi.mp4` | was `…-en/renders/FINAL-1080p-en.mp4` |
| Archived source | `src/hi/` | `src/en/` |
| Runtime | **195.20 s (3:15)** · 11.75 Mb/s video (~11.93 overall) | **178.60 s (2:59)** · 12.2 Mb/s video |
| Voice | ElevenLabs **Harsh** — **Devanagari Standard Hindi** (NOT Nastaliq) | ElevenLabs **Brian** |
| Script | [[script-hi]] (9 lines h1–h9) | [[script-en]] (9 lines en1–en9, US rewrite not a translation) |
| Title (recommended) | "Credit Card Minimum Payment: Ek Jaal — ₹50,000 par ₹88,614 Byaj" | "The Credit Card Minimum-Payment Trap: $6,000 Costs You $9,506" |
| Publish pack | [[youtube-metadata-hi]] | [[youtube-metadata-en]] |

Structure of both cuts: **blockframe-9** (hook → roadmap → concept → good-vs-bad →
how-the-minimum-works → action → math-counter → do-today → recap).

## Hero numbers (with sources)

- **hi: ₹50,000 card @ ~40% APR, 5% minimum only → 208 months (17+ yrs) + ₹88,614
  interest** — more than the principal. Sources: Minimum Amount Due ≈ 5% of balance,
  ₹100 floor, interest covered first / no negative amortization = RBI norms + issuer
  MITC 2026; ~40% APR = illustrative India retail range (40–45%), not any single bank =
  Federal Bank / ICICI MITC 2026; the 208 / ₹88,614 pair = ₹100-floor amortization
  model computed (B₀ = ₹50,000). On screen, month-1 split: ₹2,583 min / ₹1,667 interest
  / ₹916 off principal.
- **en: $6,000 card @ ~22% APR, minimum (1% + interest) only → 215 months (~18 yrs) +
  $9,506 interest** — more than borrowed. Sources: min ≈ 1% of balance + that month's
  interest, ~$35 floor, interest first = issuer cardmember agreements (Chase, Capital
  One) + CFPB Regulation Z 2026; ~22% APR = illustrative US range (20–24%) = Fed G.19 /
  WalletHub 2026; 215 / $9,506 = $35-floor model (B₀ = $6,000). On screen, month-1
  split: $170 / $110 / $60; 12-mo balance $5,318.
  - **⚠ Numeral note:** the en interest is **$9,506**, NOT the $9,496 that still appears
    in [[script-en]] / [[storyboard-en]] (pre-build hand estimate). The **build
    calculator regenerated it** — render, thumbnail and description all say $9,506. Do
    not "correct" it back.
- Both markets' facts staged in [[facts-staging]] — promotion to
  `knowledge/money-facts-2026` is the **orchestrator's** step, not archive's.

## QA (from the fin-render logs — both MASTER QA PASS)

| | hi (attempt 3) | en (attempt 3) |
|---|---|---|
| Runtime vs timing.json | 195.20 s, **+0.03 s** (0.9 frame) | 178.60 s, **+0.018 s** (0.54 frame) |
| VO placement drift | max **0.045 s** (s8); 7/9 flat +0.022 s; zero accumulation | max **+0.093 s** raw (en7 — its own 0.071 s head-lead); encode-isolated +0.022 s; zero accumulation |
| True peak | **−3.23 dBTP** (< −1) | **−4.74 dBTP** |
| Loudness | −22.0 LUFS (broadcast-safe; ~8 LU under YT −14) | −21.0 LUFS |
| VO content | 9/9; hero round-anchors spoken; **208 / ₹88,614 on-screen ONLY (absent from VO)** | 9/9; **215 mo / $9,506 on-screen ONLY (absent from VO)** |
| Black segments | 0 | 0 |

Optional pre-publish loudness lift toward −14 LUFS is available on both (peak headroom
allows it) — orchestrator's call, not a gate fail.

## Thumbnails (3 variants per cut, creator picks at upload)

`vault/videos/good-debt-vs-bad-debt/src/thumbs/thumbnail-{hi,en}-v{1,2,3}.png` (source:
`…-thumbs/index.html` — hi §v1/v2/v3, en §env1/env2/env3, one shared project).
- **v1 — recommended** THE PUNCH: centred red mega **₹88,614 / $9,506** over the
  calculator texture. Centred → breaks the channel's left-aligned streak.
- v2 THE TIME TRAP: 208 MAHINE / 17 SAAL · 215 MONTHS / 18 YEARS — closest to the
  last-3 red/left/photo family (the safe continuity pick).
- v3 THE SPLIT: the month-1 anatomy (₹1,667 / $110).

Red is the trap throughout; green is deliberately absent (the thumbnail sells the
trap, not the escape). Backgrounds are the video's OWN re-graded scene photos — no
new/cross-video images, no AI-collage, no shocked-face. **Chosen: v2 for both cuts**
(creator pick, 2026-07-29). **New creator rule: one v2-style thumbnail from now on, not three.**

## AI-enhance prompts (2026-08-06) — v2 / v2

Fourth video through the plate-only pass ([[../../knowledge/design-thumbnail-ai-enhance]]).
No blocker here: `chosen:` was filled at upload with **v2 on both cuts**, so the tiles to
enhance were never in doubt — the only video in the backlog where that was already true.

**The claim on both tiles is TIME, so the plate has to say time.** Not money, not
disaster. The two enhanced scenes signal duration with **a thick stack of paper whose
bottom sheets have yellowed and whose top sheets are fresh** — a physical prop that reads
as *years of this* at browse size, carries no numeral, no axis and no label, and stays on
the right side of §5b's *physical props yes, data graphics no* line.

Three constraints here that the earlier prompts did not need:

1. **Green is forbidden**, not merely unused. This video's colour thesis is that red is
   the trap and the tile sells the trap, not the escape. A model handed "credit card
   debt" will reach for a green tick, a cut-up card or a `PAID` stamp unprompted.
2. **No escape imagery at all** — no scissors cutting a card, no broken chain, no
   cleared balance. Same reason. These are named explicitly because they are the single
   most predictable stock answer to this topic.
3. **No prop that credit-history already used** — no hourglass, no red cloth-tied file,
   no brass key, no car key. The two videos publish on the same channels and the enhance
   prompt is now the cheapest place to control cross-video visual sameness, which is this
   channel's standing open problem.

Both source plates carry **legible background text** (the hi ledger is covered in
handwritten figures, the en document reads `busin…`). Both prompts kill it, using the
surface-level phrasing from §5bb rather than the weaker "no legible characters" that let
lorem ipsum through on credit-history.

### hi — `thumbnail-hi-v2.png` → @cashguruguides

```
Enhance this 16:9 YouTube thumbnail. Rebuild ONLY the photograph behind and around the
existing type. This is a photo-retouch task, not a redesign.

ABSOLUTE RULE — PRESERVE ALL EXISTING TEXT PIXEL-FOR-PIXEL. Do not re-render,
re-letter, restyle, translate, transliterate, move, resize or re-space ANY text or its
container shapes. Every glyph must return byte-identical:
  • "MINIMUM = JAAL" — near-black letters on a rounded red pill (#ef4444), upper left
  • "208 MAHINE" — cream (#f5f3ec) heavy caps
  • "17 SAAL" — red (#ef4444) mega line, the largest element in the frame
  • "₹50,000 ka card clear karne me" — cream, below the mega line
Keep the rupee glyph ₹ exactly as drawn. Add NO new text, numbers, labels, signs,
handwriting, figures, stamps with words, logos, watermarks or captions anywhere.

REGION: rebuild only the right ~35% of the frame plus the area behind the type. The left
column must stay in deep shadow so all four text lines keep their contrast.

SCENE: one continuous photoreal scene — a dark wooden desk at night, lit by one warm
practical light from the left. ONE hero group on the right: a thick tied stack of folded
paper statements, the sheets at the bottom yellowed and curling with age while the top
sheets are white and fresh, with a plain unbranded card lying FACE DOWN on top of the
stack, and the existing magnifying glass kept where it is, resting on the desk. Shallow
depth of field, dust in the air, deep falloff to near-black at the frame edges.
Photographic, 50mm at f/2, not CGI, not a render, not an illustration.

THE IDEA THE IMAGE MUST CARRY: time passing, slowly, on the same debt. The age gradient
in the paper stack is the whole point — make it unmistakable.

TONE — ordinary, worn, administrative, patient. Scuffed wood, soft paper edges, muted
colour. No drama, no disaster, no torn or burning paper, no spotlight, no light rays.
Equally: no wealth, no cash piles, no gold, no luxury, no glitter.

COLOUR LOCK: NO GREEN anywhere — not a plant, not a ledger line, not a tick, not a
banknote, not a highlight. This tile sells the trap, not the escape. Warm amber, cream,
deep brown and near-black only.

NO ESCAPE IMAGERY: no scissors, no cut or broken card, no broken chain, no "paid" or
"cleared" stamp, no tick, no crossing-out, no open lock, no upward arrow.

CURRENCY LOCK: Indian only. No US dollars, no foreign notes or coins. Banknotes are not
needed here — do not render cash at all.

PAPER RULE: every paper surface is blank, or covered by the props, or so far out of
focus that no line of type is resolvable. No blocks of body copy, no lines of lettering,
no filler text, no handwritten figures, no ruled ledger columns with entries in them, no
printed rows. The card shows NO number, NO name, NO bank logo, NO network mark, NO chip
detail — it is face down.

DO NOT USE these props (already used on this channel's other videos): hourglass, clock,
calendar, red cloth-tied document file, brass key, car key, key fob.

FORBIDDEN CONTENT: no people, no faces, no hands, no body parts (this channel is
faceless, permanently). No charts, pie graphs, bar graphs, gauges, dials, score meters,
receipts with legible lines, checklists, progress bars, arrows or infographics of any
kind — physical props yes, data graphics no. No collage, no panels, no left-to-right
sequence: ONE hero group that survives at 320×180. No props implying "financial
freedom", "debt free", "no stress" or a fast fix — this video promises none of those.

OUTPUT: 16:9, 1280×720 framing, photoreal, cinematic.
```

### en — `thumbnail-en-v2.png` → @moneymavens101

```
Enhance this 16:9 YouTube thumbnail. Rebuild ONLY the photograph behind and around the
existing type. This is a photo-retouch task, not a redesign.

ABSOLUTE RULE — PRESERVE ALL EXISTING TEXT PIXEL-FOR-PIXEL. Do not re-render,
re-letter, restyle, move, resize or re-space ANY text or its container shapes. Every
glyph must return byte-identical:
  • "MINIMUM = TRAP" — near-black letters on a rounded red pill (#ef4444), upper left
  • "215 MONTHS" — cream (#f5f3ec) heavy caps
  • "18 YEARS" — red (#ef4444) mega line, the largest element in the frame
  • "to clear a $6,000 card on minimum" — cream, below the mega line
Add NO new text, numbers, labels, signs, handwriting, figures, stamps with words, logos,
watermarks or captions anywhere.

REGION: rebuild only the right ~30% of the frame plus the area behind the type. "18
YEARS" runs to roughly two-thirds of the frame width, so the usable clean area is narrow
— keep the left two-thirds in deep shadow so every line keeps its contrast.

SCENE: one continuous photoreal scene — a dark wooden desk at night, lit by one warm
practical light from the left. ONE hero group on the right: a thick stack of paper
statements, the sheets at the bottom yellowed and curling with age while the top sheets
are white and fresh, with the existing pen resting across them and a plain unbranded
desk calculator sitting beside the stack, its display dark and blank. Shallow depth of
field, dust in the air, deep falloff to near-black at the frame edges. Photographic,
50mm at f/2, not CGI, not a render, not an illustration.

THE IDEA THE IMAGE MUST CARRY: time passing, slowly, on the same debt. The age gradient
in the paper stack is the whole point — make it unmistakable.

TONE — ordinary, worn, administrative, patient. Scuffed wood, soft paper edges, muted
colour. No drama, no disaster, no torn or burning paper, no spotlight, no light rays.
Equally: no wealth, no cash piles, no gold, no luxury, no glitter.

COLOUR LOCK: NO GREEN anywhere — not a plant, not a ledger line, not a tick, not a
calculator key, not a highlight. This tile sells the trap, not the escape. Warm amber,
cream, deep brown and near-black only.

NO ESCAPE IMAGERY: no scissors, no cut or broken card, no broken chain, no "paid" or
"cleared" stamp, no tick, no crossing-out, no open lock, no upward arrow.

CURRENCY LOCK: US only. No rupee symbol, no foreign currency. **Do NOT render banknotes
at all** — dollar bills come back with garbled serials and wrong portraits. Cash is not
part of this scene.

PAPER AND DISPLAY RULE: every paper surface is blank, or covered by the props, or so far
out of focus that no line of type is resolvable. No blocks of body copy, no lines of
lettering, no filler or lorem-ipsum text, no printed statement rows, no handwritten
figures. The calculator display is OFF and empty, and its keys carry no legible digits or
symbols. No brand name on the calculator.

DO NOT USE these props (already used on this channel's other videos): hourglass, clock,
calendar, manila folder, car key, key fob, credit card shown face up.

FORBIDDEN CONTENT: no people, no faces, no hands, no body parts (this channel is
faceless, permanently). No charts, pie graphs, bar graphs, gauges, dials, score meters,
receipts with legible lines, checklists, progress bars, arrows or infographics of any
kind — physical props yes, data graphics no. No collage, no panels, no left-to-right
sequence: ONE hero group that survives at 320×180. No props implying "financial
freedom", "debt free", "no stress" or a fast fix — this video promises none of those.

OUTPUT: 16:9, 1280×720 framing, photoreal, cinematic.
```

### Result — both returned 2026-08-06, one pass each ✅

Eight tiles across four videos now, **still zero garbled letters and zero invented
promises.** Every preserved string came back byte-identical on both cuts, including the
`₹` glyph and both red pills.

**The age-gradient instruction is the strongest single line written into any prompt so
far.** Both stacks came back with genuinely yellowed, curling sheets at the bottom and
clean white ones at the top — the hi stack tied with twine, the en stack loose under the
pen. It reads as *years of this* at browse size with no numeral, no axis and no label. An
abstract claim (17/18 years) now has an object. **Reuse this construction whenever the
claim is a duration or a count.**

Also held on both: no green, no cash, no people or hands, no escape imagery, no charts,
one hero group, and the card on the hi tile is face-down and completely blank.

### ⚠️ Three deviations — two of them are prompt bugs, not model failures

**1. The desk lamp is now in frame on three consecutive tiles, and the prompt put it
there.** Both prompts described the lighting as *"one warm practical light from the left"*
— credit-history's said *"as if from a desk lamp."* The model rendered **the lamp**, not
just its light, all three times. So the DO-NOT-USE list added in §5bc worked for the props
it named and was silently defeated by the lighting clause of the same prompt. **Fix:
describe light as `warm practical light from off-frame left, the source not visible`.**
Naming a fixture places the fixture.

**2. The calculator keys came back fully legible** — `7 8 9`, `MC MR M− M+`, `AC`, `%`,
`÷` — against an explicit *"its keys carry no legible digits or symbols."* The display
obeyed (dark and blank); the keys did not. The lesson is the one the banknote ban already
proved and this prompt failed to apply: **an object that inherently carries type cannot be
constrained into not carrying it — leave it out of the scene entirely.** The stack, pen
and lamp already carried the idea; the calculator earned nothing.

**3. The en top sheet has printed body copy again** — faint paragraphs on the white sheet
under the pen, the same slip as credit-history's manila folder, despite this prompt using
the strengthened §5bb surface phrasing. **Second occurrence, both on an `en` tile with a
document in the hero group.** The stronger wording reduced it (faint and partial here vs a
full lorem-ipsum page there) but did not eliminate it. Both are harmless at 320×180 and
both tiles ship.

**Also check at 1:1 before upload:** a couple of the calculator's top-right keys read as
faintly **teal**. If they are green rather than grey-blue they breach this video's
`NO GREEN` colour lock. Small enough to be invisible at browse size, but it is a stated
rule and it should be confirmed, not assumed.

### Owed

Same as credit-history: **the returned PNGs are not on disk**, so the ≥40 % assert is
unrun. `17 SAAL` entered at ~55 % and `18 YEARS` at ~65 %, the two widest margins in the
catalogue, so this pair is the least likely to fail it — but unrun is unrun.

```
vault/videos/good-debt-vs-bad-debt/src/thumbs/thumbnail-hi-v2-ai.png
vault/videos/good-debt-vs-bad-debt/src/thumbs/thumbnail-en-v2-ai.png
```

**Props now spent on these two channels** — carry forward into the next video's
DO-NOT-USE list: hourglass, clock, calendar, red cloth-tied file, brass key, car key,
key fob, manila folder, **desk lamp, magnifying glass, tied paper stack, calculator,
dark scratched wooden desk**.

## Run events + learnings worth keeping

**⛔ CHANNEL SAMENESS — HARD flag, enforcement line crossed (both channels).** This is
the **5th consecutive blockframe-9 ~3-min cut on EACH channel**: 50-30-20 →
emergency-fund → needs-vs-wants → pay-yourself-first → **this**. pay-yourself-first
explicitly warned "the next upload would be the 5th" — this is that upload. Per Gate 2,
mass-production sameness is the one category judged channel-level. This pair still
publishes fine (actionable forward, not retroactively), **but the next finance cut MUST
change architecture** — medium-tier per-line-chapters, a different layout, or a
different length band. A 6th blockframe-9 is an indefensible template run. **Escalate to
creator/orchestrator BEFORE the next cut is scripted.** *(the sameness policy is
enforceable now; whether it actually costs views = unvalidated — no analytics yet)*

> **WHAT ACTUALLY HAPPENED (added 2026-07-29 by fin-archive):** it wasn't. `credit-history`
> was then researched, scripted, voiced, built, rendered and packaged on the same
> architecture — **the 6th consecutive blockframe-9 on both channels.** This warning is the
> third of three that changed nothing, which is itself the finding: the control is in the
> wrong place. `tier` is chosen in `run.json` *before* fin-script; a milestone note and a
> publish pack are read *after* the artifact exists. See [[../credit-history/index]].

> **CLOSED 2026-07-30 — do not act on the flag above.** The control did move into code
> (`pipeline_check.next_architecture()` rotating the default), and then the creator made the
> decision the flag was demanding: thirteen styles were mocked up and compared side by side,
> and **blockframe-9 was chosen deliberately.** `tools/format.json` now carries
> `architecture_lock: "blockframe-9"`, so repetition here is a decision, not drift — and
> varying the layout "to be safe" now contradicts the creator. The sameness budget moved to
> the non-layout levers (transitions live, SFX kit present, music bed owed).
> Full record: [[../../knowledge/design-finance-blockframe]] §0.

**HERO-MATH DOCTRINE (worked — reuse for any model-dependent number).** The
minimum-payment payoff is floor/model-dependent, so the VO speaks ONLY floor-independent
anchors + round ranges ("17+ years / nearly the whole principal in interest"; "the
better part of two decades / more than you borrowed") while the exact integer (208 /
₹88,614; 215 / $9,506) is computed in build code and shown **on screen only, never
spoken**. Verified 3 ways: orchestrator Python, fin-facts closed-form, build node. QA
explicitly confirms the false-precise integers are ABSENT from narration.

**FONT GLYPHS (recurring build risk — fix at source).** The self-hosted `FinanceSans`
subset has **no `~` (U+007E)** and **no `>` (U+003E)** — visible use falls back to a
non-deterministic system font. Build must render them as CSS (the `.gt` chevron, same
em-border technique as `.arr`/`.tri`) or avoid the glyph (write "around 22%" not "~22%";
"18 YRS" not "~18 YRS"). Cost the en build a fix pass. Fix the subset — or lint for these
two glyphs — at source so every future build stops re-hitting it.

**CURRENCY-PURITY FOOTNOTE TRAP (cost the hi script a retry).** The script currency check
is a blunt whole-file substring match, so an agent's OWN "no $" / "no ₹" compliance note —
if written with the forbidden glyph — fails its own check. Standing rule for every finance
agent: **state the currency rule in words, never type the forbidden glyph.** Cost
fin-script-hi attempt 2.

**ORTHOGRAPHY — hi finance = Devanagari, NOT Nastaliq.** The hi finance cut is
**Devanagari Standard Hindi** (voice Harsh). A launch-arg said "Nastaliq" and was
correctly rejected — Nastaliq belongs to a different (Urdu) channel that does not exist
in `tools/format.json`. Do not route finance-hi through the Nastaliq lane. (The
vault's Nastaliq rule governs the *history/Urdu* work, not finance-hi.)

**ASSET FRAME-GATE (worked — front-load next time).** Full-frame render QA (gate two)
caught backgrounds that thumbnail-eyeballing missed: an antique coin depicting a **Hindu
deity** (revered-figure violation), plus foreign-language / cross-market b-roll (German
legal text, Polish metallurgy book, a US road in the ₹ cut). The **hi cut needed a full
5-slot re-source** (fin-assets attempt 2, [[logs/fin-assets-hi-2|fin-assets-hi-2]]);
front-loading those lessons let the en cut pass the frame gate first time. **Always
frame-gate at full res, never thumbnail size.** The **India-finance Pixabay pool is
small + heavily consumed** — poison map in that log: one demonetised ₹500 pile is the
immovable #1 for every rupee query (escape only via `#N`); ~3 clean rupee images exist
channel-wide; homonym traps recur ("bill"→a bird, "coins"→a €1 coin). Reach first for
`#N`-past-₹500, magnifier-over-ledger, calculator-keypad macro, a seedling closer, and
denomination-free coin stacks.

> The frame-gate, glyph, currency-check, orthography and hero-math items are
> pipeline/engineering facts — reproducible, not analytics-dependent — so they are stated
> as facts. Anything about **audience response** below is marked unvalidated.

**Thumbnail composition observation:** v1 (a centred red mega-number over the video's own
re-graded scene photo) is a fresh composition vs the channel's red/left-text-over-money-photo
streak — a genuine v1↔v2 A/B if the creator wants one. *(unvalidated — no analytics yet)*

## Published + archived (2026-07-29)

**State: LIVE on YouTube (both cuts) · source archived · studio dir deleted.**

| Cut | Channel | URL | Thumbnail |
|---|---|---|---|
| hi | @cashguruguides | https://youtu.be/f-doI5d0NRk | v2 |
| en | @moneymavens101 | https://youtu.be/gC2QlQiLqhw | v2 |

**Thumbnail chosen: v2** for both cuts (the time-trap / red-left family; `chosen:` filled
in both packs). **New creator rule 2026-07-29: make ONE thumbnail (the v2 style) from now
on, not three** — pipeline updated (fin-package + check_package).

**Source: `src/{hi,en,thumbs}/`** — composition, meta/package JSON, `gen_vo_*.sh`, the VO
lines (`assets/voice/*.txt`), the image prompts (`assets/img/*.src`), stock CREDITS and the
six thumbnail PNGs. `studio/videos/good-debt-vs-bad-debt*` is **deleted** per the
finished-video rule ([[../../CLAUDE]]): first the two masters, both `node_modules` and the
QA snapshots (~2.15 GB, on the scheduled upload), then the whole tree once the URLs landed.
**Re-render is reproducible, not free** — the scene photos and VO mp3s are gone, so a
rebuild re-pays image gens + ElevenLabs off the archived prompts and lines.

Still owed:
- **lane scrape** — `library.db` has **NO comparable videos** for the debt /
  credit-card-explainer lane (≥100 views, ≥240 s); from run.json `owed`. Orchestrator's step.
- **analytics after 28 days** — only then may any learning here touch
  [[../../knowledge/best-practices]].

Flagged for the pipeline (engineering, not a deliverable): the `FinanceSans`
missing-glyph subset and the substring-match currency check both **recur** — fix at
source (font subset / lint; word-not-glyph agent rule) so future runs stop paying for them.

Related: [[script-hi]] · [[script-en]] · [[storyboard-hi]] · [[storyboard-en]] ·
[[youtube-metadata-hi]] · [[youtube-metadata-en]] · [[audit-hi]] · [[audit-en]] ·
[[../../knowledge/design-finance-blockframe]] · [[../pay-yourself-first/index]]
