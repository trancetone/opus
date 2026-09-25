# What Search Unearthed the Top Posts

Reverse-engineered from the 65 reels published 25 Jul to 12 Sept 2026, pulled
from Metricool on 12 Sept.

**Caveat on method.** Nothing records how a source was found. Metricool stores
what was published, not how it was discovered. What follows is inferred from
what each post needed in order to exist, not recovered from a log. The
`found_via` field in `queue/candidates.json` records this going forward.

## The top performers

| Views | Saves | Hold | Subject | Named technique | Named collaborator |
|---|---|---|---|---|---|
| 84,180 | 2,701 | 65.8% | *Excalibur* (1981) | green filtration across exteriors | Alex Thomson |
| 63,746 | 1,646 | 63.4% | *Nashville* (1975) | portable eight-track recording | Jim Webb |
| 46,399 | 1,436 | 58.4% | *The Parallax View* (1974) | anamorphic negative space | Gordon Willis |
| 25,807 | 632 | 48.7% | *Stalker* (1979) | sepia to colour at the Zone boundary | Tarkovsky |
| 13,028 | 170 | **70.3%** | *Ghosts Before Breakfast* | stop-motion against Méliès stop trick | Richter, Méliès |
| 7,800 | 185 | 61.9% | *Zardoz* (1974) | costume colour as class marker | Geoffrey Unsworth |
| 7,538 | 197 | 53.0% | Altman 1970s | sustained zoom | Altman |
| 6,080 | 121 | 61.2% | transition to sound | the blimp, the icebox booth | — |
| 5,381 | 147 | 58.5% | *Black Narcissus* (1947) | glass matte painting for colour control | Powell and Pressburger |

## The signature

Every post above names **a specific technique** and, in seven of nine cases,
**a specific technical collaborator**, usually a cinematographer or sound
designer rather than the director.

The underperformers in the same window invert exactly that. Each of these opens
on a person and their formation rather than on a technique:

| Views | Hold | Opens on |
|---|---|---|
| 1,637 | 33.5% | Maya Deren's theoretical position |
| 1,273 | 39.7% | Greenaway trained as a painter |
| 1,030 | 42.5% | Jarman did not begin as a filmmaker |
| 1,421 | 57.2% | Eisenstein's five categories of montage |

This is the decoder and survey split visible in the source material rather than
in the caption. **Cinematographer-and-technique searches produce decoders.
Director-and-biography searches produce surveys.** The Greenaway post is the
clearest case: the analysis already flagged it as the best-researched caption on
the account, and it opens on a biography and lands at 39.7% hold.

## The finding that matters for the pipeline

These posts were not found by browsing YouTube.

The captions cite Powell on why the mountains were painted on glass, Zsigmond's
shift from pre-exposure to post-exposure between two films, Deslandes's argument
that Méliès more likely studied an Alfred Clark print than discovered the stop
trick by accident, Minett's statistical comparison of Altman's zoom usage
against seventy contemporaneous films, and Tarkovsky's own rejection of symbolic
readings in *Sculpting in Time*.

None of that surfaces from a video search. It comes from production histories,
cinematographer interviews, and film scholarship.

**So the real sequence is mechanism first, footage second.** A mechanism worth
explaining is identified in the literature, and then footage that demonstrates
it is located. The footage search is the easy half and runs second: once the
subject is *Excalibur*'s green filtration, finding *Excalibur* footage is
trivial.

A pipeline that searches YouTube first and asks what it can say about the
results is running this backwards, and it would reliably produce surveys,
because what YouTube surfaces on a director's name is retrospectives and
career overviews.

## Two search stages

**Stage one, the mechanism.** Not YouTube. Production histories, American
Cinematographer and ASC interviews, technical retrospectives, DVD commentary
transcripts, sound and camera department oral histories. The query shape that
matches the winners:

- `<cinematographer> <film> cinematography`
- `<named technique> <film or era>`
- `how <film> achieved <specific look>`
- `<film> production history <department>`

Bias toward the technical collaborator over the director. Willis, Zsigmond,
Unsworth, Thomson and Webb produced the top posts. Searching a director's name
tends to return career surveys, which is the shape that fails.

Favour mechanisms with a **production constraint story** behind them. The
strongest posts explain why a technique was adopted: a camera that could not
move because microphones picked up its noise, executives reading flashed
dailies as ruined footage, five months of Irish rain absorbed into the
palette. The constraint is what makes the rule portable.

**Stage two, the footage.** Now YouTube, and only to satisfy the demonstrable
requirement in `CRITERIA.md` section 1. Query shape:

- `<film title> <year> clip`
- `<film title> <specific scene where the mechanism is visible>`
- `<film title> restoration trailer` for clean transfers

Screen for a clean, croppable transfer that actually shows the mechanism. If no
footage demonstrates it on screen, the mechanism fails at this stage regardless
of how good the research is. Sound mechanisms need audible proof, not visible.

## One tension worth naming

The four highest-performing posts are all rights-reserved studio features:
*Excalibur*, *Nashville*, *The Parallax View*, *Stalker*.

The public domain material in the same window performs differently rather than
badly. The Richter and Méliès post holds **70.3%**, the highest hold rate on the
account, at 13,028 views. Hold rate is the leading indicator, so public domain
avant-garde sources hold attention well while reaching fewer people.

Restricting sourcing to Creative Commons and public domain would therefore
exclude the exact category that produced the account's four biggest posts. That
is a decision to take deliberately, not one to discover later. See section 6 of
`CRITERIA.md`.
