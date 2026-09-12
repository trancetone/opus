# Sourcing Criteria

What qualifies a YouTube video as a candidate for Moving Image Arts Instagram.

> **STATUS: SCAFFOLD.** The editorial sections below are placeholders marked
> TODO. They are deliberately not filled in with guesses. Until the owner
> supplies them, screening cannot run unattended, and any candidate should be
> brought to the user rather than auto-passed.

## 1. Curatorial Profile

The standing description of what the Moving Image Arts audience actually
responds to, derived from Instagram performance rather than asserted from
taste. Step 1 of the skill regenerates the evidence for this; this section is
where the conclusion lives between runs.

Rank past reels by retention (`IGRE27`) and saves (`IGRE12`), not likes. Then
name what the top performers share.

TODO: fill in once a look-back has been run.

| Dimension | What performs | Evidence |
|---|---|---|
| Subject | TODO | |
| Era or period | TODO | |
| Visual texture | TODO | |
| Pacing | TODO | |
| Speech or silent | TODO | |
| Clip length | TODO | |

**Search terms.** The profile expressed as things to actually type into
YouTube.

TODO: list them. Include terms that have produced good candidates and terms
that looked promising but returned noise, since knowing what not to search is
half the value.

## 2. Subject Matter

TODO: what the video has to be about to qualify.

The `miac-content` skill names the existing content territory as film history,
visual art, cinema culture, experimental film, digital art, and documentary.
State here how sourcing narrows or extends that, and name what is out of scope.

## 3. Hard Filters

Mechanical rules applied before any editorial judgment. A candidate failing any
of these is rejected without further consideration.

| Filter | Rule | Rationale |
|---|---|---|
| Source duration | TODO | Opus bills per source minute, so this is the main cost control |
| Minimum views | TODO | |
| Maximum age | TODO | |
| Language | TODO | |
| Has usable speech or is visual-only | TODO | Affects whether captions carry the clip |
| Resolution floor | TODO | Upscaled or low-resolution sources look worse after a 9:16 crop |

## 4. Rights

Every candidate carries a `rights` value. A candidate whose rights cannot be
established is rejected with reason `rights-unclear`.

Open search across YouTube returns mostly rights-reserved material, so in
practice this filter rejects more candidates than the editorial ones do. Two
things make it cheaper to satisfy: YouTube's own Creative Commons filter
(`videoLicense=creativeCommon` on the Data API, or the Features filter in the
web interface), and preferring sources whose underlying footage is old enough
to be out of copyright.

| Value | Meaning |
|---|---|
| `public-domain` | Term expired or never held. Safest. |
| `cc-by` | Creative Commons, attribution required in the caption. |
| `own-channel` | Moving Image Arts holds or controls the footage. |
| `licensed` | Written permission exists. Note where it is recorded. |
| `commentary` | Used as the subject of commentary or criticism. Narrower than it looks, and it depends on the caption actually doing commentary work. |
| `unclear` | Reject. |

Note that a YouTube uploader's own license is not always theirs to grant. A
public domain film uploaded by a channel that added its own score or titles is
two rights questions, not one.

TODO: confirm which values are acceptable in practice, and where license or
permission records are kept.

## 5. Editorial Judgment

Applied to candidates that clear the hard filters.

TODO: describe what makes a clip strong rather than merely eligible. The most
useful form is a handful of worked examples, both directions: videos that
should have been pulled, and near misses that should not.

## 6. Clip Shape

What the finished Instagram clip should look like. Feeds `customPrompt`,
`clipDurationsSec`, and the range on submission.

| Setting | Value |
|---|---|
| Aspect ratio | `portrait` (9:16), always set explicitly |
| Target duration | TODO. The `miac-content` skill says Reels run 10 to 30 seconds. |
| Captions | TODO |
| Auto hook | TODO. `enableAutoHook` prepends an AI generated hook, which may conflict with the Moving Image Arts voice rules. |
| Brand template | TODO. Org currently has only the two stock presets, neither branded. `Preset template 1` is the default and is **landscape**, so `aspectRatio` must always be set explicitly. `Preset template 2` is portrait but uses word-level karaoke caption animation, which fights the Moving Image Arts voice. A branded portrait template needs creating. |

## 7. Volume

TODO: how many candidates per run, and how many scheduled posts per week.

Budget context: 900 Opus credits per month, billed per source minute. Twenty
sources averaging fifteen minutes each costs 300 credits, so roughly sixty
such sources per month is the ceiling.
