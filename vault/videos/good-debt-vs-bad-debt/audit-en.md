---
summary: fin-audit gate-one verdict for good-debt-vs-bad-debt en (US) cut, attempt 1. All 8 checks hold — no edits, nothing killed. Every $ figure traced; the ~22% APR and US "1% + interest / ~$35 floor" minimum were re-fetched and confirmed live against Fed G.19 + WalletHub + Chase + CFPB Reg Z.
updated: 2026-07-28
source: fin-audit attempt 1 — independent re-fetch of Fed G.19, WalletHub, Chase minimum-payment page, CFPB Reg Z Appx M2 (Capital One softened, Forbes 403 — both non-blocking)
---

# Audit — good-debt-vs-bad-debt / en / attempt 1

PASS

## Independence re-fetch (check 1) — every load-bearing number

| Number in script | Re-fetch / trace result |
|---|---|
| ~22% APR — "illustrative, typical range" (en5, en7) | CONFIRMED, live + current. **Fed G.19** (federalreserve.gov, primary) → 200: **22.15%** assessed-interest / 20.94% all-accounts, May 2026 data (released 2026-07-08). **WalletHub** → 200: **22.16%** new-offer / 20.94% existing (July 2026) — staging logged 22.21%, now 22.16%, a sub-0.1pp weekly drift the "~22% / typical range" anchor absorbs. **Forbes** → HTTP 403 (bot-block, not a missing figure), a 3rd corroborator only; the claim stands on Fed-primary + WalletHub. Traces to HARD Claim $-1. |
| Minimum = 1% of balance + interest (or ~$35 floor) (en1, en5, en7) | CONFIRMED. **Chase** (primary) → 200: "**$40 or 1% of your statement balance, plus any interest and late fees since the last billing cycle — whichever is greater**"; balance < $40 → full balance. **CFPB Reg Z Appx M2** (regulator) → 200: illustrative "**2% of the outstanding balance or $20, whichever is greater**". **Capital One** → 200 but the page has softened to a generic "percentage of the balance plus new interest charges and late fees" — the specific "$25 or 1%" staging recorded is no longer shown. NON-BLOCKING: the "1% + interest" mechanism is carried by Chase (exact primary) + CFPB; the on-screen **$35** is an explicit illustrative midpoint of the $25–$40 issuer band (Chase's $40 anchors the top), the VO never speaks a floor figure, and the "Chase / Capital One agreements" cite still holds because Capital One's live page still describes the %-of-balance + interest mechanism. Traces to HARD Claim $-2. |
| $6,000 balance (en1, en7) | fin-script illustrative pick inside staging's sourced "$5,000–$6,000 typical US card debt" band; labelled illustrative on screen, not presented as a sourced average. NOT a rupee conversion. |
| Month-1 split $170 / $110 / $60 (en1) | COMPUTED, floor-independent (1%·B=$60, i·B=$110, sum $170 at 22%); orchestrator's independent Python calculator locked it. Not hand-re-derived (per orchestrator). These are the permitted spoken anchors. |
| $5,318 after 1yr / 215 months / $9,496 interest (en7, on-screen ONLY) | Build-calculator locked ($35-floor model); traces to staging's THE TERMINATING MODEL + build-handoff #5. On-screen $9,496 sits inside the orchestrator's build-locked ~$9,496–$9,506 band (≈$10 spread = estimate rounding, not a defect). Displayed, never spoken. Not hand-recomputed (per orchestrator). |
| +$20 more than the minimum (en6 on-screen, en8 VO) | run.json `action_step` ("en: even $20 more"); en6 effect kept qualitative ("cuts years off") — no fabricated payoff figure. |

**Orchestrator's four hero-math asks:** (a) every $ figure traces to a HARD claim / COMPUTED line — YES. (b) VO speaks only floor-independent anchors/ranges ($170/$110/$60; "over five thousand" after a year; "the better part of two decades"; "more in interest than you borrowed" / "over nine thousand") and **never** a false-precise spoken integer ($5,318 / 215 / $9,496 are on-screen only) — CONFIRMED. (c) "illustrative — typical range" framing on the ~22% APR present — YES (en7 on-screen "~22% — illustrative, typical range" + VO "around twenty-two percent — typical if you carry a balance"). (d) no ₹, no India institution, no rupee-to-dollar conversion — CONFIRMED by grep (0 ₹ glyphs; "rupee"/"lakh" appear only in anti-leak guardrail prose, never in VO/on-screen; no RBI/ICICI/HDFC/Federal Bank).

## Other checks

2. **Char budget:** 165s × 15 c/s = 2,475 ±10% (2,228–2,723). Script table ~2,502 (101.1%); spot-counts (en1 289, en2 151) match the table. Inside band. Build ffprobe-measures each clip before lock (script mandates it).
3. **Hook payoff (TIGHTEST):** en1 thesis "It's a trap" lands ~6.7s (with the 0.4s lead-in) and the on-screen $170/$110/$60 focal split reveals from scene start — payoff well inside 15s. The VO's numeric interest-reveal clause ("$110 of that is pure interest") completes ~15.3s with lead-in, i.e. at the boundary. PASS, with a build advisory: ffprobe-measure en1 and keep the interest/principal reveal ≤15s; if measured TTS runs slower than 15 c/s, trim en1. (Same advisory the hi cut carried.)
4. **No product/platform recommended:** Chase / Capital One / CFPB / Fed / WalletHub appear only as rate/rule evidence in source foots; "your card's app" is generic; no card/fund/product picked. Pass.
5. **Currency purity:** **0** ₹ glyphs in script-en.md (grep). "rupee"/"lakh" occur only in the US-REWRITE guardrail + "deliberately NOT used" notes (production prose, never VO/on-screen) — the anti-leak mechanism, not a leak. No India institution named. 46 `$[digit]` hits, all expected en figures. Pass.
6. **VO text:** every number spelled out (en1 "a hundred seventy", en7 "around twenty-two percent" / "over nine thousand"); zero bare Latin digits and zero `(n:n)` cite-refs in any VO paragraph. Digits live only in on-screen text, as intended. Pass.
7. **Persona:** no host persona, no first-person expertise (VO is 2nd-person "you"; no "I/my/in my experience"), no investment pick (good-debt = education/skill/business categories, not a security/fund; "compounding" is a concept). Subscribe is the channel monetisation CTA (YouTube 2026 carve-out). Pass.
8. **Layout lints:** one focal per scene ✓; cascades ≤5 items (en1 split=3, en7 reveal=3, roadmap/recap chips 4) ✓; ≤3 chips/row (en2 & en9 2×2, en4 3/col) ✓; ≤22 chars/chip — longest is "GOOD GROWS, BAD DRAINS" = 22 (at cap, OK); en already ships "COMPOUNDS AGAINST YOU" (21), the exact fix the hi cut needed → no edit required ✓; every scene carries a keyword image (photo_free_scene_ratio 0) ✓; colour table thesis-aligned (warn/red = interest-trap + bad debt, fund/green = good debt + the escape, target/amber = the card, pop/orange = CTA) ✓. Non-blocking storyboard note: en6's green span sits on "MINIMUM" inside "PAY MORE THAN THE MINIMUM"; the accent may read better on "MORE" (the escape) — the colour table itself does not argue against the thesis, so advisory only. Column headers ("BAD DEBT — just spending", 24 chars) are headers, not chips — outside `max_chip_chars`, consistent with the hi audit.

## Edits made

**None.** Every number traced and survived the source re-fetch; all 8 checks hold as written. Because no byte of the script changed, the script hash is unchanged and downstream voice work does **not** need to re-run on account of this audit.

Nothing killed.
