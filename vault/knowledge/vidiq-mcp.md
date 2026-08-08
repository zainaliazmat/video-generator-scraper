---
summary: What the vidIQ MCP is worth to this channel — the live-data lane the vault never had, and the one hole it genuinely fills (post-publish retention). Also the constraint that shapes every use of it: 150 credits a month = 30 paid calls. Mechanics live in the skill, not here.
updated: 2026-08-06
source: vidiq.com/claude + full schema read of the analytical tool set + live balance/user_channels calls, 2026-08-06
stage: adopted — measurement only, generation family rejected
---

# The vidIQ MCP — the live lane

Registered project-scope in `.mcp.json` (`https://mcp.vidiq.com/mcp?src=claude`,
`Bearer ${VIDIQ_API_KEY}`). **How to call it is `.claude/skills/vidiq/SKILL.md`** —
costs, filters, traps, six priced recipes. This note is only what it is *worth*.

## Account state (2026-08-06)

Free tier: **150 renewable credits/month** (resets the 29th) + a 40-credit
non-renewing add-on. Most calls cost 5, so the real budget is **30 paid calls a
month**. That number, not the tool list, is what determines how this gets used.

⚠️ **Only @moneymavens101 (`UChNmDWhioyD5S_08AI6cSaA`, the US/$ channel) is
authorized.** @cashguruguides is not connected, so the owned-channel tools —
`channel_analytics` (retention, traffic sources) and `subscriber_insights`
(best time to post) — work for the **-en cuts only** until the creator
authorizes the second channel. Everything else works on any public channel.

**First real run: japanese-money-methods packaging, 2026-08-06, 80 credits.**
Hindi title **84 → 94**, English **80 → 84**, both tag blocks rebuilt on volume
data, both descriptions re-led. Full write-ups in
[[../videos/japanese-money-methods/youtube-metadata-hi]] and
[[../videos/japanese-money-methods/youtube-metadata-en]]; the reusable method
went into the skill as recipes R3/R3b/R4.

## What it adds that the vault did not have

| Existing lane | What vidIQ adds |
|---|---|
| `backend/study.py` + `library.db` — a scrape, archived, point-in-time | Live breakout data across 135M channels, filterable by *title language* and subscriber band, so a small-channel format win is separable from a big-channel view count |
| YouTube autocomplete checks in `fin-package` — proves a phrase is *typed* | Search **volume and competition per country**, so we learn whether a typed phrase is typed by ten people or ten thousand |
| Title candidates argued from `long_form_scripting` | A CTR score per candidate. Ship only when score and autocomplete agree — a high score on a phrase nobody types is exactly the failure `videos/first-lakh-first-thousand/youtube-metadata-hi` documented |

**Autocomplete proves a phrase is *typed*; vidIQ says *how often*.** That is the
whole relationship, and the 2026-08-06 run showed it cuts both ways. Autocomplete
had verified all twenty Hindi tags — and every one of them sat inside `kakeibo`,
a **3,507-searches/month** term in India, with the market's real volume
(`personal finance` 303,719, `money management` 51,885) entirely unreached.
It also missed `japanese money habits` outright — on topic, **31,899/month, 4×
the phrase in the English title** — because no seed produced it and a
completion-only method cannot surface a phrase nobody thought to type.
Neither source replaces the other; a pack that carries only one is half-blind.

**The hole it actually closes: post-publish analytics.** Nearly every video note
in [[index]] carries "owed: analytics after 28 days" and nothing in the repo
could ever pay it. `channel_analytics` on our own channel returns the 100-point
**audience-retention curve**, traffic sources, and geography. Where the curve
falls is where the script failed — that is the first feedback loop this pipeline
has ever had from a shipped video back into [[skills/long_form_scripting]].
Two videos are already live and waiting for it: `credit-history`
(`j_YM-im4qz4` · `yoN-gAATN6Y`).

## Decisions

1. **Measurement only.** The generation family (`generate_video`,
   `generate_script`, `generate_thumbnail`, `voiceover_generate`,
   `generate_music`, `motion_graphics`, `compose`, …) is **not used.** The
   pipeline owns production end-to-end and
   [[design-finance-blockframe]] §0 is a code-enforced architecture lock a
   generated asset cannot satisfy. Secondary reason: 22–25 credits each is most
   of a topic-selection pass. Generic AI video is the crowd we are trying to
   leave, not join.
2. **No `fin-*` agent calls it during a run.** Same conclusion as
   [[claude-design-mcp]], for a different reason: the agents have no credit
   budget to reason about and a mid-run 402 would fail a stage. vidIQ is used
   *around* `/finance-video` — topic selection before, autopsy after — by the
   orchestrating session, which can read `vidiq_balance` first.
3. **Nothing it returns is a fact.** Volumes, RPMs and
   `video_earnings_estimate` are models with a date on them.
   [[niches/us-market-2026]] already records the cost of treating guessed CPMs
   as evidence. Findings go into the right vault note dated and with the tool +
   params that produced them; raw JSON goes nowhere.
4. **Read-only against YouTube.** The only write verb is
   `update_competitors`, which edits our own watchlist. It cannot upload or
   retitle anything, so it needs no ship-gate.

## The trap worth naming here

Every geo parameter in the API means **where the channel is registered** — not
the audience, not the language. `channelCountry: 'IN'` returns Indian channels
publishing in English, which is a different market from the one
[[niches/india-finance-market]] describes. The Hindi cut's data comes from
`language: 'hi'` (+ `contentType: 'long'`, which non-English requires). Getting
this backwards produces a confident, well-sourced, wrong topic pick.
