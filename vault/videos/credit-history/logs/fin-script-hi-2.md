# fin-script log — credit-history, cut `hi`, attempt 2 (2026-07-29)

## Scope

Attempt 1 passed on content and failed one gate only:

```
FAIL script-hi
  ✗ currency purity: '$' appears in the -hi script
```

`check_script()` in `tools/pipeline_check.py` is a **whole-file substring scan**
(`if fmt["cuts"]["hi"]["forbidden_currency"] in text`). It has no notion of VO vs
prose vs code fence, so a claim ID that borrows the market glyph as a prefix trips
it exactly as a real price would. The VO and on-screen text were already ₹-pure at
attempt 1 — no spoken or on-screen currency changed in this attempt.

Attempt 2 is a **three-reference rename**. No VO rewrite, no re-timing, no
re-sourcing.

## What I read

1. `vault/CLAUDE.md` — two-home rule (already loaded).
2. `tools/format.json` — confirmed `cuts.hi.forbidden_currency` is the US symbol
   and `cuts.hi.chars_per_second` is still 12.5, i.e. the timing table below is
   unchanged and still correct.
3. `vault/videos/credit-history/script-hi.md` — full read before rewriting.
4. `vault/videos/credit-history/facts-staging.md` — confirmed the claim IDs there
   are `Claim <market>-n`; the US block is claims one to five, so the FICO-weights
   claim is unambiguously **the US-market claim 2**.

No re-read of the style/niche/design notes: nothing in this attempt touches VO,
structure, imagery or layout.

## The three edits

| Line (v1) | Was | Now |
|---|---|---|
| 154 | s4 deliberate-omission blockquote, `facts-staging Claim <glyph>-2` | `facts-staging **Claim US-2** — the US-market claim two` |
| 294 | "Deliberately NOT used" row, `FICO's weights (Claim <glyph>-2)` | `FICO's weights (**Claim US-2**, the US-market claim two in facts-staging)` |
| 308 | currency-purity row pasted the config value verbatim inside backticks | names the key without the glyph: "`format.json` pins `cuts.hi.forbidden_currency` to the US dollar symbol" |

Line 308's row also now records *why* the alias exists, so a future attempt does
not "helpfully" restore the literal claim ID and re-fail the same gate:

> the check is a whole-file scan — the glyph must not appear anywhere in this
> file, not even in a claim ID, which is why US-market claims are cited as
> `Claim US-n` here.

## Guard integrity (the thing that must not weaken)

Both exclusions stay explicit and grep-able. Post-edit grep of the script:

- **"7 years"** — line 24 (the ⚠ two-things block, "NEVER '7 years'… the US FCRA
  rule"), line 178 (s5's rule, "say 36 months / three years, never '7 years'"),
  line 292 ("Deliberately NOT used" → REJECTED per the RED FLAG section).
- **FICO weights** — line 27 (⚠ block, "NEVER a percentage weight"), line 154
  (s4 deliberate omission), line 295 ("Deliberately NOT used"), plus s4's on-screen
  foot: *"CIBIL names these factors — it publishes no percentage weights."*

Untouched, verbatim from attempt 1: all nine VO paragraphs, the 9-segment
blockframe, s5's 36-cell grid hero, s7's calculator-output handoff (#5), the RBI
₹100/day omission, the whole fact-trace table, and the build handoff.

## Numbers (unchanged from attempt 1)

- Segments: **9** (blockframe-9, short tier).
- VO chars: **~2,110** vs the 165 × 12.5 = **2,062** budget → **+2.3%**.
- Est. VO **~169s**; rendered **~181s** with 9 × 1.4s lead-in/tail — inside the
  short tier's 60–300s range.
- Trim lever if measured TTS runs long: **s7**, the rate-card mechanism sentence.

## Verification

`rg '\$' vault/videos/credit-history/script-hi.md` → **no matches**. The glyph
appears nowhere in the file: not in VO, on-screen text, prose, blockquotes, tables,
code fences or backticks.
