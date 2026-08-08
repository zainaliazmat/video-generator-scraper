---
summary: fin-script log — japanese-money-methods, cut hi, attempt 1. LONG/ledger-rail, 92 lines, 7,544 chars, est. 652.6s (10:53) vs the 660s target (−1.1%). Premise correction applied; no Japan-vs-India comparison anywhere; India's saving rate deliberately unused.
updated: 2026-08-01
source: run.json + facts-staging.md + knowledge/video-studies/japanese-money-methods.md + format.json + skills/long_form_scripting.md + knowledge/niches/india-finance-market.md
stage: fin-script, cut hi, attempt 1
---

# fin-script — japanese-money-methods / hi / attempt 1

**Artifact:** `vault/videos/japanese-money-methods/script-hi.md`

## Read (in order)

`vault/CLAUDE.md` · `tools/format.json` · `facts-staging.md` · the study note ·
`vault/skills/long_form_scripting.md` · `vault/knowledge/niches/india-finance-market.md`
(Standard Hindi per the 2026-07-28 creator decision — `haryanvi-hindi-script-style.md` was
**not** read) · `run.json` · `knowledge/finance-audit-2026-07-29/03-design.md` §4A for the
ledger-rail spec · `videos/first-lakh-first-thousand/script-hi.md` as the per-line-chapter
reference implementation.

## Numbers

| | |
|---|---|
| Lines (= clips = scenes) | **92** across **8 chapters** |
| Total VO chars | **7,544** |
| Char budget | `(660 − 92 × 0.8) × 13.03` = **7,640** → **−1.3%** |
| Est. VO | 578.9s |
| Est. padding (`tiers.long` 0.25 + 0.55 per line) | 73.6s |
| **Est. runtime** | **652.6s = 10:53** vs 660s target → **−1.1%** |
| Average scene | 7.09s (`target_scene_seconds` 6.5, `max` 9.0) |
| Longest / shortest line | 103 chars (8.7s scene) / 57 chars (5.2s scene) |

Chapter split: 10 / 11 / 12 / 13 / 12 / 14 / 12 / 8.

## Decisions that needed making

1. **Ch1 carries no number at all.** The study's conclusion 1 narrows the old
   "first number inside 8 seconds" rule for this topic: the category winner spends 40s of
   second-person pain before its first promise at 15.8× subs. Promise lands 0:54, first
   number 1:12 — eighteen seconds later, inside the ~15s tolerance the study sets.
2. **India's saving rate (I1 7.0%, I3 34.2%) is not in the script at all.** The hard rule
   forbids a head-to-head, and stating India's rate anywhere in a video hooked on Japan's
   rate creates the comparison by adjacency even with no sentence making it. Ch5 uses the
   channel's ₹30,000 worked example instead. This is the single largest deviation from what
   a naive read of the topic would produce, and it is recorded in "Deliberately NOT used".
3. **J8 (BOJ Chart 2) is used in the `hi` cut**, at 3.4–3.5, as percentages only — no `$`
   glyph, no conversion, and an on-screen foot stating it is an **asset-mix** comparison and
   explicitly not a saving-rate one. `facts-staging.md` names this the only safe
   cross-market fact, and the "saving is not investing" beat is what makes the four methods
   land as behavioural tools rather than as a national explanation.
4. **Promise three, deliver four.** Title and 2.1 sell three methods; Taru wo Shiru opens at
   8:31 = 78% (TOP's fourth ran 72–87%). The ~70% mark instead lands on 6.7 — the admission
   that the famous four kakeibo categories are a later Western addition. That admission is
   the video's Von Restorff beat and its honesty moat: every competitor teaches them as
   Hani Motoko's.
5. **₹6,000, not ₹5,000, as 20% of ₹30,000.** The shipped `first-lakh-first-thousand` cut
   used ₹5,000 for the same "20% of ₹30,000" split, which is arithmetically wrong. Corrected
   here and flagged in the fact trace so a later stage does not "restore" consistency with a
   wrong figure.
6. **Font-subset trap caught at script time, not build time.** The vendored face carries 97
   codepoints and **no CJK**, plus no `~` `×` `→` `▶` `¥`. So: on-screen Japanese is romaji
   only, kanji live inside the photograph (the tsukubai), `~1%` became `ABOUT 1%`, `30×`
   became `30 TIMES`, and yen figures are written `JPY 197,432`. `facts-staging.md` asks for
   `~1%` on screen; that substitution is recorded in the fact trace rather than made silently.
7. **`RAIL OFF` on exactly seven scenes** is the anti-sameness device inside ledger-rail —
   the rail retracts and the photo goes full-bleed on the hook, the thesis, the honest line,
   the one question, the admission, the stone and the close. Documented so the build does not
   spread it.

## Compliance self-check

- Every figure traces to a named `facts-staging.md` row; the trace table is in the artifact.
  No number appears whose source line does not exist.
- **No Japan-vs-India or Japan-vs-US saving-rate comparison**, spoken, on screen, or by
  adjacency.
- **No `$`, no US institution, no ¥→₹ conversion.** `₹` only.
- **No number attached to mottainai, hara hachi bu or taru wo shiru** — 5.1's on-screen foot
  says so explicitly.
- Digits spelled out in every VO line; on-screen numerals carry the exact figures.
- VO is in the `>` block only; all on-screen text is English/Hinglish/romaji.
- Persona: no host persona, no first-person expertise, no fund/stock/scheme pick. **मैं** and
  **हम** appear in no VO line. PPF, the SIP minimum and the ₹250 tier appear as price
  evidence, each with a `foot:` saying so.
- The four blog-tier claims `facts-staging.md` §5 predicted this stage would hit (the 37-vs-4
  contrast, the "kakeibo saves 35%" claim, the Okinawa calorie/lifespan numbers, the mangled
  ₹2,000→₹400 arithmetic) are all listed as rejected in the artifact, so the audit stage does
  not re-find them.

## Owed to later stages

- **fin-storyboard:** 92 images, three continuous-zoom hold pairs, 12 frames that must be
  Indian, 1 flat-lay that must be a photograph rather than a card.
- **fin-build:** the ElevenLabs cap in `run.json` is 30 per stage against 92 clips — batch it.
- **fin-audit:** the ₹6,000-vs-₹5,000 divergence from the shipped cut is deliberate; the
  `~1%` → `ABOUT 1%` screen substitution is deliberate.
- **The `-en` cut has no on-topic competitor in the packet** (the study's own open item —
  the `japan` lane returned macro and history). Its packaging is otherwise inferred from
  this cut, and its hero is J8/U3 + BEA, not the FIES pair.
