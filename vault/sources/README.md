# Sources — one note per primary source document

Schema and rules: [[../knowledge/fact-integrity]] §1–2.
The link direction is **source ← claim → video**, never video → source.

A note here records a DOCUMENT, not a figure. Figures live in `../claims/`, one per
claim, so that when this document expires every dependent claim (and through them every
video) surfaces in the dashboard query.

Filename = the `source-id`. Subfolder = the agency.

```yaml
---
type: source
source-id: irs-pub590b-2026
agency: IRS
document: "Publication 590-B, Distributions from IRAs"
url: https://www.irs.gov/pub/irs-pdf/p590b.pdf
tier: primary            # primary | secondary  (see fact-integrity §1)
as-of: 2026-01-15
retrieved: 2026-08-15
expires: 2027-01-31
expiry-class: annual     # annual | monthly | stable
screenshot: "[[../../screenshots/irs-pub590b-20260815.png]]"
topics: [rmd, ira, retirement-tax]
---

## Figures captured
| Figure | Value | Page | Notes |
|---|---|---|---|

## Verbatim quote (short, for on-screen use)
>

## What this source is NOT authoritative for
-
```
