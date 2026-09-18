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

## 1b. The Mechanism Needs a Turn

The apparatus is not the story. A person doing something is the story, and the
apparatus is what they did it with.

A segment that only describes equipment is inert, however precise it is. A
bracket, a wheelchair, a lens height: these are facts, and facts alone do not
hold anyone. What holds is a **reversal**, something going differently than
expected, with the technique sitting inside it.

Look at where the turn is in the captions that performed:

| Post | The turn |
|---|---|
| *McCabe & Mrs. Miller* flashing | Warner Bros. executives read the dailies as ruined footage |
| Méliès stop trick | The camera jams, a bus becomes a hearse, and a historian later disputes that it was an accident at all |
| *Excalibur* | Five months of near-constant rain, which the production leaned into rather than fought |
| Steadicam telex | Kubrick spots fourteen exposed frames nobody else caught, then buries the decisive question at the end |
| Coates on the cut | She would have rendered the dissolve on digital and never seen the straight cut at all |

And where it is absent in the ones that failed: an artist trained as a painter,
an artist who did not begin as a filmmaker, a theoretical position, five
categories of montage. Description without event.

**Screen for this directly.** Does something go wrong, get caught, get
disputed, get refused, or surprise the person who did it? If the segment is
only a correct account of how something was built, it will read as a
specification rather than a story, regardless of how good the technique is.

This sharpens the constraint rule in section 1. A production constraint matters
because it supplies a turn, not because a constraint is inherently interesting.

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
| **Footage of the work itself** | The source must show the film. A person talking to camera with no footage cannot demonstrate anything. Narration laid over the footage is fine and is usually better. | The proof has to be on screen. Narration that points at what is visible does the "state a rule" work while the footage does the "prove it" work. |
| **Survives the delivery format** | The mechanism must still be perceptible as a vertical clip on a phone speaker. Spatial and multichannel sound mechanisms fail here: the proof is the position of sound around a listener, which mono phone playback destroys. | Ruled out Walter Murch's quintaphonic mix on *Apocalypse Now*, a strong mechanism by every other test. Screen for this before the research, not after. |
| **Clean enough to crop** | Will survive a 9:16 crop and the subtitle burn. | Letterboxed or low-resolution uploads degrade badly in portrait. |
| **Minimum duration** | **Roughly ten minutes.** A 1 to 3 minute target clip needs a source several times longer to leave any choice. | A 111 second source cannot yield the target format at all, whatever the curation does. |
| ~~Minimum duration~~ | Superseded. Previously: roughly three minutes. Below that a source yields few clips, lower curation scores, and no room to choose. | The Coates interview ran about 111 seconds and produced three usable clips against nine from a source four times longer. |
| **Duration** | Not a quality filter. Length showed no correlation with performance, r = +0.06. Treat source length purely as an Opus credit cost. | A 28 second and a 172 second post both broke out. |

## 3a. Required Structure: Speaker On Camera and Voice Under the Examples

The target format is a mix of the practitioner **on camera** and the same
practitioner **as voice over the film examples**. The clip should move between
the two rather than sitting in either.

**This is a property of the source, not something Opus can create.** Opus cuts
and reframes what it is given. If the source alternates between a talking head
and film clips playing with their own audio, every clip drawn from it will
alternate the same way.

So screen the source for how it was cut:

| Pattern | Usable |
|---|---|
| Practitioner speaks; their voice continues while the film example plays underneath | **Yes. This is the target.** |
| Practitioner speaks, then the film plays with its own dialogue and sound, then they resume | Weak. Reads as an interview with illustrations rather than an explanation. |
| Practitioner on camera throughout, no footage | No. Nothing is demonstrated. |

A transcript gives a partial signal: film dialogue appearing as its own speaker
turns means the film is playing with its own audio at least some of the time.
It cannot confirm the good case, since a voice continuing over silent footage
looks identical to a voice over a static shot.

Properly produced documentaries and featurettes do this by construction, which
is why `Visions of Light` and `The Cutting Edge` are the model. A two-camera
interview with clips dropped in usually does not.

## 3b. Narration and Source Provenance

Narrated sources suit Opus Clip considerably better than silent footage.
Curation ranks segments from the transcript and captions are generated from
speech, so a source with no speech gives the tool almost nothing to work with.

But where the narration comes from changes what the post is. Three source
types, in descending order of preference:

| Type | Narration | Whose analysis | Rights layers | Voice match |
|---|---|---|---|---|
| **Primary source** | The practitioner explaining their own work: interviews, commentary tracks, department oral histories, archival lectures | Theirs, and authoritative | Usually one, sometimes none | Neutral. An expert speaking plainly reads as analysis, not as another channel's branding |
| **Own narration** | Generated or recorded in the house voice over clean footage | Moving Image Arts | One, the underlying film | Exact, by construction |
| **Third-party video essay** | Another creator's essay | Theirs, borrowed | Two: the essayist's work and the underlying film | Poor. Another channel's register in your feed |

**Prefer primary source.** It matches the account's strongest measured
signature directly: seven of the top nine posts name a technical collaborator,
and the strongest available version of that is the collaborator explaining the
work in their own voice.

**Own narration is the default** where no primary-source interview exists.
`audio_tts` and `audio_tts_direction` on the Magnific connector can generate it
against the house voice rules.

**Third-party video essays are the fallback, and a weak one.** The post becomes
a repost of someone else's analysis rather than the account doing the work,
which is both the brand problem and the thing the commentary posture in section
6 rests on. If used at all, credit the essayist in the caption.

**Note on government-produced sources.** Material produced by US federal
agencies is generally not subject to copyright, which makes an agency-produced
interview unusually clean. That covers the agency's own footage only. Film
clips embedded inside such a video carry their own rights.

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

**The remit is visual storytelling.** Visual technique, cinematography,
editing, camera, light, colour, and anything else carried by the moving image.
This is a positioning rule set by the organisation, not an inference from
performance, and it overrides the measured data where they disagree.

It does disagree in one place worth knowing. The analysis found sound
outperforms editing and camera, and the account's eight-track recording post
is among its largest, on the reasoning that the test is demonstrable in the
clip rather than visible in a frame. The remit gives that category up
deliberately. Open question recorded in `spec-conflicts.md`: whether sound for
film is out entirely, or only when detached from the image.

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

## 6. Rights and Detection

**Posture, as determined by the organisation.** Moving Image Arts is a
non-profit and this material is used for educational purposes. Clips are short
excerpts from feature films, used as the subject of technical analysis, in
captions that do visible analytical work on the footage they show. This is a
commentary and criticism use. That determination is settled and is not
relitigated per candidate.

Sourcing therefore does **not** restrict to public domain and Creative Commons.
Restricting that way would exclude the category that produced the account's four
largest posts.

### What still needs tracking

Automated platform enforcement is a separate system from the legal question and
does not perform a fair use analysis. Meta's Rights Manager matches content and
acts on the match. A clip can be squarely defensible and still be muted, blocked
or removed, and repeated flags carry account-level consequences that are worth
more than any single post.

So the `rights` field stays, but its job changes. It no longer gates
publication. It records exposure, so the pattern is visible across the queue
rather than discovered through a strike.

| Value | Detection exposure |
|---|---|
| `public-domain` | None. No match to assert. |
| `cc-by` | None in practice. Attribute in the caption. |
| `own-channel` | None. |
| `licensed` | None. Note where the permission is recorded. |
| `commentary` | Real. The default for studio features. Defensible, and still matchable. |
| `unclear` | Treat as `commentary` for exposure purposes, and note why it could not be determined. |

### Practical notes

**Audio is the strongest detection vector.** Matching is more aggressive on
audio than on picture, and most aggressive on music. A clip carrying a film's
score is more exposed than one carrying dialogue or room tone. This bears
directly on sound-mechanism posts, which are among the account's best
performers, so it is a tradeoff to make knowingly rather than a reason to avoid
the category.

**Shorter excerpts are both better practice and lower exposure.** The analysis
found length uncorrelated with performance, so there is no cost to taking only
what demonstrates the mechanism.

**The caption is part of the posture.** A decoder caption states a rule,
demonstrates it, and generalises it, which is the analytical work that
distinguishes this use from reposting. Keeping captions genuinely analytical is
not only the thing that performs, it is the thing that makes the use what the
organisation says it is. A clip posted without that work is weaker on both
counts.

**Public domain carries zero detection exposure and holds attention best.** The
Richter and Méliès post holds 70.3 percent, the highest on the account. Public
domain sourcing is not a fallback, it is a strong category on its own terms.
Prefer it where a mechanism can be demonstrated equally well from it.

**If a post is flagged**, record it against the candidate in the queue. A
pattern across several flags is worth more than any single one, and only the
queue will show it.

## 7. Search Terms

Reverse-engineered from the top performing posts in
`reference/what-search-found-them.md`. Nothing recorded how the historical
sources were found, so these are inferred from what each post needed in order
to exist. The `found_via` field in the queue records it going forward.

**Search in two stages. The first is not YouTube.**

### Stage one, the mechanism

| Pattern | Example |
|---|---|
| `<cinematographer> <film> cinematography` | Gordon Willis, *The Parallax View* |
| `<named technique> <film or era>` | flashing, *McCabe & Mrs. Miller* |
| `how <film> achieved <look>` | *Excalibur* green filtration |
| `<film> production history <department>` | *Nashville* sound department |

Sources: production histories, American Cinematographer and ASC interviews,
technical retrospectives, commentary transcripts, department oral histories.

**Bias toward the technical collaborator, not the director.** Seven of the top
nine posts name a cinematographer or sound designer. Director-name searches
return career surveys, which is the failing shape.

**Prefer mechanisms with a production constraint attached.** A camera immobilised
because microphones caught its noise. Executives reading flashed dailies as
ruined footage. Five months of rain absorbed into a palette. The constraint is
what makes the rule portable.

### Stage two, the footage

| Pattern | Purpose |
|---|---|
| `<film title> <year> clip` | general |
| `<film title> <scene where the mechanism is visible>` | targeted |
| `<film title> restoration trailer` | clean transfers |

### Terms that produce the failing shape

Avoid as entry points. Each produced a post below 1,700 views.

- A director or artist name alone, which returns biography and career overview
- `<artist> philosophy` or `<artist> approach`, untethered to one work
- Categories and taxonomies rather than one operation

TODO as the pipeline runs: record which literature sources repeatedly yield
usable mechanisms, and which channels yield clean croppable transfers.

## 8. Clip Shape

| Setting | Value |
|---|---|
| Aspect ratio | `portrait` (9:16), always set explicitly |
| Target duration | **60 to 180 seconds.** Set it explicitly with `clipDurationsSec: [[60, 180]]` on submission. Clips under about 30 seconds read as fragments. |
| ~~Target duration~~ | Superseded. Previously: give it room. Length does not predict performance (r = +0.06), so brevity buys nothing, and clips under roughly 30 seconds have read as fragments: they state a fact and stop before anything develops. Prefer segments with space for a turn to land. Working preference is roughly 45 to 90 seconds, from editorial judgement rather than measurement. |
| `clipDurationsSec` | `[[60, 180]]`. Always set it, but treat it as a preference rather than a guarantee. It held exactly on a 15 minute source and was ignored on a 4.7 minute one, which returned clips of 30 to 47 seconds. A short source cannot be carved into many segments of a minute or more, so Opus degrades rather than refusing. This is a further argument for the source length floor: below it, the format target silently stops applying. The earlier advice to leave this wide was wrong: it reasoned from performance data, where length is uncorrelated, but clip length here is an editorial format decision rather than a performance one. |
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
