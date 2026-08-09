---
summary: The finalized voiceover pipeline for videos — write & proofread scripts in Nastaliq Urdu (human layer), then transliterate word-for-word to Devanagari (Hindi script) for ElevenLabs TTS, because ElevenLabs supports Hindi but NOT Urdu and Devanagari spells vowels explicitly. Includes per-emotional-zone voice settings, prosody rules, model choice, and the nukta pronunciation risk. NEW (creator rule 2026-07-18): generate ONE CLIP PER LINE, join with ≥0.5s inter-line pause — the timeline then falls out by construction.
updated: 2026-07-22
source: creator A/B test (Pompeii lines 03–05, voice Vikram S) + web research 2026-07-15 (ElevenLabs docs, TTS G2P literature) + first full Rule-0 run (Firaun, 56 clips, 2026-07-19) + Firaun line-granularity rebuild (56 paragraphs → 307 lines, 23:05, 2026-07-22). Tools: [[../../tools/tts/elevenlabs_tts.py]] (API) + [[../../tools/tts/generate_firaun_vo.py]] (line-driven batch driver + timeline)
---

# Voiceover / TTS pipeline (ElevenLabs)

## Rule 0 — ONE CLIP PER LINE (creator rule, 2026-07-18, learned on Pompeii; line def hardened on Firaun rebuild 2026-07-22)

**Generate TTS separately for each script LINE — never one long clip per chapter, and never per
paragraph.** A **line = one spoken sentence or clause (~2–8 s of TTS)**, NOT a multi-sentence
block. One line = one clip = one scene = one exact timeline anchor.

**Why a line, not a paragraph (Firaun rebuild, 2026-07-22):** Firaun v1 was authored as **56
paragraphs**, so each paragraph became one 1–5 min clip (the Madyan-chapter clip alone ran 69 s).
At paragraph granularity the timeline anchors only ONCE per paragraph, so the 3–4 scene images
sitting under it get split by *guessed weights* and drift seconds off the words — the exact
"image/timeline mismatch" the creator hit. Fix: re-lined the 56 paragraphs → **307 lines**; now an
editor who can read the text but not hear the audio can map every scene precisely, because each
line has its own clip with a known duration.

When assembling, join the line clips with **tiered gaps** (added at JOIN time, never baked into the
TTS text — keeps clips reusable):

| Gap | Where | 
|---|---|
| **0.20 s** | breath between lines of the same paragraph |
| **0.40 s** | at a segment boundary |
| **1.0–3.0 s** | ONLY at marked beats (collapse = 3 s, «اب؟» hard cut = 1.5 s, chapter ends = 1 s) |

A flat 0.5 s per line is WRONG at this granularity — across 307 lines it adds ~2.5 min of dead air.

**Why (the Pompeii tax this kills):** Pompeii's VO was generated per-chapter, so scene timings
had to be *recovered* from the monolithic audio — char-length prediction + `ffmpeg silencedetect`
snapping + creator-fixed `FIX_START` overrides across three rebuild rounds ("visuals lag the
voice" bug). With per-line clips, every line's start time = sum of prior clip durations + gaps —
**the timeline is known by construction**, no silence detection, no drift, and a flubbed line
re-generates alone without touching its neighbours.

- ffprobe each clip after generation; log `line_id → duration` (this table IS the edit timeline).
- **Byte-fidelity when re-lining: SLICE the source string, never retype it.** Agents retyping
  mixed Urdu/Devanagari words silently swap scripts (لاش↔लाश، مسالہ↔मसाला) = wrong TTS
  pronunciation. Gate the split with a programmatic reconstruction check: concat of the new lines,
  cite-refs/tags stripped, MUST equal the source paragraph byte-for-byte, or the split is rejected.
- v3's take-to-take variability now costs one line, not one chapter — re-roll cheaply.
- Continuity caveat: **`eleven_v3` has no request-stitching** (no `previous_text`/`next_text` —
  400 `unsupported_model`; § Continuity below), so continuity is seed+voice only; keep
  voice/settings/seed constant. Per-line generation makes prosody slightly choppier across a
  paragraph — acceptable per creator; group only where a multi-line sentence genuinely needs one breath.

## The core rule — PIPELINE B (creator-decided 2026-07-15, on v3)

**Master script = Nastaliq Urdu** (human proofreads/edits here). **Engine input = Devanagari base
with Perso-Arabic /z/ words written INLINE in Urdu script.** NEVER change words, only script.

How we got here (the full arc, so nobody re-litigates it):
1. First A/B was on **v2**, which supports Hindi but NOT Urdu → Devanagari won. We built a
   Devanagari+IPA pipeline on that basis.
2. Switched to **`eleven_v3`** for expressiveness. **v3 supports Urdu** (1 of its 74 langs).
3. On v3, a **Hindi-speaker voice reads Devanagari `ज़` as `ज` (z→j): zalzala→"jaljala".** This is
   the voice's phonology, NOT a spelling bug. **IPA forcing sounded robotic — deprecated.**
4. Feeding the SAME word in **Urdu script** to v3 makes it read as Urdu → correct /z/. Confirmed.
5. But some words read WRONG in Urdu and right in Devanagari (e.g. کنواں/wells → کुओं).
6. **Creator chose Devanagari as base, Urdu inline for the z/f/q words** (Option B). Tradeoff
   accepted: z is frequent → many inline Urdu words per chapter, more mixed-script lines.

**The inline trick (both directions):** a word in the "wrong" script inside the other-script line
makes v3 switch language for that word. Use Urdu-inline for /z/ words in a Devanagari line; use
Devanagari-inline for the rare word Urdu mispronounces (کुओں). This REPLACES the old IPA approach.

**Order:** finalize Nastaliq → transliterate to Devanagari → inline-Urdu every ز/ف/ق word →
generate on v3 → proof-listen. No IPA.

## Pronunciation fixes — how

- **/z/ (and f/q, sometimes gh/kh) words → write inline in URDU script** inside the Devanagari line.
  Confirmed working: زلزلہ، زمین، زندگی، زیادہ، ہزار، گزر، لفظ، زوردار، جہاز، زرا، آتش فشاں، تاریخ.
- **Rare Urdu-mispronounced word → write inline in DEVANAGARI** (e.g. کुओं for کنواں/wells).
- **Spelling variants** still help within a script (double-waw plural کنووں vs hamza کنوؤں) — cheap
  short-clip A/B to pick the one the engine says right, then log it.
- **IPA in `/slashes/` is a last resort only** — v3 supports it but whole-word IPA sounds robotic
  on this voice (rejected by creator 2026-07-15). Prefer the inline-script trick.

**Two-zone proof-listen every batch:** (a) z/f/q/gh/kh words, (b) Islamic/Arabic terms
(Allah, Qaum-e-Lut, verse refs). Script controls the sound; **accent is the voice** — if accent
authenticity matters, switch voice (tested Harsh/Ranbir — all Hindi voices drop /z/; a true
Pakistani/Urdu-speaker voice is the only clean accent fix, needs a voice ID from the library).

## Voice settings — per emotional zone (not one global)

Storytelling = varying the delivery. Settings map to story beats. Counterintuitive: **solemn wants
HIGHER stability (steady/heavy), urgent wants LOWER (performative/varying).** Similarity 0.75–0.85
(1.0 over-enunciates). Style higher = more drama. Speed <1 = weightier.

Since v3 is the chosen model, emotion is driven mainly by **inline audio tags** at the beat where
the feeling shifts, with settings as the baseline. Tags: `[dramatic tone]`, `[awe]`, `[pause]`,
`[whispers]`, `[sad]`, `[sigh]`, `[urgent]`, `[somber]`. Place sparingly — one per beat, not per line.

| Zone (Pompeii example segs) | v3 audio tags | stability / style / speed | Feel |
|---|---|---|---|
| Ordinary morning, setup (01–22) | (none / `[pause]` before turns) | 0.45 / 0.35 / 0.95 | calm, warm, intrigue |
| Eruption, panic (23–37) | `[urgent]`, `[dramatic tone]` | 0.35 / 0.55 / 1.00 | urgent, loud, dramatic |
| Deaths, casts, reveal (38–58) | `[somber]`, `[whispers]`, `[pause]` | 0.50 / 0.30 / 0.85 | hushed, slow, heavy |
| Ibrah / Quran coda (61a–64) | `[somber]`, `[awe]`, `[long pause]` | 0.50 / 0.25 / 0.88 | reverent, measured |

Won baseline (use if unsure): **stability 0.40, similarity 0.80, style 0.50, speed 0.95.**

## Prosody baked into the text

- `<break time="0.8s"/>` for deliberate pauses (max 3s; **don't overuse** — too many → speed-up/artifacts). v2 only.
- **Em-dash `—` and ellipsis `...`** = natural pauses. The Nastaliq master already uses these → transliterate them through to the Devanagari.
- ⚠️ **CAPS-emphasis is Latin-only — useless in Devanagari** (no letter case). Emphasis levers for Hindi = punctuation, `<break>`, and (v3) audio tags.

## Model choice — DECIDED: `eleven_v3` for documentary narration

**Creator A/B, 2026-07-15 (Pompeii 03–05, voice Vikram S):** tuned-v2 beat flat-v2; **v3 + audio
tags beat tuned-v2.** Verdict: **"for documentary-type videos, v3 is perfect."** And the
`[dramatic tone]` tag *did* steer on Hindi/Devanagari text — so v3's emotion tags work here, not
just in English. **Default model = `eleven_v3`.**

- Baseline settings that won: **stability 0.4 / style 0.5 / speed 0.95** (voice Vikram S `st8o4LADtfxckX2PH08x`).
- v3 uses **`[pause]` / `[short pause]` / `[long pause]`**, NOT `<break>`.
- v3 is more variable take-to-take → set `--seed` and be ready to re-roll a bad take.
- Emotion is **scripted inline via audio tags** placed at the beat where the feeling shifts.
- `eleven_multilingual_v2` stays the fallback if a v3 take is inconsistent on a long line.

## Continuity across many segments

⚠️ **`previous_text`/`next_text` (request stitching) is NOT supported by `eleven_v3`** (API returns
`unsupported_model`, confirmed 2026-07-15). Since v3 is our chosen model, continuity instead comes
from keeping **voice + settings + `--seed` constant** across chapters, and generating in reasonably
sized chunks (a chapter of ~5 segments at a time) so prosody flows within each take.
(`--prev-text`/`--next-text` remain usable only if we ever fall back to `eleven_multilingual_v2`.)

## Tool cheatsheet — [[../../tools/tts/elevenlabs_tts.py]]

```
# tuned dramatic line (v2):
venv/bin/python tools/tts/elevenlabs_tts.py --voice <ID> --file line.txt \
  --stability 0.35 --style 0.5 --speed 1.0 --seed 42 --out out.mp3

# hushed/reverent line:
... --stability 0.55 --style 0.2 --speed 0.85
```
Key in `.env` (gitignored). Outputs → `assets/tts-samples/` (gitignored). Key currently lacks
`voices_read` permission → can't `--list-voices`; get voice IDs from the ElevenLabs UI (⋮ → Copy Voice ID).

## What the first full Rule-0 run taught us (Firaun, 56 clips → re-lined to 307, 2026-07-19 → rebuild 2026-07-22)

Pompeii proved Rule 0 in theory (per-chapter clips, timings *recovered*). Firaun was the first
video generated one-clip-per-block from the start. It worked — the timeline fell out by
construction, zero silencedetect, zero FIX_START. **The 2026-07-22 rebuild then showed 56 "blocks"
were still paragraphs**, re-lined them to **307 true lines** (canonical
`script-v2-nastaliq-lines.md` + `script-v2-devanagari-lines.md`; generator now line-driven), and
locked the line definition + tiered-gap model in Rule 0. Result: 307 clips, total runtime 23:05,
timeline correct by construction. Four things are now standing rules:

1. **STRIP CITE REFS FROM THE ENGINE TEXT.** Nastaliq masters embed `(28:4)`, `(20:12-14)`
   mid-line. Those are on-screen cite chips, **never spoken** — if they reach the engine the
   narrator reads "twenty-eight colon four" into the middle of an ayah. Strip with
   `\s*\(\s*\d+\s*:\s*[\d\s,–-]+\)` before generating. This is a *silent* failure — nothing
   errors, you just get a ruined take.
2. **SPELL DIGITS OUT IN THE ENGINE LAYER.** Scripts write `3000 سال`, `1881`, `2021` as digits
   (the Nastaliq usool). Latin digits inside a Devanagari line are a coin-flip for
   English number-reading on v3. Write `तीन ہزار`, `अठारह सौ इक्यासी`, `दो ہزار इक्कीस` instead
   — cheaper than A/B-testing every number. **The master keeps its digits** — this is a
   transliteration fix, never a master edit (pipeline rule 2).
3. **NARRATION RATE ≈ 12.0–12.2 chars/s** of Nastaliq master text, and it transfers across
   videos (Pompeii 12.0 → Firaun 12.2, measured across all 6 zones). **Budget the script length
   BEFORE writing it:** 22 min ≈ 16,000 chars. Firaun's Madyan chapter was budgeted 2:30 and
   written at ~3,900 chars → came in at 5:13. A 30-second check at script time would have
   caught it.
4. **Make the batch driver resumable and offline-testable.** 56 sequential API calls will fail
   partway eventually. Skip-if-exists + `--only <id> --force` means a crash costs nothing and a
   bad take re-rolls alone. A `--selftest` that runs with no network (block count, cite-refs
   stripped, no bare digits, no Arabic artifacts, zone map complete) is what actually prevents
   "one bad setting × 56 clips" — run it before every batch.

**Zone settings that worked** (Firaun, voice Vikram S, similarity 0.80, seed 42, `eleven_v3`):

| Zone | stab / style / speed |
|---|---|
| default / hook | 0.40 / 0.50 / 0.95 |
| WARM storytelling | 0.45 / 0.35 / 0.95 |
| REVERENT (kalam, 10:92, ibrah) | 0.50 / 0.25 / 0.88 |
| PEAK TENSION (escape→drowning) | 0.35 / 0.55 / 1.00 |
| COOL / forensic (investigation) | 0.42 / 0.30 / 0.95 |
| BRISK / punchy (myth stamps) | 0.40 / 0.50 / 1.02 |

Overlaps resolve **most-specific-wins**: reverent beats warm (a kalam beat sitting inside Act 1),
brisk beats cool (myth stamps inside the investigation half). Encode that ordering in the driver,
don't hand-maintain a flat 56-row map.

**Join gaps belong to assembly, not the TTS** — and are **tiered, not flat** (see Rule 0's table:
0.20 s intra-paragraph breath, 0.40 s at a segment boundary, 1.0–3.0 s only at marked beats — e.g.
the collapse = 3.0 s). Keeping gaps out of the generated audio is what lets a clip be re-rolled
without touching its neighbours.

⚠️ **Proof-listen is still owed after every batch** — the text is correct *by construction*, but
z/f/q/gh/kh words, Islamic terms and spelled-out numbers need a human ear before ship.

## Related
- [[../knowledge/urdu-script-style]] — Roman-Urdu voice/style rules (spoken register).
- [[../videos/video-hist-01-pompeii/script-v1-nastaliq]] — Nastaliq master (first user of this pipeline).
- [[../videos/video-hist-02-firaun/script-v1-devanagari-tts]] — engine-input layer, first full Rule-0 run.
- [[../videos/video-hist-02-firaun/script-v2-nastaliq-lines]] — human canonical, 307 lines + scene cues + cites (line-granularity rebuild).
- [[../videos/video-hist-02-firaun/script-v2-devanagari-lines]] — TTS engine input, line-driven.


---

## Records drained from `tools/format.json` (2026-08-09)

Provenance and resolved incidents. `format.json` is the constants file; its own
`_comment` says rationale belongs here, and 47% of it was rationale.

### `cuts.en._chars_per_second_trap`

RESOLVED 2026-08-07 — kept as the record of how it was resolved, because the ordering rule still applies to the hi key. The bug was never the rate alone: fin-script budgeted chars as target_seconds × rate, which ignores the per-line scene padding that is not audio, so a wrong rate and a wrong formula cancelled and both cuts still hit target. Fixing either one alone breaks that cancellation — raising the rate first would have made every script ~17% long. Order followed: (1) fin-script and fin-audit both derived (target − lines × (lead_in + tail)) × rate independently on passive-income-number and logged the override; (2) the orchestrator's confirm-block formula was corrected in .claude/commands/finance-video.md; (3) only then was chars_per_second raised. Evidence that the key was wrong rather than noisy: across 78 lines of passive-income-number-en, ALL 78 drifted negative against expected_seconds. Noise is two-sided; a wrong key is one-sided.

### `cuts.hi._chars_per_second_note`

14.281 measured 2026-08-08 across all 81 per-line clips of passive-income-number-hi on AMRUT (5,919 chars / 414.454s of audio). Was 13.03, measured on HARSH across first-lakh-first-thousand-hi and carried over on the assumption the voices matched. They do not: Amrut is 9.60% faster per line, and the drift was ONE-SIDED — 71 of 81 lines short against expected — which is the documented signature of a wrong key, not noise (see cuts.en._chars_per_second_trap; en showed 78/78). Ordering rule was already satisfied: the speech-time budget formula was corrected 2026-08-07, so raising the rate now does not un-cancel a second error. This is the FLAT delivered rate including pause silence, which is what script budgeting needs; pipeline_check adds tts.pause_seconds on top per line.

### `cuts.en._chars_per_second_note`

17.57 = the mean of three FLAT measurements on the cuts we actually ship (first-lakh-first-thousand-en MEDIUM 17.73 · japanese-money-methods-en LONG 17.39 · passive-income-number-en MEDIUM 17.588). Raised from 16.1 on 2026-08-07, once the both-or-neither precondition below was finally met. ⚠ SHORT CAVEAT: the 16.1 it replaces was itself measured, on SHORT cuts (16.11, 16.64). The gap is mechanical, not noise — SHORT writes shorter lines, so punctuation-pause time is a bigger share of each clip and the flat chars/second comes out lower. This single key is now tuned for MEDIUM/LONG, which is all the channel has shipped since 2026-07-30. If a SHORT cut is ever made again, expect scripts ~9% long and re-measure before trusting this number.

### `cuts.hi._voice_note`

Creator pick 2026-08-07 after an A/B listening test: Amrut Deshmukh (Educational Hindi Voice) replaces Harsh (Clear & Calm Documentary Narrator), the locked channel voice since 2026-07-28. Chosen to match style E. Samples: studio/voice-tests/passive-income-number/. RUNTIME: free. ⚠ CORRECTED 2026-08-08 — this note previously said the two voices landed within 0.2s on a 58-second passage so no re-budget was needed. That was measured on a CONTINUOUS read, and it was wrong by 9.6% at the per-line level. A continuous read carries inter-sentence pause INSIDE the audio; per-line clips push that same pause out into lead_in + tail padding, where it stops counting as speech. Measure every future voice A/B on PER-LINE CLIPS or it will always under-report the flat rate by roughly the padding it absorbs. Same copy: 118.0s continuous vs 107.20s as 21 per-line clips.

### `tts._pause_seconds_note`

Silence the voice actually takes at each mark, added to the flat chars/rate estimate in pipeline_check.expected_seconds. Without it the cold-open hook — short punched clauses, the winning format in this niche — self-flags as truncated: first-lakh-first-thousand line 1.1 measured 5.88s against a 3.84s flat estimate (+53%) purely from one danda and one em-dash. Symmetric tolerance means this makes genuinely SHORT clips easier to catch, not harder.

### `scene._lead_tail_tier_note`

lead_in/tail are charged PER LINE, so they scale with line count and a value tuned at SHORT's 9 lines is wrong at MEDIUM's ~86. At 0.4+1.0 the hi cut spent 120.4s of its 566s on inter-line padding; with tts.pause_seconds already buying 80.5s of in-line pause that is 35% of the video in silence. MEDIUM/LONG override to 0.25+0.55 (68.8s), landing 514.8s against the 510s target. Creator 2026-07-31: 'looks professional and engaging not dead.'
