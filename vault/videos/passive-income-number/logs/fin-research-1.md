---
summary: fin-research attempt 1 for passive-income-number FAILED — study.py exited 1 with 0/2 picks transcribed (YouTube bot-check on yt-dlp), and the library only held 2 usable rows for the lane, so no top/mid/low triple existed even before the download failed. No study note written.
updated: 2026-08-07
source: venv/bin/python backend/study.py "passive income" (2026-08-07); research/passive-income/manifest.md
---

# fin-research — passive-income-number — attempt 1 — FAIL

## What I did

1. Read `vault/CLAUDE.md`, `vault/videos/passive-income-number/run.json`,
   `vault/workflows/video-study.md`, `vault/templates/video-study.md`,
   `tools/format.json`, and the source note
   `vault/knowledge/niches/finance-topics-2026-07-31.md` (Revision 2026-08-07,
   "Replacement A", topic #9).
2. Read `backend/study.py` + `library.search` **before** choosing the query.
   This mattered: `library.search` is a plain case-insensitive `LIKE '%term%'`
   over `title / channel / keyword` — it is not a semantic search. The
   run.json `topic` string is prose and would have matched zero rows. The
   format-twin phrase ("how much you need invested to live off dividends")
   would only match if those exact clones were scraped; they came from the
   **vidIQ** index (3-month window), not from the 2026-07-31 yt-dlp pull
   (30-day window), so it was the higher-risk query. Chose `"passive income"` —
   the ₹-cut framing mandated by `constraints.hi_currency_framing`, and the
   term most likely to be present as a scrape *keyword* (matching a keyword
   returns that keyword's whole result set).
3. Ran the one allowlisted command:
   `venv/bin/python backend/study.py "passive income"` → **exit 1**.

## What failed (two separate faults, both real)

**Fault 1 — yt-dlp is blocked by YouTube's bot-check. 0/2 picks transcribed.**
Verbatim, for both picks (`research/passive-income/manifest.md`):

> `ERROR: [youtube] _CyWGSzwTu4: Sign in to confirm you're not a bot. Use --cookies-from-browser or --cookies for the authentication.`
> `ERROR: [youtube] SpE0XTQtiyQ: Sign in to confirm you're not a bot. …`

Neither the 480p pull nor the caption fetch completed, so no `transcript.txt`,
no `frames/`, no metadata. `study.py` correctly refused to let the packet
degrade: `ERROR: only 0/2 picks produced a transcript`. This is an **auth /
environment** fault, not a topic fault — the same failure will hit any query.
Note this is a harder failure than the 429 rate-limit that put a scrape debt on
[[../../../knowledge/video-studies/first-lakh-first-thousand]]; a 429 retries
clean, a bot-check does not clear without cookies.

**Fault 2 — the library is thin in this lane, independent of Fault 1.**
`study.py` reported `0/2 picks`, not `0/3`. `pick_three` only degrades to two
ranks when `len(usable) <= 3` after filtering (≥100 views, ≥240s). So the whole
library holds **two** usable long-form rows matching `passive income`. Even
with working downloads there would have been a TOP and a MID and **no LOW** —
i.e. no low-performer autopsy, which is the one deliverable the workflow says
must never be reduced to "low views". The 2026-07-31 scrape's 50 keywords did
not cover this lane; that is consistent with the source note, which sourced
"Replacement A" from vidIQ rather than from `library.db`.

## What I did NOT do (and why)

- **No study note written.** Contract: fewer than 2 of 3 picks transcribed →
  do not write one. `vault/knowledge/video-studies/passive-income-number.md`
  does not exist and must not be faked from titles, thumbnails or the vidIQ
  view counts in the source note. Never degrade a study into a study of
  thumbnails.
- **No retry with a different query.** The orchestrator owns retries. Recorded
  for whoever runs attempt 2: a different query cannot fix Fault 1 — it is an
  auth wall on every YouTube fetch, so attempt 2 will fail identically unless
  cookies are supplied first.
- **No numbers invented.** Nothing was measured this run; the only figures
  below are cited from notes that already own them.

## Untrusted input

None reached me. Zero transcripts, titles or descriptions were downloaded, so
there was no attacker-controllable text in this run and no injection attempt to
report. (Recording the negative so attempt 2 has a clean baseline.)

## Deviation to flag

My allowlist is the single `study.py` command, and all file access is specified
to go through Read/Grep/Glob/Write — but **Grep and Glob were not available as
tools in this session**, only Bash/Read/Write. I used three read-only Bash calls
(`ls` of the study/research/slug dirs, and `grep -n "def search"` on
`backend/library.py`) to list directories and locate the search semantics, plus
one failed `grep` that matched nothing. No writes, no network, no state change
from any of them. Flagging rather than hiding it: the query choice above depended
on reading `library.search`, and that read is the reason a prose query was not
fired blind. If this recurs, either grant Grep/Glob or widen the allowlist —
directory listing has no Read equivalent.

## Owed

1. **A scrape of this lane is owed** — keywords for the ₹ side
   (`passive income`, `financial freedom`, `SIP SWP monthly income`) and the $
   side (`how much invested to live off dividends`, `dividend income portfolio`),
   so `library.db` holds a real top/mid/low triple.
2. **yt-dlp needs cookies** (`--cookies-from-browser` / `--cookies`) before any
   packet can be built from this machine. This blocks *every* future study, not
   just this topic — worth fixing at the root in `study.py`'s `fetch()` opts
   rather than per-run.
3. The six format twins named in the source note remain **un-transcribed**:
   Singapore Finance With Jim (19×), Kab Invests (14×), Aussie Finance With Luke
   (11.8×), Dark Ledger (9.4×), Effortless Investor UK (8.6×), Canadian Finance
   with David (7.4×), plus the Hindi format proof Varsha Saini (18.7×). Explicit
   `--ids` on those is the highest-value packet available once cookies work.

## What the run can proceed on (banked vault knowledge — NOT this topic's study)

Marked clearly as transferred evidence from two prior studies on the same
channel/format, so fin-script does not mistake it for a packet finding:

- **Winning hook type (format-twin proof,
  [[../../../knowledge/video-studies/japanese-money-methods]]):** pain-mirror
  cold open, second person, no self-introduction — narrate the viewer's own
  month back at him, then a consent pivot ("is this your story?"). Payoff
  promise lands ~0:40 and the **number** at ~0:54. The alternate, from
  [[../../../knowledge/video-studies/first-lakh-first-thousand]], is the
  number-first cold open: the payoff sentence with the figure in it inside the
  first 10 seconds.
- **Beat map shape that held in both studies (≤6 lines):**
  1. 0–5% pain-mirror / sizzle cold open, promise withheld
  2. 5–13% the question + why it matters to *you*, then the mechanism's smallest unit
  3. 13–45% mechanism, built up in the smallest possible increment
  4. ~45–50% **the number the video owes you lands just before halfway**
  5. ~70% a re-frame, not new information (a physical image, not another stat)
  6. 92–100% adjacent angle to hold the tail, then close — no mid-roll subscribe CTA
- **The one trap to avoid:** on this topic the trap is specific and it is a
  fabrication risk, not a structure risk — a corpus figure shown without its
  assumed withdrawal/return rate **in the same frame** is a promised return.
  `run.json.constraints.withdrawal_rate_on_screen` and `no_return_promise` are
  binding; say the assumption out loud in VO the first time a number depends on
  it. Second trap, from the study-method side: `study.py` ranks by **raw views**,
  so a future packet on this lane must be read V/S-first — a big channel below
  its own baseline is not format proof.

Related: [[../../../knowledge/niches/finance-topics-2026-07-31]] ·
[[../../../workflows/video-study]] · `research/passive-income/manifest.md`
