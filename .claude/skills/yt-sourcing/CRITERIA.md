# Sourcing Criteria

What qualifies a YouTube video as a candidate for Moving Image Arts Instagram.

> **STATUS: SCAFFOLD.** The editorial sections below are placeholders marked
> TODO. They are deliberately not filled in with guesses. Until the owner
> supplies them, screening cannot run unattended, and any candidate should be
> brought to the user rather than auto-passed.

## 1. Source Channels

Channels tracked in Metricool as the discovery feed.

TODO: list the channels. For each, note whether everything it posts is worth
screening, or only a particular series or format.

| Channel | Scope | Notes |
|---|---|---|
| TODO | | |

## 2. Subject Matter

TODO: what the video has to be about to qualify.

The `miac-content` skill names the existing content territory as film history,
visual art, cinema culture, experimental film, digital art, and documentary.
State here how the YouTube sourcing narrows or extends that, and name the
subjects that are explicitly out of scope.

## 3. Hard Filters

Mechanical rules applied before any editorial judgment. A candidate failing any
of these is rejected without further consideration.

| Filter | Rule | Rationale |
|---|---|---|
| Source duration | TODO | Opus bills per source minute, so this is a cost control |
| Minimum views | TODO | |
| Maximum age | TODO | |
| Language | TODO | |
| Has usable speech or is visual-only | TODO | Affects whether captions carry the clip |

## 4. Rights

Every candidate carries a `rights` value. A candidate whose rights cannot be
established is rejected with reason `rights-unclear`. This is not optional and
is not a judgment call to defer to the model.

| Value | Meaning |
|---|---|
| `public-domain` | Term expired or never held. Safest. |
| `cc-by` | Creative Commons, attribution required in the caption. |
| `own-channel` | Moving Image Arts holds or controls the footage. |
| `licensed` | Written permission exists. Note where it is recorded. |
| `commentary` | Used as the subject of commentary or criticism. Narrower than it looks, and it depends on the caption actually doing commentary work. |
| `unclear` | Reject. |

TODO: confirm which of these values are acceptable in practice, and where
license or permission records are kept.

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
| Aspect ratio | `portrait` (9:16) |
| Target duration | TODO. The `miac-content` skill says Reels run 10 to 30 seconds. |
| Captions | TODO |
| Auto hook | TODO. `enableAutoHook` prepends an AI generated hook, which may conflict with the Moving Image Arts voice rules. |
| Brand template | TODO. Check `opusclip_list_brand_templates`. |

## 7. Volume

TODO: how many candidates per run, and how many scheduled posts per week.

Budget context: 900 Opus credits per month, billed per source minute. Twenty
sources averaging fifteen minutes each costs 300 credits, so roughly sixty
such sources per month is the ceiling.
