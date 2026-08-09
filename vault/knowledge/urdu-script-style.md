---
summary: The creator's Urdu scriptwriting VOICE — casual first-person tone, digits for numbers, no affiliate talk. Ground truth = his 11 sample lines (2026-07-05). ⚠ The SCRIPT it was originally written in, Roman Urdu, is RETIRED (creator 2026-07-18): every script file is now Nastaliq, transliterated to Devanagari for TTS — see §3 and [[../workflows/voiceover-tts]]. Read this for register, never for orthography.
updated: 2026-08-09
source: Creator's own rewrite of video-02 Urdu script lines 01–11 (2026-07-05 session)
stage: ADOPTED for tone and register — the ROMAN-URDU SCRIPT is SUPERSEDED BY workflows/voiceover-tts.md (creator 2026-07-18: scripts are always Nastaliq)
---

# Urdu script style — the creator's voice (ALWAYS follow)

Every Urdu script is written in **Roman Urdu, in the creator's own register**. He reads
these aloud for VO, so the text must match how he actually talks and types.

## Spelling conventions (his chat-style Roman Urdu)

Follow his phonetic collapses — do NOT "correct" them to textbook romanization:

| His spelling | Standard | Meaning |
|---|---|---|
| `ha` | hai | is |
| `ma` | main / mein | I / in |
| `na` | ne / na | (ergative) / not |
| `ka` | ke / ka / ki (loose) | of |
| `sa` | se | from/with |
| `or` | aur | and |
| `wo` | woh | that/he |
| `ap` | aap | you |
| `isa` | ise / usay | it (obj.) |
| `jasa ka` | jaise ke | like/such as |
| `hova` | hua | happened |
| `kasa` | kaise | how |
| `dakh / dakho` | dekh / dekho | see |
| `raha ho` | rahe ho / raha hoon | (progressive) |

Keep internal consistency within a script; when a word isn't in his samples, pick the
spelling closest to his pattern (vowel-collapsed, as typed in Pakistani chat).

## Voice & tone

- **First-person walkthrough**: "ma na ... kiya" — he recounts what HE did, step by step
  ("First step:", "Second step:", "Third step:" as literal English labels).
- **Direct audience address**: "ap log", promises to share: "ma ap logo ka sath share
  karon ga ta ka ap log isa try kar sako."
- **Honest failure-sharing is brand voice**: he shares what he tried that FAILED "ta ka
  ap logo ka time bach saka or ap kuch productive bana sako."
- Simple short sentences. Everyday words. **No literary Urdu** — never guftagu,
  qadam-ba-qadam, imaandar, jaiza, khwahish-type vocabulary; use discussion, step by
  step, honest, try instead.
- **English tech terms untranslated and freely mixed**: analyze, reference document,
  copyright free, local project structure, render command, fonts, colors, motion
  graphics, timeline.
- Explaining-to-a-friend framing: "us sa kaha ka is video ko analyze karo or dakho..."
  (he narrates his prompts to Claude as reported speech).

## Sounding HUMAN, not generated (research layer, 2026-07-05)

Studied real spoken-Urdu transcripts (Kashif Majeed's YouTube-automation course,
tNPD4r39CWA, ~2900 caption lines; Aasan Computer AI-tools review, -g9Gnx5MFsU) +
conversational-writing best practices (Paul Graham "Write Like You Talk";
CMI; KnowledgeOne audio-script guide). What separates a real Pakistani creator's
speech from a translated/generated script:

**Markers real Urdu creators use constantly (sprinkle, don't saturate):**
1. **Self-question → answer**: "Result kya nikla? Ak production runbook." /
   "Pehle kya hota tha? Mostly..." — the single strongest humanizer.
2. **`Theek ha?` checkpoint** after landing a point (Kashif uses it every 2-3
   sentences in a course; in a produced video 4-6 total is right).
3. **`Acha` / `Acha ab ruko` / `to chalo`** as topic-change markers.
4. **`yani` restatement** — say the fact twice, second time simpler ("10 guna,
   yani 10x").
5. **`dakho` / `suno` / `yaad rakhna`** direct-address imperatives.
6. **`jo ha na` / `na?` tags** mid-sentence (very light touch — 2-3 per script).
7. **Repetition for emphasis**: "sirf or sirf", "poora ka poora", "Sab. / Bas."
   one-word punch sentences.
8. **Personal micro-asides**: "sach bataon?", "mujha khud yaqeen nahi aaya",
   "ap ko maza aaya gi ya wali" — his own reaction to his own content.
9. **"Ab ap soch raha ho ga ka..."** — voicing the viewer's thought, then
   answering it.
10. **Concrete numbers spoken like a friend**: "koi 20 minute", "koi 2-3 ghanta"
    (koi = approx), never precise-sounding prose.

**What makes a script feel AI-generated (avoid):** uniform sentence lengths, every
line a complete tidy sentence, formal connectors (lehaza/mazeed/is ke ilawa),
zero questions, zero fragments, information-dense lines with no breathing room,
translation parity with an English source (same clause order line by line).

**The test (Paul Graham):** read each line aloud and ask "kya ma dost ko aisa hi
kehta?" If not, rewrite it with what you'd actually say.

## Hard rules

1. **Numbers as digits**: `5 ghanta`, `4 minute`, `1080P`, `747`, `1841` — never
   spelled out.
2. **NO affiliate / "nobody pays me" talk** — creator removed it from the whole script
   (2026-07-05). Don't add monetization disclaimers.
3. **RULE CHANGE (creator, 2026-07-18): scripts are ALWAYS written in Nastaliq** —
   Roman Urdu register is retired for script files. Nastaliq usool live in
   [[../videos/video-hist-01-pompeii/script-v1-nastaliq]] (English words in Urdu
   script, easy Urdu over literary, SOV spoken flow). TTS pipeline unchanged:
   Nastaliq master → Devanagari — [[../workflows/voiceover-tts]]. (The spelling
   table above now applies only to the creator's own chat/notes, not scripts.)
4. When he rewrites lines himself, his phrasing wins — fold the rest of the script
   around it.

## Ground truth — his own sample lines (2026-07-05, verbatim)

> **01** - jo video ap abhi dakh raha ha, us ka har ak frame claude na design kya ha na
> ka kisis insam na. is ma koi editing software jasa ka premier pro ya DaVinci use nahi
> hova, balka ya to koi timeline ha hi nahi har scene ak text file ha jo ail command sa
> render hoti ha.
>
> **04** - video ka akhir ma ya pora workflow ma ap logo ka sath share karo ga ta ka ap
> log isa try ar sako. or ma ap ka sath wo tareqa bhi share karo ga jinha ma na try kiya
> but failed ta ka ap logo ka time bach saka or ap kuch productive bana saka.
>
> **06** - second ma na wo video claude ko di or us sa kaha ka is video ko analyze karo
> or dakho is ma kon sa font, colors animations, motion graphics istalmal hova ha video
> ki raftear kaya ha or ak apna liya ak referance document bano jisa intamal kar ka tum
> same video bana sako.
>
> **11** - normal video editors like premier and capcut ka andar hum khud har cut lagata
> ha. timeline ko khud manually adjust karta ha.

(Full 11-line sample in the 2026-07-05 session; applied result: [[../videos/video-02-claude-edits-video/script-v3-urdu]].)
