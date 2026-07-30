---
summary: Live YouTube scrape (1,881 videos, last-30-days uploads, 2026-07-31) picking the next 5 finance topics for @cashguruguides (₹) + @moneymavens101 ($). Ranked by views-per-subscriber, not raw views — the small-channel breakouts are the winnable ones.
updated: 2026-07-31
source: yt-dlp scrape via backend/youtube_scraper.py, 50 keywords × month filter, rows in ../../../library.db (first_seen 2026-07-31); 70-video full-detail pass for subscriber counts + exact upload dates.
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
