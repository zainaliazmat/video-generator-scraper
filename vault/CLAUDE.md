# Vault — operating manual (read me first)

This folder is the **knowledge layer** for the faceless YouTube channel project.
It is an Obsidian vault AND a plain markdown folder — Claude Code reads it
natively with Read/Grep; the human opens it in the Obsidian app. No MCP, no
plugin, no sync machinery.

## The three-layer memory rule (one home per fact — never duplicate)

| Layer | Home | Owns |
|---|---|---|
| **Data**      | `../library.db` (SQLite)  | Raw scraped video rows: views, subs, dedup, times_seen. Numbers live HERE, never in notes. |
| **Knowledge** | this vault (markdown)     | Durable prose: skills, niche dossiers, verified facts (dated + sourced), scrape findings, video artifacts, templates. |
| **Decisions** | Notion decisions log      | What was decided / killed / pending, session log entries, current status. |

Notion page: "Faceless YouTube Channel — Decisions & Learnings Log"
https://app.notion.com/p/38f4c89fff95819b96dac503872bba6c

## Cross-surface boundary (the load-bearing rule)

claude.ai web sessions **cannot see this vault** (it is local). Claude Code
sessions **can**. Notion is the only store both surfaces reach, so:

- Anything a web session must know goes **into the Notion log**, not only here.
- The skill files in `skills/` are **canonical**. The copies in the claude.ai
  project knowledge are snapshots — when a skill changes here, the human
  re-uploads it to the web project. Record every skill change in the Notion log
  so web sessions know their copy is stale.
- Artifacts that exist only in the web project (see `videos/video-01/status.md`)
  must be pasted here to become durable.

## Session protocol (how this vault learns over time)

1. **Start** (channel work): read the Notion log §1 Current Status first.
2. **Work**: cite facts from vault notes; verify anything stale (facts carry
   dates — AI-tool prices move monthly, re-verify per the skill's rules).
3. **End**: distill what was learned into the right vault note (update, don't
   append-forever), then add a dated entry to the Notion log
   (template: `templates/notion-log-entry.md`).

Git versions this vault — history of every note IS the audit trail of learning.

## Note conventions

- Frontmatter on every note: `summary:` (1–2 sentences — lets a session preview
  without opening), `updated:` (date), `source:` where the facts came from.
- Every factual claim carries its date and source inline. Triangulate ≥2 sources
  for money/spec claims (per the channel skill).
- Link related notes with `[[wikilinks]]`. `index.md` is the catalog — keep it
  current when adding notes.
