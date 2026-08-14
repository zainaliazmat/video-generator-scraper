---
summary: The 30-video launch slate for Money Mavens (50+ US retirement money) — 12 search-intent, 12 browse-intent, 6 experimental, with real vidIQ title scores where they exist. Publishing order alternates search/browse. **Only the first 10 are committed** (creator, 2026-08-15) — build those, read the response, then decide whether to continue or change.
updated: 2026-08-15
source: creator plan `01-30-video-launch-slate.md` (2026-08-15), built from live vidIQ title scoring + US outlier teardowns. Title scores marked in bold are real tool returns from that session, never rounded.
stage: ADOPTED — the topic queue; first 10 committed, 11-30 provisional
---

# Money Mavens — 30-video launch slate

**Channel** `UChNmDWhioyD5S_08AI6cSaA` (@moneymavens101) · **Audience** Americans 50+
**Format** 8–12 min long-form, faceless, AI voiceover · **Cadence** 3/week (Mon/Wed/Fri)

> **Scope decision (creator, 2026-08-15): build the first 10 only.** Ship them, read the
> response against the day-14 / day-30 gates in [[../../workflows/moneymavens-90-day-plan]],
> then decide whether to continue the slate as written or change it. Videos 11–30 stay
> here as a queue, not a commitment.

## The title-score gate

**Discard anything below 75. Report the real number. Never round up.**

A **bold number** is a real return from `vidiq_score_title` / `vidiq_generate_titles`.
**UNSCORED** means the working title has not been through the scorer — score it at
production time, with the finished script summary as the `description`, because titles
score better when the tool can see what the video actually contains.

Scoring evidence from the build session — nine clusters generated against real US
outlier titles as competitive seed:

| Cluster | Top | 2nd | 3rd |
|---|---|---|---|
| Medicare late enrollment | **95** | 86 | 85 |
| Old credit cards after 60 | **92** | 85 | 83 |
| RMDs | **92** | 86 | 83 |
| Scam red flag | **91** | 85 | 81 |
| Survivor benefits | **90** | 85 | 78 |
| POD / probate form | **87** | 83 | 81 |
| SS claiming age | **86** | 81 | 77 |
| FDIC coverage | **85** | 85 | 83 |
| SS taxation | 81 | 81 | 69 |

**On the SS-taxation cluster:** all eight generated options promised outcomes the video
cannot deliver ("keep your benefits", "stop losing money", "minimize taxes") and were
rejected on the no-overpromise rule. Two honest replacements were written by hand and
scored **83** and 78; the 83 is used. This is the rule working — a high score on a
promise the script cannot keep fails gate 8 of [[../fact-integrity]] §8.

## THE COMMITTED TEN — publishing order

Alternation is deliberate: **search builds the durable floor, browse supplies the spikes
that feed it.** Never two browse videos back to back in the first month.

| # | ID | Slug | Title | Score | Intent | Len |
|---|---|---|---|---|---|---|
| 1 | S1 | [[../../videos/medicare-enrollment-windows/index]] | Medicare Enrollment Windows: Don't Get Hit With This Permanent Fee | **95** | search | 9 |
| 2 | B3 | [[../../videos/keep-old-credit-cards/index]] | Retirement Finance: The Real Reason You Need to Keep Old Credit Cards | **92** | browse | 9 |
| 3 | B1 | [[../../videos/bank-account-probate-form/index]] | Is Your Bank Account Protected from Probate? Use This 1 Form | **87** | browse | 9 |
| 4 | S2 | [[../../videos/required-minimum-distributions/index]] | Required Minimum Distributions: Don't Make This Costly Mistake | **92** | search | 10 |
| 5 | B2 | [[../../videos/scam-red-flag/index]] | The 1 Red Flag That Proves It's a Scam (Seniors Beware) | **91** | browse | 10 |
| 6 | S6 | [[../../videos/social-security-survivor-benefits/index]] | Lost a Spouse? Don't Miss These Social Security Survivor Payments | **90** | search | 10 |
| 7 | S3 | [[../../videos/social-security-claiming-age/index]] | Claiming Social Security at 62 vs 67 vs 70: What's the Best Strategy? | **86** | search | 10 |
| 8 | S4 | [[../../videos/fdic-deposit-insurance/index]] | Your Bank Balance Might Not Be Fully Insured: Here's Why | **85** | search | 9 |
| 9 | B4 | [[../../videos/fdic-joint-and-trust-coverage/index]] | Joint Accounts and Trust Funds: Does Your FDIC Coverage Double? | **77** | browse | 9 |
| 10 | S5 | [[../../videos/social-security-tax-threshold/index]] | The Social Security Tax Threshold That Has Never Been Adjusted for Inflation | **83** | search | 10 |

⚠️ **B4 scored 77** — it clears the 75 floor by two points and is the weakest committed
title. Re-run `vidiq_generate_titles` against the finished script before producing it;
if nothing beats 77, ship it, but it is the first candidate to drop if the ten become nine.

### Why these five open the channel

1. **S1 first (95)** — the highest real score in the slate, on the largest keyword
   (`medicare`, 65.1K US). Lead with the strongest scored asset, not the favourite topic.
2. **B3 second (92)** — the only opener connecting to the existing library.
   `yoN-gAATN6Y` already covers FICO weights and FCRA §1681c(a); B3 is the 50+ version of
   ground already sourced. Fastest possible turnaround for video two.
3. **B1 third (87)** — pure browse-intent, modelled on the highest-view outlier found
   (467,547 views from a 19.7K-sub channel). Video 3 tests whether outlier packaging works.
4. **S2 fourth (92)** — back to search. Alternating in the first six tells YouTube two
   things about the channel at once instead of one thing twice.
5. **B2 fifth (91)** — the broadest topic in the set. Scams reach past the retirement
   audience to anyone with an older parent — the first realistic shot at traffic beyond
   the core demographic.

## The remaining twenty (queued, not committed)

**Search:** S7 IRMAA · S8 Original Medicare vs Advantage · S9 Spousal benefits ·
S10 Earnings test · S11 Extra standard deduction over 65 · S12 Qualified charitable distribution
**Browse:** B5 Adding an adult child to your account · B6 Your will does not control these
accounts · B7 When one owner of a joint account dies · B8 3 things Medicare does not cover ·
B9 The finance office after the car price · B10 Minimum payments on a fixed income ·
B11 State unclaimed property · B12 Part D penalty
**Experimental (one variable each, never two):** E1 read the IRS table line by line ·
E2 the Fed's own survey on retirees · E3 three claims that fall apart at the source ·
E4 beneficiary form walkthrough · E5 3-minute cut of the best of #1–15 (tests runtime) ·
E6 answering questions from the last 10 (needs comments to exist first)

Full working titles, hooks, thumbnail concepts and required sources for all thirty are in
the creator plan `01-30-video-launch-slate.md`. They are copied into a video note when a
video is committed, not before — an uncommitted row is a candidate, not a spec.

## Thumbnail direction

From `vidiq_similar_thumbnails` (US, 3-month window), the pattern across the 50K–500K
view cluster of small US senior-finance channels:

- **A single concrete object** as the subject — a form, a card, a bank window, a table.
  **Not a person, not a chart.**
- **One red element only.** Circle, arrow, or line. Never two.
- **Two to four words** of on-image text maximum, and **never a repeat of the title**.
- High contrast, cool background, warm subject.
- No emoji, no brackets. ALL-CAPS does work in this niche (`Rd07Bc_Q0LM`, 257,650 views,
  breakout 221.66, uses "ILLEGAL") but **one word per thumbnail at most**, or none.

This is compatible with the standing thumbnail rules ([[../design-thumbnail-ai-enhance]])
and tighter: the object-only rule replaces "one hero group", and "one red element" is
stricter than the palette allows in general.

⚠️ **Thumbnail generation has not been run and needs approval.** First five properly:
5 × `vidiq_generate_thumbnail` @22 + 5 × `vidiq_score_thumbnail` @5 + refinement passes
@22 ⇒ budget **~180–250 credits**.

Related: [[../us-english-script-style]] (how to write them) · [[../fact-integrity]] (the
evidence bar) · [[../../workflows/moneymavens-90-day-plan]] (the gates that judge them).
