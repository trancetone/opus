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

## 2. Caption length: under 80 words, or 80 to 160

**The conflict.** The `miac-content` skill and the analysis both say the body
runs under 80 words. The spec says roughly 80 to 160, which at the top end is
double.

**Empirical tiebreak.** The spec's own worked example is **81 words**. It sits
at the floor of its stated range, not the middle, and is consistent with the
other two documents. Nothing in either document demonstrates a 160 word caption.

**Recommendation.** Treat roughly 80 words as the working target and the 160
upper bound as unsupported. If long captions are wanted, that is a change worth
testing deliberately rather than inheriting from a range nothing exemplifies.

---

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

The analysis found hashtag specificity real but weak, r = +0.33, and found
generic tags clustering on the worst performers. The count matters less than
the proper-noun composition, which all three documents agree on.

**Recommendation.** 5 to 7, mostly proper nouns. Treat the worked example's 10
as drift rather than precedent.

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
