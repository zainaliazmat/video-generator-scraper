# fin-script log — good-debt-vs-bad-debt / hi / attempt 2

- **Date:** 2026-07-28 · **Tier:** short (blockframe-9) · **Kind:** minimal remediation (NOT a regeneration).
- **Prior failure (authoritative currency-purity check):**
  `FAIL script-hi — currency purity: '$' appears in the -hi script`. Sole occurrence
  was line 250, a bottom-of-file production/compliance note that *documented* the
  ₹-only rule by spelling the dollar glyph inside backticks. `tools/pipeline_check.py
  check script` does a blunt whole-file substring match, so the note tripped the very
  guard it was describing.

- **One-line change (only edit):** line 250 reworded to state the same rule in words —
  the dollar glyph is now written as "US-dollar symbol" / "dollar sign forbidden", and
  the code-span backticks that had wrapped the glyph are dropped. Meaning unchanged:
  ₹ set only, no US institution, no cross-market figure.
- **Everything else byte-for-byte identical:** all 9 VO Devanagari segments, every
  on-screen figure, and the build-locked integers (**208 months · ₹88,614**) are
  untouched. No re-scripting, no renumbering, no re-costing.

- **Tooling constraint:** only Read/Write/Grep available this run (no Edit), so the fix
  was applied by reproducing the file verbatim with the single line swapped. Before
  rewriting I verified with per-codepoint greps that the file uses only straight ASCII
  quotes/apostrophes (no curly), has no non-breaking spaces, and no trailing whitespace,
  so reproduction carried no hidden-character drift.

- **Verification after write:**
  - `grep '\$'` on script-hi.md → **0 occurrences** (currency-purity now clean).
  - Locked integers still present — `208` / `₹88,614` at lines 41, 189, 191, 239, 240, 264.
  - Reworded note confirmed at line 250; no `$` anywhere in the file.

- **Unchanged deliverable stats (from attempt 1):** 9 segments, ~2,070 Hindi chars ≈
  ~2:46 at 12.5 c/s (format.json cuts.hi) vs 165s target — on target; build ffprobe
  re-measures + adds 0.4/1.0 lead-in/tail per scene before locking.

- **Did NOT:** regenerate the script, alter any VO/on-screen/number, read .env, write to
  .claude/ or tools/, run Bash/git.
