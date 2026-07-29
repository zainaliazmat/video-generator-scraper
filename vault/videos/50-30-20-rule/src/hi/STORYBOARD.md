# STORYBOARD — 50-30-20 Rule (Hindi / India)

**Project:** `studio/videos/50-30-20-rule-hi/` · **Script:** `assets/voice/hindi-lines.json` (hi1–hi9)
**Runtime:** 3:13 (193.45s) · **VO:** ElevenLabs **Harsh** `HTUuC7OeeEt6OL5fViVe` (hi, standard accent, informative_educational) — defaults (stability 0.5 / similarity 0.75 / style 0)
**Facts:** all numbers from [[../../../vault/knowledge/money-facts-2026]] — nothing on screen that isn't in that note.
**Design base:** inherited from `emergency-fund/index.html` — dark `#0d1017`, full-bleed Pexels photo under `grayscale(.32) brightness(.62) contrast(1.05)`, tinted radial scrim, grain overlay, Arial Black, chips / stamps / count-ups, one slow Ken-Burns per scene.

## What's new vs emergency-fund

**The three-bar meter is this video's signature.** One horizontal 100%-wide bar,
split into three segments, introduced in S3 and carried through to S9. It is the
only visual that changes shape — and its re-proportioning in S8 (50/30/20 →
65/15/20) *is* the video's argument. Everything else is chips and photos.

New palette tokens on top of the emergency-fund set:

| Token | Hex | Means |
|---|---|---|
| `--needs` | `#38bdf8` | ज़रूरतें — 50% |
| `--wants` | `#f59e0b` | शौक — 30% |
| `--save`  | `#22c55e` | बचत — 20% (hero) |
| `--warn`  | `#ef4444` | the squeeze / what breaks |
| `--pop`   | `#ff5c39` | CTA only |

On-screen text stays **English/Hinglish** (₹30,000, NEEDS, SAVE) per the India
niche rule — narration carries the Hindi.

## Beats

| # | t (start / dur) | VO@ | On-screen | Visual (Pexels brief) | Motion |
|---|---|---|---|---|---|
| **S1 · HOOK** | 0 / 23.06 | 0.40 (21.86) | kicker `SALARY DAY → 20th` · huge `WHERE DOES IT GO?` · counter `₹ ?` → turns red · stat stamp `INDIA SAVES 7%` · fix stamp `50 · 30 · 20` | Indian young man checking phone banking app, evening, city street; cut-ins: empty wallet, UPI payment screen, crowded metro commute | `₹ ?` pops then `breathe` 3s (taunting) · photo cross-fade on each cut-in · `₹ ?` → red + pulse on "सिर्फ सात प्रतिशत" · `50·30·20` stamp pops last at ~+19s |
| **S2 · PROMISE** | 23.06 / 9.59 | 23.46 (8.39) | 4 chips: `THE RULE` · `3 BUCKETS` · `₹30,000 MATH` · `INDIA PATCH` | Indian rupee notes fanned on a table, soft top light | chips `rise` one per spoken item, ~1.6s apart |
| **S3 · THE RULE** | 32.65 / 21.16 | 33.05 (19.96) | **meter appears**, three segments `50 NEEDS / 30 WANTS / 20 SAVE` · then warn stamp `IN-HAND, NOT CTC` | Indian office desk, laptop + calculator + notebook | meter draws left→right over 2.5s at "पचास…तीस…बीस" · each segment labels as it lands · `IN-HAND, NOT CTC` stamp pops at ~+14s (the beat everyone gets wrong), `pulse` after |
| **S4 · NEEDS 50%** | 53.81 / 25.10 | 54.21 (23.90) | meter dims to `--needs` segment only · chips `RENT` `GROCERIES` `POWER` `COMMUTE` `EMI (MIN)` · then the turn: `1BHK BENGALURU ≈ ₹25,000` · warn bar `METRO NEEDS = 60–70%` | Indian apartment block / to-let board; cut-in: crowded local train or bus commute | chips `pop` in sequence · at ~+13s ("पर सच सुनो") the needs segment **overflows past 50%** to 65% in red, shoving wants/save right — the visual gut-punch · hold, then `NOT YOUR FAULT — CITY MATH` foot line |
| **S5 · WANTS 30%** | 78.91 / 18.10 | 79.31 (16.90) | meter highlights `--wants` · chips `EATING OUT` `OTT` `WEEKEND` `CLOTHES` · stamp `CAP IT, DON'T KILL IT` | Indian friends at a café / street food at night, warm lights | chips `pop` fast (0.4s apart, this is the fun scene) · stamp pops at ~+11s · foot line `a budget that bans joy dies in 2 weeks` |
| **S6 · SAVINGS 20%** | 97.01 / 29.23 | 97.41 (28.03) | meter highlights `--save`, others fade to 25% · ordered list `1 EMERGENCY FUND → 2 SIP / RD → 3 EXTRA EMI` · stamp `HIGH-INTEREST PAYOFF = GUARANTEED RETURN` · foot `SIP FROM ₹500 · CHHOTI SIP ₹250` | Indian piggy bank / small savings tin; cut-in: phone showing a mutual-fund SIP screen (generic, no brand) | list items `rise` 1-2-3 · save segment gets a `glow` + slow `breathe` for the whole scene · `₹500` foot line lands last at ~+24s |
| **S7 · WORKED EXAMPLE** | 126.24 / 24.92 | 126.64 (23.72) | head `₹30,000 IN-HAND` · three count-ups feeding the meter: `₹15,000` `₹9,000` `₹6,000` · foot `₹6,000/mo = ₹72,000/yr` | Indian bank passbook / ATM slip, shallow depth of field | each segment **fills with its number counting up** as spoken — needs (1.2s), wants (1.2s), save (1.2s) · foot line `rise` at ~+20s · this is the payoff shot, keep it clean |
| **S8 · THE PATCH + ACTION** | 151.16 / 26.64 | 151.56 (25.44) | stamp `THE INDIA PATCH` · meter **re-proportions 50/30/20 → 65/15/20** · rule text `CUT WANTS, NOT SAVINGS` · `THE 20 NEVER MOVES` · then `DO THIS TODAY` → `AUTO-TRANSFER ON SALARY DAY` | Indian hand on phone setting a bank auto-debit; cut-in: calendar with the 1st circled | meter animates to 65/15/20 over 1.5s at "चलाओ पैंसठ, पंद्रह, बीस" — **save segment stays exactly the same width**, and that's the point: `pulse` it while wants shrinks · action chips at ~+19s |
| **S9 · RECAP + CTA** | 177.80 / 15.65 | 178.20 (14.45) | 3 recap chips `50 NEEDS` `30 WANTS` `20 FUTURE` · line `SPLIT IT ON SALARY DAY` · `3× THE NATIONAL AVERAGE` · `▶ SUBSCRIBE` | Indian sunrise over a city rooftop — forward-looking, warm | chips `pop` 1-2-3 · `3×` pulses · SUBSCRIBE pops on the spoken word at ~+13s |

## Master timing

| Section | Scenes | Duration |
|---|---|---|
| Hook + promise | S1–S2 | 0:00–0:32 |
| The rule + three buckets | S3–S6 | 0:32–2:06 |
| Proof (worked example) | S7 | 2:06–2:31 |
| Patch + action | S8 | 2:31–2:58 |
| Recap + CTA | S9 | 2:58–3:13 |

## Asset list — AS BUILT (Pixabay, fetched via `tools/stock/pixabay_fetch.py`)

| File | What it is | Verdict |
|---|---|---|
| `s1.jpg` | ₹ coin stacks rising on a ₹500 note | ✔ strong |
| `s1-wallet.jpg` | hands opening an empty wallet (S1 cut-in) | ✔ strong |
| `s2.jpg` | current-series ₹500 notes + Indian coins, macro | ✔ **best in set** |
| `s3.jpg` | hand + pen over financial charts, calculator | ✔ |
| `s4.jpg` | hand holding house keys, houses behind | ✔ neutral |
| `s5.jpg` | Indian dhaba at night, neon menu boards | ✔ authentically Indian |
| `s6.jpg` | coin stacks with seedlings + savings jar | ✔ |
| `s7.jpg` | plain wooden table top | ✔ **deliberately quiet** — the busiest data scene gets the calmest background |
| `s8.jpg` | dark concrete/stone texture | ✔ **replaced after render QA** — the original phone shot had `AT&T` + "slide to unlock" legible behind the climax text |
| `s9.jpg` | golden sunrise over an open road | ✔ mood, not geography |

**Sourcing reality (learned 2026-07-27):** Pixabay's India library is
heritage/tourist-heavy and thin on contemporary urban-professional life —
"indian man…" queries returned non-Indian, Japanese and rural-poverty subjects.
So this cut is deliberately **object-led**: the ₹ notes and coins carry the
cultural signal, not faces. Photos sit at `brightness(.62)` under heavy type, so
they're texture, not information. Cut-ins that couldn't be sourced honestly
(`s1-upi`, `s1-commute`, `s4-commute`, `s8-cal`) were **dropped rather than
faked** — S1 keeps one cross-fade, the rest are single-photo scenes.

To swap any photo: `python3 tools/stock/pixabay_fetch.py --query "…" --out assets/img/sN.jpg --force`
(append `#3` to a query to take the 3rd result). No HTML change needed.

## Deliberate placeholders
- No fund, bank or app named on screen (generic SIP/RD only) — niche rule.
- Meter percentages are the only animated numerals; everything else is static type.

## Sign-off
- [ ] Creator approved this spec — date: __
- [x] Voice locked — Harsh; A/B samples in `assets/voice/_voice-samples/`
- [x] Built into `index.html` — `npm run check` passes (0 errors, 29/29 WCAG AA)
