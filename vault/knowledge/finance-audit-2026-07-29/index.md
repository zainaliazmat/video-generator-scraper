---
summary: Full-stack audit of the finance video system (8 parallel research agents, 2026-07-29) — script, design, storyboard, visuals, motion, sound, packaging, performance. Two structural root causes explained most defects: fin-build scaffolded each cut by copying the previous cut's HTML, and every control in the pipeline RECORDED rather than changing anything. **Six fixes shipped the same day (§8)**: the shared blockframe.css + motion.js template, architecture rotation, scene transitions, loudness normalisation, the en chars/sec correction, and the `#N` stock-search bug. What remains is ranked in §2; open creator decisions in §5. Raw agent reports are the numbered appendices.
updated: 2026-07-29
source: 8 general-purpose research agents run 2026-07-29 against the repo + open web; every figure re-derived from a shipped artifact or a cited primary source. §0 (publishing status) corrected by the creator the same day — the videos are scheduled, not failed.
---

# Finance video system — full audit, 2026-07-29

Eight agents, one domain each. Every claim in the appendices carries a `FACT` /
`UNVALIDATED` tag, because **no analytics exist for any video on either channel**
and the difference between measurement and belief is the whole value of this
document.

Appendices (raw agent output, kept verbatim):
[[01-performance]] · [[02-script]] · [[03-design]] · [[04-storyboard]] ·
[[05-visuals]] · [[06-motion]] · [[07-sound]] · [[08-packaging]]

Follow-up research, 2026-07-30, after the creator approved 8-minute videos (§9):
[[09-longform-story]] (structure + the worked-example ruling) ·
[[10-medium-tier]] (production cost + breakage) · `transcripts/` (18 caption
files from the benchmark set — the evidence behind §9's structural claims)

---

## 0. Item zero — the ten videos are scheduled, not yet public

**RESOLVED by the creator, 2026-07-29.** They are **scheduled** and will go
public on their own. No action, no audit until they are live.

Recorded because it cost a research cycle and will mislead the next session
otherwise: from outside, a scheduled upload is indistinguishable from a private
one. All ten return oEmbed `403` (control → `200`; oEmbed serves *unlisted*
videos at 200, so 403 means private **or** scheduled-unpublished), and both
channels' `/videos` tabs list zero videos. So **no external check can confirm a
video is live before its scheduled time** — a scraper cannot tell "scheduled" from
"failed to publish", and neither could this audit.

Two consequences that stand regardless:

1. `knowledge/channels.md` and the five milestone notes say `live · archived`.
   They are *scheduled*, which is not the same state. Cosmetic today; it becomes
   wrong the moment someone reasons about dates from those notes.
2. **Analytics genuinely do not exist yet**, so every claim in this audit about
   audience *response* stays a prior (§7). The engineering measurements do not
   depend on it.

The creator has **kept the finished-video rule as-is** (a handed-over URL means
done). That is a deliberate call: the creator knows the schedule, and the rule's
signal is the handover, not the URL's public reachability.

---

## 1. Two structural root causes

Most individual defects below are symptoms of these two. Fixing the symptoms
without these buys one clean video and then drifts again.

### 1a. `fin-build` is told to copy the previous video

`.claude/agents/fin-build.md` step 1 points the build agent at the **previous
cut's `index.html`**. There is no shared stylesheet, no committed generator.
Found independently by three agents ([[03-design]] #2, [[06-motion]] #4,
[[04-storyboard]] #2). Consequences, all measured:

- **Five divergent implementations.** `hi` and `en` have drifted for five videos;
  `.decision` names two different components inside one run.
- **Five different motion vocabularies.** The newest cut — the one `fin-build` is
  told to copy — is missing `fill`, `countUp` *and* `drift`, and leans on
  `exit`/`popEach`, which are documented nowhere. "Nine helpers" is fiction.
- **Fixes don't propagate.** The `en` cut's `.gt` chevron fix never reached the
  `hi` cut, which shipped a system-font fallback in its 76px hero.
- **Generators evaporate.** good-debt's `build.mjs` was "scratchpad, not
  committed" — gone.
- **Four cuts have no `@font-face` at all** (`50-30-20`, `emergency-fund` →
  `"Arial Black", system-ui`), so the vault's "no system-font dependency" claim is
  retroactively false and those archives are not reproducible at parity.
- It is also a large part of the sameness itself: each video inherits its
  predecessor wholesale, then grows bespoke components nobody reuses. **The
  variance budget is being spent on the layer that doesn't move** ([[03-design]]).

**Fix:** extract `tools/scaffold/assets/css/blockframe.css` +
`tools/scaffold/motion.js` + the parameterised generator; delete "read the newest
archive" from `fin-build.md` step 1.

### 1b. Every control records; none refuses

The architecture-repetition warning was written **four** times — three milestone
notes *and* structured JSON in `good-debt-vs-bad-debt/run.json` `owed[3]`.
`grep -rn owed tools/ .claude/commands/` returns **no readers** ([[03-design]]).
Six identical videos shipped anyway.

The same pattern elsewhere: `format.json`'s `colors`, `type_ladder_px` and
`tiers.*.architecture` are read by no code; 9 of 12 `layout` constants exist only
as prose in agent prompts; `pipeline_check.py` has **zero** motion assertions;
`fin-build.md:36` claims "pipeline_check asserts the four timing copies" — it does
not; `fin-audit` check #8 audits the storyboard's colour table but **runs before
`fin-storyboard`**, so nothing audits the storyboard and nothing compares build to
storyboard.

**Fix:** the gate goes in `pipeline_check.doctor()` at preflight — before
`run.json` exists, before spend. It already takes `--tier` and the orchestrator
already halts on its failure; only the predicate is missing.

---

## 2. The action board

Ranked by leverage ÷ cost. Costs are the agents' estimates against real files.

### Tier 0 — closed by the creator, 2026-07-29

| # | Action | Decision |
|---|---|---|
| 1 | Diagnose the 10 videos | **Closed** — scheduled, will go public; audit them once live |
| 2 | Download the 5 pairs' masters back from Studio | **Declined** |
| 3 | Gate `archive_cut.py` on oEmbed 200 instead of URL-exists | **Declined** — the rule stands as written |
| 4 | Correct the `live · archived` records | **Deferred** — revisit when they are actually live |

### Tier 1 — cheap and mechanical (no taste required, all `FACT`)

**Items 5, 6, 7 and 10 are DONE (2026-07-29)** — see §8.

| # | Action | Evidence | Cost |
|---|---|---|---|
| 5 | `loudnorm I=-14:TP=-1.5` two-pass, video stream-copied | **Ran on the real master: −21.19 → −14.17 LUFS, −1.26 dBTP, 19.8 s.** YouTube attenuates but never applies gain; all six cuts play 7–8 dB under the feed. `TP=-1.0` lands at ≈−0.76 after AAC and fails fin-render's own gate | 20 s CPU/cut |
| 6 | `cuts.en.chars_per_second` 15.0 → **16.1** | Brian measured at 16.11 (hi's 12.5 is right at 12.62); every en script budgeted 7.4% long | one number |
| 7 | Fix `#N` in `pixabay_fetch.py` | **Reproduced: `sheet("x") == sheet("x#3")` byte-identical** — `cmd_candidates` discards `want`. The vault's only documented escape from the immovable demonetised-₹500 top hit does not exist | ~2 lines |
| 8 | `.src` must record the picked cell index | **Reproduced:** re-fetching an archived `.src` returns result #1, not the shipped image. Falsifies the archive-reproducibility claim in `vault/CLAUDE.md` | ~1 line |
| 9 | Asset ledger keyed by md5, spanning **published** videos | Today's dedupe matches 46 files, **zero from the 5 live pairs** — archive drops `*.jpg`, then studio is deleted. Duplicate assets are the machine-readable evidence for the inauthentic-content policy | ~20 stdlib lines |
| 10 | Scene transitions (`dissolve` 0.45s default, `shove`, `gate`) | **Measured from rendered pixels:** hard-cuts 8×, boundary frame-delta 5.85–10.72 vs mid-scene 0.053–0.377 (16–200×); 5 of 8 trip a generic cut detector. The framework writes only `visibility` on `.clip`, and scenes are `position:absolute`, so `opacity`/`transform` is unowned — and `check_html` passes unchanged | **12 LOC** |
| 11 | Constant-velocity `ken` | Amplitude fixed at 0.16 over the whole scene → s7 (28 s) moves **0.32 px/frame**; the payoff scene is the closest thing to a freeze | 2–6 LOC |
| 12 | Font-subset glyph check in `check_build` | Subset is 97 codepoints; `> → ▶ × ≈ ~ ¢` absent and 6/10 cuts type one literally — including the 76px hero of a shipped cut. **Both regressions are post-subset, in the last two videos** | commit `subset.txt` + ~8 lines |
| 13 | `check_build` asserts the four timing homes + storyboard element IDs | Reads neither the JS `S` map nor the `<audio>` rows, so a corrupt map ships green; the ID diff would have caught 4 dropped cut-ins on good-debt and 6 on credit-history | ~25 lines |

### Tier 2 — structural

| # | Action | Why | Cost |
|---|---|---|---|
| 14 | **DONE** — `blockframe.css` + `motion.js` in `tools/scaffold/`; "copy the previous cut" deleted from `fin-build` | root cause 1a | see §8 |
| 15 | **DONE, but not as a gate** — the creator's call was *"don't block the run, implement it properly so next time it won't happen."* So the architecture **rotates by default** instead of refusing a repeat | root cause 1b | see §8 |
| 16 | Thumbnail sameness check on **layout**, not number+photo | All ten shipped thumbnails are one literal layout; `fin-package`'s check compares the number and the photo, so it passes every time. A channel page **is** a thumbnail grid | a few lines |
| 17 | Promote per-scene tail; "no scene ends >2.5 s after its last cue" | 12.6 s (7.1%) fixed padding, 9.0 s guaranteed dead; 28.08 s (15.7%) sits past its last animation; SUBSCRIBE is on screen **1.96 s** | ~20 lines |

### Tier 3 — format decisions (need your call, §5)

Runtime tier · script skeleton · music/SFX · image sourcing · title system ·
brand marks. Detailed below.

---

## 3. Per-domain findings

**Performance** ([[01-performance]]). No public numbers exist, so the agent
measured the market instead: across 235 scraped videos, our **90–300 s band is the
worst-performing band in both markets** (median 11 views IN / 33 US, n=44) against
20 m+ at 140,076 / 59,114. Every breakout in its set is ≥8 minutes — including a
**1,680-sub** Hindi channel doing 57,870 views on an 8m13 video (34× its subs)
while 690k-sub Money Guy did 18,547 on 4m05. Channel size is not the gate; runtime
correlates. `library.db` holds 1,124 rows across 22 keywords and **zero** finance
at any threshold, stale since 2026-07-07; `run.sh` + `SP_FILTERS["year"]` fills it
as-is, but note `study.py`'s ≥240 s floor structurally excludes our own format from
its own comparison set.

**Script** ([[02-script]]). The sameness is **lexical**, and that half is recorded
nowhere: `Four things:` opens 4/4 English roadmaps verbatim, `Then don't say nobody
warned you` closes 4/4, `DO THIS TODAY` appears in 8/8. The "US rewrite, not a
translation" rule holds for *facts* (genuinely strong — different statutes,
mechanisms, hero numbers) and fails for *script*: clause-for-clause isomorphic,
traced to `fin-script.md:44` "read the Hindi script only for structure" — at nine
fixed beats, structure *is* the script. Slot 2 (roadmap) burns 6–7% of runtime
restating the title at 0:20–0:32, inside the drop window, in the exact form
`long_form_scripting.md` §4 bans. Slot 9 is a recap where §6 mandates a next-video
loop — **0 of 8 scripts has one.** Credit where due: the hooks are the strongest
part and have improved unprompted; the peak sits correctly at 65–81%.

**Design** ([[03-design]]). 108 of 108 shipped scenes are a centred column over a
graded photo. Three alternatives costed, all reusing every existing token:
**`ledger-rail`** (kill `place-items:center`, 300px left rail with the scene index
at the unused thin weight axis, photo to a hard-edged right panel — deletes the
scrim and every text-shadow, ~40 lines, cheapest); **`statement-card`** (photo
full-bleed and stronger, all type in one pinned panel card whose *contents* swap —
kills the exit-centre/pop-centre gesture that fires 6× per video, reads most
different at 3 seconds); **`split-register`** (hard 62/38 split, nothing ever on
the photo — cheapest CSS, most expensive storyboard). Free fourth: drop the
roadmap and recap bookends → 7 scenes, ~30 s shorter, out of the 2:46–2:59 band.

**Storyboard** ([[04-storyboard]]). Word-level cue timing was **never implemented
on any cut** — `fin-build`'s Bash allowlist has no `venv/bin/python`, so whisper is
unrunnable in the only stage that writes cue times. And it is **not worth building
as specified**: modelled against the real VO, worst cue drift is −0.36 s, mean
|0.19 s|, and fin-voice measured the most timing-critical cue in the video at 0.1 s
error. Drift cancels when sentences are evenly sized, which these scripts are.
Cheaper route if wanted: piggyback one `silencedetect` pass in `batch.py`
(fin-render already proved it "exact to the sample" on this audio) and anchor to
sentence boundaries — ~15 lines, no new dependency, vs ~80 + an allowlist edit.
**This supersedes the design doc's §6 prescription.**

**Visuals** ([[05-visuals]]). A pair needs 18–32 images and costs 75–144 stock
calls over 8–12 retry rounds; the API is free, the cost is agent time plus roughly
one extra build+render cycle per pair. Recommendation: **generate everything except
currency, ~$15/month** at ~8.7 pairs/mo (Imagen 4 Standard $0.04 → $11.80; Nano
Banana $0.067 → $19.77, halved on Batch). Adobe Stock at this volume is $249.99/mo.
Keep banknotes photographic — models inherit currency restrictions and a
plausible-but-wrong ₹500 is worse than a real photo of a withdrawn one. Which
implies the real change: **stop making ₹ notes the India signifier.** Indian
*environments* (kitchen, shop QR standee, EMI passbook) carry the market better,
are what stock lacks, and are what AI does well. Evidence the pool is exhausted:
India signifiers per hi cut went 3 → 2 → **0** (credit-history shipped `manometer`,
`pocket watch`, `cardboard boxes`). Pexels/Unsplash are a *different* pool, not a
deeper one (measured). Don't add Unsplash — its API Terms require on-screen
attribution that `CREDITS.txt` doesn't discharge.

**Motion** ([[06-motion]]). **65.4% of the English cut has zero foreground
motion**; 21 static runs over 2 s (28 in hi), worst 6.6 s — against a documented
"no static frame beyond ~2 s" rule with zero assertions behind it. Eight new
helpers specced seek-safe and deterministic: `wipe`, `parallax`, `countDown`,
`drain`, `draw`, `rack`, `slam`, `stack`. `breathe(dur)` is mis-documented —
`breathe(x,t,3.0)` runs 6.0 s, and one cut breathes an element for 2.6 s after
`exit` hid it, at 0.09 px/frame (invisible regardless). The installed HyperFrames
skill's rule #1 is *"Every composition uses transitions. No exceptions,"* and
`hyperframes_production.md:57` already requires a `Transition` storyboard column
that the finance template dropped. **Honesty flag from the agent itself:** its
competitor benchmark rests on SEO listicles and is low-signal; ~2 h of running the
same `scdet` method over three competitor videos would convert it to measurement.

**Sound** ([[07-sound]]). Root cause of the loudness miss: ElevenLabs returns clips
at −24.1 LUFS (en) / −25.2 (hi) and there is **no gain staging anywhere**. A flat
+8 dB is impossible (crest 17.8 dB). Music: **YouTube Audio Library, $0/mo** — the
only source with a first-party *"won't be claimed through Content ID"* guarantee
and, critically, **no channel-count limit**, so both monetised channels are covered
by construction. `studio/library/music/` already exists and its README already says
this. Paid fallback **Uppbeat Creator $62.93/yr, 3 safelists** (their catalogue *is*
in Content ID — both channel IDs must be safelisted). ⚠️ **Epidemic Sound Personal
is one channel per platform and does not cover this.** ⚠️ **`media-use`'s offline
BGM fallback is MusicGen, CC-BY-NC 4.0 — non-commercial, sitting in the default
path.** There is ~1.78 s of true silence between every line, ~16 s = 9.2% of
runtime. TTS `style: 0.0` is the flattest value the API accepts, unseeded takes
aren't reproducible, and `batch.py` hardcodes two voice params in violation of the
one-home rule.

**Packaging** ([[08-packaging]]). See §4 — the policy verdict is the important
part. Also: `-en` titles run 60–67 chars against a US market average of **50.2**
(n=240); **0%** of live hi titles use "?" against India's **34%** (n=254);
captions appear in **0 of 11** packs though `timing.json` + VO lines are both
already on disk (~20 lines for SRT). Title system proposed as **four shapes with
the previous upload's shape disqualified** (`last_title_shape` in run.json, ~3
lines) rather than one formula. Native Test & Compare on 3 titles, decided on
**watch-time share** — the only performance signal available without analytics,
and the packs already write 4–5 titles and bin them.

**Faceless caveat, worth a real decision:** 22/22 sampled competitors in both
markets use a face, and FinnovationZ and Two Cents — the two "faceless finance
works" exemplars in the vault — have **both moved to faces**.

---

## 4. Policy — real vs speculation

Separated against primary sources ([[08-packaging]]).

**Real policy.** `answer/1311392`, updated 2025-07-15, renamed "repetitious" →
**"inauthentic content"**, three buckets, clarified 2026-07-16 by Matt Halprin on
Creator Insider: (1) generic/repetitive/templated, (2) off-putting, (3) AI personas
on sensitive topics — verbatim *"AI-generated podcast hosts offering financial
guidance."* Enforcement: *"monetization may be removed from your entire channel,"*
reapply after 90 days.

**Speculation, widely repeated, and in our own vault.** "YMYL applies" — that is a
*Google Search* rater concept, absent from all YouTube policy. "Finance needs
credentials" — no such rule; every source asserting it was an uncited SEO blog.
"Disclaimers protect you" — unsupported. And the vault's *"5th consecutive crosses
the line"* is a **house rule**, not a platform threshold; no YouTube source states
any number.

**Our exposure.** Bucket 3 — **LOW**: no persona, no stock picks, disclaimer
present. The vault's 2026-07-28 resolution is correct; keep it. Bucket 1 — **the
real risk, and worse than the vault records**, because the vault audits sameness in
architecture and runtime while the thumbnails are one literal layout across all ten
and the check that should catch it compares the number and the photo. Disclosure:
"set No" is defensible on the Studio checkbox wording, but YouTube's own 2024 blog
lists *"synthetically generating a person's voice to narrate a video"* as
disclosable — ambiguous rule, zero-cost hedge (YouTube states disclosing *"won't
limit a video's audience or impact its eligibility to earn money"*), asymmetric
downside. Take the hedge.

---

## 5. Decisions — creator, 2026-07-29/30

1. **Publishing** — closed. Scheduled; audit once live. (§0)
2. **Runtime tier — GO to ~8 minutes.** Creator: *"we can make the video 8
   minutes long but we have to do a proper research how to write finance long
   scripts make it like a story so user can engage with it and its easy for
   everyone to understand finance with an example story."* So the deliverable is
   not "a longer video" — it is a **story-led beat sheet built around a worked
   example, understandable by a beginner**. Research commissioned 2026-07-30
   (story structure + `medium`-tier production cost); this section is the brief.
3. **Architecture — rotation is live, the set is being chosen.** `blockframe-9`
   and `ledger-rail` are in `format.json`; `statement-card` and `split-register`
   are specced in [[03-design]] and previewed for the creator at true 1920×1080
   geometry. Composes with the free 7-scene bookend cut.
4. **Faceless — SETTLED, permanently.** Creator: *"no i dont want to show my
   face."* This closes the question; the 22/22-competitors-use-a-face finding in
   [[08-packaging]] is noted and **overridden by creator preference**. Do not
   re-raise it, and do not propose a synthetic or AI presenter as a workaround —
   that lands in exactly the policy bucket §4 warns about ("AI personas on
   sensitive topics", named verbatim for financial guidance). Every future
   recommendation treats faceless + synthetic voice as fixed constraints.
5. **Sound — DONE (§8).** Music bed + the 7-sound kit, SFX generated from the
   ElevenLabs API per the creator's instruction.
6. **Images — DEFERRED.** Creator: *"no i dont want to switch to ai images now
   may be in future."* Stock stays; the `#N` fix and the asset ledger are the
   mitigations. Note [[10-medium-tier]] may find the image pool is the binding
   constraint on 8-minute videos — if so, this decision needs revisiting on
   evidence, not preference.

## 6. Vault corrections owed

Beyond §0. Each is a `FACT`-tagged contradiction found against a shipped artifact:

- `best-practices.md`'s thumbnail section (*"ENERGY BEATS AUTHENTICITY… glow/fire/
  glossy… red keyword box"*) is the **opposite** of the shipped finance system and
  of `fin-package`'s own "never red-box".
- `best-practices.md`: *"Hindi market searches in ENGLISH keywords"* — refuted by
  the pipeline's own autocomplete pulls. Roman Hinglish autocompletes broadly;
  pure Hindi returns nothing.
- `india-finance-market.md`: *"Titles/descriptions: English"* — stale.
- `design-finance-blockframe.md`: "one grade override per video max" is unenforced
  and broken 4× (`emergency-fund/en` has two). `hyperframes_production.md` §6
  records the *opposite and correct* rule — match brightness per image. Lock
  `grayscale`+`contrast`, make brightness a per-image calibration.
- `design-finance-blockframe.md` §4 "No SFX" reads as a fork artefact, not a tested
  decision — and silently covers music, which it never names. §4's component list
  describes `needs-vs-wants` and is three videos stale. `.mega` 290px is unused
  since then; `.huge`'s 112px is used once in ten cuts — the top two ladder rungs
  are decoration. `drift` is documented "for photo-free scenes", retired
  2026-07-28, contradicting itself two lines later.
- `design-finance-blockframe.md` §6 prescribes whisper; measurement says
  silencedetect beats it on this audio (§3).
- `voiceover-tts.md:120` "default model `eleven_v3`" — finance runs the *fallback*
  `multilingual_v2`, which is **correct** here. Lane-scope it or someone will
  "fix" format.json and spend credits making the read worse.
- `hyperframes_production.md:43` track bands stated as a hard rule; `hyperframes-core`
  says *"there's no fixed convention"* and finance already ships VO on track 10.
  Real rule is only "no same-track time overlap". `:106` targets −16 LUFS (a mic
  chain); YouTube wants −14.
- `stock-photo-sourcing.md`'s escalation clause points at `[[scene-image-prompt-rules]]`,
  which **is not in the vault** — it exists only as a Claude memory file the fin-*
  agents cannot read. The ₹2000 note's 2023 withdrawal is documented nowhere.
- `@moneymavens101`'s About text is a byte-copy of the Hindi channel's, and the US
  channel calls itself **"Paisa School"**. Neither finance channel has a real About.

## 8. Implemented, 2026-07-29

Creator approved items 5, 6, 7, 10, 14 and 15. All three tools carry a runnable
`--selftest`; all pass.

| What | Where | Verification |
|---|---|---|
| **Loudness** — two-pass `loudnorm I=-14:TP=-1.5`, video stream-copied, writes `PUBLISH-1080p-<cut>.mp4` beside the master and refuses to overwrite it | `tools/loudnorm.py` (new) · orchestrator step after the encode · `check_render` now requires the file | Ran on both real `credit-history` masters: **en −21.19 → −14.17 LUFS, −1.26 dBTP**; **hi −22.17 → −14.08 LUFS, −1.40 dBTP**. ~20 s each. Both PUBLISH files exist now. |
| **Scene transitions** — `dissolve` (0.45s default) + `shove` (act change) + `sceneTransitions()` one-call wiring | `tools/scaffold/assets/js/motion.js` · `fin-build` step 2 · `fin-storyboard` 4b · design doc §5 rule 0 | `check_build` asserts every non-final scene overlaps the next by `transition_seconds`. Run against the shipped `credit-history-en`: **0.000s on all 8 boundaries** — the hard-cuts the `scdet` measurement found. Selftest covers pass and fail. |
| **`chars_per_second`** en 15.0 → **16.1** | `tools/format.json` | Measured 16.11 / 16.64 on shipped cuts. Confirm block updated (en budget ~2,475 → ~2,656). |
| **`#N` on the contact-sheet path** — was parsed and discarded, so `'q#3'` returned a byte-identical sheet to `'q'`; now a start offset. Sheet log prints `from #N`. | `tools/stock/pixabay_fetch.py` `cmd_candidates` | Selftest asserts `c[0].full` ends `#1`, `d[0].full` ends `#3`, and they differ. This is the documented escape from the demonetised-₹500 top hit — it now exists. |
| **The master template** — one stylesheet, one motion file, **linked not copied** | `tools/scaffold/assets/{css/blockframe.css,js/motion.js}` (new) · `fin-build` step 1 rewritten | 291 lines CSS (braces balanced), `node --check` clean on the JS. `fin-build` no longer says "read the newest archived index.html". Also fixed in the canonical copy: `breathe(dur)` ran for 2×`dur`. |
| **Architecture rotation** — `pipeline_check.py architecture` returns the least recently used entry; the orchestrator writes it to `run.json` before `fin-script`; `fin-build` applies its `body_class`, `fin-storyboard` boards for it | `tools/format.json` `architectures` · `pipeline_check.next_architecture()` · orchestrator §2 step 2a | Backfilled `architecture: blockframe-9` into the 3 existing `run.json` files, so the rotation knows what actually shipped. It now returns **`ledger-rail`** — the next video changes layout with nobody having to remember. Second architecture shipped as a `.rail` modifier in `blockframe.css` (~50 lines), so the rotation has somewhere real to go. |

**Deliberately not done** (out of the approved scope, still on the board):
AI image generation (creator: "maybe in future" — the `#N` fix and the ledger
are the Pixabay mitigations for now); the forbidden-glyph lint; per-scene tails;
constant-velocity `ken`; the thumbnail layout check; SRT captions; music and SFX.

## 9. The 8-minute format — research in, one fork to settle

Two agents, 2026-07-30: [[09-longform-story]] (structure + words, evidence base =
8 real videos pulled with the repo's own yt-dlp, transcripts kept in
`transcripts/`) and [[10-medium-tier]] (production cost + breakage, measured
against real masters).

**Agreed.** Target 510s. The structure is `story-ladder-12` — twelve beats, first
payoff before 1:15, mechanism named only at the turn (beat 6), a declared mid-roll
boundary at 5:20, a **counter-case** as the peak (same character, one variable
changed, the delta is the payoff), an honest-limit beat, and a named next-video
loop. **No roadmap, no recap** — 5 of blockframe-9's 9 beats survive. Encode
~112 min/pair, disk ~5.2 GB steady (both current `format.json` figures are
wrong — `short` claims 1.0 GB against **2.81 GB measured**).

**The honest worked example — settled.** A **named composite, declared as an
assumption set.** Not testimony, not a real person, not bare "you". Both
highest-traction Hindi videos on our topics do exactly this (Zerodha Varsity;
Malodia's named brothers, 1.46M views). The declaration goes inside the first 25s,
once, and is grep-checkable:

> **en** — "Meet Marcus. Marcus isn't a real person — he's an average, built out of
> what Americans actually financed last year. Every number of his is real."
> **hi** — "एक बंदा है — नाम रख लेते हैं रोहित। रोहित असली नहीं है, पर उसके सारे नंबर असली हैं।"

Rules: every number traces to `facts-staging`; no dialogue, no biography, no
testimony; the counter-case is the *same* character with one variable changed;
a different name per video **and** per cut. A real cited case beats a composite
when `fin-facts` can find one.

### ⚠ The fork: how many VO lines?

The two agents disagree, and it is not a detail — it decides whether
`fin-build`'s core 1:1 assumption survives.

| | [[10-medium-tier]] | [[09-longform-story]] |
|---|---|---|
| VO lines per cut | **28** | **~86** |
| Line shape | ~18s paragraph | single sentence |
| Scenes | 28 (1 line = 1 scene) | ~24 (lines **grouped** into scenes) |
| Images per cut | ~20, via reuse across 2–3 non-adjacent scenes | same — decoupled from lines |
| `check_build` | untouched | `len(scenes) == len(lines)` must become a mapping |
| EL calls per pair | 56 | ~220 |

**Recommendation: decouple lines from scenes — take the ~86-line model.**

1. **Cost is not the differentiator.** ElevenLabs bills characters, not requests,
   and the script length is identical either way. 56 vs 220 is a *cap* question,
   and that cap (`max_elevenlabs_calls: 30`) turns out to be **prose in the
   orchestrator markdown, enforced by no code at all**.
2. **The paragraph model contradicts the documented TTS rule** — single-sentence
   lines, one clip per line, tiered gaps ([[../../workflows/voiceover-tts]]).
   blockframe-9's 18s paragraphs already violate it; scaling that to 28 scales
   the violation.
3. **It is the only version that fixes cue timing.** [[04-storyboard]] measured
   char-interpolated cues drifting up to −0.36s. Short lines make each clip's
   boundary a real anchor, which is cheaper and more accurate than the
   faster-whisper work that note priced and rejected.
4. **Images stay solvable either way** — the binding constraint is scene count,
   not line count, and both models land at ~20–24 backgrounds per cut with
   non-adjacent reuse.

Cost of the recommendation over the 28-line path: `timing.json` lines gain a
`scene` field, `check_build`'s 1:1 assert becomes a grouping check, and
`fin-build` places N audio rows per scene instead of one. Everything else in
[[10-medium-tier]]'s change list is unaffected.

### Blockers to clear before the first 8-minute run

- `max_elevenlabs_calls` must move **into `format.json`** and be enforced by
  `pipeline_check`, not asserted in prose.
- `architectures` rotation is **tier-blind** — at MEDIUM it can hand `fin-script`
  and `fin-build` contradictory architectures. Needs a `--tier` filter.
- `fin-script.md` still points MEDIUM at the *history* channel's per-line build.
- `tiers.*.disk_gb_per_pair` is wrong for both tiers (measured 2.81 GB for SHORT).
- `known_benign` is empty, and the required 0.45s scene overlap is exactly the
  kind of finding the hyperframes linter reports — resolved for scene sections by
  alternating `data-track-index` (§8), but re-verify at 24+ scenes.
- **`build.mjs` is the real work** — the scaffold's `package.json` declares it and
  ships none, so every cut rewrites the generator by hand. The newest cut
  (`credit-history-en`) has a working one to promote.

**Honesty flags carried from the agents:** the single strongest video in the
benchmark set (34.45 views/sub, 8m13) is a **no-story, no-numbers list with a
spoken table of contents** — so runtime replicates, story does not; and
`long_form_scripting.md` assumes a human voice, screencasts and affiliates, so
roughly half of it does not apply to these channels, yet `fin-script` reads it
whole.

## 7. What stays unvalidated

Everything about audience *response*. No CTR, no retention curve, no impressions —
and none can exist until §0 is resolved. Engineering facts (drift, loudness, hash
collisions, glyph coverage, cut detection) are reproducible and stated as facts;
every claim that a change will *perform* better is a prior. The runtime-band
evidence in [[01-performance]] is the strongest market signal here and it is still
correlation across other people's channels, not a test of ours.

Related: [[../design-finance-blockframe]] · [[../channels]] ·
[[../../workflows/finance-video]] · [[../best-practices]] · [[../../CLAUDE]]
