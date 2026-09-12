# Sourcing Criteria

What qualifies a YouTube video as a source for Moving Image Arts Instagram.

Derived from `reference/decoder-clips-what-works.md`, an analysis of 55 reels
published 1 Aug to 9 Sept 2026. Read that document for the evidence. This file
is the operational translation of it into sourcing rules.

Caption voice is specified separately in `reference/caption-voice-spec.json`.
Where that spec and the analysis disagree, see `reference/spec-conflicts.md`.
Those conflicts are unresolved, so do not silently pick a side.

**The finding that governs everything here:** a clip performs when its first
sentence hands the viewer a mechanism they can use on another film. Caption
form is roughly a 7.8x multiplier on reach. Subject is roughly 1.7x. Nothing
else tested positive.

Sourcing cannot fix a caption. But the wrong footage makes the right caption
impossible, and that is what this file screens for.

## 1. The Sourcing Test

A decoder caption has three parts: state a rule, **prove it inside the clip**,
leave the rule portable. Part two is a constraint on footage.

> **Screen every candidate on this:** does this video contain footage where a
> mechanism is visible or audible on screen, within a few seconds, in a single
> work?

If the proof would have to be asserted in the caption rather than seen or heard
in the clip, the source fails, however good the underlying idea is.

## 2. What Makes Footage Demonstrable

Ranked by how fast a mechanism reads on screen. From the subject analysis, the
gap is about speed of perception, not importance.

| Mechanism | Sourcing note | Evidence |
|---|---|---|
| **Colour** | Strongest. A filter or palette shift reads instantly. | Kieślowski colour post, 2,894 |
| **Light** | Strong. Exposure, contrast, negative space. | Willis *Parallax View*, 41,799 |
| **Sound** | Strong, and does not need to be visible at all. | Altman eight-track, 50,641 |
| **Editing** | Weaker. Relationships between shots take longer to see. | 1,413 median |
| **Camera** | Weaker, same reason. | |

Prefer sources where the mechanism is colour, light, or sound. Editing and
camera can work, but need a longer clip to land, which costs more credits for
a lower expected return.

Note that the account's highest-save post demonstrates the Kuleshov effect,
which is editing. The rule is a tendency, not a prohibition.

## 3. Source Shape

| Requirement | Rule | Why |
|---|---|---|
| **One work per clip** | The source must allow a clip covering a single film. Multi-film compilations are usable only with `rangeStart`/`rangeEnd` isolating one work. | Surveys collapse. Four films in one post, 564. Two careers in one post, 260. |
| **Footage of the work itself** | The source must show the film, not only a person talking about it. | The proof has to be on screen. A talking-head-only clip cannot demonstrate anything. |
| **Clean enough to crop** | Will survive a 9:16 crop and the subtitle burn. | Letterboxed or low-resolution uploads degrade badly in portrait. |
| **Duration** | Not a quality filter. Length showed no correlation with performance, r = +0.06. Treat source length purely as an Opus credit cost. | A 28 second and a 172 second post both broke out. |

## 4. Post Type

The voice spec defines three post types. Only one of them is served by this
pipeline.

| Type | Sourced from | In this pipeline |
|---|---|---|
| `technique_decoder` | YouTube | **Yes. The default and the only type this pipeline targets.** One mechanism, one work, explained technically. |
| `event_recap` | Moving Image Arts live events | No. Footage comes from the organisation's own events, not YouTube. |
| `figure_overview` | Career-spanning | Contested. The analysis identifies this shape as its canonical failure case, at a 261 median. See `reference/spec-conflicts.md` section 1. Do not source for it without a decision. |

## 5. Subject

Subject is secondary but not neutral.

**In scope.** Film craft, history, and technique. Canon narrative film performs
best as a decoder, 2,262 median. Avant-garde and video art also work, 1,322.
Fame of the subject predicts nothing, so an obscure 1928 Dada short is as
viable as a canonical feature.

**Out of scope.** Internet and contemporary media subjects. Five posts, none
above 266, including one written as a correct decoder. The reason is structural
rather than editorial: the account can surface in a film history niche and
cannot in a general content-creation one. Do not source videos whose subject is
social platforms, creator culture, or contemporary digital media.

**The modern parallel is a landing, not a premise.** Source footage for the
film craft argument, not for the contemporary comparison. Roughly 90 percent
film craft, one closing sentence of connection. Sources built around a
present-day comparison as their organising claim perform like surveys.

## 6. Rights

Every candidate carries a `rights` value. A candidate whose rights cannot be
established is rejected with reason `rights-unclear`.

The decoder format helps here rather than hurting. A clip that states a rule,
demonstrates it on screen, and generalises it is doing analysis, which sits
better under a commentary and criticism posture than footage posted without
comment. Keep that alignment deliberate: the caption should do visible
analytical work on the footage it uses.

Watch the layering. A video essay is two rights questions, the essayist's work
and the underlying film. An archival or restoration upload is usually one. A
public domain film uploaded with an added score or new titles is two again.
Prefer the shallowest stack that still demonstrates the mechanism.

| Value | Meaning |
|---|---|
| `public-domain` | Term expired or never held. Safest. |
| `cc-by` | Creative Commons, attribution required in the caption. |
| `own-channel` | Moving Image Arts holds or controls the footage. |
| `licensed` | Written permission exists. Note where it is recorded. |
| `commentary` | Used as the subject of analysis. Depends on the caption actually doing that work. |
| `unclear` | Reject. |

TODO: confirm which values are acceptable in practice, and where any license or
permission records are kept.

## 7. Search Terms

TODO. The one part of the profile the analysis does not supply, because it
measured published posts rather than how their sources were found.

Worth recording as the pipeline runs:

- Terms that produced usable sources
- Terms that looked promising and returned noise
- Channels that repeatedly yield clean, croppable footage of single works

Until this section is filled, discovery runs on supplied links or web search
against the mechanism vocabulary in section 2.

## 8. Clip Shape

| Setting | Value |
|---|---|
| Aspect ratio | `portrait` (9:16), always set explicitly |
| Target duration | No fixed target. Length does not predict performance. Let the mechanism decide how long it takes to prove. |
| `clipDurationsSec` | Leave wide. Constraining it optimises for a variable that showed r = +0.06. |
| `enableAutoHook` | **Off.** It prepends an AI hook, and hook lines are explicitly against the house voice. The first sentence has to be the mechanism, which is an editorial decision, not a generated one. |
| Captions | On. |
| Brand template | Org has only the two stock presets, neither branded. `Preset template 1` is the default and is **landscape**. `Preset template 2` is portrait but uses word-level karaoke animation, which fights the voice. A branded portrait template needs creating. |

`customPrompt` should name the specific mechanism being demonstrated, so
curation favours the segment where it is visible.

**Grounding factual claims.** The voice spec requires every factual claim to
come from a verifiable source rather than general familiarity, and says to ask
for the clip's transcript rather than guess at its content. `opusclip_get_transcript`
satisfies this directly: pull the transcript before writing any caption that
quotes or paraphrases what is said on screen.

## 9. Volume and Budget

Cadence drives totals more than per-post quality does. Three to four reels a
day produced 251,451 views in five days; three reels over six days produced
7,819, with the same formula applied.

This collides with the Opus budget, and the collision defines the sourcing
strategy:

- 900 credits per month, billed per source minute
- Three to four reels a day is roughly 100 reels a month
- That allows about **9 source-minutes per published reel**

A 45 minute source therefore has to yield about five usable clips to stay in
budget. Single-mechanism short sources do not sustain the cadence on their own.
Prefer sources rich enough to carry several distinct mechanisms, and use
`rangeStart`/`rangeEnd` to submit only the stretches that do.

Check `opusclip_get_usage` before every batch.
