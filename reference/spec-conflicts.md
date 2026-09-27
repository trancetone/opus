# Unresolved Conflicts Between the Voice Spec and the Performance Analysis

Three documents govern Moving Image Arts output and they do not agree. Listed
here so the pipeline does not quietly pick one and so the choices are made
deliberately.

| Source | What it is |
|---|---|
| `miac-content` skill | Account level house style, not in this repo |
| `reference/decoder-clips-what-works.md` | Measured analysis, 55 reels, Aug to Sept 2026 |
| `reference/caption-voice-spec.json` | Caption voice spec, version 1.0 |

The spec appears to predate the analysis, or at least not to incorporate it.

---

## 1. `figure_overview` is the analysis's canonical failure case

**The conflict.** The spec defines `figure_overview` as a valid post type,
"general philosophy/role of an artist across their career, not tied to one
piece," and gives two example subjects, one of which is Nam June Paik's role in
founding video art.

The analysis lists, as its worked example of a caption that fails, a sentence
stating that Nam June Paik is widely credited as the originator of video art.
It recorded 114 views. The analysis groups this shape as "survey" and measures
surveys at a 261 median against 2,954 for decoders, and says plainly that one
mechanism and one work is the rule.

So the spec's second post type, and one of its two named examples, is the exact
thing the analysis identifies as what kills a clip.

**Why it matters for sourcing.** A career-spanning figure overview needs
different footage, usually multiple works or an interview, than a single
mechanism demonstration. Screening cannot serve both.

**Recommendation.** Drop `figure_overview`, or restrict it to cases where a
career-level claim is still demonstrable on screen in one clip. Default to
`technique_decoder`.

---

## 2. Caption length: measured, not asserted

**The conflict.** The `miac-content` skill and the analysis both say the body
runs under 80 words. The spec says roughly 80 to 160.

**Neither is right.** Measured against the captions actually published, both
documents understate it. Sampling the top performers:

| Post | Views | Body words |
|---|---|---|
| *Excalibur* green filtration | 84,180 | ~183 |
| *McCabe & Mrs. Miller* flashing | 3,716 | ~200 |
| *The Parallax View* anamorphic | 46,399 | ~175 |
| Altman zoom lens | 7,538 | ~195 |
| Méliès stop trick | 738 | ~190 |

**Working range: 175 to 200 words.** The 80 word rule describes nothing that
was published. The spec's 80 to 160 is closer but still short at the top end.

An earlier version of this file argued the spec's own worked example (81 words)
settled the question in favour of the short rule. That was wrong: the worked
example is unrepresentative of the published captions, which run more than
twice its length.

Note that length does not predict performance, r = +0.06. The reason to match
~180 words is consistency of voice, not reach.

## 3. The banned-openers rule tests a variable the analysis ruled out

**The conflict.** The spec bans, as literal first words, constructions like
"<Name> was/is/describes/began/trained as". That is a syntactic rule.

The analysis explicitly tested opener syntax and found it predicted nothing:
a mechanical test on whether a caption opens on a person or on a work had no
predictive value, and it notes that **the two biggest posts on the account both
open on a person's name**. Its conclusion is that the distinction is semantic,
not syntactic.

Applied literally, the spec's rule would reject the account's two best posts.

**Why the spec is still pointing at something real.** Bio openers correlate
with survey captions. The rule works as a smell test and fails as a filter.

**Recommendation.** Keep it as a warning, not a rejection. Replace the filter
with the analysis's semantic test: does the first sentence hand the viewer a
rule they could apply to a film that is never mentioned? A caption opening on a
person's name passes if the rest of the sentence delivers the mechanism.

---

## 4. Hashtag count, minor

The skill and the analysis say 5 to 7. The spec says 5 to 9. The spec's own
worked example carries **10**, exceeding its own range.

**Measured practice is 6 to 8.** Excalibur and the flashing post carry 8,
Méliès and Parallax View 7, Varda 6. So the spec's 5 to 9 is about right and
the skill's 5 to 7 is slightly narrow.

The analysis found hashtag specificity real but weak, r = +0.33, and found
generic tags clustering on the worst performers. The count matters less than
the proper-noun composition, which all three documents agree on.

**Recommendation.** 6 to 8, mostly proper nouns, closing on #FilmHistory and
#MovingImageArts as the published captions consistently do.

---

## 5. Open question: "Buzz"

The spec's `event_recap` type refers to a 1-in-3 Buzz-specific post cap, going
to 1-in-1 in a final countdown week, citing an IG content strategy document not
in this repository. The analysis separately records a "Buzz pastiche" post at
254 views as an example of a modern parallel placed as the core claim rather
than the closing line.

Not resolvable from the documents supplied. Needs the content strategy document
or an explanation of what Buzz is before `event_recap` can be automated. Event
clips come from Moving Image Arts live events rather than YouTube, so this sits
outside the sourcing pipeline either way.

---

## 6. Open question: does the visual remit exclude sound for film

The organisation's stated remit is visual storytelling: visual technique,
cinematography, editing, and anything carried by the moving image. Sound
mechanisms are therefore not sourced.

This is a deliberate positioning choice and it overrides the performance data,
which points the other way. The analysis records that light, colour and sound
outperform editing and camera, and that the requirement is a mechanism
demonstrable in the clip rather than visible in a frame, citing the Altman
eight-track post at over 50,000 views as a sound mechanism that is not visible
at all.

Unresolved: whether sound for film is excluded entirely, or only when it is
detached from the image. A post about how a sound was built to accompany a
specific visual event would sit differently from one about a sound effect
considered on its own.
