---
summary: Publish pack for the US/English ($) cut of Pay Yourself First — title options, description with real chapter timestamps from timing.json, tags, 3 thumbnail variants + chosen line, Gate 2 compliance. Research caveat — no fresh autocomplete pull was possible this run; en evidence reused from the dated 2026-07-27 pulls in the emergency-fund and 50-30-20 en packs + WebSearch 2026-07-28.
updated: 2026-07-28
source: Chapter times = scene_start values in studio/videos/pay-yourself-first-en/assets/voice/timing.json (QA-verified, VO drift 0.021s, runtime +0.041s — fin-render log). Search evidence = [[../emergency-fund/youtube-metadata-en]] + [[../50-30-20-rule/youtube-metadata-en]] (autocomplete + competitor scrape, 2026-07-27) + WebSearch 2026-07-28.
---

# YouTube publish pack — Pay Yourself First (English / USA cut)

**Channel:** @moneymavens101
**Video:** `studio/videos/pay-yourself-first-en/renders/FINAL-1080p-en.mp4` (2:57.8, 1080p, 12.85 Mbps, QA PASS)
**Thumbnails (creator picks at upload):** `vault/videos/pay-yourself-first/src/thumbs/thumbnail-en-v1.png` · `-v2.png` · `-v3.png` (source: `vault/videos/pay-yourself-first/src/thumbs/index.html` §ev1/§ev2/§ev3)

| Variant | Composition | Numerals (all in script-en.md) |
|---|---|---|
| **v1 — recommended** | THE MATH — centered, photo-free dark block, green. "$400 ↓ every payday → **$4,800**" + 12-tick strip | $400 · $4,800 · 12 (en7) |
| v2 | THE HOOK — empty-pocket photo, red, left text. "EMPTY BY / THE 20TH?" + draining 1→20 bar | 20 (en1) |
| v3 | THE FLIP — calculator photo, "SPEND FIRST" struck / "SAVE FIRST" green. "even 5% works" | 100 (en4) · 5% (en2/en8) |

**chosen: v2** _(read back 2026-08-06 from the creator's own screenshot of the live tile — exact match to `src/thumbs/thumbnail-en-v2.png`. **v4 was NOT used**, and neither was the title it was built for — the live title is "Why Your Account Is Empty by the 20th (Pay Yourself First)". AI-enhance prompt: [[index]] §AI-enhance prompts.)_

**Thumbnail sameness finding (last 3 on this channel — vault packs):**
needs-vs-wants ("YOU THINK $86. IT'S $219." over $100 bills), 50-30-20 ("RENT EATS
YOUR ENTIRE 50%" over townhouses), emergency-fund ("ONE REPAIR FROM BROKE" over a
car in the shop) are **all** photo + big left-aligned text. v2 here continues that
streak (money-hardship photo + left text + red question) — usable, but a fourth
photo/left/red would be a near-duplicate composition run. **v1 is the first-ever
green, centered, photo-free thumbnail on @moneymavens101** — the honest framing
for a video whose payoff is a growing number, and the pattern-breaker. Note: the
12-tick strip already appeared on the needs-vs-wants en thumb — kept deliberately
as the series brand, not a duplication accident.

## ⚠ Research caveat — read before trusting the tags

**No fresh YouTube-autocomplete pull was possible in this run.** The pipeline's
allowlisted tools have no autocomplete fetcher, and `backend/study.py` returned
"No usable videos in the library" for `pay yourself first` / `paycheck` /
`save money` (topic never scraped — same gap the hi run logged). So: **no
invented evidence.** Everything below reuses the **dated 2026-07-27** verified
pulls recorded in [[../emergency-fund/youtube-metadata-en]] and
[[../50-30-20-rule/youtube-metadata-en]] (suggestqueries hl=en gl=US +
competitor scrape) — one day old, same US savings demand cluster — plus a
2026-07-28 WebSearch. Re-verify at upload if in doubt.

**What that evidence says, applied to this topic:**
- **The live US lane is the payday routine.** Nick Invests' "Do This EVERY Time
  You Get Paid (Payday Routine)" sat at **350k** on the 2026-07-27 scoreboard,
  and a 2026-07-28 WebSearch finds that exact formula heavily cloned across 2026
  ("Do This EVERY Time You Get Paid in 2026 (Paycheck Routine)" etc., at least 6
  near-identical titles). The lane is real demand; **the exact "Do This EVERY
  Time You Get Paid" phrasing is off-limits** (their 350k title, and now a slop
  cluster).
- **Verified autocomplete strings adjacent to this video** (2026-07-27):
  `how much should i save per paycheck` · `how to split your paycheck (for
  savings)` · `high yield savings account (explained)` · `save $1000` ·
  `budgeting for beginners (2026)` · `how to save money fast` ·
  `how to budget and save in your 20s`.
- **`pay yourself first` as a US search string is unverified** — no autocomplete
  evidence. A 2026-07-28 WebSearch shows the phrase is carried mostly by
  bank/credit-union education pages (Capital One, Bankrate, RBFCU), i.e. the
  concept is in circulation but YouTube search volume is unproven. Use it as the
  title parenthetical and in tags, not the title lead.

## Title (pick one — English, channel rule)

1. **Why Your Account Is Empty by the 20th (Pay Yourself First)** (58 chars)
   ← **recommended.** The hook verbatim — a felt problem, not a keyword —
   with the rule name as the parenthetical concept-bonus. Pairs best with
   thumbnail v1 (title gives the problem, thumb gives the $4,800 payoff);
   with v2 it repeats the same beat (fine, but redundant).
2. The Morning-After-Payday Transfer: $400/Month → $4,800/Year (59) — the
   payday lane without Nick's phrasing, plus the US winning formula (specific $
   number). Best pair with v2 or v3.
3. How Much Should You Save Per Paycheck? Start at 10% — Automatically (67) —
   leads with the verified `how much should i save per paycheck` autocomplete
   string. Highest floor, lowest ceiling.
4. Pay Yourself First: How to Save $4,800 a Year Without Willpower (63) —
   rule-name lead for concept search; demand unverified (see caveat), use only
   if the creator wants the rule name discoverable.

### vidIQ round (creator-supplied score, 2026-07-28)

Option 1 scored **56/100** — vidIQ's title model is keyword-weighted and the
hook contains no searched phrase. Its 81–84 suggestions are pattern templates;
two are honest restatements of this video's thesis and were adopted below, three
were rejected ("$5 Trick" misdescribes the content, "Build Emergency Funds
While You Sleep" cannibalizes our emergency-fund upload, "5% vs Everything
Else" promises a comparison we didn't make).

5. **Stop Trying to Save What's Left | Start Saving First** (52) — vidIQ 81,
   verbatim our s3 thesis. ← **new search-side recommendation.**
6. Why Your Willpower Fails at Saving (The Real Reason) (52) — vidIQ 81,
   matches s5; curiosity pattern without fabricating anything.
7. Stop Saving What's Left — Pay Yourself First ($400 → $4,800) (59) — hybrid:
   contrast pattern + rule keyword + the US number formula.

8. The $5 Trick That Saves You Thousands Without Thinking (54) — vidIQ 83,
   **creator pick 2026-07-28.** Honest ONLY with the bridge: "$5" = $5 of
   every $100 = the script's 5% ladder ($200/mo → $2,400/yr — "thousands" ✓).
   Pair with **thumbnail-en-v4.png** (built for it: "THE $5 TRICK = $2,400/YR ·
   $5 of every $100, moved automatically"). If this title is used, keep the
   description's 5% sentence prominent so the promise is cashed early; the
   hook VO ("empty by the 20th") still works as the cold open.

**Recommended play: use vidIQ's A/B Testing on option 1 vs option 5** — that
tests browse-hook vs search-pattern with real CTR instead of a model score.
The browse-not-search finding (needs-vs-wants) argues for 1; the score argues
for 5; only the test settles it. Thumbnail pairing: v1 (the $400→$4,800 math
poster) pairs with 5/6/7 — title carries the method, thumb carries the payoff,
no repeated words. Avoid pairing 7 with v1 (repeats the numbers).

## Description

```
Pay yourself first — the automatic savings method that fixes why your account is always empty by the 20th. You're not reckless: you save whatever's left, and there's never anything left. Nearly 1 in 4 American households ends the month with nothing.

The fix is a 100-year-old rule from The Richest Man in Babylon (1926): pay yourself first. Flip the formula — income − savings = expenses — and make it automatic: a transfer that moves a fixed amount into a high-yield savings account (different bank, FDIC insured) the morning after every payday. Money you never see, you never spend.

The math: on a $4,000 take-home, 10% is $400 a payday — $4,800 in a year. And $400 is the exact emergency about 4 in 10 American adults can't cover in cash. Same number, two different lives. Can't do 10%? Start at 5% — $200 a month is $2,400 a year. Right now, you're saving zero.

⏱ CHAPTERS
0:00 Why your account is empty by the 20th
0:20 What you'll know by the end
0:31 Flip the formula — income − savings = expenses
0:51 Pay Yourself First — the 100-year-old rule
1:04 Why willpower loses ($1.00 earned → 3¢ saved)
1:27 The day-after-payday auto-transfer
1:48 The math — $400 → $4,800
2:18 Do this today — even 5% works
2:37 Recap

📊 SOURCES
• Nearly 1 in 4 US households report nothing left at month-end — Bank of America Institute, Nov 2025
• Median usual weekly earnings, full-time workers: $1,251 — U.S. Bureau of Labor Statistics, Q2 2026
• Personal saving rate 3.0% (May 2026) — U.S. Bureau of Economic Analysis
• About 4 in 10 adults could not cover a $400 emergency expense with cash or its equivalent — Federal Reserve, SHED 2025
• "Pay yourself first" / "A part of all you earn is yours to keep" — George S. Clason, The Richest Man in Babylon (1926)

⚠️ This video is general financial education, not financial advice. No bank, app or fund is recommended — high-yield savings and FDIC are named generically. $400/month is an example on a $4,000 take-home — pick your own number for your own paycheck.

#PayYourselfFirst #PaydayRoutine #PersonalFinance
```

Chapter times are the render's truth: `scene_start` per line in
`studio/videos/pay-yourself-first-en/assets/voice/timing.json` (master runtime
+0.041 s vs timing.json; VO drift 0.021 s — fin-render QA PASS).

## Tags (paste as a comma list)

```
how much should i save per paycheck, how to split your paycheck, how to split your paycheck for savings, high yield savings account, high yield savings account explained, save 1000 dollars, budgeting for beginners, budgeting for beginners 2026, how to budget your money, how to budget and save in your 20s, how to save money fast, personal finance for beginners, pay yourself first, pay yourself first budgeting, payday routine, automate your savings, emergency fund, stop saving whats left, start saving first, automatic savings transfer, why saving money is so hard, pay yourself first method
```

The first 12 are autocomplete-verified 2026-07-27 (see caveat above). The last
5 (`pay yourself first`, `pay yourself first budgeting`, `payday routine`,
`automate your savings`, `emergency fund`) are topical/descriptive — no fresh
US autocomplete evidence this run. Hindi/Hinglish strings deliberately absent —
they belong to the ₹ cut (standing rule from the emergency-fund pack).

## Gate 2 compliance

- **Altered-content disclosure toggle: set "No".** Narration is synthetic
  (ElevenLabs "Brian") but no realistic synthetic media is presented as real —
  motion graphics + licensed stock photos only, so YouTube's altered-content
  disclosure is **not triggered** and no on-screen disclosure is required or
  present. The narrator is a voice, not a persona: no name, no credentials, no
  advisor framing (persona rules enforced at script/audit — the 2026
  AI-expert-persona carve-out hits finance hardest in the US,
  [[../../knowledge/niches/us-market-2026]]). Description carries the
  education-not-advice disclaimer.
- **Channel-level sameness — FLAG, one away from the line.** Uploads on
  @moneymavens101: 50-30-20 (9 scenes, 3:43) → emergency-fund (9 scenes, 2:46)
  → needs-vs-wants (9 scenes, 2:50) → **this (9 scenes, 2:58) is the 4th
  consecutive near-identical structure** (blockframe-9: hook → roadmap →
  concept → rule → audit → action → math-counter → do-today → recap). Fine to
  publish, but the **next upload would be the 5th** — vary the architecture
  (medium-tier per-line-chapters, or reorder/merge beats) or this becomes the
  one enforcement category that is judged channel-level (mass-produced
  sameness). Same flag, same count, on the hi channel.
- **Category:** Education. **Language:** English (US). **Audience:** not made
  for kids.
- **End screen / pinned comment:** cross-link the ₹/Hindi cut
  ([[youtube-metadata-hi]]), and vice versa.
- **Pinned comment suggestion:** "Scheduled your transfer for the day after
  payday? Reply with just your % — even 5 counts." (one-number replies are the
  lowest-friction comments there are — same pattern as the prior packs.)

## If this underperforms

The payday lane has real demand but a crowded clone-field around one phrasing.
Levers in order: swap to title #2 (the $-number formula), then re-test the
thumbnail (v1 ↔ v2 is a genuine composition A/B, not a variant tweak).

Related: [[script-en]] · [[storyboard-en]] · [[audit-en]] · [[youtube-metadata-hi]] · [[../../knowledge/design-finance-blockframe]] · [[../../knowledge/us-english-script-style]]
