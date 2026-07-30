# 01 — Performance grounding + competitive benchmark

Agent: grounding. Date of retrieval: **2026-07-29**. Repo: `/home/zain-ali/Documents/YoutubeScraper` (read-only; nothing written outside scratchpad).

Every claim below is tagged `FACT` (verifiable artifact / retrieved number / cited spec) or `UNVALIDATED` (plausible, untested).

---

## 0. THE HEADLINE — none of the 10 videos is public

`FACT` **All 10 "live" videos are PRIVATE. Both channels have zero public uploads. Public view count for every one of them is not "low" — it does not exist.**

Two independent methods agree, plus a positive control:

| Method | Command / endpoint | Result |
|---|---|---|
| **(a) Project's own engine** — yt-dlp 2026.06.09 from `venv/bin/`, the same library `backend/youtube_scraper.py` drives | `extract_info(watch?v=<id>)` × 10 | **10/10** → `ERROR: [youtube] <id>: Private video. Sign in if you've been granted access to this video.` |
| **(a2)** same engine, channel tabs | `youtube.com/channel/UCHbj4hVEud49Sy2e9-V9gcg/videos` and `.../UChNmDWhioyD5S_08AI6cSaA/videos` | **both** → `ERROR: [youtube:tab] …: This channel does not have a videos tab` (a channel with ≥1 public upload always has one) |
| **(a3)** same engine, handles | `@cashguruguides`, `@moneymavens101` | channel objects resolve (description returned) but `entries: 0`, `channel_follower_count: None`. No `/shorts`, no `/streams` tab either. |
| **(c) oEmbed** | `youtube.com/oembed?url=…&format=json` × 10 | **10/10 → HTTP 403** |
| **control** | same oEmbed on `dQw4w9WgXcQ` (Rick Astley) | **HTTP 200**, full JSON — proves the method distinguishes public from private |

`FACT` The method that did **not** work: **WebFetch on youtube.com is useless here.** Both `watch?v=` and `@handle` fetches returned only YouTube's footer nav (the page is a JS SPA); it could neither confirm nor deny visibility. WebSearch was not needed for step 1.

`FACT` **Spillover: the history channel's first video is also 403.** `qyBqfJGwnEI` ("A Century of Travel", recorded in `vault/knowledge/channels.md` as uploaded + scheduled to publish **2026-07-11**, i.e. 18 days ago) also returns oEmbed 403. So this is not a finance-pipeline bug — it is a **project-wide publishing failure across three channels spanning ~3 weeks**.

### Why (root cause, high confidence)

`FACT` The vault's finished-video rule (`vault/CLAUDE.md`) is: *"a video is finished the moment its YouTube URL exists. Handing over the URL is the signal — nothing else is."* `tools/archive_cut.py` then copies source into `vault/videos/<slug>/src/` and **deletes the studio directory**.

`FACT` **A YouTube URL exists from the moment an upload begins — before visibility is ever set.** A private or scheduled upload has a fully-formed `youtu.be/<id>` URL.

`FACT` Grepping the publish packs (`vault/videos/*/youtube-metadata-*.md`) and `.claude/agents/fin-package.md` for `visibility|private|unlisted|public|schedul` returns **no instruction anywhere to set visibility to Public**. The only hit is an unrelated pinned-comment suggestion. The pipeline specifies title, description, tags, thumbnail and chapters — and never the one field that makes the video exist for viewers.

**Therefore:** the URL-is-done rule fires on a signal that is satisfied by an unpublished upload, `archive_cut.py` destroys the untracked studio source, and the vault records `LIVE on YouTube` — for a video nobody can open. `UNVALIDATED` (only the creator's Studio can confirm) whether each is set Private outright or Scheduled with a publish date that never fired; the distinction does not change the remedy.

---

## 1. The 10-video table

`FACT` — retrieved 2026-07-29 by yt-dlp + oEmbed as above. Runtimes/voices from `vault/index.md` + `tools/format.json`.

| # | Slug | Cut | Channel | Video ID | Public status | Views | Views/day | Title (as recorded in vault; **not** verifiable on YouTube) |
|---|---|---|---|---|---|---|---|---|
| 1 | needs-vs-wants | hi | @cashguruguides | `I9cxxhcdfg0` | **PRIVATE** (403) | **n/a — 0 public** | **0** | Har Saal ₹24,564 Chup-Chaap Gayab — Aapke Subscriptions Ka Sach |
| 2 | needs-vs-wants | en | @moneymavens101 | `4DimmIqnxSM` | **PRIVATE** (403) | **n/a — 0 public** | **0** | You Think You Spend $86 a Month on Subscriptions. It's $219. |
| 3 | 50-30-20-rule | hi | @cashguruguides | `FstXhGwOCjo` | **PRIVATE** (403) | **n/a — 0 public** | **0** | ₹30,000 Salary Kaise Manage Kare \| 50-30-20 Rule Ka India Version |
| 4 | 50-30-20-rule | en | @moneymavens101 | `-qrvQMrETn0` | **PRIVATE** (403) | **n/a — 0 public** | **0** | The 50/30/20 Budget Rule Doesn't Survive 2026 Rent (Here's the Fix) |
| 5 | emergency-fund | hi | @cashguruguides | `vZG7fkPwpzI` | **PRIVATE** (403) | **n/a — 0 public** | **0** | One Repair From Broke — Emergency Fund Explained in Haryanvi \| Start With ₹2,500 |
| 6 | emergency-fund | en | @moneymavens101 | `6dFBciWSs0o` | **PRIVATE** (403) | **n/a — 0 public** | **0** | Emergency Fund 2026: How Much, Where to Keep It, How to Start |
| 7 | good-debt-vs-bad-debt | hi | @cashguruguides | `f-doI5d0NRk` | **PRIVATE** (403) | **n/a — 0 public** | **0** | Good Debt vs Bad Debt / minimum-payment trap (₹ cut) |
| 8 | good-debt-vs-bad-debt | en | @moneymavens101 | `gC2QlQiLqhw` | **PRIVATE** (403) | **n/a — 0 public** | **0** | The Credit Card Minimum-Payment Trap ($ cut) |
| 9 | pay-yourself-first | hi | @cashguruguides | `PKU0_TeJ9_c` | **PRIVATE** (403) | **n/a — 0 public** | **0** | Pay Yourself First (₹ cut) |
| 10 | pay-yourself-first | en | @moneymavens101 | `mlvp4xZTROg` | **PRIVATE** (403) | **n/a — 0 public** | **0** | Pay Yourself First ($ cut) |

**Could NOT be retrieved (and why):** actual on-YouTube title, publish date, thumbnail, view/like/comment counts, subscriber counts — **all blocked by the private status**, for all 10. The titles above are what the *vault* claims; none is confirmed against YouTube. Subscriber count for both channels reads `None` (hidden or zero).

### 2. What the numbers say

`FACT` **There is no spread, because there is no data.** Views-per-day is 0 for all ten. Neither channel outperforms. No topic stands out. The `-hi` vs `-en` comparison, the "which topic worked" question, and the 28-day-analytics item that five milestone notes list as "owed" are all **unanswerable and will stay unanswerable until the videos are made public.**

`FACT` This is not "uniformly near-zero" — near-zero would still be a signal (impressions served, CTR measurable). **Zero distribution is a different category:** the algorithm has never been given the videos to test. Nothing about the script, design, storyboard, visuals, motion, sound or packaging has been falsified or confirmed by any audience, ever.

**Consequence for the other seven agents:** every recommendation in this research round is a **prior**, not a finding. There is no A/B evidence, no retention curve, no CTR, no "this hook worked". Any agent output phrased as "the data shows our X underperforms" is fabricating. The correct framing for all seven is: *here is the change, and here is the metric that will test it once publishing is fixed.*

`UNVALIDATED` but worth stating: the strongest argument for the sameness critique is **not** that blockframe-9 performed badly (it never performed at all) — it is the policy argument already in `vault/knowledge/niches/us-market-2026.md` and the competitive structure in §3 below.

---

## 3. Competitor benchmark (real retrieved numbers)

`FACT` **Method:** the project's own engine. 10 search queries (5 India/Hindi, 5 US/English) through `youtube.com/results?search_query=…&sp=EgIIBQ%3D%3D` (the **"this year"** filter, single-encoded — per the `&sp=` gotcha in `vault/knowledge/scraping-playbook.md`), flat extraction, 25 results each = 250 rows → **235 unique videos**. Then full detail-fetch on 24 selected small-to-mid performers. Nothing written to `library.db`.

Queries — **IN:** `personal finance hindi`, `paise kaise bachaye`, `budget kaise banaye hindi`, `emergency fund hindi`, `investing for beginners hindi`. **US:** `personal finance for beginners`, `how to budget money`, `emergency fund how much`, `50/30/20 budget rule`, `pay yourself first saving`.

### 3a. The duration finding — the single most decision-relevant number in this document

`FACT` Median views by runtime band, videos published within the last year:

| Band | India/Hindi (n=120) | | US/English (n=114) | |
|---|---:|---:|---:|---:|
| | **n** / median views | max | **n** / median views | max |
| Shorts <90s | 1 / 45 | 45 | 6 / 16 | 185 |
| **90–300s — OUR EXACT BAND** | **21 / 11** | 270,150 | **23 / 33** | 18,547 |
| 5–10 min | 33 / 2,275 | 406,293 | 34 / 21 | 785,932 |
| 10–20 min | 33 / **69,549** | 2,570,785 | 29 / **6,146** | 1,608,915 |
| 20 min+ | 32 / **140,076** | 5,834,532 | 22 / **59,114** | 4,807,035 |

`FACT` Median runtime of a finance video surfacing in these searches: **705 s (11:45) in India, 546 s (9:06) in the US.** Interquartile range IN 384–1262 s, US 296–1081 s.

`FACT` **Our runtime (~2:45–3:15, `tools/format.json` tier `short`: 60–300 s, default 165 s, `blockframe-9`, 9 lines) sits in the worst-performing band in both markets** — median 11 views (IN) and 33 views (US), i.e. a 6,300× / 1,800× gap to the 20-min band. The band is not empty (n=44) — it is populated and it is a graveyard.

`FACT` The 90–300 s outliers are instructive and are **not** our format:
- IN 270,150 — Saurabh Bhatt, *"My low budget lighting setup for youtube videos"* — a gear/setup video, off-topic bleed-in.
- IN 16,939 — *Sagar Sinha Podcast Clips*, "Emergency Fund कहाँ रखे?" — a **clip cut from a long podcast**, not a standalone short explainer.
- US 13,666–18,547 — six near-identical *Web Mind* videos, "Money manager budget tracker app kaise use kare" — **screen-recorded app tutorials** answering a literal how-do-I-use-this search.
- The genuine short *explainers* in-band — `Money Mantra Hindi` (115), `Rakesh Foji` (102), `EconoIQ` (75), `Math's ki Finance` (64), `TalkQuest` (26), `StockXCrypto` (15), `Audio Book Summary` (24) — are **exactly our format and topic** ("Emergency Fund Kya Hota Hai?", "Personal Finance for Beginners | Budget, Saving & Investing") and they all sit **double-digit**. This is the look-alike graveyard that `vault/skills/youtube_channel_skill.md:96` warns about, and **we are already in it.**

### 3b. Benchmark set — 24 detail-fetched videos

`FACT` All fields retrieved 2026-07-29 via yt-dlp detail extraction. `v/day` = views ÷ days since upload. `v/sub` = views ÷ channel subscribers (>1.0 = the video escaped its own audience — a format/packaging win rather than a channel-size effect, per `vault/workflows/video-study.md` step 3). `ch` = chapter count.

| Mkt | Channel | Title | Views | v/day | Subs | **v/sub** | Runtime | ch | Uploaded |
|---|---|---|---:|---:|---:|---:|---:|---:|---|
| IN | Neeraj joshi | How to Start Trading for Beginners | 531,068 | 1,770 | 5.12M | 0.10 | 12m37 | 0 | 2025-10-02 |
| IN | Sagar Sinha Podcast | CA Explained: क्यों नहीं बन पाते लोग Financially… | 517,608 | 3,951 | — | — | **101m40** | 13 | 2026-03-20 |
| IN | **Explained In minutes** | This ₹9000 Finance course is Free !!!! | 510,960 | **10,871** | 112k | **4.56** | 24m40 | **29** | 2026-06-12 |
| IN | warikoo | New 65-20-15 RULE for Your BUDGET | 508,373 | 1,790 | 7.09M | 0.07 | 22m04 | 0 | 2025-10-18 |
| IN | Sagar Sinha | Salary Management कैसे करें \| Scientific Method | 488,205 | 1,616 | 4.94M | 0.10 | 17m43 | 0 | 2025-09-30 |
| IN | warikoo | 30-Day Money Plan to TRANSFORM Your FINANCES | 445,477 | 1,337 | 7.09M | 0.06 | 29m05 | 0 | 2025-08-30 |
| IN | DEEPAK BAJAJ | How to Build An Emergency Fund? \| 6-Step Formula | 64,914 | 184 | 1.52M | 0.04 | 14m34 | 0 | 2025-08-12 |
| IN | **Easy Life With Monika** | घर का खर्च कैसे कम करें \| पैसे बचाने के आसान तरीके | 57,870 | 183 | **1,680** | **34.45** | 8m13 | 0 | 2025-09-16 |
| IN | Value Research Hindi | Emergency Fund — ज़रूरी क्यों और कितना होना चाहिए | 56,006 | 212 | 96.9k | 0.58 | 7m40 | 10 | 2025-11-07 |
| IN | Money Mode | Groww App Kaise Use Kare \| Intraday Trading | 4,611 | 4,611 | 286k | 0.02 | 12m28 | 0 | 2026-07-28 |
| IN | Zerodha Varsity Hindi | Why Should You Invest? (Hindi) \| For Beginners | 4,521 | 53 | 4.55k | 0.99 | 11m52 | 9 | 2026-05-05 |
| IN | Yt Ritik | Groww App Kaise Use Kare \| Intraday Trading | 3,461 | 3,461 | 669k | 0.01 | 27m56 | 0 | 2026-07-29 |
| US | Jay Shetty Podcast | 7 Money Lessons I Wish I Knew in My 20s! | 533,030 | 1,563 | 5.82M | 0.09 | 27m45 | 10 | 2025-08-22 |
| US | **Nick Invests** | The Smartest Order to Invest Your Money (Step-by-Step) | 529,482 | 1,904 | 189k | **2.80** | 19m47 | 0 | 2025-10-24 |
| US | Humphrey Yang | Never Keep Over THIS AMOUNT in Your Bank | 453,141 | 1,546 | 2.06M | 0.22 | 12m47 | 7 | 2025-10-09 |
| US | **The Frugal Rich** | 126 MEALS FOR $30? (Extreme Grocery Budget Tips) | 365,712 | 1,223 | 92.2k | **3.97** | 10m37 | 0 | 2025-10-03 |
| US | **Clever Girl Finance** | No Savings. No Investments. Here's Exactly What I'd Do | 354,330 | 1,221 | 219k | **1.62** | 17m04 | 0 | 2025-10-12 |
| US | **Nick Invests** | Do This EVERY Time You Get Paid (Payday Routine) | 350,440 | 1,274 | 189k | **1.85** | 19m21 | 0 | 2025-10-27 |
| US | The Money Guy Show | Why Your Emergency Fund Might Be Too Small | 18,547 | 53 | 690k | 0.03 | **4m05** | 0 | 2025-08-17 |
| US | Web Mind | Money manager budget tracker app kaise use kare | 18,215 | 92 | 56.8k | 0.32 | **2m28** | 0 | 2026-01-13 |
| US | life and numbers | Going Over My Budget for January | 17,498 | 84 | 84.2k | 0.21 | 26m47 | 0 | 2026-01-03 |
| US | Web Mind | Money tracker smart budget app kaise use kare | 4,648 | 28 | 56.8k | 0.08 | **2m00** | 0 | 2026-02-14 |
| US | EveryDollar | Why the 50/30/20 Budgeting Rule Doesn't Work | 4,054 | 11 | 19.3k | 0.21 | **2m20** | 0 | 2025-07-31 |
| US | Retirement 4 the Rest of Us | How Much Cash for Your Retirement Emergency Fund | 3,834 | 20 | 5.53k | 0.69 | 16m04 | 0 | 2026-01-22 |

**Small-to-mid channels that actually escaped their audience** (`v/sub` > 1.5, the real benchmark cohort):

| Channel | Subs | Views | v/sub | Runtime |
|---|---:|---:|---:|---:|
| Easy Life With Monika (IN) | **1,680** | 57,870 | **34.45** | 8m13 |
| Explained In minutes (IN) | 112k | 510,960 | 4.56 | 24m40 |
| The Frugal Rich (US) | 92.2k | 365,712 | 3.97 | 10m37 |
| Nick Invests (US) | 189k | 529,482 | 2.80 | 19m47 |
| Nick Invests (US) | 189k | 350,440 | 1.85 | 19m21 |
| Clever Girl Finance (US) | 219k | 354,330 | 1.62 | 17m04 |

`FACT` **Every one of the six is ≥ 8 minutes. The shortest breakout in the set is 8m13.** `FACT` A 1,680-sub channel pulled 57,870 views on an 8-minute Hindi household-savings video — **channel size is demonstrably not the barrier**; format and topic framing are.

`FACT` **Counter-example that proves the runtime point is not about authority:** The Money Guy Show has **690,000 subs** and its 4m05 emergency-fund video did **18,547** views (`v/sub` **0.03**) — while 1,680-sub Monika did 3× that on an 8-minute video. Short runtime underperforms *even with 400× the subscriber base*.

### 3c. Hooks — verbatim first ~14 seconds

`FACT` Retrieved as auto-caption VTT via yt-dlp (rate-limited to 3 of 6 attempts; HTTP 429).

- **Clever Girl Finance** — 354k views, 17m04, v/sub 1.62:
  > "So, let's have a real conversation. If I had to start from zero, no savings, no investments, no financial cushion, what would I do? Starting from zero, starting over can be overwhelming, but it is possible with clear intention and with a clear strategy. So, in today's video…"
- **Nick Invests** — 529k views, 19m47, v/sub 2.80:
  > "You know what drives me absolutely crazy? Watching people throw money at the stock market like they're feeding coins into a slot machine, completely ignoring the fact that they've got credit card debt charging them 22%…"
- **The Frugal Rich** — 365k views, 10m37, v/sub 3.97:
  > "All right. There's this woman named Christine who decided to feed her family of six for an entire week using x amount of dollars. I'm gonna let you guess how much money she used. 300? No. How about 100? Not even. She decided to only use $30 to feed her whole family for an…"

`FACT` **All three top-performing hooks are first-person and personality-led** — an opinion ("drives me absolutely crazy"), a personal hypothetical ("if I *had* to start from zero… what would *I* do"), or a named-character story with a direct guessing game aimed at the viewer. None opens with a definition, a statistic, or a neutral third-person framing.

`FACT` **This collides head-on with a binding rule already in the vault.** `vault/knowledge/niches/us-market-2026.md` §"What this means" rule 1: *"**No host persona, ever.** Never a named/implied AI presenter, never first-person expertise ('I recommend', 'my advice'). Narrate cited sources."* That rule is correctly derived from Google's AI-Personas policy — and it forecloses the exact hook style that the three highest `v/sub` videos in this benchmark all use.

`UNVALIDATED` The likely resolution is that the policy prohibits a *synthetic expert persona giving advice*, not narrative voice as such: a story about a named third party (The Frugal Rich's "a woman named Christine"), a second-person address ("if you had to start from zero"), or a stated-emotion cold open about a *cited* fact may all be reachable without a first-person advisory persona. **This needs an explicit ruling before the script agent writes to it** — it is the sharpest unresolved tension in the whole project.

### 3d. Format observations across the benchmark set

- `FACT` **Chapters are rare, not universal:** 18 of 24 have zero chapters, including 5 of the 6 breakouts. Chapters are not a traction lever in this data.
- `FACT` **The faceless + synthetic-voice cohort is essentially absent from the traction set.** In 235 unique videos, the recognisable faceless/templated cluster is *Web Mind* (six near-duplicate app-tutorial videos, 4.6k–18.2k views, `v/sub` 0.08–0.32) — surviving on literal how-to search intent, not on browse/suggested. Every high-`v/sub` breakout in the set is a presenter-led or narrated-personality channel. `UNVALIDATED` whether a well-made faceless finance explainer *could* break out — this sample contains no positive example, which is evidence of difficulty but not proof of impossibility.
- `FACT` **Long-form is where the money is in both markets**, and India skews longer than the US (median 705 s vs 546 s; IN 20m+ median 140k views).
- `FACT` **Our format's specced constraints, from `tools/format.json`:** `photo_free_scene_ratio: 0.0` (every scene has an image), `max_static_hold_seconds: 2.0`, `max_simultaneous_elements: 6`, tier `short` = 9 lines / `blockframe-9`. `vault/knowledge/design-finance-blockframe.md:163`: *"**No SFX.** The finance format is voice + motion only."* No music, no SFX, no logo — confirmed in spec, not just assumed.

### 3e. A note on web sources for this niche

`FACT` A WebSearch for faceless AI finance channels returned, as its top hits, `faceless.my`, `reap.video`, `aimagicx.com`, `overseeros.com`, `autoadify.com`, `passiveyieldlab.com`, `videoai.me` — including a specific claim of *"50,000 subscribers, 500,000 monthly views, $3,000–5,000/month AdSense at 12 months"* with no dashboard behind it. `vault/knowledge/niches/us-market-2026.md` §"Rule zero: the CPM tables are fiction" **names `faceless.my` explicitly** among the sources whose economics claims were refuted 0–3 across 206 research agents. **Rule zero holds; I reproduced the fiction and am not citing it.** No number from that search is used anywhere in this document.

---

## 4. Direct answer — what separates a finance explainer that gets traction from one that does not?

**Verified (`FACT`, from the 235-video sample):**
1. **Runtime above ~8 minutes.** Every breakout in the benchmark is ≥8m13; the 90–300 s band medians 11 (IN) / 33 (US) views. This is the strongest, cleanest signal in the data, it holds in both markets, and it holds *across* channel size (690k-sub Money Guy's 4-minute video lost to a 1,680-sub channel's 8-minute one).
2. **Channel size is not the gate.** A 1,680-sub channel did 57,870 views (34.45×). Small channels break out in this niche routinely.
3. **The short-explainer lane is actively crowded with look-alikes at double-digit views** — competitors publishing our exact topic at our exact length are visible and dead. We are not early to an empty lane; we are late to a saturated dead one.
4. **First-person, opinion- or story-led hooks** on all three top-`v/sub` videos whose captions I could retrieve. Zero definition-first openers among them.
5. **Chapters are not a lever** (5 of 6 breakouts have none).

**Inferred (`UNVALIDATED`):**
6. Longer runtime probably wins because it signals *sufficiency* — a 3-minute answer to "how much emergency fund do I need" reads as a summary of what the viewer already half-knows, while a 12-minute one promises the whole decision. `FACT`-adjacent support: the highest-`v/day` video in the set (Explained In minutes, 10,871/day) is 24m40 with 29 chapters — maximal thoroughness, explicitly signposted.
7. The winning axis is likely **specificity of situation** ("₹30,000 salary", "family of six for $30", "the smartest *order*") over **definition of concept** ("what is an emergency fund"). Our slugs are concept-shaped; the breakouts are situation-shaped.
8. Faceless + synthetic voice is probably a real handicap in this specific niche (money advice leans on trust), but the sample contains no counterexample either way. It should be treated as a hypothesis, not a verdict.

---

## 5. The owed scrape

`FACT` **Still true, and worse than recorded.** `library.db` (1,208,320 bytes, mtime **2026-07-07**) holds **1,124 rows** across a single `videos` table, spanning **22 keywords** — every one an AI-tools or cinematic-history lane (`Claude Code tutorial`, `history documentary`, `ancient egypt documentary`, `HyperFrames HeyGen`, `make faceless videos AI`, …). `last_seen` range **2026-07-01 → 2026-07-07**.

`FACT` **Zero finance rows at any threshold** — not just zero at ≥100 views / ≥240 s. There is no finance keyword in the DB at all. `FACT` None of our own 10 video IDs is present either.

`FACT` This is exactly why `backend/study.py` returned *"No usable videos in the library"* for `pay yourself first` / `paycheck` / `save money` during the pay-yourself-first run — logged in `vault/videos/pay-yourself-first/youtube-metadata-en.md`, which then had to fall back to reused 2026-07-27 evidence. The gap has been silently degrading publish packs for at least three videos.

**Could existing tooling fill it? Yes — nothing needs to be built.** `FACT` The engine already does this: `backend/youtube_scraper.py` `run_scrape()` takes search URLs, pulls full detail (views, likes, comments, duration, upload date, subscriber count, tags, category, language, channel description) and upserts into `library.db` one row per `video_id`, refreshing rather than duplicating on re-see, with automatic top-up paging when >50% of a batch is already known. `./run.sh` drives it from the TUI's Scrape screen.

**Roughly how:**
1. Run the TUI scrape with the **"This year"** upload-date filter (`SP_FILTERS["year"] = "EgIIBQ%3D%3D"`, single-encoded — do **not** "fix" it to the double-encoded browser form).
2. Feed ~10–16 finance keywords per lane. The 10 I used above are a working starting set and produced 235 unique videos in one pass; extend with the topic backlog (`credit-history`, `sip`, `mutual fund basics hindi`, `credit score`, `how to save money fast`, `sinking funds`, `budgeting apps`).
3. 60 results/keyword at `FETCH_FULL_VIDEO_DETAILS = True` → order of 600–1,000 rows per lane. Wall time is the constraint (a full-detail pass opens every video page; my 250-row flat pass took a few minutes, detail on 24 took similar) — expect tens of minutes to a couple of hours, and note yt-dlp **HTTP 429** rate-limiting appeared during my caption pulls, so pace it and keep `PAUSE_BETWEEN_URLS`/`PAUSE_BETWEEN_CHANNELS` at defaults.
4. Once landed, `backend/study.py "<topic>"` works for finance for the first time: it picks TOP/MID/LOW by views at ≥240 s / ≥100 views and builds the transcript + keyframe packet that `vault/workflows/video-study.md` step 2 assumes.
5. **Caveat `FACT`:** the ≥240 s comparability floor in `study.py` means the library will select **8–30-minute** competitors. Our 165–195 s cuts are below that floor — the tool has been, by construction, unable to find anything comparable to what we make. That is itself a verdict on the format.

I did **not** run this scrape: writing to `library.db` is outside my read-only scope. My 235-video pass lives in scratchpad JSON only.

---

## 6. Contradictions with what the vault currently documents

1. `FACT` **"LIVE on YouTube" is false in every instance.** `vault/knowledge/channels.md` §D and §E list all 10 as `live · archived`; five milestone-note `summary:` lines say `LIVE on YouTube`; `vault/index.md` says `UPLOADED + ARCHIVED`. All 10 are private. `vault/videos/needs-vs-wants/index.md:55` — *"**State: LIVE on YouTube (both cuts)**"* — is contradicted by oEmbed 403 and yt-dlp `Private video`.
2. `FACT` **The finished-video rule's core premise is unsound as written.** `vault/CLAUDE.md`: *"a video is finished the moment its YouTube URL exists… Handing over the URL is the signal — nothing else is."* A URL exists before publication. The rule then triggers `archive_cut.py`, which **deletes source that no git tracks** (`studio/` is gitignored and its own repo — `vault/CLAUDE.md` and the post-delivery-cleanup memory both stress this). Five pairs of source have been destroyed on a false completion signal. The rule needs a public-visibility check, not a URL check — and the check is cheap: `curl -o /dev/null -w "%{http_code}" "https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v=<id>&format=json"` must return **200**.
3. `FACT` **The history channel is affected too**, which `vault/knowledge/channels.md` §B does not reflect: *"✅ FIRST VIDEO DELIVERED… uploaded + scheduled to publish 2026-07-11 02:00 PKT: https://www.youtube.com/watch?v=qyBqfJGwnEI"*. 18 days past that date, oEmbed returns 403.
4. `FACT` **Both channels ship the same About description, and the US one is wrong.** `@moneymavens101` returns, verbatim and identically to `@cashguruguides`: *"Money basics that actually make sense.\n\nPaisa School breaks down personal finance for young people earning their first s…"*. A US/English/$ channel is describing itself as **"Paisa School"**. `vault/knowledge/channels.md` documents bespoke, SEO-passed About text for channels A and B but records **none** for D and E — so this was never specified and the two channels were configured as copies.
5. `FACT` **The "28-day analytics" item owed on five milestone notes can never come due.** It is listed as pending work on needs-vs-wants, 50-30-20-rule, emergency-fund, good-debt-vs-bad-debt and pay-yourself-first. Private videos accrue no analytics; the 28-day clock has not started on any of them.
6. `FACT` **The vault's own sameness escalation was directionally right but under-argued.** `vault/index.md` carries a *"⛔ HARD sameness flag — 5th consecutive blockframe-9 on BOTH channels; the next cut MUST change architecture."* The benchmark now supplies the missing evidence — but reframes it: the binding problem is **not** that the 9-block architecture repeats, it is that **the 165–195 s tier it belongs to is the lowest-performing runtime band in both markets**. Changing architecture *within* the `short` tier would leave the primary defect untouched.
7. `FACT` **A pre-existing asset-reuse defect is recorded and unfixed:** `vault/knowledge/design-finance-blockframe.md:259` — one `s9.jpg` is *"byte-identical in three shipped projects across **both** channels"* because Pixabay's top hit is deterministic. The prescribed fix (md5-keyed asset ledger refusing a reused hash) is written down but there is no evidence it was implemented. Cross-channel identical imagery is precisely the mass-production pattern that `us-market-2026.md` identifies as the live channel-level enforcement exposure.

---

## 7. What the other seven agents should be told

- `FACT` **Nothing has been tested.** No recommendation this round can cite audience response. Every agent's output is a prior with a proposed test, not a finding.
- `FACT` **Fix publishing before anything else.** Until visibility is Public, every other change has zero measurable effect. This is a Studio toggle, not a production change — the cheapest fix in the project and the precondition for all the rest.
- `FACT` **Runtime is the highest-leverage single variable in the retrieved data**, and it is a *tier* change (`tools/format.json` already defines `medium` = 510 s and `long` = 600 s+ with a `per-line-chapters` architecture and a working reference implementation at `studio/videos/firaun-ka-anjaam/build.py`). The lever exists in the codebase and is unused for finance.
- `UNVALIDATED` **The persona question must be ruled on before scripting.** Winning hooks are first-person; the vault's policy rule forbids first-person. Someone has to decide where narrative voice ends and prohibited advisory persona begins.
- `FACT` **The comparable-video library is empty for finance and the tooling to fill it already works.** Any agent claiming a competitor pattern without either running that scrape or citing this document's 235-video pass is guessing.
