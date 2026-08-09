---
summary: Live YouTube scrape (1,881 videos, last-30-days uploads, 2026-07-31) picking the next 5 finance topics — **revised 2026-08-07 by a vidIQ re-check: topic #3 (saved-by-age) demoted, two replacements added; see the revision section** for @cashguruguides (₹) + @moneymavens101 ($). Ranked by views-per-subscriber, not raw views — the small-channel breakouts are the winnable ones.
updated: 2026-08-07
source: yt-dlp scrape via backend/youtube_scraper.py, 50 keywords × month filter, rows in ../../../library.db (first_seen 2026-07-31); 70-video full-detail pass for subscriber counts + exact upload dates.
stage: ADOPTED — niche research; figures carry their own dates
---

# Next 5 finance topics — evidence (2026-07-31)

## Method
50 keywords (India-Hindi + US-English), YouTube "past month" upload filter,
40 results each → **1,881 videos** into `library.db`. Shorts and off-topic drift
(gaming/vlogs, which YouTube search injects heavily) filtered out. The top 70
finance videos ≥30k views got a full-detail pass for **subscriber count**, so the
ranking metric is **V/S = views ÷ subscribers** — raw views just re-find the
mega-channels we cannot outrank.

## The load-bearing finding
`Story of Success` (UCQN6lI4Qx1YyifwoYfyazQQ) is a **4,660-subscriber faceless
Hindi channel** with four breakouts in 90 days:

| Views | V/S | Len | Title |
|---|---|---|---|
| 226,845 | 48× | 21:50 | पहला ₹1 लाख कैसे जोड़े \| Japan का Money Secret |
| 140,473 | 30× | 19:22 | 1 साल में 1 लाख — Japan + 50/30/20 |
| 131,089 | 28× | 16:37 | Emergency Fund कैसे बनाएं जापानी तरीके से |
| 73,776 | 16× | 17:24 | पैसा बचाने के ये 3 जापानी तरीके \| जापानी लोग गरीब क्यों नहीं होते? |

Same channel's 3–6 min uploads on the same themes: **237–3,353 views**. Format and
topic held constant, only length changed. ⚠️ **Length caveat:** every breakout in
this niche this month sat at **15–22 min**, not 8–10. Our 8–10 min format is a
constraint we chose, not one the data endorses — worth a deliberate test.

## The five (each proven in BOTH markets)

1. **The first ₹1 lakh / first $1,000 is the hardest**
   ₹: 226,845 @ 48× subs (above) + 140,473 @ 30×. $: Nischa "first $20k in July
   2026" 306,463; Mark Tilbury "If I Started Investing in 2026" 233,125.
   Also the missing rung in our own ladder — the six shipped videos are all
   *defense* (budget, emergency, debt); this is the first *offense* one.

2. **Japanese money methods — why Japanese people don't go broke** (Kakeibo)
   ₹: 73,776 @ **15.8× subs — the single highest V/S in the whole 1,881-video
   pull**; same channel's Japanese-method emergency-fund cut did 131,089 @ 28×.
   Evergreen, faceless-native, and Kakeibo already has US personal-finance
   recognition for the $ cut. 3–4 methods = a natural chapter structure.

3. **"Am I behind?" — how much you should have saved by age**
   $: Money Guy Clips 65,915 @ **6.6× subs** (10k-sub channel, 10:01); Humphrey
   Yang "Average 401K Balance By Age – 2026" 237,440; Erin Talks Money 108,662 +
   70,215; Invest With Queenie 88,595 @ 1.03×.
   ₹: `retirement ke liye kitna paisa chahiye india` p90 = 115,400; "Why You Need
   ₹12 Crores to Retire" 167,818.
   Pure stat-card content — the blockframe design's strongest form.

4. **Why a good salary still leaves you broke — the affordability math**
   $: A Homestead Journey "Americans Are Posting Their Paychecks" 1,221,431 @
   **4.7× subs**; CNN "Why more Americans will never buy a home" 252,700;
   "Vanishing Middle Class" 175,731; MS NOW affordability crisis 113,558.
   ₹: Raj Shamani "End Of Middle Class Dreams & Loan Trap" 1,146,147; StudyIQ
   "Double Income, Record Debt: Middle Class का कड़वा सच" 115,648; Sagar Sinha
   "पैसे को इन 6 Assets में रखना सीखो, Bank में नहीं" 1,032,343.
   The hottest *emotional* cluster in both markets right now, and structural
   (wage vs rent/grocery math) rather than a news event, so it does not decay.

5. **Gold — what you actually get back when you sell**
   Evergreen anchor: Zero1 by Zerodha "Reality of Buying GOLD Jewellery in
   INDIA!" 227,942 (making charges + GST + resale purity loss — a permanent
   truth). Riding a live 2026 gold/silver drawdown confirmed by six independent
   channels in 30 days: FinnovationZ "Will Gold Crash to 1 Lac" 237,679; Silver
   Dragons 217,611; 24 News HD 255,383; "Gold Down 26%, Silver Down 50%" 89,123;
   Abhishek Kar ×3 (98,731 / 72,161 / 61,030); Vijay Vikram Singh 58,857.
   **Do not make a price call** — that expires. The cost-of-ownership angle is
   evergreen and rides the attention.

## Revision 2026-08-07 — vidIQ re-check: #3 DEMOTED, two replacements

Ran R1 (`vault/knowledge/vidiq-mcp.md`) on the live vidIQ index, 20 credits:
`outliers` hi + en (`contentType:'long'`, `publishedWithin:'threeMonths'`,
subs 1,000–500,000, limit 50) and `keyword_research`
(`research` "retirement savings by age" country US · `country_search broad`
"savings money" and "passive income investment" country IN).

**#3 "Am I behind — saved by age" is demoted.** It fails the both-markets bar
this note itself set:
- **Search demand is thin and old.** `retirement savings by age` = **9,144/mo
  global**, competition 55, and **no reportable US in-country volume**; the age
  anchors that do carry volume are **60** (5,142) and **65** (4,364) — a
  pre-retiree audience, not our 25–40 budgeter. Parent lane for comparison:
  `retirement planning` 510,917 global / 102,183 US.
- **No ₹ pair exists.** The India semantic expansion of "savings money" returns
  `personal finance` 303,719 · `how to save money` 20,480 · `money saving tips`
  20,331 · `how to save money fast` 15,497 — **no age or retirement keyword at
  any volume**, and no Hindi outlier in 3 months is about savings-by-age.
- **The lane is owned by advisors.** Every "how much do you need" breakout in
  the en pull is a CFP/wealth-management channel serving 55+ (Cody Gunn 27.3k
  subs→213,440; Holy Schmidt 321,636; James Shack ×2). The only by-age breakout
  is country-specific and modest (Invest With Queenie AU, 86.3k→111,563 = 1.3×).

**Replacement A — the passive-income number ("how much invested to live off
it"). ← CREATOR PICK 2026-08-07, this is topic #9.** The strongest *replicable* pattern in the pull: one title cloned per
country by small channels, every clone a breakout — Singapore Finance With Jim
5,560→106,210 (**19×**), Kab Invests 1,870→26,488 (14×), Aussie Finance With
Luke 24,900→292,989 (11.8×), Dark Ledger 24,600→231,862 (9.4×), Effortless
Investor UK 3,070→26,414 (8.6×), Canadian Finance with David 9,190→68,235
(7.4×). All 8–15 min, pure stat-card math = blockframe's strongest form.
⚠️ **The ₹ cut must not say "dividends"** — India volume for `dividends` 2,531 ·
`live off dividends` 2,907 · `dividend investing` 2,807. Frame it as passive
income / financial freedom: `financial freedom` **92,825** · `passive income`
**46,094** · `passive income ideas` 34,152 · `how to get rich` 47,293. Hindi
format proof: Varsha Saini 2,000 subs→37,497 (**18.7×**) on SIP compounding.

**Replacement B — the one-rule savings mechanic.** Biggest single small-channel
breakout in the en pull: William Explains Money 14,200→**396,692 (28×**,
breakout 1046, 891 s) "The $50 Rule That Quietly Builds a Year of Savings".
₹ side is the same shape and has the volume: `how to save money` 20,480 ·
`money saving tips` 20,331 · `how to save money fast` 15,497; Hindi outliers
WealthNama 5,920→37,531 (6.3×, "ये 8 Money Rules"), sandhya and anayra
14,600→90,720 (6.2×, "10 फालतू खर्चे बंद किए"), Ali Wealth 34,100→49,360
("30 Day Money Saving Challenge"). Lower ceiling than A and it would be our
**seventh defense video** — that is the argument against it, not the data.

**Hindi lane note (do not chase blind):** the top Hindi V/S in the pull is not
personal finance at all — low-investment *business ideas* (Diksha Lodhi
3,090→163,089 = **52.7×**; Eternal Stories 7,760→100,868 = 12.9×) and
Chanakya/Osho money wisdom (Moun shakti 6,450→160,601 = 24.8×). Different
channel promise from @cashguruguides; logged as evidence, not as a topic.

**Length:** the winners here run **9–15 min**, not the 15–22 min the 2026-07-31
pull found. LONG tier as shipped on japanese-money-methods is fine.

## Deliberately rejected (do not re-test blind)
- **ITR filing 2026-27** — biggest raw cluster in the pull (~1.5M views across
  15+ videos, MyOnlineCA/MySimpleGuide/Labour Law Advisor). Rejected: it is a
  screen-recording tutorial our faceless narrative pipeline cannot produce,
  India-only with no $ pair, and tied to the July filing deadline.
- **EPFO 3.0 / PF withdrawal** — 265,739 + 210,662 + 132,353 + 109,756. Same
  screen-tutorial problem; the $ pair (`401k early withdrawal penalty`) returned a
  median of **8 views**, i.e. no demand.
- **"Budget-nerd" US keywords** — `sinking funds`, `cash stuffing`,
  `no spend challenge`, `roth ira for beginners`, `financial mistakes in your 20s`
  all returned medians of 5–2,000 views. Saturated by small creators; no oxygen.

Related: [[india-finance-market]] · [[us-market-2026]] · [[../channels]]
