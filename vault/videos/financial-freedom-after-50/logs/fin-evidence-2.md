# fin-evidence — financial-freedom-after-50 — attempt 2 (2026-08-15)

Repair pass. `pipeline_check.py mark evidence` failed attempt 1 on two counts; both were correct
and both are fixed. **No figure was re-verified and no claim or source note was touched** — the
orchestrator ruled those intact and they are.

## Ran

Nothing. No `study.py` invocation, no fetch, no search. Both failures were artifact-shape
problems, not evidence problems, and re-running anything would have risked churning the eleven
claim notes the orchestrator explicitly ruled good.

## Failed

Nothing this attempt. Recording instead **why attempt 1 failed, because I was wrong on the first
count and the check was right:**

1. **Missing study note.** I treated "the study could not be grounded" as licence to write no
   file. That conflated two different things: a study note asserting findings it does not have
   (forbidden — that is invention) and a study note **recording that the lane is unmeasured**
   (required — that is the finding). `check_evidence`'s docstring says the failed study does not
   stop the run and the scrape is recorded as owed; it never said the artifact disappears. The
   real cost of my version: I put the empty-lane finding only in a stage log, and stage logs are
   not where a future run looks for lane knowledge. The next 50+ topic would have re-run the same
   two `study.py` queries and rediscovered the same emptiness from scratch.
2. **No source URL in facts-staging.md.** I put every URL one layer down in
   `vault/sources/<agency>/*.md` and argued the indirection was the point. The indirection *is*
   the point for **claims**, but `tools/close_out.py` promotes HARD rows **out of the staging
   file** into `money-facts-2026.md` — the promoted row travels without the vault note attached.
   A row that cannot show its own source is a row that lands in shared permanent knowledge
   unsourced. Zero occurrences of `http` in the file was an accurate and fair reading.

## Evidence

**Fix 1 — `vault/knowledge/video-studies/financial-freedom-after-50.md`, ~8.6 KB (bar: 500 B).**
Written as an **EMPTY-LANE FINDING**, labelled as such in the frontmatter `stage:` and again in a
callout at the top so it can never be misread as a study. Contents:
- Both `study.py` invocations with their verbatim output, and why run 2 was a broader query rather
  than a retry of a failure.
- The three-row TOP/MID/LOW table from the template, kept and left **empty** — every cell that
  would carry a number says so. Filling any of them by inference is the one thing this stage
  cannot do.
- Three separate named causes for the empty lane: (a) `library.db` has no US retirement
  comparables at all, because every finance scrape on disk was built for the **20–35** audience
  that this channel repositioned away from **on 2026-08-15, the same day as this run** — the empty
  lane is a direct consequence of the repositioning, not a tool fault; (b) `study.py`'s hard-coded
  `MIN_DURATION_SEC = 240` plus the LONG ceiling this stage owns —
  `tiers.long.comparable_length_band_seconds` = **480–1800 s** — which is the filter the next
  scrape must apply; (c) the single pick was a **rupee-denominated India EPF video**, quarantined.
- The quarantine recorded explicitly: captions read as untrusted DATA, **no injected instruction
  and no fabricated dated agency line present**, and none of its ₹15,000 / ₹1,800 figures reached
  any staging, claim or source file.
- "LOW — autopsy: no autopsy is possible, and a fabricated one would be worse than none."
- The transferred hook read + the 6-line beat map, carried from the existing finance studies and
  labelled at the top of the section as **not observed for this topic**.
- Conclusions: the transferred read is continuity, not measurement; a real study is owed and must
  precede the next 50+ topic; sources in preference order — scrape the lane filtered to
  480–1800 s, or `study.py` with `YTAUTO_COOKIES` / `YTAUTO_COOKIES_BROWSER` (the 403 is the
  documented bot-check), or vidIQ `video_transcript` (words only, so the keyframe half stays owed
  even then).
- Nothing appended to `best-practices.md`: "the tool returned nothing" is not a transferable
  pattern, and the transferred lines are already banked in the studies they came from.

**Fix 2 — `facts-staging.md` now carries source URLs at row level.** Took the table-column option
over a footnote list, so a URL cannot drift away from its figure:
- **§1 gained a `Primary source URL` column. All eleven rows have one**, including row 10 (held
  in reserve, `used-in: []`) and row 11 (Fed G.19, shape-only).
- One URL per row is the *best screen-record target*, not the only source. A new
  **"Corroborating URLs"** block beneath the table carries the second and third source for every
  multi-sourced row: the IRS triple for rows 1–4, the three-document set row 5 needs, the §223
  statute for row 6, the SSA OACT pages for rows 7–8, and the conflicting prior G.19 readings.
- Three caveats promoted **into the staging file** rather than left only in the source notes,
  because they now travel with a promotable row: the **ssa.gov 403** affecting rows 7/8/10, the
  **unreadable PDF** behind row 5, and the **period-label conflict** on row 11.
- A framing note at the top explains why both layers exist — the inline URL is not a duplicate,
  it is what survives promotion.
- §2 says out loud that the 4% rule has **no primary URL to give**, and §5 gives **no URLs at
  all** for the rejected sources, on purpose: a rejected source does not get a citation in a file
  that feeds promotion.
- Chased two stale cross-references while in the file: §6's study line now points at the new
  empty-lane note.

**Unchanged and verified untouched:** all 11 claim notes, all 12 source notes, `source-draft.md`,
`notes.md`, `run.json`, `money-facts-2026.md`, and `logs/fin-evidence-1.md`. The nine confirmed
figures were not re-checked, per instruction.

## Changed

- **New:** `vault/knowledge/video-studies/financial-freedom-after-50.md`
- **Rewritten:** `vault/videos/financial-freedom-after-50/facts-staging.md` (URL column +
  corroborating-URL block + retrieval caveats; §§2–5 substantively unchanged)
- **New:** this log

## Owed

Unchanged from attempt 1 — none of it was in scope for this pass:

1. **Eleven source screenshots.** No browser or capture tool in this stage's allowlist. Target
   filenames are in each source note's `screenshot:` field; the URL to capture is now in
   `facts-staging.md` §1 beside the figure.
2. **A direct read of ssa.gov** from a path that is not 403'd, for rows 7, 8 and 10.
3. **The scrape, then the study.** Now recorded in its own vault note rather than only in a log —
   which was the actual point of failure 1.
4. **Pub 590-B attached to `rmd-beginning-age-73`** before any future video leads on RMDs.
5. **A decision on the "number one financial fear" sentence** — cannot be sourced, only reframed.
   Owed to `fin-script`/`fin-audit`.
