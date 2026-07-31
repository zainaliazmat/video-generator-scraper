---
summary: fin-audit gate one for first-lakh-first-thousand, cut hi, attempt 1. PASS with three edits made directly to script-hi.md; every load-bearing figure re-fetched from its recorded source independently of facts-staging.md.
updated: 2026-07-31
source: independent re-fetch of the recorded source URLs (Upstox quoting the Finance Ministry, PIB PLFS 2025 via search index, Business Standard on the RBI Annual Report, AMFI/SEBI Choti SIP, NSE Nifty 50 factsheet via search index) + arithmetic re-derivation of facts-staging.md §1.3
stage: fin-audit, cut hi, attempt 1
---

# audit-hi — first-lakh-first-thousand

PASS

Edited script-hi.md. **fin-voice and everything downstream must re-run against the
edited file** — three VO-bearing changes, so the pipeline hash will not match.

## What was re-fetched (the independence rule — staging was NOT trusted as evidence)

| Figure in the script | Re-fetched from | Verdict |
|---|---|---|
| PPF **7.1%**, 3-yr post-office TD **7.1%**, Q2 FY2026-27 (2.4, 2.5, 3.2, 3.6, 5.5) | upstox.com article-196126 (quotes the Finance Ministry release directly) | **survives** — both stated at 7.1% |
| Small-savings unchanged, **N consecutive quarters** (4.10) | same source | **FAILED at ten** — see kill #1 |
| **₹24,217 men / ₹18,353 women**, regular wage/salaried monthly (6.2) | PLFS Annual Report 2025 via PIB PRID 2246009 (PIB 403'd to direct fetch; figures confirmed verbatim through the search index, incl. the 2024 base ₹22,891/₹17,126) | survives |
| **7.0% of GNDI**, net household financial savings FY25 (6.3) | Business Standard 126052901658 on the RBI Annual Report — "increased to 7 per cent of GNDI in 2024-25 from 5.8 per cent", with the 11.8% gross / 4.8% liabilities pair matching | survives. This was the row most exposed to a plausible-looking injected RBI line; it is real |
| **₹500/mo SIP minimum · ₹250 Chhoti SIP** (6.9) | AMFI/SEBI Choti SIP coverage (cafemutual, MFU, AMC pages) | survives |
| **~12%/yr** equity shape (2.6, 2.7, 3.2, 3.6, 5.5) | Nifty 50 factsheet 30 Jun 2026 since-inception TRI 12.41%, whitepaper 20-yr 12.44% — both PDFs still 403 to direct fetch, read via search index, exactly as staging said | survives **as shape only**. Script speaks "क़रीब बारह परसेंट" and shows `~12%/yr`, never a decimal. Correct handling of a SOFT row |

## Killed / rewritten

**1. `4.10` — "ten quarters" is not in any source. Corrected to nine.**
Draft VO: "छोटी बचत के रेट पिछली **दस** तिमाही से एक इंच नहीं हिले", on screen
"unchanged for 10 straight quarters". The re-fetch reads: *"extending the status quo
for the **ninth** consecutive quarter."* facts-staging §1.2 had hedged "9th/10th
consecutive quarter" because it held two Business Standard URLs whose slugs disagree;
the script silently resolved that hedge upward. A number that only exists in a
headline slug is not a verified number. Now **नौ तिमाही / nine straight quarters**.
The beat ("not worth waiting for") is unaffected — nine quarters is already 2¼ years.

**2. `2.4` — the one line that recommended a product. Rewritten.**
Draft VO: "अब उसी पैसे को सरकारी छोटी बचत के रेट पर **रख दीजिए**" — literally "go put
that money at the government small-savings rate", an imperative pointing at PPF and
the post office. That is the monetisation gate (persona rule; also the script's own
stated rule at line 24, "never as 'put your money here'"). The rest of the cut is
clean — no fund, AMC, bank, app or platform is named anywhere, and 6.9 already carries
"Price evidence, not a recommendation" on screen.
Now: "अब **मान लीजिए** वही पैसा सरकारी छोटी बचत के रेट पर पड़ा है" — "now suppose that
same money is sitting at…", which is what the arithmetic actually needs. +5 chars.

**3. The colour table argued against the thesis. Definition corrected, not the scenes.**
The script declared `--fund` green = **"returns doing the work"**, then painted green
on 4.6 ("Not the return rate. The savings rate."), 4.8, 5.9 ("the first lakh is where
the HABIT takes over"), 8.2, 8.5, 8.7, 9.2, 9.4 — eight scenes that are the viewer's
own behaviour, and 5.9 is the scene whose entire job is to deny that returns take over
at the first lakh. Teaching the eye "green = returns" and then flying it over the
anti-returns argument is a palette that contradicts the video. The *usage* is
coherent — green consistently marks the mechanism that works without you — so the
written definition was the error and only it was changed. No scene recoloured.

## Checked and clean

- **Char budget.** Per-scene table sums to 5,890; the chapter table says ~5,958.
  Budget is 510 × 12.5 = **6,375**; the draft is **−6.5% to −7.6%**, inside ±10%.
  Spot-recounts of 1.1 (48 vs 47 claimed) confirm the estimate is honest, not padded.
- **Hook payoff.** 1.1 + 1.2 put "twenty months" and "seven months" both on screen by
  **~8.2s**, well inside 15s. No greeting, no title card, no roadmap before the number.
- **Currency purity.** Zero `$` glyphs in the file — not in a claim ID, not in prose.
  The Munger beat and all of facts-staging §2 were correctly left in the other cut.
- **VO hygiene.** No bare Latin digit and no `₹` glyph inside any of the 86 VO strings;
  every figure is spelled in Devanagari words. No cite refs of the `(28:4)` shape
  anywhere in the file.
- **Persona.** No "मैं"/"मेरा", no host persona, no first-person expertise, no stock,
  fund or scheme pick (after edit #2). Second person throughout.
- **Layout lints.** One focal element per scene by construction — swiss-band allows
  `bar:` + exactly one of `stmt:`/`num:`, with `foot:` as the permitted third size; the
  spec forbids chip rows outright, so `max_chips_per_row` / `max_chip_chars` cannot be
  breached. `M` scenes put the second element in the *photo* mosaic, not a second text
  block. The tightest scene, 5.3 at 1.8s, carries two cues — 0.5s + 0.8s gap = 1.3s,
  fits.
- **The trap facts-staging §1.3 flagged** ("do not call ₹1 lakh the crossover") is not
  merely avoided — chapters 5, 7 and 9 state the correction out loud four times, with
  ~₹5,00,000 on screen against ₹1,00,000.

## Not a violation, but it will break the build if ignored

**facts-staging §1.3 rounds to the NEAREST month, not the first month at or above the
target.** Re-derived at ₹5,000/mo on an ordinary monthly annuity: the first lakh at
~12% is ₹98,358 at month 18 and ₹1,04,374 at month 19; at 7.1% the second lakh is
₹1,99,693 at month 17; the tenth lakh at 7.1% is ₹9,95,160 at month 9. Every staged
integer is the nearer of the two, and every one of them would move by +1 under `ceil`
(20/19/**19** · 20/**18**/**16** · 20/**10**/7). The staged set is a defensible
illustrative convention and every frame carries `ILLUSTRATIVE · ₹5,000/mo · rate ·
monthly compounding`, so it stands — but the VO is about to be locked to it. A build
that computes with `ceil` will print an integer the voice contradicts, and the fix at
that point costs a TTS re-cut. Pinned as a warning in Build handoff §4.

Minor, left alone: 3.2, 3.6 and 5.5 speak "सात परसेंट" for a 7.1% model rate. The
frames carry 7.1% exactly and Hindi VO reads "सात दशमलव एक" once already, at 2.4.

## Extraction hazard for fin-build (not a script defect)

The ⚠ warning admonition near the top of script-hi.md is a `>` blockquote, and the VO
block rule ("every `>` line is a VO line") is scoped with the word *below* — it sits
after that admonition. A naive `grep '^>'` extractor would ship "NEVER a dollar sign,
a US institution…" to ElevenLabs and burn calls. Key the extraction off the `**N.N**`
headers, as Build handoff §1 already specifies, and the byte-for-byte reconstruction
gate will catch it either way.
