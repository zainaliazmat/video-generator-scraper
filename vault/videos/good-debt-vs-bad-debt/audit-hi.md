---
summary: fin-audit gate-one verdict for good-debt-vs-bad-debt hi cut, attempt 1. All 8 checks hold after 1 audit edit (s2 over-length chip). Every ₹ figure traced; the sourced APR/minimum/RBI figures were re-fetched and confirmed against Federal Bank MITC + the RBI Master Direction.
updated: 2026-07-28
source: fin-audit attempt 1 — independent re-fetch of Federal Bank MITC + RBI Credit-Card Master Direction
---

# Audit — good-debt-vs-bad-debt / hi / attempt 1

PASS

## Independence re-fetch (check 1) — every load-bearing number

| Number in script | Re-fetch / trace result |
|---|---|
| ~40% APR — "illustrative, typical retail range" (s7) | CONFIRMED, conservative. Federal Bank MITC (`federal.bank.in` — the real RBI-mandated `.bank.in` banking TLD, not a spoof) shows **45.00% p.a. (3.75%/mo)** for AMB < ₹50,000, 23.88% for higher tiers, revised eff 2026-01-10. 40% sits at/below the retail-band top → the "illustrative, typical range" label is correct. ICICI (`icici.bank.in`) returned **HTTP 403** (bot-block, not a missing figure); Federal Bank issuer-primary + the RBI direction cover the band. Traces to HARD Claim ₹-1. |
| 5% minimum + ₹100 floor, interest paid first (s5, s7) | CONFIRMED. Federal Bank MITC: "MAD = sum of **5% of Total Amount Due (subject to minimum of Rs. 100/-)** + EMIs + GST + Fee." Traces to HARD Claim ₹-2. |
| RBI: min must cover 100% of interest / no neg-amortization (s5 foot) | CONFIRMED. RBI Master Direction (Credit/Debit Card Issuance & Conduct, 2022, reaffirmed 2025): MAD = higher of (100% interest+fees+taxes; 5% of total payment due) + past-due/over-limit + EMIs, "so there is no negative amortisation." Corroborated across multiple independent restatements — **no planted/dated RBI line**; the figure matches the regulator formula, not one unverified page. |
| Month-1 split ₹2,583 / ₹1,667 / ₹916 (s1) | COMPUTED closed-form, floor-independent; traces to staging COMPUTED month-1 line; orchestrator's Python calculator locked. Not hand-re-derived (per orchestrator). VO speaks 2,583 & 1,667 (permitted anchors), rounds 916 → "नौ सौ" (~900). |
| ₹40,045 / 208 months / ₹88,614 (s7, on-screen only) | Build-calculator locked (₹100-floor model); trace to staging COMPUTED lines (range 200–210 mo / ₹85–90k). Not hand-recomputed (per orchestrator). Displayed, never spoken. |
| ₹50,000 balance; +₹1,000 action step | Hero example + run.json `action_step`; the +₹1,000 effect kept qualitative (no fabricated payoff). |

**Orchestrator's four hero-math asks:** (a) every ₹ figure traces to a HARD claim / COMPUTED line — YES. (b) VO speaks only floor-independent anchors/ranges (2,583 / 1,667 / ~900; ~₹40,000 after a year; 17+ years; ~₹90,000) and **never** a false-precise spoken integer — CONFIRMED. (c) "illustrative — typical range" framing on the ~40% APR present (s7 on-screen + VO "भारत में आम बात") — YES. (d) no $ figure / US institution in the hi cut — CONFIRMED by grep (zero `$`; only "dollar" hit is the negative meta-note on line 250).

## Other checks

2. **Char budget:** 165s × 12.5 c/s = 2,063 ±10% (1,856–2,269). Script table ~2,070 (100.3%); per-scene estimates match visible text length. Inside band. Build ffprobe-measures before lock (script mandates it).
3. **Hook payoff (TIGHTEST):** the trap-proof — interest-reveal ("1,667 is just interest") — completes ~15.0s content (≈15.4s with the 0.4s lead-in); the on-screen focal split (₹2,583/₹1,667/₹916 + "IT'S A TRAP") reveals earlier as the numbers are spoken. Lands at the boundary → PASS with a mandatory build advisory (see NEXT/edits): ffprobe-measure s1 and keep the interest/principal split ≤15s; if measured TTS runs slower than 12.5 c/s, trim s1.
4. **No product/platform recommended:** Federal Bank / ICICI / RBI appear only as MITC/source evidence in foots; UPI + phone-banking are generic b-roll. No card/fund/product picked. Pass.
5. **Currency purity:** zero `$` anywhere in script-hi.md. Pass.
6. **VO text:** zero Latin/Devanagari digits, zero `(n:n)` cite-refs — all figures spelled out in Devanagari. Pass.
7. **Persona:** no host, no first-person expertise (grep clean for मैं/मैंने/मेरा), no investment pick (compounding = concept/analogy; education/skill/business = good-debt categories). Subscribe is a channel CTA. Pass.
8. **Layout lints:** one focal per scene ✓; cascades ≤5 items (s1 split=3, s7 rows=3) ✓; chips ≤3/row ✓; colour table thesis-aligned (warn/red = interest trap + bad debt, fund/green = good debt + escape) ✓. **VIOLATION:** s2 chip "COMPOUNDING AGAINST YOU" = 23 chars > `max_chip_chars` 22 → fixed by edit. Non-blocking note: s6's green span sits on "MINIMUM" inside "PAY MORE THAN THE MINIMUM"; storyboard may prefer the accent on "MORE" (the escape). The colour table itself does not argue against the thesis, so this is advisory, not a violation.

## Edits made (script-hi.md — downstream must re-run against edited script)

1. **s2 chip:** `COMPOUNDING AGAINST YOU` (23 chars) → `COMPOUNDS AGAINST YOU` (21 chars). Why: exceeded `max_chip_chars` 22. **On-screen text only — the VO paragraphs are byte-identical**, so the TTS audio is unchanged; the script hash changes, so the pipeline gate must re-acknowledge and the storyboard/build must pick up the corrected chip.

Nothing killed — every number traced and survived the source re-fetch.
