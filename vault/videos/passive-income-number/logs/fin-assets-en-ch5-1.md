# fin-assets — passive-income-number · en · ch5 · attempt 2 (log keyed -1 so mark finds it)

Closing out attempt 1, which promoted 16 images and then stalled in the terminal
full-resolution pass without writing a log. Nothing was re-fetched wholesale; the
gate was run on the files already on disk, and only the slots that failed it moved.

## Ran

1. `tools/image_sheet.py … --chapter 5` → `IMAGES-ch5.jpg` (16 cells), read for repetition.
2. Full-resolution `Read` of all 16 promoted jpgs, in two batches of eight (s53–s60,
   s61–s68) with a progress marker between — the batching that avoids attempt 1's
   600s silence. Both looks owed, both taken.
3. `pipeline_check check assets --chapter 5` (the YHIGH / bytes / attribution gate).
4. Cross-project md5 dedupe with the `find … -print0 | xargs -0 md5sum | uniq -Dw32` form.
5. Five slots re-picked or re-queried; sheet rebuilt and re-read; gate re-run to PASS.

## Failed

Nothing outstanding. Six defects were found and closed here; two of them would have
reached a render.

**HARD — gate failures / licence-class defects**

| slot | defect | how found | fix |
|---|---|---|---|
| **s60** | source **YHIGH 93 < 110**. Kraft envelopes on a black ground — no highlights for the locked grade. Also failed sound-off: two overlapping kraft pieces + a tape roll do not say "same paycheck, two prices" | `pipeline_check` | re-queried onto a **light** ground (`…on a white table daylight`) — the material rule: matte kraft has no specular ceiling, so the ground has to supply the highlights. Cell 4: two identical kraft envelopes side by side, white ground. **PASS** |
| **s66** | the shipped binder carried **legible German text and a readable brand mark** — `Sparda-Bank`, an `IBAN: DE39…`, `KV-AG ausgezahlt`, `Antrag zur Rückz.` — under a line about **US BLS household spending**. Invisible at contact-sheet size by construction | full-res read | four sheets; see the s66 trail below |

**STRONG — statement / repetition defects**

| slot | defect | fix |
|---|---|---|
| **s63** | shipped as a **corridor of ~15 storage doors**, structurally a near-twin of **s59** (the protected PEAK 2): same deep one-point perspective, same cool grey industrial vanishing point, same lit ceiling. Two of the chapter's number scenes saying the same thing. It also contradicted its own cue (§10: "a **single** storage-unit door, roller shutter closed, plain") | free re-pick from the existing sheet, `--pick s63=2` — no fetch. A single closed red roller door, flat-on, padlock. Kills the twin **and** honours the cue |
| **s57** | see the carry-forward ruling below | restored unchanged after three sheets proved the pools hold nothing better |
| **s65** | shipped as a **cropped part-month** under 5.13 *"the whole month, not one slice of it"* | **kept, flagged** — all five alternatives were worse (see Evidence) |

**Rejected candidates, and why** (consistency matters more than any single call):
faces (s66 c4 portrait, the two-person desk shots), readable brand marks (`Sparda-Bank`,
`IKEA`, an Apple laptop, `Small Business Accounting Checklist`), foreign-language text
(`PARAGON FISKALNY`, `NIP 527-010-33-85`, `JUNHO`, `AGOSTO`, `Koud`/`Warm`), foreign
currency (złoty amounts on the receipt), fabricated source documents (a generic pie
chart, a 1989 *Monthly Labor Review* cover with a library barcode), cross-chapter
repeats (see below), and one literal repeat of ch4's own s46 photograph.

## Evidence

**Gate.** `PASS assets-en` on the final 16. The only measured failures during the run
were `s60 YHIGH 93` (shipped state) and `s57 YHIGH 66` (a candidate I promoted and the
gate rejected — see below). Everything else cleared on the first measurement.

**Dedupe.** Final run: empty output = no collision anywhere on either channel.
It was **not** empty mid-run: `s66.jpg` came back **byte-identical
(`8ea48255…`) to `passive-income-number-en-ch2/…/s13.jpg`.** That was an open book of
blurred number tables that I had chosen precisely because it was text-free — the hash
proved the cut had already spent it 53 scenes earlier. This is the check earning its
keep; the `find` form saw it, the old `md5sum studio/videos/*/assets/img/*.jpg` glob
would have read zero files for this chapter-based cut.

### The carry-forward ruling — `chapters._carry_forward_en_ch4_to_ch5_s57`

Asked plainly: does s57 read as the next rung DOWN from s46's shipped trickle, or as a
different statement, and if different, is it the right one?

I read the shipping file: **`…-en-ch4/assets-ch4/final/s46.jpg` is a park standpipe with
a brass tap running a thin twisted stream to the ground**, sunlit, colour, wide-ish.
Confirmed as the ruling describes — §10's ladder has been spent one rung early.

s57 as promoted is **not a repeat** of it (different object, framing, tonality) and it
is **a different statement, not the next rung down**. My first reading was that the
different statement was the *wrong* one: the tap is fully off and the bucket empty, so
the frame asserts **zero**, while 5.5 asserts *"about one percent"* — a small but real
flow, and the chapter pays out a finite $5,555,556 precisely because 1% > 0.

I then tested that by trying to source the right statement, and reversed myself:

- Sheet 2, `thin stream of water from a brass tap filling a metal cup`: cell 1 came back
  as **s46's own photograph** (a literal repeat, banned); cell 5 carried legible Dutch
  (`Koud`/`Warm`); cell 3 added an undeclared hand and too generous a stream; cell 6
  was six taps under a "one tap" line. Best was cell 2 (a brass tap with one drop
  hanging). I promoted it and **the gate rejected it at YHIGH 66** — the "dark frame
  holding nothing" failure, measured, not guessed.
- Sheet 3, `thin trickle of water falling into a glass in bright daylight`: six cells,
  **no tap in any of them** (a water texture, a river, a hand throwing water from a wine
  glass, a glass on wood, drops on twigs, a café table).

Eighteen cells across three sheets, zero usable. That is consistent with
`en_tank_becomes_a_drawn_layer_2026-08-10` — the pools refuse this motif — and it is why
the tank is a drawn layer in this cut at all.

**Restored s57 to the original frame, byte-identical (340,664b), and I now think it is
the right call rather than merely the available one.** The defensible reading is not
flow but **scale disproportion**: a tiny wall spigot high on the wall above a large
empty galvanised bucket on the floor. That is exactly 5.5 — *"same tank, smaller tap:
take only what it hands you"* — and it is what makes $5.6M the answer four scenes later.
The residual cost, stated plainly for fin-editor: it is **B&W** and it is a black iron
wall spigot, so it carries neither the "brass tap on a plain steel body" constant nor
the colour of the other three tank frames. §10's declared fallback ("tap/stream macros
in the same material family") covers it, but the rhyme is weaker than the storyboard
intended, and no fetch available to this stage can strengthen it.

### The s66 trail — four sheets, and what each one taught

The slot wants "a thick statistical release, body illegible" (§10 also lists s66 among
the frames that must carry **no legible title, figure or agency name**).

1. **shipped (Pexels binder)** — legible German + `Sparda-Bank` + an IBAN. Reject.
2. **`@commons` "postal square building bureau of labor statistics"** — attempt 1 had
   already built this sheet and stalled before promoting, which is why `manifest.json`
   and the `.src` sidecar disagreed on disk. Sheet returned **3 of 6 cells** (the lossy
   sheet, exactly as warned): a 1989 *Monthly Labor Review* cover with a barcode, the
   Postal Square Building, and a portrait of a Labor official. I promoted the building —
   the correct ladder rung for a named institution, and it *is* BLS's headquarters — and
   **the full-resolution read killed it**: two large green banners reading
   **"National Postal Museum"**, the postal frieze inscription
   (*MESSENGER OF SYMPATHY AND LOVE…*), a `US POST OFFICE` sign and two identifiable
   people on the steps. Every legible mark in frame names the **wrong institution**.
3. **stapled-document re-query** — every viable cell repeated **ch3's s33** ("fingers
   resting on a thick clipped stack of papers"); the rest carried a face, an Apple logo,
   a mortgage application, or a legible "Small Business Accounting Checklist".
4. **receipt re-query** — cell 4 (a $5 bill with two receipts) looked ideal on the grid
   and the **full-res read found a Polish IKEA fiscal receipt**: `PARAGON FISKALNY`,
   `NIP 527-010-33-85`, `IKEA RETAIL Sp. z o.o.`, złoty amounts, a barcode. Wrong
   language, wrong currency, readable brand — the `1 ZŁOTY` defect verbatim, on a
   dollar line. Cell 5 (the text-free open book) then failed the **md5 dedupe** against
   ch2's s13.
5. **`wide row of similar american suburban houses`** — cell 5: US new-build townhouses,
   vinyl siding, garage doors, house numbers 716/714, no people, no cars, bright.
   **Promoted, PASS.**

Why the object changed rather than the adjective: this slot's subject *is* text, and
text is where nationality and brands live — three of four sheets failed on legible marks
that were invisible at grid size. Naming a subject that **cannot carry text** was the
root-cause fix, the same lesson as naming the denomination. Sound-off it is stronger
than the document ever was: identical repeated homes = *the average American household*,
which is what 5.14 actually says.

**Cross-chapter checks that constrained the s66 re-pick** (read from every chapter's
manifest, not from memory): paper-edge macro spent at **s16**, clipped stack at **s33**,
open bound volume at **s15** (and the exact file at **s13**), groceries at **s19/s20**,
a US-currency top-down at **s40**, lobby mailboxes at **s28**.

### Attribution — one defect fixed by hand

`CREDITS.txt` line 14 was an **orphan**:
`Original uploader was AgnosticPreachersKid at en.wikipedia<TAB>CC BY-SA 3.0` —
a dangling half-row left by the rejected Postal Square pick, asserting a **CC BY-SA 3.0**
licence for a file no longer in the chapter. Removed by hand.

**Root cause, for whoever owns `tools/`** (I may not write there): a Commons `author`
string can contain a **newline**, so `commons_hits` writes a CREDITS row that spans two
lines; the re-key on a later `--pick` matches only the keyed first line and leaves the
second behind. Any Commons pick that is subsequently re-picked strands a licence line.
Verified final state: 16 slots, 16 credit rows, **zero orphan rows**, zero files on disk
outside the manifest, zero manifest entries without a file.

### Rank / luma — deliberately not a verdict

Per `predictions_missed_a_sixth_time_2026-08-10` I am not handing a rank table
downstream. What I can say from measurement rather than prediction: the only frames the
gate has ever measured below the floor in this chapter were s60 (93) and a rejected s57
candidate (66); everything shipping cleared. On the invariant — *a substantive beat must
not be left in the chapter's darkest frame* — **s59 is the chapter's most substantive
beat (PEAK 2, the video's own answer) and is visibly its lowest-key frame**, but it
holds two fluorescent tubes, lit door slats, pillars, pipes and a pallet stack, i.e.
real subject, real edges, real falloff, which is the failure mode the floor actually
predicts (pack item 6: the failure is contrast collapse and emptiness, **not** darkness).
I did **not** touch s59 to chase a rank: moving it would be forbidden anyway if it pushed
a more substantive beat to the bottom, and no available fix improves it.

What I did do, as a side effect of fixing real defects, was lift three of the chapter's
darkest frames — s60 (black → white ground), s63 (dark corridor → bright red), s66
(sepia binder → daylight) — which raises the floor around s59 without touching it.
**Settle this on the encode, not on my read.**

### Flagged for fin-editor — considered, not missed

- **s55** is the cut's only `.mega` (300px `ABOUT 1%`) and §10 asks for "the calmest
  background in the chapter". The NYSE facade's **top ~55% is a dense sculptural
  frieze**. The sound-off read is strong and the institution is real and correctly
  American, so I kept it, but the `.mega` legibility risk is real and is a layout call,
  not a sourcing one. Its own gold `STOCK EXCHANGE` lettering is legible (a real
  institution, not a fabricated source, not a brand).
- **s66 → s67 are adjacent domestic exteriors.** Daylight / dusk, plural / singular,
  new-build / colonial, front-on / through bare trees — different photographs and a
  deliberate plural→singular move matching 5.14→5.15, but two house frames back to back
  is worth one editorial look.
- **s64** (road arrows) shows **four to five arrows** under a *"three routes"* line with a
  3-chip counted cascade; and the embedded tram rails + arrow style read faintly
  **European**, though the frame carries no signage, text, plates or vehicles.
- **s65** kept with a known weakness: a **cropped part-month** under *"the whole month,
  not one slice of it"*. All five alternatives were worse — cells 1/2/3/5 carry
  **`JUNHO`, `AGOSTO`** or bilingual Spanish/French day names, and cell 6 is a
  **single-day planner page**, which argues with the line far harder than a crop does.
- **s58** carries no hand, though §10 lists s58 among the five hand frames; the panel
  states the beat without one.
- **s63** carries a small `0004` unit plate and **s59** a `32` on the roller door —
  stray numerals on scenes that display hero numbers. Both read as facility labels.
- **s66** has a ~1%-of-frame sliver of Tyvek house wrap (`TYP…`) at the extreme left
  edge, and two small `PRIVATE RESIDENCE` yard signs. Judged below the brand-mark bar;
  naming them so the judgement is auditable.
- **s56 / s62** are both number macros on warm dark grounds, six scenes apart. Distinct
  compositions and distinct beats; watch, not a defect.

## Changed

- `studio/videos/passive-income-number-en-ch5/assets-ch5/final/s60.jpg` — re-queried, cell 4
- `…/s63.jpg` — free re-pick, cell 2 (no fetch)
- `…/s66.jpg` — re-queried ×4, final cell 5
- `…/s57.jpg` — restored byte-identical after three sheets; net no change
- `…/manifest.json` — queries for s57 (restored), s60, s66 updated to what actually shipped;
  this also closes the manifest/`.src` divergence attempt 1 left on s66
- `…/CREDITS.txt` — orphan CC BY-SA row removed; all 16 rows verified against disk
- `…/IMAGES-ch5.jpg` + `.json` — rebuilt and re-read after the last pick
- `.src` sidecars for the four re-picked slots (written by the tool)

Accepted **16 / 16**. Re-picked **4** (s60, s63, s66, and s57 restored). Dropped **0** —
every scene keeps its background, per the standing rule. No lottie in this chapter.

## Owed

1. **`s56b.jpg` and `s67b.jpg` do not exist.** §10 (lines 778/788) and the scene table
   mark s56 (5.4) and s67 (5.15) as **`swap`** scenes needing an in-scene second framing
   — "tighter on the second table" and "tighter on the lit window" — derived by ffmpeg
   crop from the promoted source, not fetched. ch2's `s10b` and ch4's `s42` exist and are
   recorded in their manifests with the exact `crop=` string, so the convention is
   established; **ffmpeg is not on this stage's allowlist**, so I cannot produce them.
   Route to whoever made s10b/s42. Sources are in place at 1880-wide for both.
2. **Settle the darkest-frame rank on the encode**, not on this log — see above. s59 is
   the frame to measure.
3. **`tools/stock/pixabay_fetch.py`**: the newline-in-Commons-author bug that strands a
   CREDITS row on re-pick (root cause above). One-line fix at the write site; I may not
   write `tools/`.
4. fin-editor's calls on s55's `.mega` background and the s66→s67 adjacency.
