---
summary: The fact-integrity standard for Money Mavens — the US primary-source whitelist, the as-of date rule, the three-label discipline (verified/estimate/opinion), screenshot-the-source, the anti-pattern reject list, verbatim disclaimer + its four placements, the correction policy, and the ten-point pre-publish gate. Personal finance is YMYL; this is a survival requirement, not a nicety.
updated: 2026-08-15
source: creator plan `02-fact-integrity-standard.md` v1.0 (2026-08-15), adopted verbatim in substance. Review every 6 months — next review 2027-02-15.
stage: ADOPTED — the evidence bar for every Money Mavens video; supersedes nothing, tightens [[evidence-discipline]]
---

# Fact-integrity standard — Money Mavens

> **BOX — the whole evidence rule. Read the body only where it sends you.**
> 1. **Whitelist or nothing.** A figure on screen comes from BLS · BEA · FRED/Federal
>    Reserve · IRS · SSA · CMS/Medicare · Treasury · CFPB · FDIC/NCUA · SEC/investor.gov ·
>    FTC · Census · CBO · Fannie/Freddie · MSRB/EMMA · state treasurer/NAUPA. **FICO** is
>    primary *for the FICO score only* — say "FICO's published category weights", never
>    "studies show". Anything else is SECONDARY and must be labelled so. An aggregator
>    (NerdWallet, Investopedia, Bankrate) is a lead to the primary document, never a source.
> 2. **Every figure carries "as of [Month Year]"** on the frame that shows it, and an
>    `expires:` + `expiry-class:` in its vault claim note. Annual class re-verifies every
>    January; monthly class re-verifies before every publish that uses it.
> 3. **Three labels, on screen AND in script — verified fact · reasonable estimate ·
>    my opinion.** Never let a label drift mid-sentence; split the sentence instead.
>    An estimate shows the word "example"/"illustration" in frame plus its inputs.
> 4. **Screenshot-the-source**: screen-record the REAL page, URL visible, hold ≥3 s,
>    highlight exactly ONE row. Never rebuild a government table in a graphics tool.
>    Save the capture to `vault/screenshots/` so a later page change cannot orphan the cite.
> 5. **No model output without its inputs visible.** No decimal on anything inherently
>    imprecise — the long-run market return is a SHAPE, never a number.
> 6. **Never name a specific fund, bank, card, or security as good.** Category and
>    mechanics only.
> 7. **The disclaimer appears in FOUR places** — spoken (≤0:45 if any figure lands
>    before then), on screen at the first dollar figure, in the description above the
>    fold, and pinned on any tax / Medicare / SS-claiming video.
> 8. **The ten-point gate blocks publish on any single failure** — §8 below.
>
> **Open the body when:** you are picking a source (§1 table says what each agency is
> NOT authoritative for), setting an expiry (§2), or handling a published error (§7).

Personal finance is YMYL content. Accuracy is a survival requirement.

## 1. US primary-source whitelist

Only these are cited as **[PRIMARY]**. Everything else is secondary and labelled so.

| Source | Authoritative for | NOT authoritative for |
|---|---|---|
| **BLS** | CPI inflation, wages, employment, CPI-W (the COLA input) | Anything forward-looking; state/local variation beyond published series |
| **BEA** | Personal saving rate, personal income and outlays, GDP | Household-level behaviour; anything about individuals |
| **FRED / Federal Reserve** | Interest rates, fed funds target range, SHED survey findings | Predictions of future rates; product pricing |
| **IRS** | Tax brackets, standard deduction, contribution limits, RMD tables, Pub 590-B / 915 / 554 | State tax; individual liability; anything a preparer would sign |
| **SSA** | Benefit rules, full retirement age, COLA amount, survivor and spousal rules, earnings test | A personal benefit estimate; Medicare specifics |
| **CMS / Medicare.gov** | Medicare Parts A/B/C/D rules, premiums, IRMAA brackets, penalties, enrollment windows | Plan-level detail; whether a specific drug or doctor is covered |
| **Treasury / TreasuryDirect** | Treasury yields, savings bond rates and rules | Corporate or municipal pricing |
| **CFPB** | Consumer protection rules, credit reporting rights, complaint data | Product recommendations; scoring model internals |
| **FDIC / NCUA** | Deposit insurance limits, ownership categories, national deposit rate caps, bank failure facts | Whether a specific bank is "safe" as an investment |
| **SEC EDGAR / investor.gov** | Company filings, registration status of advisers and brokers | Whether an investment is good |
| **FTC** | Scam and fraud data, auto-dealer rules, Consumer Sentinel reports | Legal advice on a situation |
| **Census** | Demographics, household composition, income distribution | Causation of anything |
| **CBO** | Federal budget and program projections | Certainty — CBO output is a projection, always labelled as one |
| **Fannie Mae / Freddie Mac** | Conforming loan limits, mortgage survey data | An individual's rate |
| **MSRB / EMMA** | Municipal securities disclosure | Suitability |
| **State treasurer / NAUPA** | Unclaimed property programs | Amounts owed to any individual |

**FICO** is a special case: a private company, but the **owner** of the FICO score, so its
published category weights are primary *for the FICO score specifically*.

## 2. Date-stamping rule

Every figure on screen carries **"as of [Month Year]"**; every claim note carries a
re-verification interval.

**Expires annually — re-verify every January** (`expiry-class: annual`)
IRS brackets and standard deduction · IRA/401(k)/HSA contribution limits · SSA COLA and
taxable wage base · Medicare Part B premium, deductible and IRMAA brackets · SS
earnings-test limit · full retirement age by birth year (changes by cohort — still check).

**Expires monthly or faster — re-verify before every publish that uses it** (`monthly`)
CPI / inflation · fed funds target range · Treasury yields · FDIC national deposit rate
caps · personal saving rate.

**Stable but not permanent — re-verify annually** (`stable`)
FDIC coverage limit per ownership category · FCRA retention periods (7 years, 10 for
bankruptcy) · RMD age thresholds and the Uniform Lifetime Table.

> **The single biggest source of stale-content complaints is an annually-expiring number
> sitting inside an evergreen video.** Every claim note carries `expires:`; the dashboard
> query finds them ([[../dashboard]]).

## 3. The three-label discipline

Every claim is exactly one of three things, and the label appears **on screen and in script**.

| Label | On-screen treatment | Script phrasing |
|---|---|---|
| **Verified fact** | Source name + as-of date in the lower third | "According to the IRS, as of January 2026, …" / "The Fair Credit Reporting Act sets this at seven years." |
| **Reasonable estimate** | The word "example" or "illustration" visible in frame, plus the inputs | "This is a worked example, not a national average. At $800 a month and a 4% return, the model gives…" / "Run your own numbers." |
| **My opinion** | No source line; a visibly different lower-third colour | "This next part is my read, not a rule. Here is what I would want to know before deciding." |

**Never let a label drift.** If a sentence starts as a verified fact and ends as an
inference, split it into two sentences with two labels.

## 4. Screenshot-the-source

Show the actual government table. It is a credibility device and a retention device.

- Screen-record the real page. **Do not rebuild it in a graphics tool.**
- Leave the URL visible in frame or in the corner.
- Hold **at least 3 seconds** — long enough to read one row.
- Highlight exactly one row or one line. Never annotate more than one thing.
- Save the capture to `vault/screenshots/{source-id}-{YYYYMMDD}.png` beside its source
  note. If the page changes later, the cited state still exists.

⚠️ **Pipeline note:** a source screenshot is a distinct asset class from stock
photography — the sound-off stock-sourcing rules do not apply to it, and it is never a
rebuilt graphic. The 3-second hold clears the enforced build gate
(`scene.max_scene_seconds`, 9.0s) with room to spare, so no exemption is needed. But
`scene.max_static_hold_seconds` (2.0, guidance) still has something to say: **give the
shot motion** — the highlight arriving, or a slow push — or a 3-second static frame reads
as dead air. Constants: `format.json source_screenshot`.

## 5. Anti-patterns — automatic rejection at the gate

| Anti-pattern | Why it fails | Fix |
|---|---|---|
| Round number with no source | Unfalsifiable, and viewers notice | Cite it or cut it |
| "Studies show" / "experts say" | No such source exists | Name the study and year, or delete the sentence |
| Aggregator cited as primary | NerdWallet, Investopedia, Bankrate report *on* primary sources | Follow the link back to the agency and cite that |
| National average presented as personally applicable | "The average retiree has X" tells an individual nothing | "This is the national figure. Yours will differ, and here is what moves it." |
| Survivorship-biased example | Only showing the person who succeeded | Show the distribution, or say plainly you are showing one case |
| Outdated figure in an evergreen video | The #1 complaint driver | Date-stamp + expiry query |
| A decimal on something inherently imprecise | Implies precision you do not have | Use the shape of the number |
| Naming a specific fund, bank, card or security as good | Crosses from education into advice | Category and mechanics only |

## 6. Disclaimer language and placement

**Verbatim standard disclaimer:**

> This video is general financial education, not financial, tax, or legal advice. No
> specific product, fund, bank, or provider is recommended. Figures are current as of the
> date shown on screen and change over time. Confirm anything that affects your own
> decision with the issuing agency or a licensed professional.

**All four placements are required:**
1. **Spoken**, in full or condensed, within the first 45 seconds if any figure appears before then.
2. **On screen** as a lower third at the first appearance of any dollar figure.
3. **In the description**, above the fold, before the chapters.
4. **In the pinned comment**, on any video touching taxes, Medicare, or Social Security claiming.

**Additions:** "Confirm with a tax professional" (tax) · "Confirm with Medicare.gov or
SHIP, your state's free Medicare counseling program" (Medicare).

## 7. Correction policy

| Threshold | Action | Deadline |
|---|---|---|
| Typo, wrong on-screen date, non-material rounding | Pinned comment noting the correction | 48 hours |
| A figure is wrong but the conclusion still holds | Pinned comment **and** a correction line at the top of the description | 24 hours |
| A figure is wrong and the conclusion changes | Unlist immediately, fix, re-upload as a new video; leave the old one unlisted with a description note pointing to the new one | Unlist same day |
| A rule or law stated wrong in a way that could cost a viewer money | Unlist immediately — do not wait to decide. Fix, re-upload, and open the new video by naming the correction. | Unlist within the hour |

**Never silently edit a description to hide an error.** The pinned comment is the record.

## 8. Ten-point pre-publish fact gate

Run in under five minutes. **Any single failure blocks publish.**

1. Does every number on screen have a named source in the frame?
2. Does every number carry an "as of [Month Year]"?
3. Is every source on the §1 whitelist, or explicitly labelled secondary?
4. Has every annually-expiring figure been re-verified since the last January?
5. Has every monthly figure been re-verified this month?
6. Is every claim tagged verified fact / estimate / opinion, on screen and in script?
7. Is any model output presented without its inputs visible?
8. Does the title promise anything the video does not deliver?
9. Is any specific product, fund, bank, or security named as a recommendation?
10. Is the disclaimer present in all four required places?

**If you cannot answer all ten in five minutes, the script is not finished.**

Related: [[evidence-discipline]] (the general pipeline proof rules) ·
[[us-english-script-style]] (register + architecture) · [[../dashboard]] (the expiry queries).
