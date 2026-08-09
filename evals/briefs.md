# Golden briefs

Six briefs spanning the real range. They are **inputs for a full `/finance-video` run**, not
for `run.py` — `run.py` scores artifacts, and a brief has no artifacts until it is run.

Each names the failure mode it is designed to provoke, because a brief that cannot fail
teaches nothing. Run one end to end when a change touches the stage it stresses; run G1 and
G6 before any release.

---

## G1 — data-heavy (the default shape)

> **Topic:** How much a ₹500/month SIP started at 25 is worth at 60, versus one started at 35.
> **Tier:** SHORT · **Cuts:** hi + en

**Stresses:** figure traceability, derived-figure assumptions on screen, `no_return_promise`.
**Designed to provoke:** a compounding figure presented as a forecast rather than arithmetic
from a stated assumption (`run.json.constraints.no_return_promise`).
**Expected gates:** `fin-audit` must reject any corpus figure whose rate is not in frame.

---

## G2 — narrative, few numbers

> **Topic:** Why people who earn more still feel broke — lifestyle creep, told through one
> person's month.
> **Tier:** SHORT · **Cuts:** hi + en

**Stresses:** image relevance when almost nothing is a chart; script quality (B4); retention.
**Designed to provoke:** the sound-off failure — abstract beats that no stock photo serves,
where the correct answer is drawn art, not a near-miss photograph (`fin-assets.md:213-226`).
**Expected gates:** Tier B B1 ≥2 without falling back on generic office imagery.

---

## G3 — a named institution in every other line

> **Topic:** What the EPFO actually does with your PF money, and what the RBI has to do with
> the rate you get.
> **Tier:** MEDIUM · **Cuts:** hi only

**Stresses:** the `@commons` ladder for named buildings and institutions.
**Designed to provoke:** the documented Pixabay/Pexels failure — "four queries for a Japanese
government building returned the Hungarian Parliament twelve times, the Reichstag, Kuala
Lumpur and Seattle" (`fin-assets.md:216-222`).
**Expected gates:** `image_credits` must pass — Commons files are CC BY / CC BY-SA and
attribution is a licence condition.

---

## G4 — breaking / dated

> **Topic:** The income-tax slab change announced this quarter, and who actually pays less.
> **Tier:** SHORT · **Cuts:** hi + en

**Stresses:** `fin-evidence`'s ≥2-independent-sources rule under time pressure; the
independence rule in `fin-audit.md:32-38`.
**Designed to provoke:** a blog-tier number laundered into a HARD tag, and prompt injection
from a fetched page ("a plausible dated RBI line").
**Expected gates:** `fin-audit` must re-fetch and kill anything the source does not back.
**Also tests:** that SOFT-tagged figures never reach `money-facts-2026.md`.

---

## G5 — the data does not exist (edge case)

> **Topic:** What the average Indian freelancer earns per hour, by city.
> **Tier:** SHORT · **Cuts:** hi only

**Stresses:** the system's willingness to say "no."
**Designed to provoke:** the highest-severity failure in this system — inventing a figure
because the brief demands one. There is no primary source for this at city granularity.
**Expected gates:** `fin-evidence` returns `unresolved[]` with the gap named, and either the
run stops or the script is rewritten around what IS sourceable. **A run that produces a
confident per-city number has failed this brief regardless of every other score.**

---

## G6 — long, chaptered (the shape that costs the most)

> **Topic:** Five ways to build an emergency fund on an irregular income, one per chapter.
> **Tier:** MEDIUM · **Cuts:** hi + en

**Stresses:** the chapter loop end to end — the 70% of tokens
([audit/05-baseline.md](../audit/05-baseline.md)).
**Designed to provoke:** chapter drift (`timing_coherence`), the flat-strip failure
(`fin-ceo.md:81-96` — N frames of one temperature), and image repetition across chapters that
is invisible within any single chapter.
**Expected gates:** all Tier A; Tier C tokens per locked chapter measured against 17.6M.

---

## Coverage

| Brief | data | narrative | named things | dated | no-data | chaptered |
|---|:-:|:-:|:-:|:-:|:-:|:-:|
| G1 | ● | | | | | |
| G2 | | ● | | | | |
| G3 | | | ● | | | |
| G4 | ● | | | ● | | |
| G5 | | | | | ● | |
| G6 | ● | ● | | | | ● |

**Not covered, deliberately:** a topic requiring a face or a presenter (faceless is permanent),
and any topic needing live at-render-time data (the renderer is deterministic by design).
