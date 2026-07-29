# fin-script log — credit-history, cut `hi`, attempt 1 (2026-07-29)

## What I read (in order)

1. `vault/CLAUDE.md` — two-home memory rule; facts live in one home only.
2. `tools/format.json` — `cuts.hi` (₹, forbidden `$`, voice Harsh
   `HTUuC7OeeEt6OL5fViVe`, **12.5 chars/s**), `tiers.short`
   (`range_seconds [60,300]`, `default_target_seconds 165`, `blockframe-9`,
   `lines 9`), `layout` (max 3 chips/row, ≤22 chars, cascade ≤5,
   **`photo_free_scene_ratio: 0.0`**, `keyword_images: true`), `colors`.
3. `vault/videos/credit-history/facts-staging.md` (attempt 2, status ok).
4. `vault/videos/credit-history/run.json` — target 165s, brief, hero, action step.
5. `vault/skills/long_form_scripting.md` — hook-written-last, open loop not
   announcement, one idea per sentence, ~70% reward beat, peak-end.
6. `vault/knowledge/niches/india-finance-market.md` — **Standard Hindi (Harsh)**
   is the locked channel voice; Haryanvi retired for finance; on-screen text
   English/Hinglish; 12.5 chars/s; lakh formatting.
7. `vault/knowledge/design-finance-blockframe.md` — grade, tint ladder, type
   ladder, `ken` alternation, **every-frame-has-image rule**, timing contract,
   imagery rules (no phone-screen bg, no repeated images, calmest bg on densest
   scene).
8. Precedent scripts: `vault/videos/pay-yourself-first/script-hi.md` and
   `vault/videos/good-debt-vs-bad-debt/script-hi.md`.

**Per the contract I did NOT read** `haryanvi-hindi-script-style.md` (wrong lane
since the 2026-07-28 creator decision) or `us-english-script-style.md` (that is
the `-en` cut's guide).

## Contract deviation — the study note does not exist

`vault/knowledge/video-studies/credit-history.md` is **absent**. `run.json` records
`fin-research` as **rescued**, and `logs/fin-research-1.md` explains why:
`library.db` (mtime 2026-07-07) predates the finance pivot and holds **zero**
finance-lane videos, so `backend/study.py` exited non-zero on both
`"credit history"` and `"credit score"`. The research stage correctly refused to
fabricate a study.

**What I did instead of inventing one:** inherited the retention shape from the two
*shipped* hi cuts (`pay-yourself-first`, `good-debt-vs-bad-debt`) plus
`long_form_scripting.md`, and recorded that substitution in the script's
frontmatter `source:` field. **No hook type, beat map or competitor claim is
asserted in the script that would need a study to back it.** This remains owed:
a finance scrape into `library.db`, then a real study before the next topic.

## Decisions made, and why

### 1. The two cross-market traps are the whole job on this topic
facts-staging opens with a RED FLAG section, and it is correct. Both traps are
excluded and both exclusions are made *checkable* by a grep-able warning block at
the top of the script:

- **No "7 years."** That is FCRA §1681c(a) — the US rule. India has no statutory
  auto-delete. The hi cut carries **36 months / three years** (CIBIL's own
  month-by-month window) and nothing longer.
- **No percentage weights.** 35/30/15/10 are FICO's published weights for FICO's
  score. CIBIL publishes none. s4 names the factors **ranked, without numbers**,
  and the on-screen foot states out loud that CIBIL publishes no weights — so the
  absence reads as deliberate rather than as an omission a later stage might
  "helpfully" fill in.

### 2. The hero scene uses staging's own blessed wording, not the statutory claim
The tempting line is "no law in India deletes it." True per the one industry-press
reading of CICRA 2005 — but the statute's primary text was **never obtained**
(indiacode.nic.in and rbi.org.in both unreachable), so it is a SOFT
characterisation resting on a single 2015 secondary. s5 makes the same point using
**CIBIL's own quote** — *"will always be a part of your credit history"* — which is
exactly the wording facts-staging blesses, and which needs no statute behind it.

### 3. Two RBI numbers dropped entirely
- **₹100/day compensation** — staging says explicitly it "needs an RBI primary
  before it goes on screen." No RBI page was ever read (403 / socket closed). Cut.
- **Fortnightly 15th/last-day reporting** — same SOFT bucket, same missing primary.
  It is a good beat ("a miss surfaces in about two weeks"), but s5 already lands
  the 36-month hero and a second unhedgeable number there is pure downside. Cut,
  and recorded in the script's "deliberately NOT used" list so a later stage does
  not rediscover it as a gap.
- **Free annual report kept** — staging names it "the safest of the three for
  screen" and it is the action step's enabler. It carries s8's first instruction.

### 4. The ₹30 lakh / ₹30,000-salary mismatch is answered, not dodged
staging flags it. I made the gap the argument: the VO says the score bills you *on
the day you take the big loan*, which is precisely the brief's "why it matters
before you ever need it" beat. staging forbids improvising a nearer-term
personal/two-wheeler example (none was sourced) — the script says so in a callout
so the build stage cannot invent one either.

### 5. s7 speaks a round anchor, screen carries the range
VO: "क़रीब पंद्रह सौ रुपये" (~₹1,500/mo). Screen: `₹1,390 – ₹1,860`. The spoken
figure sits inside the sourced COMPUTED ₹-A range rather than reciting a
false-precise pair at 12.5 chars/s — same discipline as good-debt-vs-bad-debt's
"17+ years / nearly ₹90,000" handling. Build handoff #5 requires the integers to be
regenerated by the calculator, not carried over from this file. No bank name, no
specific rate, no rate-card date on screen (Claim ₹-4's on-screen rule).

### 6. Format compliance
- **9 segments**, blockframe order exactly: hook · roadmap · concept · rule ·
  audit · action · the math · do-this-today · recap+CTA.
- **Every scene carries a bg photo** (`photo_free_scene_ratio: 0.0`, creator rule
  2026-07-28) plus keyword-matched cut-ins, each naming the VO word it lands on.
  s2 and s7 — the scenes the older shipped pair left photo-free — get the
  *calmest* images (`stack of tied document bundles`, `blueprint paper texture`),
  managing density by choosing a quieter photo, never by dropping it.
- **Fresh imagery only.** s9 deliberately does *not* close on
  `young indian man … phone`: both shipped hi cuts used it and §7 bars repeats
  across videos and channels.
- Chips ≤3/row and ≤22 chars; s4's ranked ladder is a 4-item cascade (≤5 cap).
- Per-video colour table + tint ladder + `ken` alternation declared up front.
- **Persona rules:** no "मैं", no host, no first-person expertise, no lender or
  product pick. CIBIL appears as terminology only.
- **All digits spelled out** in Devanagari VO (छत्तीस, तीन सौ, नौ सौ, तीस लाख,
  पंद्रह सौ …). Zero bare Latin digits in any VO paragraph. On-screen numerals
  carry the exact figures.
- **₹ only.** No `$`, no US institution, no FICO figure anywhere in the cut.

## Budget

| | |
|---|---|
| Segments | **9** |
| VO chars | **~2,110** |
| Char budget (165 × 12.5) | **2,062** |
| Overrun | **+48 chars (+2.3%)** |
| Est. VO runtime | **~169s (2:49)** vs 165s target |
| Est. rendered runtime | **~181s** (+9 × 1.4s lead-in/tail) — inside the 60–300s short range |

Longest scene: **s7 at ~310 chars / ~24.8s** — named in the script as the trim
target if measured TTS runs long. Char counts are Devanagari code points including
combining matras, which is what the 12.5 chars/s rate was calibrated on.

## Untrusted input

None. No web page, transcript or search result was fetched this run — every input
was a vault file or `tools/format.json`. facts-staging's own untrusted-input note
was read as **data**, and its embedded warning about search-tool "REMINDER"
formatting was treated as a finding to respect, not as an instruction to follow.

## Owed / next

1. A finance-lane scrape into `library.db`, then a real
   `vault/knowledge/video-studies/credit-history.md`. Every finance topic will keep
   failing fin-research until this is done.
2. An **RBI primary** before the ₹100/day or fortnightly-reporting figures can ever
   appear on screen in this or any future India credit video.
3. A **current-dated** India rate card, and a near-term (personal / two-wheeler)
   CIBIL-band grid — both are named gaps in facts-staging and both would let a
   future cut use a ₹30,000-salary-scale example instead of a home loan.
4. `script-en` is a **US rewrite**, not a translation: FICO 300–850, the **7-year**
   FCRA rule (which is legitimate over there and is the strongest claim in the whole
   facts file), and the auto-loan APR spread — *never* the 36-month CIBIL window.
