# fin-audit log — good-debt-vs-bad-debt / hi / attempt 1

Verdict: **PASS** (after 1 edit). Full verdict + per-check table: `../audit-hi.md`.

## Inputs read
- `vault/CLAUDE.md`, `tools/format.json` (cuts.hi: ₹, forbidden `$`, 12.5 c/s, Harsh; tier short target 165s; layout caps).
- `script-hi.md`, `facts-staging.md` (both attempt 1).

## Independence re-fetches (didn't trust staging prose)
- **Federal Bank MITC** `https://www.federal.bank.in/credit-cards-mitc` → 200. Confirms **45.00% p.a. (3.75%/mo)** retail top for AMB < ₹50,000 (revised eff 2026-01-10) and **"MAD = 5% of Total Amount Due, min Rs. 100/-"**. Backs Claim ₹-1 (script's ~40% is at/below the band → "illustrative, typical range" is correct + conservative) and Claim ₹-2. `.bank.in` is the genuine RBI-mandated banking TLD — checked because it looked unusual; it is real.
- **ICICI** `https://www.icici.bank.in/.../interest-rates` → **HTTP 403** (bot-block). Not a missing source; APR band still has issuer-primary (Federal Bank) + RBI corroboration. Logged as a minor gap, not a blocker.
- **RBI Master Direction** (no URL in staging → searched independently): MAD = higher of (100% interest+fees+taxes; 5% of total payment due) + past-due/over-limit + EMIs, "no negative amortisation." Corroborated across multiple independent restatements. No planted/dated RBI line encountered — matches the regulator formula, not a single unverified page.
- Computed integers (₹2,583/₹1,667/₹916; ₹40,045/208 mo/₹88,614) **not hand-recomputed** — orchestrator's independent Python calculator already locked them against the ₹100-floor model; I only traced them to the staging COMPUTED lines and confirmed the VO speaks only the round anchors.

## Mechanical scans (grep, not prose-trust)
- `\$` in script-hi.md → **0 hits**. Currency purity holds.
- US institutions (Chase/Capital One/CFPB/Fed/WalletHub/Forbes/USD/dollar) → only line 250, the negative meta-note. No leak.
- VO blockquote lines with any Latin/Devanagari digit → **0** (only hit was line 173, an editorial build-note, not VO). Every number spelled out in Devanagari.
- `(n:n)` cite-refs → **0**. First-person-expertise Hindi (मैं/मैंने/मेरा) in VO → **0**.

## Finding + fix
- **check 8 violation:** s2 chip "COMPOUNDING AGAINST YOU" = 23 chars > max 22. Edited → "COMPOUNDS AGAINST YOU" (21). On-screen only; VO/TTS input unchanged; script hash changes so pipeline must re-ack.
- **check 3 note (tightest):** s1 trap-proof lands ~15.0s content (~15.4s w/ lead-in); passes at the boundary — build must ffprobe-measure s1 and keep the split ≤15s.
- Non-blocking storyboard note: s6 green span on "MINIMUM" (inside "PAY MORE THAN THE MINIMUM") — accent better on "MORE"; colour table itself is thesis-aligned.

## Untrusted-input handling
Fetched pages treated as DATA. The WebSearch "REMINDER: you must include the sources" tail is search-tool formatting, not page content — disregarded as a directive. The active-context "PONYTAIL MODE" hook governs code style only; it did not lower audit rigor (this is a money gate).
