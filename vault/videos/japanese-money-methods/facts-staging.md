---
summary: Staged money facts for japanese-money-methods (long, hi+en). Resolves the fin-research debt on "Japan saves 37% vs India 4-8%" — the 37 is REAL but is a narrow survey measure; Japan's national-accounts household saving rate was 1.1% in 2024. Nothing here is promoted to shared knowledge until the render passes.
updated: 2026-08-01
source: Horioka NBER WP 33181 (rev. Jan 2026, read direct); Statistics Bureau of Japan FIES 2024 annual summary (read direct); Bank of Japan Flow of Funds Japan/US/Euro overview (read direct); BEA Personal Income & Outlays June 2026; RBI Annual Report 2025 via Business Standard; Fujin no Tomo Sha (publisher primary); vault/knowledge/money-facts-2026.md
stage: fin-facts attempt 1 — STAGING ONLY, do not merge into money-facts-2026.md
---

# facts-staging — japanese-money-methods

**Write rule:** this file only. `vault/knowledge/money-facts-2026.md` and
`subscription-economics-2026.md` were READ, not written. The orchestrator
promotes HARD rows after the render passes.

---

## 0. The hero numbers

| Cut | Hero | Source line |
|---|---|---|
| **hi (₹)** | Japan's own government publishes **two** household saving rates for 2024: **37.8%** (Family Income & Expenditure Survey, salaried-worker households) and **1.1%** (National Accounts, everybody). The viral "Japan saves 37%" is the first one. | Statistics Bureau of Japan, *Kakei Chōsa* 2024 annual summary, Table I-2-2 (黒字率 37.8%) + Horioka, NBER WP 33181, p.7 |
| **hi (₹) anchor** | Regular wage/salaried Indian average monthly earnings **₹24,217 men / ₹18,353 women**; worked example **₹30,000/mo in-hand** | PLFS Annual Report 2025 (PIB) — already HARD in [[../../knowledge/money-facts-2026]] |
| **en ($)** | Japanese households hold **51.0%** of their financial assets in cash and deposits; US households hold **11.5%**, and **41.5%** in equity — one table, one date, no conversion | Bank of Japan, *Flow of Funds — Overview of Japan, the United States, and the Euro area*, 29 Aug 2025, Chart 2, data as of end-March 2025 |
| **en ($) anchor** | US personal saving rate **2.7% (June 2026)**; worked example **$4,000/mo take-home** | BEA Personal Income & Outlays, rel. 2026-07-30 — re-verified live today |

---

## 1. JAPAN — the debt fin-research flagged (RESOLVED)

The claim to kill: *"Japan saves 37% of salary, India 4–8%"* (TOP `fQyN80dLDpQ`, 0:54).
**Do not inherit it, and do not simply call it false — it is a real number used wrong.**

| # | Claim | Figure | Date | Sources | Tag |
|---|---|---|---|---|---|
| J1 | Japan household saving rate, **National Accounts (SNA)** — net household saving ÷ net household disposable income, all households | **1.1%** | calendar 2024 | (1) Horioka, Charles Yuji, *Household Saving in Japan: The Past, Present, and Future*, NBER WP 33181, Nov 2024 rev. Jan 2026, body p.2 and p.7 — https://www.nber.org/system/files/working_papers/w33181/w33181.pdf (read direct). (2) Shape corroborated by [JCER](https://www.jcer.or.jp/english/household-savings-rate-going-up-or-down) (FY2000 <10%, FY2013 −0.9%, FY2017 2.3%) and (3) [Trading Economics citing Cabinet Office](https://tradingeconomics.com/japan/personal-savings) (quarterly 0.0–3.9% through 2025) | **HARD** on the rate. ⚠ the *decimal* 1.1 is single-sourced to Horioka quoting the Cabinet Office — **say "about one percent", show `~1%`** |
| J2 | Japan household saving rate, **Family Income & Expenditure Survey (家計調査)** — 黒字率 for two-or-more-person **salaried-worker** households only | **37.8%** | calendar 2024 | (1) **Statistics Bureau of Japan / MIC, *Kakei Chōsa* 2024 annual summary, section I-2(4) and Table I-2-2** — https://www.stat.go.jp/data/kakei/2024np/pdf/summary.pdf, p.11 (read direct, Japanese primary). (2) Horioka NBER WP 33181 p.7, same figure | **HARD** — two independent, one is the issuing agency |
| J3 | Why the two differ (the whole hook) | FIES **covers only salaried-worker households**; the National Accounts "include everyone including the self-employed, the unemployed, the retired, and private unincorporated enterprises" + conceptual and measurement differences. Horioka: the FIES figure is "**more than 30 times as high**" | 2024 | Horioka NBER WP 33181 p.7 (verbatim), citing Ueda & Ohno 1993, Unayama & Yoneta 2018a/b, Unayama 2023 ch.14 | **HARD** |
| J4 | FIES 2024 salaried-worker household, monthly averages | income **¥636,155** · disposable income **¥522,569** · consumption **¥325,137** · surplus (黒字) **¥197,432** · avg propensity to consume **62.2%** | 2024 | Statistics Bureau, same PDF, Table I-2-2 | **HARD** |
| J5 | **Where that surplus goes** — the "they save but don't invest" beat | Of the ¥197,432 monthly surplus: net deposits **¥175,241**, net securities purchases **¥6,705**, net insurance **¥13,976**, net land/housing loan repayment **¥34,544** | 2024 | Statistics Bureau, same PDF, section I-2(4) notes 3–7 | **HARD** (raw ¥ figures) · the *ratio* (≈89% to deposits, ≈3% to securities) is **COMPUTED** — label illustrative |
| J6 | Historical peak — where the "Japan is a nation of savers" myth is actually true | **23.2%** at the mid-1970s **postwar** peak (the wartime rate reached ~44%, so "peak" without the qualifier is wrong); exceeded 15% only during the **25 years 1961–1986**; "no higher than 5% during the past two decades (since 2002)" **except the 2020 Covid spike, which Horioka carves out explicitly**; **negative** in 2013–15, 2017 and 2023 ⚠️ **corrected 2026-08-01 by fin-audit-hi** — the pre-correction wording dropped "postwar" and the Covid carve-out, and fin-script inherited both faithfully. **Promote to money-facts-2026.md in THIS corrected form only.** | 1955–2024 series | Horioka NBER WP 33181, body p.2, p.11 and Fig. 1 (read direct); corroborated by JCER ("about 23 percent" mid-1970s) and the [RIETI](https://www.rieti.go.jp/en/columns/a01_0615.html) / NBER w21555 literature | **HARD** |
| J7 | **The cultural explanation is rejected by the primary literature** | Horioka: "culture, tradition, and national character **are not a major determinant**" of Japan's household saving rate — because the rate was low or negative during much of Japanese history and *rose* from the mid-1950s to the mid-1970s. His explanations are demographic + unavailability of consumer credit, no social safety net until the 1970s, fast income growth, the Maruyū tax break (abolished 1988), state saving-promotion campaigns, and land prices | 2026 | Horioka NBER WP 33181, §3 and §9–10 (read direct) | **HARD** |
| J8 | Japanese household financial assets, composition vs the US and euro area | **Japan ¥2,195tn**: currency & deposits **51.0%**, insurance/pension 26.0%, equity 12.2%, investment trusts 6.0%, debt securities 1.4%. **US $128.8tn**: currency & deposits **11.5%**, equity **41.5%**, investment trusts 13.1%, insurance/pension 26.6%. **Euro €33.6tn**: currency & deposits 31.8% | end-March 2025 | **Bank of Japan, Research & Statistics Dept., *Flow of Funds — Overview of Japan, the United States, and the Euro area*, 29 Aug 2025, Chart 2** — https://www.boj.or.jp/en/statistics/sj/sjhiq.pdf (read direct) | **HARD** — a single table stating both markets, so this is **not** a cross-market conversion |
| J9 | Latest total (freshness check on J8) | Household financial assets **¥2,386tn** at end-March 2026 (+7.1% YoY); cash & deposits **¥1,126tn** (+0.6%); stocks ¥398tn (+28.6%, record); investment trusts ¥165tn (+25.7%) | 2026-03-31, rel. 2026-06-25 | BOJ Flow of Funds Q1 2026 preliminary via [Nippon.com/Jiji](https://www.nippon.com/en/news/yjj2026062500282/) + [Bloomberg](https://www.bloomberg.com/news/articles/2026-06-25/japan-s-household-assets-rise-to-2-386-trillion-at-end-of-march) | **SOFT** — two independent wires, BOJ primary PDF for this quarter not read. Cash share ≈47% is **COMPUTED** from the two wire figures |

### The scripting rule this produces (load-bearing)

**Do the debunk with Japan's own two numbers. Do not run a Japan-vs-India or
Japan-vs-US saving-rate head-to-head anywhere on screen.** J1 (1.1%) and India's
RBI 7.0% are *different measures* — net household saving ÷ net disposable income
vs net household **financial** savings ÷ GNDI — and putting them side by side
would repeat exactly the error this stage was sent to fix. Japan's 37.8% vs 1.1%
is internally consistent (one government, one year, two published surveys) and is
a stronger hook anyway.

The safe cross-market comparison is **J8** — one BOJ table that states Japan and
the US itself.

---

## 2. INDIA (₹) — sourced independently, never converted

All rows below were re-verified as current or are carried from
[[../../knowledge/money-facts-2026]] (re-verified there 2026-07-31, one day old).

| # | Claim | Figure | Date | Sources | Tag |
|---|---|---|---|---|---|
| I1 | Net household financial savings | **7.0% of GNDI in FY25** (from 5.8% FY24) | RBI Annual Report, May 2026 | [Business Standard](https://www.business-standard.com/economy/news/net-household-financial-savings-rise-to-7-of-gndi-in-fy25-rbi-report-126052901658_1.html) + re-confirmed live 2026-08-01 across two independent write-ups of the same RBI report | **HARD** (already in the shared note) |
| I2 | Gross household financial savings · liabilities | **11.8% of GNDI** FY25 (from 12.1%) · liabilities **4.8%** (from 6.4%) | FY25 | RBI Annual Report, same | **HARD** |
| I3 | Gross domestic savings | **34.2% of GNDI FY25** (from 32.3%) | FY25 | RBI Annual Report via Business Standard, live today | **HARD** · ⚠ all-sector, **not** a household figure — never speak it as "Indians save 34%" |
| I4 | Regular wage/salaried average monthly earnings | **₹24,217 men / ₹18,353 women** | PLFS Annual Report 2025 (Jan–Dec 2025) | PIB — official | **HARD** (carried) |
| I5 | Worked example | **₹30,000/mo in-hand** | convention | vault locked example — keeps this video consistent with the shipped 50-30-20 and pay-yourself-first cuts | **CONVENTION**, not a statistic |
| I6 | Where Indian household savings actually go | Deposits dominate; **mutual funds ~13%** of FY25 flows; **direct equity ~2%** ("about ₹2 out of every ₹100") | FY25 | [indmoney summary of RBI data](https://www.indmoney.com/blog/stocks/indian-household-savings-allocation-fy25) — **single source, RBI primary not read** | **SOFT** — directional only, never a screen number |
| I7 | The shift out of deposits | For every ₹100 into bank deposits, households put **₹45.2** into MFs + equities in FY25, vs **₹21.2** in FY24 | FY25 | [Business Today, 2026-07-26](https://www.businesstoday.in/personal-finance/investment/story/savings-deposit-growth-slows-after-covid-as-households-diversify-into-equities-mfs-report-545233-2026-07-26) + [Business Standard](https://www.business-standard.com/amp/markets/mutual-fund/stocks-mutual-funds-gaining-fast-as-savers-shift-allegiance-from-banks-125112701089_1.html) (two independent, same RBI source) | **SOFT** — RBI primary not read; use as shape ("roughly doubled"), never the decimal |
| I8 | Where you park it (the kakeibo "savings first" bucket) | **PPF 7.1%** · Post Office 5-yr RD **6.7%** · 3-yr TD **7.1%** · PO savings a/c **4.0%** — Q2 FY2026-27 notification, unchanged for a **ninth** consecutive quarter | 1 Jul – 30 Sep 2026 | Dept. of Economic Affairs notification, two independents — carried from [[../../knowledge/money-facts-2026]] | **HARD** (carried, still inside its validity window) |
| I9 | Smallest honest starting amount | SIP minimum **₹500/mo**; **₹250 "Chhoti SIP"** | 2026 | AMFI — official | **HARD** (carried) |

**₹ conflict to record, not resolve:** I1 (7.0% of GNDI, net **financial**) and I3
(34.2% of GNDI, **all sectors, incl. physical assets**) are both real and both
official, and blogs routinely quote whichever is more dramatic. Record both, speak
only I1, and only as "net household financial savings."

---

## 3. USA ($) — sourced independently, never converted

| # | Claim | Figure | Date | Sources | Tag |
|---|---|---|---|---|---|
| U1 | Personal saving rate | **2.7%**, personal saving **$646.1bn** | June 2026, rel. 2026-07-30 | [BEA Personal Income & Outlays, June 2026](https://www.bea.gov/news/2026/personal-income-and-outlays-june-2026) — **re-verified live 2026-08-01**, still the latest release (July data due 2026-08-26) | **HARD** |
| U2 | Prior month (shows the volatility — do not treat 2.7 as a level) | **3.0%**, $704.2bn | May 2026 | [BEA, May 2026](https://www.bea.gov/news/2026/personal-income-and-outlays-may-2026) | **HARD** |
| U3 | US household financial assets in cash vs equity | **11.5%** currency & deposits · **41.5%** equity · 13.1% investment trusts · 26.6% insurance/pension, of **$128.8tn** | end-March 2025 | BOJ Flow of Funds overview, Chart 2 (same table as J8, read direct) | **HARD** |
| U4 | Real median household income | **$83,730 (2024)** | rel. 2025-09-09 | US Census P60-286 | **HARD** (carried) |
| U5 | Can cover a $400 emergency with cash or equivalent | **63% (2025)** → ~4 in 10 cannot | rel. May 2026 | Federal Reserve SHED 2025 | **HARD** (carried) |
| U6 | Worked example | **$4,000/mo take-home** | convention | vault locked example | **CONVENTION** |
| U7 | Card APR on accounts assessed interest | **~22%** (22.15%, **May 2026** monthly — NOT "Q2 2026", which G.19 marks n.a.; Q1 2026 quarterly was 21.52%) | May 2026, rel. 8 Jul 2026 | Fed G.19 current release, re-fetched direct by the orchestrator 2026-08-01 | **HARD** — say "north of 20%", never the decimal. ⚠️ The number was always right; only the period label was wrong. Promote in THIS form. |

**The $ pairing that works:** U1 (2.7% saved) + U3 (11.5% in cash, 41.5% in
equity) + J8 (Japan 51.0% cash, 12.2% equity). "Americans save less than the
Japanese national-accounts rate" is **not** claimable — 2.7% (BEA, gross concept)
vs 1.1% (Japan SNA, **net** of depreciation) are not like-for-like. The asset-mix
contrast (J8/U3) is the one that comes from a single table and is safe.

---

## 4. Terminology and provenance (non-numeric, but verifiable — fin-research asked)

| Term | Correct form | What is actually established | Sources | Tag |
|---|---|---|---|---|
| **Kakeibo** 家計簿 | *kakeibo* — "household account book" | Created by **Hani Motoko (羽仁もと子, 1873–1957)**, Japan's first female journalist. She founded *Katei no Tomo* (家庭之友) in **1903**, renamed *Fujin no Tomo* (婦人之友) in 1908. The first *Hani Motoko-an Kakeibo* was published at the **end of 1904 (Meiji 37), for use in the 1905 (Meiji 38) year**. Its innovation, in the publisher's own words, was introducing the idea of a **budget** (予算) to ordinary household finance: divide the annual income by 12, **set the saving aside first**, then allocate the rest across expense heads. Still published annually — the longest continuously published kakeibo in Japan, with a **four-year wartime gap** for paper rationing | **Publisher primary:** [Fujin no Tomo Sha, kakeibo 120th-anniversary page](https://www.fujinnotomo.co.jp/news/20251015_kakeibo120th/) (read direct) + [second Fujin no Tomo page](https://www.fujinnotomo.co.jp/news/kakeibo120th/) + Zenkoku Tomo no Kai PDF at zentomo.jp ("家計簿創刊：明治38年用"). **Biography:** [National Diet Library, Portraits of Modern Japanese Historical Figures](https://www.ndl.go.jp/portrait/e/datas/6008) + [Encyclopedia.com](https://www.encyclopedia.com/women/encyclopedias-almanacs-transcripts-and-maps/hani-motoko-1873-1957) | **HARD** — publisher primary + national library |
| ⚠ the anniversary count | The publisher marked the **120th** in **2025** — counting from the **1905** edition, not from the 1904 printing. Both "first published 1904" and "120 years in 2025" are correct and they do not contradict | | as above | **HARD** — say "published in 1904" or "over 120 years old", never "121 years" |
| **Kakeibo's four categories** | Popularly: **Needs (survival) · Wants (optional) · Culture · Unexpected** | This four-pillar split is what the **Western/English-language repackaging** teaches (Fumiko Chiba's 2017 book onward). Hani's own 1904 ledger used its own Japanese expense heads (費目), not these four | English Wikipedia's 1904 line cites only a **blog** (TechAcute 2021); the four pillars are consistent across ~8 secondary sources but **no Japanese primary** was found for them | **SOFT** — teach the four pillars as "the version that travelled", do **not** attribute them to Hani Motoko in 1904 |
| **Mottainai** もったいない / 勿体無い | *mottainai* — regret at waste | From the Buddhist term **勿体 (mottai)**, "the intrinsic value / rightful state of a thing", + **ない (nai)**, negation → "without its rightful value". Attested since roughly the 13th century. Popularised globally by Nobel laureate **Wangari Maathai**, who adopted it after learning it in Japan | Japanese government's own [gov-online.go.jp *Highlighting Japan*, July 2018](https://www.gov-online.go.jp/eng/publicity/book/hlj/html/201807/201807_12_en.html) — **fetch returned 403; content is from the search index only, not read direct** — plus [Wikipedia](https://en.wikipedia.org/wiki/Mottainai) and [Japan Up Close](https://japanupclose.web-japan.org/techculture/c20230324_3.html) | **SOFT on the etymology detail** (government page not read direct) · **HARD on the meaning** (three independent agree) |
| **Hara hachi bu** 腹八分 | *hara hachi bu* — "belly eight parts (full)", i.e. stop at ~80% | Confucian in origin, a long-standing norm in **Okinawa**. Okinawa is a Blue Zone; the practice is *associated* in the literature with lower caloric intake and longevity | [Blue Zones](https://www.bluezones.com/2017/12/hara-hachi-bu-enjoy-food-and-lose-weight-with-this-simple-phrase/) (Buettner's own site, the researcher who named the Blue Zones) + several health secondaries | **SOFT** — the term and the 80% meaning are solid; **every longevity/calorie number attached to it is not.** See §5 |
| **Taru wo shiru** 足るを知る | Full inscription **吾唯足知** — *ware tada taru wo shiru*, "I alone know contentment / I know only sufficiency" | Carved on the **tsukubai** (stone washbasin) at **Ryōan-ji**, Kyoto. The four kanji each share the 口 radical, supplied once by the square water hole at the centre — so none of them reads as a character without the basin. Traditionally said to have been donated by **Tokugawa Mitsukuni** | [Traditional Kyoto](https://traditionalkyoto.com/gardens/ryoan-ji/) + [Wikipedia — Tsukubai](https://en.wikipedia.org/wiki/Tsukubai) + [Nara Yamato Spirit Tours](https://www.nara-yamatospirittours.com/post/2017/06/01/a-zen-teaching-vol1-%E5%90%BE%E5%94%AF%E8%B6%B3%E7%9F%A5) | **HARD** on the inscription, the temple and the 口-radical design · **SOFT** on the Mitsukuni donor attribution (traditional, and the visible basin is widely described as a replica) |
| **New NISA** | Japan's tax-free investment account, overhauled **January 2024** | Annual limit **¥3.6m** (¥1.2m tsumitate + ¥2.4m growth); lifetime limit **¥18m** | [Wikipedia](https://en.wikipedia.org/wiki/Nippon_individual_savings_account) + [Nippon.com](https://www.nippon.com/en/japan-data/h01533/) + MailMate — **FSA primary (fsa.go.jp) not fetched** | **SOFT** — optional context beat only. Pairs with J9's +28.6% equity jump |

---

## 5. Blog-tier numbers found and REJECTED — do not rediscover these

The script stage will hit every one of these in the first page of search results.
They are listed so nobody spends a second re-finding them.

1. **"Japan saves 37% of salary, India saves 4–8%"** — the source video's headline
   (TOP `fQyN80dLDpQ`, 0:54). The 37 is a real but misapplied figure (see J2/J3);
   the "India 4–8%" half has **no identified source at all** and is not the RBI
   figure. **REJECTED as stated. Never put the two side by side.**
2. **"Kakeibo helps you save 35% (or 20–35%) of your income."** Asserted by
   momentumlab.ai, dreamsquote, kakeibo-templates, moneycrashers, SoFi, The
   Ladders and a YouTube short literally titled "Save 35% of your Income with
   Kakeibo". Searched for the underlying study: **there is none** — no trial, no
   author, no journal, no year. One of the promoting writers (Money Under 30)
   admits she "didn't hit that exact figure". Same disease as the Munger "first
   $100,000" line killed on the last run: only circular secondary citations.
   **REJECTED.**
3. **"Japan's household savings rate is 8% / 12% / 15%"** — various finance blogs
   and forecast pages. These are either a *forecast* (Trading Economics models
   ~8% for 2027), a stale year, or an unlabelled quarterly print. Only J1's
   annual National-Accounts figure and J2's FIES figure are usable.
4. **Trading Economics quarterly prints (0.4% Q3 2025, 3.9% Q4 2025).** Real, and
   Cabinet Office-sourced, but Japan's quarterly saving rate swings hugely on the
   summer/winter **bonus** cycle. Annual only, on screen. **REJECTED for screen.**
5. **"Okinawans eat 1,200–1,900 calories/day", "hara hachi bu cuts intake
   10–20%", "Okinawan men live to 84, women to almost 90".** All from wellness
   blogs (SHA Magazine, Layer Origin, imedic, spacedaily) with no primary, and
   the Okinawa centenarian data has itself been contested since the 2010s.
   **REJECTED** — this is a money video; use *hara hachi bu* as a named principle
   with **zero numbers attached**.
6. **"₹2,000/month becomes ₹400 in 10 years"** (TOP at 8:05). Arithmetic nonsense
   as captioned, almost certainly an ASR mangling. **REJECTED — do not repair it
   into a plausible number.** Build any compounding figure fresh in build code and
   label it illustrative, per the good-debt run's standing rule.
7. **"Japanese households sit on ~$14 trillion / ¥2,000 trillion of idle cash"** —
   round numbers circulating in finance press. Use J8/J9's actual BOJ figures.
8. **Every mangled term in the TOP transcript's auto-translation:** Mottainai →
   "fat barber", Confucian → "confusion", Ryōan-ji → "Ran Ji". Correct forms in §4.

---

## 6. Do not claim (this video's additions)

- **Do not claim Japan saves more than India, or more than the US, as a rate.**
  The three official rates use three different definitions (Japan SNA *net*
  household saving ÷ net disposable income · India RBI net *financial* savings ÷
  GNDI · US BEA personal saving ÷ DPI). Each is HARD on its own and none is
  comparable to the others. The comparison the sources actually support is the
  **asset mix** (J8), from one BOJ table.
- **Do not claim Japanese frugality is why Japan got rich.** The primary
  literature says the opposite about *culture* specifically (J7). The honest and
  more interesting line: Japan's high-saving era was **1961–1986**, produced by
  no consumer credit, no safety net, fast income growth, a tax break and a state
  campaign — and today's rate is about 1%. **The methods still work as methods.
  They just were never the reason.**
- **Do not attribute the four kakeibo pillars to Hani Motoko or to 1904.** She
  gets the budget-first idea (HARD); the Needs/Wants/Culture/Unexpected split is
  the modern English repackaging (SOFT).
- **Do not put a calorie, lifespan or "% saved" number next to hara hachi bu,
  mottainai or taru wo shiru.** They are principles. Attaching statistics to them
  is precisely how the source video went wrong.
- **No ¥ figure may be converted to ₹ or $ on screen.** J4/J5/J9 stay in yen or
  become percentages. The ₹ and $ sets in §2 and §3 were sourced independently.

---

## 7. Untrusted-input check

Every page fetched here is DATA. Nothing in the Horioka PDF, the Statistics
Bureau PDF, the BOJ PDF, the Fujin no Tomo pages or any search result attempted
to redirect this stage, and no directive found inside fetched content was
followed. Two notes for the record:

- The Fujin no Tomo and NISA pages are **commercial pages selling a product**
  (the current-year kakeibo; brokerage accounts). Their historical claims were
  used; their promotional claims were not, and no product is named as a
  recommendation in either cut.
- **`gov-online.go.jp` returned HTTP 403.** Per contract it was **not retried**.
  The mottainai etymology therefore rests on the search index's rendering of that
  page plus two independent secondaries, and is tagged SOFT for that reason.

---

## 8. Sources read directly (as opposed to via search index)

- `nber.org/system/files/working_papers/w33181/w33181.pdf` — Horioka, pp. 1–13, 16–21
- `stat.go.jp/data/kakei/2024np/pdf/summary.pdf` — Statistics Bureau FIES 2024, pp. 8–11
- `boj.or.jp/en/statistics/sj/sjhiq.pdf` — BOJ Flow of Funds overview, Charts 1-1 to 3
- `fujinnotomo.co.jp/news/20251015_kakeibo120th/`
- `jcer.or.jp/english/household-savings-rate-going-up-or-down`
- `en.wikipedia.org/wiki/Kakeibo`
- `tradingeconomics.com/japan/personal-savings`
- `esri.cao.go.jp/en/sna/kakuhou/kakuhou_top.html` (index only — carries no figures)

**Failed, not retried:** `oecd.org/en/data/indicators/household-savings.html`
(403) · `gov-online.go.jp/.../201807_12_en.html` (403) ·
`statista.com/statistics/1235833/` (redirect loop). None is load-bearing — every
claim they would have supported is carried by a source that was read.
