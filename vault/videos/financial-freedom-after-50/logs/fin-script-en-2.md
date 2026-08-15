# fin-script — financial-freedom-after-50, cut `en`, attempt 2

**Tier** long · **target** 746 s (`run.json.target_seconds`) · **output**
`vault/videos/financial-freedom-after-50/script-en.md`
**Nature of this attempt:** targeted amendment on two creator rulings, not a rework.
`mark script` PASSED at attempt 1; everything outside the two rulings is unchanged.

---

## Ran

1. Re-read the attempt-1 script in full and the two rulings from the coordinator.
2. **Ruling 1 — line 1.8 REPLACE.** Collapsed the draft's two lines (old 1.8 "For the past
   fifteen years, I've been in the trenches…" 143 chars + old 1.9 "And I've seen them build
   futures…" 108 chars = 251 chars over two lines) into the creator's single ruled line, 152
   chars. Chapter 1 goes 12 → 11 lines; the file goes 124 → 123.
3. **Renumbered chapter 1 downstream of the replacement** and chased every reference to a
   shifted id (details in Evidence — there were three, and one of them was in a different
   section of the file).
4. **Recomputed every derived number in the file** from the new line and char counts: the
   frontmatter summary, the char budget, the runtime, the tolerance percentage, the chapter
   table (lines/chars/starts/%), the per-chapter timing table, the scene average, the
   longest-line check, the TTS call count, and all eight retention-beat timecodes, which all
   shift ~6.5 s earlier because chapter 1 got shorter.
5. **Ruling 2 — hoist KEPT.** Moved it out of the flag section, marked creator-approved with
   the date in three places (header §D2, the chapter-1 preamble, and the 1.3 cue) so
   `fin-audit` meets the authorization wherever it enters the file.
6. Rewrote the "What this stage did to the creator's draft" section so it reflects the final
   state and contains nothing open.
7. Re-grepped the whole file for the forbidden currency glyph and the
   `us-english-script-style` §6 instant-reject list.

## Failed

**One real problem, found by measuring the ruled text rather than assuming it fit.**

**The creator's replacement line is 152 characters, past the 144-char line ceiling.**
At 17.57 c/s that is 8.65 s of VO + 0.8 s padding = **9.45 s**, over
`scene.max_scene_seconds` **9.0** — and `check_build` FAILS a scene that holds one photo
past that. Left alone this would have surfaced as a build failure two stages downstream,
where the fix is expensive and the cause is invisible.

**Not resolved by editing the text** — it is creator-ruled wording and the instruction was to
apply it verbatim. Resolved on the frame instead: the 1.8 cue now carries a mandatory
**two-framing** instruction (wide on the boardwalk, then a push to the couple), so no single
framing holds past 9.0 s. This is not an invention — `passive-income-number` shipped line 2.2
at 155 chars the same way, and that precedent is cited in the cue and in handoff item 2 so a
later stage does not "fix" it by cutting the creator's words.

Also worth recording: **attempt 1's header estimated this drop-in would "cost 41 chars". That
was wrong** — it *saves* 99 (251 → 152). The estimate was never measured because the drop-in
was hypothetical at the time. Every number in the amended file is measured, not carried over.

## Evidence

### The replacement, measured

| | old (2 lines) | new (1 line) |
|---|---|---|
| text | "For the past fifteen years, I've been in the trenches with people just like you, folks in their fifties and sixties who felt hopelessly behind." + "And I've seen them build futures they are excited about using the exact roadmap I'm about to share with you." | "People in their fifties and sixties who felt hopelessly behind have been building futures they are excited about, using the exact roadmap in this video." |
| chars | 143 + 108 = **251** | **152** |
| lines | 2 | 1 |
| VO seconds | 8.14 + 6.15 = 14.29 | 8.65 |
| + padding | 1.6 | 0.8 |
| clip seconds | **15.89** | **9.45** ⚠ over `max_scene_seconds` 9.0 |

Net: **−99 chars, −1 line, −6.44 s.**

### Every derived number, recomputed

```
budget = (746 − 123 × 0.8) × 17.57 = 647.6 × 17.57 = 11,378 chars   (±10% → 10,240 … 12,516)
```

| | attempt 1 | attempt 2 |
|---|---|---|
| VO lines | 124 | **123** |
| VO chars | 12,386 | **12,287** |
| char budget | 11,364 | **11,378** |
| % of budget | +9.0% | **+8.0%** (inside ±10%) |
| VO audio | 705.0 s | **699.3 s** |
| padding | 99.2 s | **98.4 s** |
| runtime | 804.2 s (13:24) | **797.7 s (13:18)** |
| vs 746 s target | +7.8% | **+6.9%** (inside `length_tolerance_pct`) |
| words @ 5.63 c/w | ≈2,200 | **≈2,182** |
| scene average | 6.48 s | **6.49 s** (`target_scene_seconds` 6.5) |
| longest line | 143 → 8.94 s ✓ | **152 → 9.45 s** ⚠ two framings required; next longest 143 → 8.94 s ✓ |
| shortest line | 43 → 2.45 s ✓ | unchanged ✓ (`min_clip_seconds` 1.0) |
| TTS calls | 124 / 154 | **123 / 154** — 31 spare |

Chapter table (only chapter 1 changed; every later chapter keeps its length and shifts
6.5 s earlier):

| Ch | lines | chars | runtime | starts (a1) | starts (a2) |
|---|---|---|---|---|---|
| 1 | 12→**11** | 1,157→**1,058** | 75.5→**69.0 s** | 0:00 | **0:00** |
| 2 | 17 | 1,678 | 109.1 s | 1:15 | **1:09** |
| 3 | 26 | 2,633 | 170.7 s | 3:05 | **2:58** |
| 4 | 18 | 1,731 | 112.9 s | 5:55 | **5:49** |
| 5 | 19 | 1,926 | 124.8 s | 7:48 | **7:42** |
| 6 | 16 | 1,777 | 113.9 s | 9:53 | **9:46** |
| 7 | 16 | 1,484 | 97.3 s | 11:47 | **11:40** |
| | **123** | **12,287** | **797.7 s** | | |

### Every retention beat, re-derived (not shifted by hand)

| beat | line | a1 | a2 | % of 797.7 s | still passes? |
|---|---|---|---|---|---|
| payoff promise | 1.3 | 0:11 | **0:11** | 1.4% | ✓ `hook_gate_seconds` 15 — **unaffected**, 1.3 precedes the replacement |
| spoken disclaimer | 3.4 | 3:23 | **3:16** | 24.6% | ✓ still before the first figure |
| first dollar figure | 3.8 | 3:46 | **3:40** | 27.6% | ✓ onscreen disclaimer fires here |
| IRS cluster | 3.8–3.25 | 3:46–5:20 | **3:40–5:14** | — | ✓ nine own-source cards |
| drop zone opens | 5.1 | 7:48 | **7:42** | 57.9% | ✓ 55–65% band is now 7:19–8:39 |
| **~70% reward** | **5.14** | 9:18 (69.4%) | **9:12** | **69.2%** | ✓ still the reward slot |
| callback | 7.7 | 12:32 | **12:19** | 92.6% | ✓ |
| single CTA | 7.10 | 12:47 | **12:38** | 95.0% | ✓ terminal, no mid-roll CTA |

**The hook gate is untouched by this amendment** — 1.1, 1.2 and 1.3 are byte-identical and
the replacement sits five lines later. The promise still starts at 11.2 s flat / ≈12.5 s
pause-loaded.

### Id renumbering — the three references that had to move

The renumber is not just the bold line ids. Grepping the file for every mention of a
chapter-1 id above 1.8 found three live cross-references, and one of them was 150 lines away
from the change:

| where | attempt 1 | attempt 2 |
|---|---|---|
| header §B, the split list | `1.10/1.11` (the roadmap sentence split) | **`1.9/1.10`** |
| header §C1 / now §D2, the hoist rationale | "…is a complete opening (now 1.10)" | **"(now 1.9)"** |
| line ids in chapter 1 | 1.9 · 1.10 · 1.11 · 1.12 | **1.8 (merged) · 1.9 · 1.10 · 1.11** |

Checked and confirmed **not** affected: the two cross-scene callbacks both point below the
change — 7.7 references **1.1** (same kitchen table) and 7.9 references **1.7** (the
notebook). Neither id moved. No `[img: …]` cue in any other chapter keys off a chapter-1 id
above 1.7.

### Section rewrite

The old header had `§C Deviations` + `§D ⚠ COMPLIANCE FLAG raised, not resolved`. That shape
is now wrong on both counts — one deviation became an authorized change and the flag became a
ruling. New shape:

- **§A** Forced factual corrections (2) — unchanged in substance; the §A2 rationale lost its
  forward-reference to the persona flag, since the flag no longer exists.
- **§B** Sentence splits (14) — ids updated, plus a new line recording that **1.8 exceeds the
  ceiling deliberately** and pointing at its cue.
- **§C** Compliance inserts (3) — was §C2/§C3; promoted to its own section now that the
  hoist has moved out, and the disclaimer timecodes updated to 3:16 / 3:40.
- **§D** **Creator rulings — both resolved 2026-08-15, neither open.** D1 is the replacement
  with the creator's ruling, the superseded `no_advice_framing` instruction named as
  non-binding, and the quoted new line. D2 is the hoist, marked **creator-approved, authorized
  structure, not a deviation**, with the note that `fin-audit` should not re-litigate it.
- The section's opening sentence now ends **"Nothing in this section is open."**

The persona rule box at the top of the file was also rewritten: it previously pointed at the
flag, and now states positively that **no first-person expertise claim remains anywhere in the
cut**, and that "I" appears only as the narrator of the video ("In this video, I'm giving
you…"), never as a practitioner. That distinction is what a monetization reviewer is actually
looking at, so it belongs in the file, not only in a log.

### Compliance re-check after the change

- **No credential claim survives.** The only first-person constructions left in VO are
  narrator-of-this-video ("In this video, I'm giving you…", "I'm here to tell you", "hear me
  out", "I know, it's not the sexiest part of finance"). None asserts experience, clients,
  years, or standing to advise.
- Both forced factual corrections stand verbatim (5.16–5.17, 4.4).
- All 14 splits and 23 joins stand.
- Disclaimer 3.4–3.5 stands, all four placements still listed, timecodes updated.
- CTA 7.10–7.12 and the subscribe ask in 7.15 stand.
- Fact trace, labels, `no_return_promise` sweep, and the "available but deliberately unused"
  list are byte-identical — the amendment touches no figure.
- Localization grep clean: zero hits for the forbidden currency glyph or any §6 instant
  reject. The only `\bflat\b` hits remain the four references to the *flat timing model*.

## Changed

1. **`script-en.md` line 1.8 replaced** with the creator's ruled text; old 1.9 absorbed into
   it. Chapter 1: 12 → 11 lines, 1,157 → 1,058 chars.
2. **Chapter 1 renumbered** 1.9/1.10/1.11 (was 1.10/1.11/1.12) and the three cross-references
   above updated.
3. **1.8's cue rewritten**: it now uses the boardwalk image (freed by the merge — the office
   -table image that carried the old "fifteen years" line is dropped from the shot list
   entirely, since nothing in the cut claims it any more), records the creator ruling and the
   date on the frame, and carries the **two-framing requirement** with its 9.45 s arithmetic
   and the `passive-income-number` 2.2 precedent.
4. **Every derived number recomputed** — frontmatter summary, budget block, both timing
   tables, chapter starts and percentages, scene average, longest-line note, TTS call count,
   all eight beat timecodes, and the disclaimer placement table (3:23 → 3:16, 3:46 → 3:40).
5. **Header §A–§D restructured** per the coordinator: the flag is gone, both rulings are in a
   resolved section dated 2026-08-15, the hoist is marked creator-approved in three places.
6. **Handoff gained one item** (now 9): *line 1.8 needs two framings inside its one scene*,
   placed second so it is read before anyone touches the storyboard.
7. **Frontmatter `stage:`** now reads *"attempt 2 — creator-ruled amendment to the attempt-1
   reformat (mark script PASSED at attempt 1)"*, and `source:` gained the rulings.

**Deliberately NOT changed** (per "leave everything else byte-identical"): every other VO
line, every other cue, the fact trace, the title options, the chapter titles, the disclaimer
text, and the `head: DISABILITY COVER` string at 4.12 — that one-word Americanization is
still owed and was explicitly out of scope for this amendment. The whole file had to be
rewritten to apply the change (this stage has Write but no patch tool), so byte-identity
elsewhere was maintained by reproduction, not by diff.

## Owed

1. **⚠ Line 1.8 must ship with two framings.** 9.45 s against `max_scene_seconds` 9.0. If
   `fin-storyboard` assigns it a single framing, `check_build` fails the scene and the only
   remaining fixes are cutting creator-ruled text or re-rendering. Handoff item 2.
2. **One-word cue fix, 4.12:** `head: DISABILITY COVER` → `head: DISABILITY INSURANCE`.
   "Cover" as a noun for insurance is British; the US term is "coverage". On-screen head, not
   VO, on no instant-reject list, and `fin-storyboard` rewrites heads anyway — carried over
   from attempt 1 and still out of scope here. Apply at the next touch of the file.
3. **`run.json → constraints.no_advice_framing` still carries the superseded instruction.**
   The coordinator says it is being updated; until it is, the constraint text in run.json
   contradicts the shipped script. This stage does not write run.json. Whoever does should
   also record ruling 2 (hoist approved) there, so a future re-read of the constraints does
   not re-open a decided question.
4. **Eleven screenshots**, including the two `ssa.gov` captures that must come from a network
   path that is not 403'd. Unchanged from attempt 1.
5. **`hook_gate_en` measured on the rendered clip** and recorded in run.json — the 11.2 s in
   the file is a model, and the two models have been 4.6 s apart before.
6. **Chapter starts regenerated from ffprobe durations** before they ship as YouTube chapters;
   `tts.pause_seconds` is not in the modelled table.
7. **The lane is still unmeasured** — scrape + study owed before the next 50+ topic, filtered
   to `tiers.long.comparable_length_band_seconds` 480–1800 s.

**MISSING-CONSTANT:** none.
