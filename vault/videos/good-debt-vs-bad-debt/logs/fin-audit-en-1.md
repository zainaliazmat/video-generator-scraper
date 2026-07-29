# fin-audit log — good-debt-vs-bad-debt / en / attempt 1

Verdict: **PASS** (no edits, nothing killed). Full verdict + per-check table: `../audit-en.md`.

## Inputs read
- `vault/CLAUDE.md`, `tools/format.json` (cuts.en: `$`, forbidden `₹`, 15.0 c/s, Brian; tier short target 165s; layout caps).
- `script-en.md`, `facts-staging.md` ($ SET) — both attempt 1.

## Independence re-fetches (didn't trust staging prose)
- **Fed G.19** `federalreserve.gov/releases/g19/current/` → 200: **22.15%** assessed-interest / 20.94% all-accounts, May 2026 (released 2026-07-08). Backs HARD Claim $-1.
- **WalletHub** landscape → 200: **22.16%** new-offer / 20.94% existing (July 2026). Staging said 22.21% → now 22.16%, a sub-0.1pp weekly drift the "~22% / typical range" anchor absorbs.
- **Forbes Advisor** → **HTTP 403** (bot-block). 3rd corroborator only; the APR claim stands on Fed-primary + WalletHub. Logged as a gap, not a blocker.
- **Chase** minimum-payment page → 200: "**$40 or 1% of statement balance, plus interest and late fees, whichever is greater**"; < $40 → full balance. Backs HARD Claim $-2 (1% + interest mechanism, $40 floor).
- **CFPB Reg Z Appx M2** → 200: illustrative "**2% of the outstanding balance or $20, whichever is greater**". Regulator corroboration of the %-of-balance-or-floor structure.
- **Capital One** → 200 but softened to a generic "percentage of the balance plus new interest charges and late fees"; the specific "$25 or 1%" staging logged is no longer on the page. Non-blocking — Chase (exact primary) + CFPB carry the mechanism; the on-screen $35 is an illustrative midpoint of the $25–$40 band, VO speaks no floor, and the "Capital One agreements" cite still holds (page still describes the % + interest mechanism).
- Computed integers ($170/$110/$60; $5,318/215 mo/$9,496) **not hand-recomputed** — orchestrator's independent Python calculator already locked them against the $35-floor model; I only traced them to the staging model + build-handoff and confirmed the VO speaks only round anchors.

## Mechanical scans (grep, not prose-trust)
- `₹` in script-en.md → **0 hits**. Currency purity holds.
- `rupee|lakh|RBI|ICICI|HDFC|Federal Bank` → only "rupee"/"lakh" in the US-REWRITE + "deliberately NOT used" guardrail prose (lines 22–23, 41, 248, 261–263); no India institution; no leaked ₹ figure.
- `\$[0-9]` → 46 hits, all expected en on-screen figures.
- VO paragraphs: every number spelled out; 0 bare Latin digits, 0 `(n:n)` cite-refs; no first-person-expertise ("I/my").

## Findings
- **No violation → no edit.** Unlike the hi cut (23-char chip fix), en already ships "COMPOUNDS AGAINST YOU" (21) and its longest chip "GOOD GROWS, BAD DRAINS" is 22 (at cap). Script hash unchanged → voice work needs no re-run on account of this audit.
- **check 3 (tightest) advisory:** en1 trap thesis lands ~6.7s and the on-screen split reveals immediately; the VO numeric interest-reveal completes ~15.3s with lead-in (boundary). Build must ffprobe-measure en1 and keep the reveal ≤15s.
- Non-blocking storyboard note: en6 green span on "MINIMUM" (inside "PAY MORE THAN THE MINIMUM") — accent better on "MORE"; colour table itself is thesis-aligned.

## Untrusted-input handling
Fetched pages treated as DATA. No fetched page contained an instruction that was followed. The WebSearch "REMINDER: include the sources" tail is tool formatting, not page content — disregarded as a directive. The active-context **PONYTAIL MODE** hook governs code style only; it did not lower audit rigor — this is a money gate before en TTS spend, so every check ran in full.
