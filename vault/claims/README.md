# Claims — one note per reusable claim

Schema and rules: [[../knowledge/fact-integrity]] §2–3.
**A video links to claims. Claims link to sources. A video never links straight to a
source** — that indirection is what makes the expiry query work: when one document
expires, every claim that depends on it surfaces, and from there every video.

One claim can be used in many videos. That is the point — fix it once, fix it everywhere.

```yaml
---
type: claim
claim-id: rmd-beginning-age
statement: ""
label: verified          # verified | estimate | opinion  (fact-integrity §3)
source: "[[../sources/irs/irs-pub590b-2026]]"
as-of: 2026-01-15
expires: 2027-01-31
expiry-class: annual
used-in: ["[[../videos/rmd-costly-mistake/index]]"]
verified: true
verified-on: 2026-08-15
---
```
