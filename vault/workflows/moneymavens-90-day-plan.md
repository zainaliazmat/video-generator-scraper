---
summary: The Money Mavens per-video production checklist and the 90-day launch plan — publishing rhythm, the four KPI gates (day 14/30/60/90) with hard thresholds, the US-watch-time remediation ladder, kill criteria, and the standing weekly/monthly/January verification tasks.
updated: 2026-08-15
source: creator plan `04-production-checklist-and-90-day-plan.md` (2026-08-15). Baselines came from live vidIQ pulls in that session — subscriber_insights returned an empty activity histogram, geography returned [NO DATA].
stage: ADOPTED — the launch plan; gates are binding, thresholds are not renegotiable after the fact
---

# Money Mavens — production checklist + 90-day plan

Slate and topic order: [[../knowledge/niches/moneymavens-launch-slate]].
Evidence bar: [[../knowledge/fact-integrity]]. Register: [[../knowledge/us-english-script-style]].

## Part A — per-video checklist

Nothing moves to the next stage until the stage above is fully checked. The `/finance-video`
stage machine owns most of this; the boxes below are the human-visible contract.

**1 · Research** — video note in `vault/videos/<slug>/` with the slate row filled in ·
target keyword + US volume recorded from `vidiq_keyword_research` · every figure the script
needs has a source note in `vault/sources/` · every source on the whitelist · every source
note carries `as-of`, `expires`, `expiry-class` · screenshot captured to
`vault/screenshots/` and linked · claim notes created and linked · `us-specific-angle`
written in one sentence.

**2 · Script** — `fin-script` run against the vault · no `MISSING SOURCE:` returned ·
hook under 25 words with no greeting · one idea per section · CTA names one physical
action doable today in under five minutes · read aloud once at speed, anything you stumble
over gets rewritten.

**3 · Fact gate — hard blocker** — all ten points of [[../knowledge/fact-integrity]] §8 ·
every claim tagged verified/estimate/opinion in script AND on screen · disclaimer in all
four places · `fact-gate-passed: true` written into the video note.

**4 · Title & thumbnail scoring** — `vidiq_generate_titles` run **with the finished script
summary as the `description`** · winner through `vidiq_score_title`, record the real number ·
**score ≥ 75, no rounding up, no proceeding below it** · title verified against the script
(promises nothing the video does not deliver) · thumbnail is one object, one red element,
2–4 words, no emoji · `vidiq_score_thumbnail` run and recorded · `title-score` +
`title-scored-on` written into the video note.

**5 · Render** — voiceover generated · every screenshot-the-source moment held 3+ s ·
every figure carries a visible source lower-third with as-of date · audio levels consistent ·
**full watch-through at 1×, not scrubbed.**

**6 · Publish** — title, description, tags, chapters set · sources block in the description
matches `sources.md` exactly · disclaimer above the fold · thumbnail checked at mobile size ·
end screen and cards point to the paired video (search ↔ browse) · pinned comment where the
topic requires it · `status: published`, `publish-date`, `youtube-id` written into the note.

**7 · 48-hour review** — `vidiq_video_stats` pulled · impressions, CTR, average view
duration and average view percentage recorded · **retention curve checked for the first 30
seconds specifically** · comments read, recurring questions captured for E6 · compared
against the running channel median · one line written in the video note: *what this video
taught you that the last one didn't* · `status: reviewed`.

## Part B — the 90-day plan

**Start:** the day S1 publishes. **Cadence:** 3/week ⇒ ~36 videos across 90 days. The
slate covers weeks 1–10; weeks 11–13 come from what the data says by then.

⚠️ **Only the first 10 are committed** (creator, 2026-08-15). Ship them, read the response,
then decide whether to continue as written or change.

### Publishing rhythm

- **Mon / Wed / Fri.** Fixed days beat optimal days when there is no audience-timing data —
  and there is none: `vidiq_subscriber_insights` returned an empty activity histogram.
- Re-run `vidiq_subscriber_insights` at **day 30**; once it returns real data, move to the
  strongest three-hour windows it reports.
- Alternate search / browse per the slate. **Never two browse videos back to back in the
  first month.**

### KPI gates — one metric, one threshold, no renegotiating after the fact

**Day 14 — gate 1: does geography resolve?**
`vidiq_channel_analytics audience_geography` must return **any non-empty row set**.
Geography is currently `[NO DATA]` because total views sit under YouTube's disclosure floor.
**Pass** → record the US share; it is the baseline for gates 2–4.
**Fail** → still under the floor. **Do not change strategy — six videos is not a signal.**
Continue to day 30 and re-check.

**Day 30 — gate 2: search traffic exists**

| Metric | Threshold |
|---|---|
| Views from `YT_SEARCH` across all videos | ≥ 100 |
| US share of watch time | ≥ 50% |
| Median views per video (last 9) | ≥ 25 |

Search retention is already 90.8% — the traffic converts when it arrives. This gate asks
only whether it arrives at all.
**Fail on search only** → titles are not matching queries. Retitle the three
lowest-impression search videos via `vidiq_generate_titles` seeded with the exact target
keyword. **Do not touch the browse videos.**
**Fail on US share** → work the remediation ladder below.

**Day 60 — gate 3: the floor is compounding**

| Metric | Threshold |
|---|---|
| Median views per video (last 12) | ≥ 100 |
| US share of watch time | ≥ 65% |
| Average view percentage, channel-wide | ≥ 40% |
| Subscribers | ≥ 50 |

100 median views puts the channel inside its peer band — seven of the fourteen US channels
mapped in the teardown average under 1,000 views/video, and the bottom of that band sits
near 105.
**Fail on views but retention holds** → packaging, not content. Two weeks on titles and
thumbnails only. **Do not change topics.**
**Fail on retention (<40%)** → content. Run **E5** (the 3-minute cut) immediately rather
than waiting for week 10.

**Day 90 — gate 4: is this working?**

| Metric | Threshold |
|---|---|
| Median views per video (last 12) | ≥ 300 |
| US share of watch time | ≥ 70% |
| Best single video | ≥ 2,000 views |
| Subscribers | ≥ 250 |
| Watch hours toward monetization | ≥ 400 |

**Pass on 3 of 5** → the sub-niche works. Commit another 90 days, build topic clusters
around whatever produced the best single video.
**Pass on fewer than 3** → kill criteria.

### If US watch-time share doesn't move

**One change at a time, two weeks apart.** Changing two things at once means you learn nothing.

1. **Check the obvious.** Channel country = United States and default language = English
   (United States) in YouTube Studio. A misconfigured setting suppresses US distribution on its own.
2. **Audit the voiceover.** A non-American accent or cadence is the most common cause of a
   US-targeted channel drawing non-US viewers. Listen to 60 s of ours against 60 s of a US
   competitor. If it does not match, change the voice before anything else.
3. **Sharpen geographic specificity in TITLES** — "Social Security", "Medicare", "IRS",
   "FDIC" in the title itself, not just the script. These words are geographic filters.
4. **Check what the traffic is.** If most non-US traffic arrives via `RELATED_VIDEO`,
   YouTube is pairing us with the wrong channels; three tightly-focused search videos on one
   keyword cluster is the fastest way to re-anchor those associations.
5. **Still below 50% at day 60 after all four** → the problem is upstream of content. Stop
   producing, diagnose for one week, then resume.

### Kill criteria

Kill only if **all four** are true at day 90:
1. Median views/video under **50** across the last 12
2. US watch-time share under **40%** after all five remediation steps
3. Channel-wide average view percentage under **30%** — even arrivals do not stay
4. No single video has cleared **500 views**

**If all four:** the audience is not reachable with this format from this channel. **Do not
pivot the sub-niche again on the same channel** — that would be two audience changes on one
algorithmic identity, and the second carries a contamination cost the first did not.

**If only some are true, the diagnosis is specific:**

| Pattern | Diagnosis | Action |
|---|---|---|
| Low views, high retention | Packaging | Titles and thumbnails only, 30 days |
| High views, low retention | Content or format | Test E5 (3-min) and E1 (screenshot-led) |
| Views fine, US share low | Distribution / signal | The five-step ladder above |
| Everything flat | Too early | 36 videos is a small sample; extend 30 days |

## Standing verification tasks

**Every Monday** — run the expiring-stats and unverified-claims queries in
[[../dashboard]]; fix anything inside 30 days; confirm nothing unverified is queued.

**First Monday of each month** — run the published-with-expired-figure query. Anything that
appears gets a pinned-comment correction the same week, per
[[../knowledge/fact-integrity]] §7. Re-verify every `monthly`-class figure.

**Every January** — re-verify every `annual`-class figure (IRS brackets and limits, SSA COLA
and wage base, Medicare premiums and IRMAA brackets, earnings-test limit) and re-check every
evergreen video that cites one.
