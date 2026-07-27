# Vault — operating manual (read me first)

This folder is the **knowledge layer** for the faceless YouTube channel project.
It is an Obsidian vault AND a plain markdown folder — Claude Code reads it
natively with Read/Grep; the human opens it in the Obsidian app. No MCP, no
plugin, no sync machinery.

## The two-home memory rule (one home per fact — never duplicate)

| Home | What it owns |
|---|---|
| `../library.db` (SQLite)  | Raw scraped video rows: views, subs, dedup, times_seen. Numbers live HERE, never in notes. |
| **this vault** (markdown) | Everything else durable: skills, niche dossiers, verified facts (dated + sourced), scrape findings, video artifacts, templates — **and all decisions/status/session notes** (what was decided / killed / pending, current status). |

This is a **Claude Code local project — the vault is the single source of truth.**
The `skills/` files are canonical. There is no external log and no other surface
to sync to: if it matters, it lives in the vault.

## Session protocol (how this vault learns over time)

1. **Start** (channel work): read `index.md` and the relevant notes for current status.
2. **Work**: cite facts from vault notes; verify anything stale (facts carry
   dates — AI-tool prices move monthly, re-verify per the skill's rules).
   Before scripting a topic, run the study loop: `workflows/video-study.md`.
3. **End**: distill what was learned into the right vault note (update, don't
   append-forever). Decisions and status update the relevant note in place —
   full analysis and evidence included; there's nowhere else for it to go.
4. **`.claude/agents/` is procedure, not memory.** Agent prompts carry *how* a
   stage works; every *fact* (rates, voices, caps) lives in `tools/format.json`
   or a vault note, read by path. When a fact changes, change it in its one
   home — never inside an agent prompt.

## Post-delivery cleanup (once a video ships to YouTube)

Standing rule (creator, 2026-07-10): **a delivered video's home is YouTube, not
this disk.** The moment a project is uploaded + scheduled, reclaim the space:

1. **Distill first, delete second.** Capture every durable learning into the vault
   (a `videos/<id>/index.md` milestone note + any reusable runbook/design/script)
   BEFORE removing anything. The render is about to be the only place some of this
   lived — text it into the vault or it's lost.
2. **Delete the heavy, regenerable assets:** the final `*.mp4` render, extracted
   frame PNGs / snapshots, audio (`*.wav`/`*.mp3`), waveform/thumbnail caches, and
   `work-*/` temp dirs. These are large and are either on YouTube now or rebuildable
   from the kept source.
3. **Keep the light text:** scripts, `DESIGN.md`, runbook, `index.html` + scene
   source, JSON meta, and the final thumbnail PNG (the deliverable). Text is tiny and
   is what future projects start from.
4. **Record the URL + publish date** in the milestone note.

**The point (creator's framing):** each shipped video is a **milestone**, not a
throwaway. The next one starts FROM its runbook + design system + learnings and must
be *better* — that compounding is the real growth. First milestone:
[[videos/video-hist-01-travel/index]].

Git versions this vault — history of every note IS the audit trail of learning.

## Note conventions

- Frontmatter on every note: `summary:` (1–2 sentences — lets a session preview
  without opening), `updated:` (date), `source:` where the facts came from.
- Every factual claim carries its date and source inline. Triangulate ≥2 sources
  for money/spec claims (per the channel skill).
- Link related notes with `[[wikilinks]]`. `index.md` is the catalog — keep it
  current when adding notes.
