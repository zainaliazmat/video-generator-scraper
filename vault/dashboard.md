---
summary: Live Dataview dashboard for Money Mavens fact integrity — expiring sources, videos with unverified claims, published videos carrying an expired figure, and slate progress. Requires the Obsidian Dataview plugin; the queries render only in Obsidian, not in a plain reader.
updated: 2026-08-15
source: creator plan `03-obsidian-vault-schema.md` (2026-08-15), paths adapted to this vault's existing layout.
stage: ADOPTED — the standing verification surface
---

# Dashboard — fact integrity

Run cadence and what to do with each result: [[workflows/moneymavens-90-day-plan]]
("Standing verification tasks"). The standard itself: [[knowledge/fact-integrity]].

> **Path note.** The creator plan specified `02-sources/`, `03-videos/`, `04-claims/`.
> This vault already had `videos/` wired into the whole `/finance-video` pipeline
> (`pipeline_check.vault_dir`, `archive_cut`, every `fin-*` agent), so the numbered
> folders were **not** adopted — the mapping is `sources/` · `claims/` · `videos/`, and
> the queries below are written against those. The schema's substance (source ← claim →
> video, with expiry) is unchanged; only the folder names differ.

## 1 — stale and expiring sources

Anything expiring in the next 30 days, worst first, with a count of how many claims break
when it does.

```dataview
TABLE
  agency AS "Agency",
  as-of AS "As Of",
  expires AS "Expires",
  expiry-class AS "Class",
  length(filter(file.inlinks, (l) => l.type = "claim")) AS "Claims Affected"
FROM "sources"
WHERE expires != null AND expires <= date(today) + dur(30 days)
SORT expires ASC
```

## 2 — videos with unverified claims

**Nothing in this table gets published. Ever.**

```dataview
TABLE
  title AS "Title",
  status AS "Status",
  fact-gate-passed AS "Gate",
  length(unverified-claims) AS "Unverified"
FROM "videos"
WHERE type = "video" AND (length(unverified-claims) > 0 OR fact-gate-passed = false)
SORT length(unverified-claims) DESC
```

## 3 — published videos carrying an expired figure

The one that catches the evergreen-content problem before viewers do. Run the **first
Monday of every month**; anything appearing gets a pinned-comment correction the same week
per [[knowledge/fact-integrity]] §7.

```dataview
TABLE
  title AS "Video",
  publish-date AS "Published",
  filter(claims, (c) => c.expires < date(today)) AS "Expired Claims"
FROM "videos"
WHERE type = "video" AND status = "published"
  AND any(claims, (c) => c.expires < date(today))
SORT publish-date ASC
```

## 4 — slate progress

```dataview
TABLE WITHOUT ID
  intent AS "Intent",
  length(rows) AS "Total",
  length(filter(rows, (r) => r.status = "published")) AS "Published"
FROM "videos"
WHERE type = "video"
GROUP BY intent
```

## 5 — the committed ten, in publishing order

```dataview
TABLE WITHOUT ID
  slate-position AS "#",
  video-id AS "ID",
  link(file.link, title) AS "Title",
  title-score AS "Score",
  intent AS "Intent",
  status AS "Status"
FROM "videos"
WHERE type = "video" AND slate-position != null AND slate-position <= 10
SORT slate-position ASC
```

## Tag taxonomy

| Prefix | Values |
|---|---|
| `#topic/` | `social-security` · `medicare` · `rmd` · `credit` · `banking` · `estate` · `tax` · `fraud` · `insurance` |
| `#agency/` | `irs` · `ssa` · `cms` · `fdic` · `cfpb` · `ftc` · `bls` · `bea` · `fed` · `treasury` · `state` |
| `#tier/` | `primary` · `secondary` · `inference` · `unverified` |
| `#expiry/` | `annual` · `monthly` · `stable` |
| `#status/` | `research` · `scripted` · `fact-gated` · `rendered` · `published` · `reviewed` |
| `#intent/` | `search` · `browse` · `experimental` |
