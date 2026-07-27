---
summary: How to write Hindi video scripts that read and sound Haryanvi — the flavor-not-rewrite strategy, the high-leverage dialect markers, humor register, and the ElevenLabs TTS reality. For the India finance channel.
updated: 2026-07-22
source: deep-research run 2026-07-22 (wf_388d2df8-2e0) — Jatland Wiki, Wikipedia (Haryanvi language), haryanvitale, viralbake, dnoun, omniglot, ElevenLabs docs. Blog-tier lexicon, cross-corroborated. NEEDS a native-speaker pass before locking spellings.
---

# Haryanvi-flavored Hindi — script style guide

Sister note to [[urdu-script-style]] (that one is the Urdu channel; this is the **India finance** channel). Pairs with [[indian-business-culture-slang]] and [[india-finance-market]].

## The core strategy: season, don't rewrite

Haryanvi is a **Western Hindi dialect** (grouped with Khariboli/Braj), mutually intelligible with Standard Hindi. So the authoring rule is: **write clean, simple Standard Hindi and season it with a handful of Haryanvi markers** — do NOT compose in a separate language. A few load-bearing markers per sentence + the right voice = reads Haryanvi, stays understandable to any Hindi speaker. (high confidence — academic + Wikipedia classification)

## The markers that do the work (Devanagari — for TTS + on-brand)

The single highest-leverage cue is the **sentence-final copula सै / सैं**, replacing standard है / हैं. Drop it at clause ends and the whole line tilts Haryanvi. (highest confidence — 5 independent sources + academic corroboration)

| Standard Hindi | Haryanvi | Meaning | Note |
|---|---|---|---|
| है / हैं | **सै / सैं** | is / are | THE marker. Use at clause end. |
| नहीं | **कोन्या** (कोन्यां) | no / not | Very distinctive. |
| तुम्हारा | **थारा** | your | |
| हमारा / मेरा | **म्हारा** | our / my | |
| बहुत | **घणा / घणे** | very / a lot | "घणा सुथरा" = very nice |
| लड़का / लड़के | **छोरा / छोरे** | boy(s) | |
| लड़की | **छोरी** | girl | |
| हाँ | **हम्बे** | yes | affirmation |
| को (object) | **-नै** | to / object marker | "छोरे नै" |
| से (from/than) | **-तै** | from / than | |
| — | **जमा गदर** | totally great | strong praise |

**Address / interjections:** ताऊ (tau, elder-uncle — warm + funny authority), भाई / वीरा (brother), बेबे (sister), राम-राम (greeting). A narrator who calls the viewer **भाई** or **ताऊ** instantly sets the rustic, one-of-us tone.

## Humor / voice register

Blunt, witty, rustic, confident — a street-smart elder telling you the obvious truth you keep ignoring. Short punchy lines. Mock-scold the viewer ("फेर ना कहियो बताया कोन्या" = *then don't say I didn't tell you*). Exaggerate with घणा. The comedy is in **delivery + attitude**, so keep sentences short and let the voice land them.

**Ready-made thrift proverb (verified, perfect for finance):**
> **घर देख कै खावै, पड़ौसी देख कमावै** — spend according to your income, earn by watching your neighbor. (Jatland + dnoun, verbatim match)

## ElevenLabs TTS reality (important)

- Voice: **`9BHTbeEKC5ZqMmvZfLW6`** (Haryanvi voice one — chosen 2026-07-22), model **`eleven_multilingual_v2`** (supports Hindi). Pipeline: `tools/tts/elevenlabs_tts.py --voice <id> --file seg.txt --out out.mp3`. See [[voiceover-tts]].
- **There is NO Haryanvi (or Hindi) accent tag** in ElevenLabs. `multilingual_v2` supports no phoneme tags either; only v3 has an `[Indian English]` tag (English only). So **Haryanvi color must come from (a) the chosen voice and (b) Devanagari word choice/spelling** — not from any tag. (high confidence — ElevenLabs primary docs)
- Alias / respelling (pronunciation dictionary) can nudge pronunciation, but its effectiveness for Haryanvi color with multilingual_v2 is **untested — trial per line**.
- Number/currency: write amounts in words or clear Devanagari for the TTS ("चालीस हजार रुपये"), even when the on-screen text shows "₹40,000".

## DO NOT USE (refuted in research — 0-3 votes)

- The **"he"** copula form ("Tu kaisa he?") — wrong; use सै/सैं.
- **"Tanna"** as a 2nd-person object pronoun — not attested.

## Standing caveat

Haryanvi spelling is **non-standardized** (सै/सैं/से, कोन्या/कोनी, हम्बे/हम्बै) and the lexicon here is blog-tier though cross-corroborated. **Get a native Haryanvi speaker to proof the first real script** before locking this as canon. Sub-dialect (Bangru/Deswali vs Bagri) also shifts forms.
