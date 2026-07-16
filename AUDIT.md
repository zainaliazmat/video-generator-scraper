# AUDIT.md — YoutubeScraper / faceless-channel project (2026-07-17)

**Method.** One cartography agent produced `MAP.md`. Five independent read-only specialists (Pipeline Archaeology, Vault Analysis, Security & Continuity, Assets/Cost/Provenance, Output Forensics) each worked from the map alone, blind to each other and to the owner's account. Their reports were synthesized, then a fresh red-team agent — which had seen none of the specialist work — attacked the draft and re-verified its key measurements. Red-team corrections are folded in and marked; where the synthesis disagrees with the red team, that is stated. Ranking follows the owner's priorities: **reliability > output quality > batch/scale > speed**.

---

## What this project is (reconstructed from evidence)

A one-person, Claude-operated faceless-YouTube video business with two co-located halves:

1. **ytauto** (`backend/`, Python/Textual TUI) — YouTube scraper feeding `library.db` (1,124 videos, 24 columns). Load-bearing only at Stage 1 (topic discovery); zero code coupling to the video build (grep across `vault/` and studio: scraper referenced only in strategy notes, never by any build script).
2. **A video production pipeline**, 7 stages confirmed by monotonic artifact timestamps: scrape/topic-lock → Roman-Urdu script → Nano Banana scene images (pasted into Google AI Studio via the `tools/prompt-runner/` chrome.debugger browser macro) → ElevenLabs TTS (`tools/tts/elevenlabs_tts.py`) → hand-written `build.py` generating a HyperFrames `index.html` → deterministic headless-Chrome render to MP4 → human proof-watch + SFX + Canva thumbnail. Knowledge lives in `vault/` (Obsidian, 41 notes, 81,112 words); renders live in the `studio/` symlink target `ClaudeHyperFrame` (8 GB, a separate git repo with a GitHub fork remote).

**Business shape (red-team addition, from `vault/knowledge/channels.md`):** this is a *three-channel* operation — Channel A **TechToolTester** (LIVE, AI-tools reviews, the affiliate/sponsor **money lane**), Channel B **HistoryFramesFilm** (LIVE, 1 video shipped, explicitly "mid-RPM, no affiliates — volume/brand play"), and Channel C **Urdu history** (decided 2026-07-07, with a rule that history topics ship in BOTH languages, Urdu-first — i.e. 2× production per history topic).

**State of play:**
- **PUBLISHED:** "A Century of Travel" — `https://www.youtube.com/watch?v=qyBqfJGwnEI`, scheduled live 2026-07-11, recorded in `vault/videos/video-hist-01-travel/index.md:5`, `vault/knowledge/channels.md:40`, and `vault/index.md:34`. *(Red-team correction — the draft audit wrongly listed "was anything published?" as its biggest unknown while the URL sat in three files every agent had read.)*
- **SHIPPED render, publish status unrecorded:** video-02 "Claude edits video" — `FINAL-…mp4` (12:03) rendered 2026-07-09, build-log says "COMPLETE & SHIPPED".
- **DRAFT, one human session from shippable:** Pompeii (`pompeii-full-draft-v3-synced-1080p.mp4`, 19:55, rendered 2026-07-17 02:34); owed: human proof-listen, real SFX, one on-screen cleanup, 4 press-still rights checks.
- **STALLED 13+ days:** video-01 (English AI-tools) — parked at "MANUAL CAPTURE PENDING" since 2026-07-03; no render exists.

## What is genuinely good (measured, not asserted)

The craft layer works, and that should be said plainly:

- Final Pompeii render duration matches summed VO within **21 ms over 20 minutes** — a constant offset, not growing drift (ffprobe: render 1195.776 s vs VO sum 1195.755 s).
- The VO set tiles script segments 01–65 (+61a) **contiguously, zero gaps, zero overlaps**, and matches the *current* script version, not a stale draft.
- Loudness spread across the 10 final clips: **1.3 dB** — no audible patchwork despite a mixed generation history.
- All 84 AI scene images are exactly **2752×1536**; evidence photos are per-file licensed in `CREDITS-evidence.md`/`LICENSES.md` with a written de-risk plan.
- The build contract is deliberately deterministic (no `Date.now`/random/network, vendored gsap, `MISSING ASSET` hard-fail) — re-renders are reproducible.
- **Backend verified healthy** *(red-team ran it)*: `pytest backend/tests` → **30 passed in 4.08 s**.
- Credential hygiene is clean: one key (`ELEVENLABS_API_KEY` in `.env`), never committed anywhere in git history (`git log --all -S` sweep), properly ignored, read via env in code.
- A real knowledge-compounding loop exists where used: `knowledge/best-practices.md` (18 wikilinks, dated study citations, "hard-won correction" entries) and the `voiceover-tts.md` "so nobody re-litigates it" dead-end ledger.

The failures below are almost entirely **continuity and process-memory failures**, not craft failures.

---

## Findings, ranked

### SEVERITY 1 — A single disk failure loses essentially everything (CAUSE) — red-team re-verified, unbroken

The owner's stated definition of done — "if my laptop dies tomorrow, I lose nothing" — currently fails in every category:

- `git remote -v` on this repo is **empty**. 39 commits exist on this disk only.
- **No commit since 2026-07-05** despite 12 days containing the project's best work: 39 uncommitted entries (`git status --porcelain`); **20 of 41 vault notes are untracked**, including all 9 Pompeii notes, both design systems, `urdu-script-style.md`, `voiceover-tts.md`.
- **Déjà Dup is configured but has never run once**: gsettings show `backend 'google'`, `include-list ['$HOME']`, `last-run` *empty*. The intent to back up exists; the backup does not.
- The studio repo has a GitHub remote, but `library/projects/` (**1,012 MB — the six actual video projects**) is gitignored, plus 4 unpushed commits and 58 uncommitted files. Whether the fork actually contains the local engine commits could not be verified without a network fetch (no `origin/main` ref locally).
- The Claude memory dir (212 MB, including the curated operating rules in `memory/`) is off-git and unbacked.

Loss ratings if the disk died now: backend code **gone forever** (committed, no remote); vault **gone forever**; studio video projects **gone forever**; `library.db`, TTS clips, scene images regenerable at cost (and see Severity 5 — the images are only *approximately* regenerable); `research/` re-downloadable.

This is #1 because it is the pure reliability failure: every other fix is worthless if the disk dies first.

### SEVERITY 2 — Rights exposure, re-aimed at the LIVE video (red-team correction)

The draft pointed all rights analysis at the unpublished Pompeii draft. The red team correctly inverted this:

- **(a) The live video** (qyBqfJGwnEI, public ~6 days, on the monetizing channel-B track) got **no rights audit at all**, and per the post-delivery cleanup rule its heavy assets were deleted after shipping (verified: `ClaudeHyperFrame/videos/a-century-of-travel/renders/` now holds only thumbnails). Its music/SFX provenance is therefore the **hardest to reconstruct and the only one that can trigger a real strike today**. No license record for its audio was found in the tree. This is the urgent item.
- **(b) Pompeii (pre-publish checklist, cheap now, expensive after publish):** `pompeii-drone-bed.mp3` underlies the entire 20-minute film and appears in **no** license doc, no TTS log, no metadata beyond an encoder tag — origin unknown. Four press evidence stills (EV-54A/56A/60A/61A) are flagged in `CREDITS-evidence.md` as rights-check-owed. And there is **no record that the ElevenLabs account was on a paid/commercial tier** when the VO was generated — the vault's own `monetization.md:25` states free tier = no commercial rights; worst case is regenerating all VO under a paid plan.

### SEVERITY 3 — Operator capacity vs channel strategy (red-team addition)

The pipeline's heaviest human tax is the image stage: ~100 supervised browser round-trips per film through a `chrome.debugger` macro that breaks on any AI Studio UI change. The vault commits to **three channels**, a weekly cadence on the money lane (A), and **bilingual (2×) production for every history topic** (`channels.md:73-77`). No document reconciles that workload with one operator. Meanwhile the explicitly-designated money channel (A) has one stalled video (video-01, parked 13+ days on manual capture) while the heaviest, lowest-RPM format (Urdu cinematic history) absorbs the most effort. That mismatch is a strategy/capacity question only the owner can answer — but the audit's job is to say the numbers don't currently add up.

### SEVERITY 4 — The written process lags and diverges from the real process (CAUSE)

Reframed per red team: the root `PRODUCTION_RUNBOOK.md` is not "wrong" — it is the **proven, deliberately-reusable playbook for the shipped travel-video format** (`video-hist-01-travel/index.md:26`: "This pipeline shipped a finished 4-min film end-to-end. Copy it; swap topic/assets."). The genuine gaps:

- **The Pompeii/Urdu path — the current main format — has no runbook.** Its process exists only in `build.py`'s docstring, `video-hist-01-pompeii/index.md`, and session memory. A hand-written 46 KB `build.py`, paid ElevenLabs v3, segment-level silence-snapping: none of that is captured as a repeatable sequence.
- **The vault's own session-end protocol is not being followed:** `vault/index.md` (the file the protocol says to read first) is stale by 10 days, omits 9 on-disk notes (~22% of the vault) including the entire Pompeii index, and carries a stale "planned" summary line for a channel that has shipped. `vault/CLAUDE.md` promises "git history IS the audit trail" while half the vault is untracked.
- **No supersession convention:** overturned decisions (`niches/cinematic-history.md` still reads "FIRST TOPIC LOCKED: Pompeii" though Travel shipped first) look identical to current ones.
- Naming drift: four folder-naming schemes across `vault/videos/`, and **`hist-01` identifies two different videos**; money figures are duplicated across `monetization.md` and `niches/ai-tools-creator-video.md` against the repo's own "one home per fact" rule.

### SEVERITY 5 — No generation-time records: the filename convention is the only schema (CAUSE)

Convergent across three independent specialists:

- State handoff between stages is purely filename convention; `build.py` hard-fails on a missing basename, but no manifest verifies "every EDL scene has an image and every image is used."
- **No seeds recorded for any of ~78 AI images** — exact reproduction is impossible; the locked character looks (the baker, the horse) cannot survive a model change. (This is why "regenerable at cost" is only true for *some* image, not *these* images.)
- No per-clip TTS generation log (which tags/settings produced each chapter; the ch4 five-variant sprawl — `v3`, `-ipafix`, `-ipafix2`, `-NASTALIQ`, `-B` — is the measurable cost of that gap).
- **Zero cost/usage records anywhere** — no dated spend, no generation counts. Budgeting the next video is guesswork.
- 17 of 27 TTS files are unlabeled dead experiments; the 10 keepers are identifiable only from prose. Three coexisting full Pompeii renders with no changelog naming the deliverable.
- Three numbering schemes (script CH1–10, audio ch2–10, images S1–S9) reconcile only through raw segment numbers.
- **Content collision (red-team verified byte-identical):** `S1-06A_epic-establishing.jpeg` and `S2-10A_vesuvius-over-city.jpeg` share md5 `6685402d…` — two storyboard-distinct shots ship the same frame, unflagged anywhere.

### SEVERITY 6 — Capability left on the table (web-verified against July 2026 docs)

- Project docs still budget Nano Banana at "200 free/day"; the current AI Studio free tier is ~**500/day**.
- **Nano Banana Pro** (Gemini 3 Pro Image, GA June 2026, ~$0.134/image ≈ $13 per 100-scene film) directly targets the project's #1 documented image pain ("Real photo, not AI fix") and legible text cards.
- The prompt-runner browser macro is fragile to any AI Studio UI change, and Google has already cut free quotas once (Dec 2025) — the image stage carries both the most human time and the most platform risk.
- ElevenLabs and HyperFrames usage matches current capability (v3 quirks correctly handled; deterministic contract matches upstream intent). `hyperframes transcribe` (word-level forced alignment) is the documented next lever if sync ever drifts again.

### Appendix — cheap cleanups (real but low-cost; collapsed per red team)

- `Pompie Assets/` (357 MB) is byte-duplicated into the studio project (~95 md5-identical pairs) with no declared source of truth, and is **not in `.gitignore`** — a `git add -A` would stage 357 MB. *(Kept as a finding, contra red team's "theoretical": the maintainer here is Claude, and a future session can edit whichever copy it finds first — divergence risk is real when no file says which copy is canonical.)*
- ~1 GB obsolete silent Pompeii v1 render is reclaimable per the vault's own cleanup rule; 3 loose `pompeii-4XX.jpg` drive-by exports duplicate named scene files.
- `.env` is mode 664; should be 600. (Low real exposure on a single-user machine.)
- `library.db` mtime 2026-07-07 — **topic decisions are running on 10-day-old scrape data**; re-scrape before locking the next topic. *(Red-team addition.)*
- `.pytest_cache` names vanished tests (test_app, test_jobs, test_serialize, test_tsv_sources, test_predict_endpoint) — features/tests were deleted; one-line flag only.
- Segment 08 has no dedicated image; unverified whether the render reuses a neighbor (fold into the owed proof-watch).
- video-01's storyboard/design live only in a claude.ai web project — a single point of loss for that video.

---

## Convergence and disagreements (preserved, not smoothed)

**Convergence (independent, therefore strong):** the continuity failure was found separately by three specialists from three directions (git state, vault tracking, studio repo state) and fully re-verified by the red team. The "no manifests, filenames are the schema" finding was reached independently by the pipeline, assets, and forensics specialists.

**Disagreements:**
1. *Vault: diary or knowledge base?* The metrics say mostly diary (72% of words are per-video scratch; 9 dead-end notes; index stale). But two agents independently found the compounding loop real where it exists (`best-practices.md`, the TTS dead-end ledger). Verdict: the mechanism works but is confined to ~2 notes and not enforced by any process.
2. *Filename handoff: brittle or proven?* One specialist called it brittle; forensics measured it producing a 21 ms-accurate 20-minute film. Both are true: it works under one careful operator+Claude and has no guardrails beyond `build.py`'s hard-fail.
3. *Scene images: regenerable?* Continuity said "regenerable at cost (~1 day of quota)"; provenance said exact reproduction is impossible (no seeds, model drift). Provenance wins for the flagship's visual continuity.
4. *Synthesis vs red team, stated dissents:* (a) index.md staleness is individually cosmetic (red team is right) but is retained as *evidence of the abandoned session-end protocol*, which is a cause, not a cosmetic; (b) asset duplication is retained as a real finding, not padding, because the maintainer is Claude and no file declares the canonical copy. All other red-team objections were accepted and folded in above.

## Causes vs symptoms

**Causes:** (C1) zero off-disk redundancy; (C2) session-end/commit discipline abandoned since Jul 5; (C3) no generation-time record habit (manifests, seeds, settings, costs); (C4) duplication with no declared source of truth; (C5) channel commitments not reconciled with operator capacity.
**Symptoms — do not fix directly:** stale index, missing-runbook gap, orphan TTS files, unlabeled renders, ch4 sprawl, money-fact duplication, naming drift. Fixing C1–C5 makes these disappear or become one-time cleanups.

## Couldn't determine (for Phase E reconciliation)

1. **Music/SFX provenance of the LIVE travel video** — its assets were deleted post-delivery; only the owner knows what the bed track was and where it came from.
2. **ElevenLabs account tier** at VO generation time (monetization-clearance of all existing VO hangs on this).
3. **Origin of `pompeii-drone-bed.mp3`.**
4. **Post-publish performance loop:** `video-hist-01-travel/index.md:50` promises "measure CTR/AVD once live and feed it back" — no analytics data exists in the tree; the compounding-growth loop is unverified against the one real published result.
5. Whether the GitHub fork actually holds the studio engine commits (needs one network fetch).
6. Whether Déjà Dup was ever authenticated to Google or setup simply stalled.
7. Whether video-02 was actually published (a final render + "SHIPPED" note exist; no URL recorded, unlike the travel video).
8. Whether `Pompie Assets/` (113 files) is a staging superset or stale snapshot of the studio images (97 files).
9. The Canva thumbnail step's actual mechanics (no template or exported PNG in the tree).
10. Per-beat A/V alignment of Pompeii v3 (the human proof-watch the project itself says is owed).

## Questions for the owner (Phase E — asked only because evidence cannot answer them)

1. What is the music bed in the published travel video, and where did it come from? (Assets deleted; nothing in the tree records it.)
2. Is your ElevenLabs plan a paid/commercial tier, and was it at VO-generation time?
3. Was video-02 published to YouTube? (No URL recorded anywhere, unlike travel.)
4. Which is the intended long-term identity: the three-channel bilingual plan in `channels.md`, or something narrower? The workload math in Severity 3 needs your answer, not more evidence.
5. Did Déjà Dup setup fail, or was it never finished? (Determines whether the continuity fix is "click resume" or "choose a backup method.")
