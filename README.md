# opus

Sourcing pipeline for Moving Image Arts Instagram.

Finds YouTube videos matching the curatorial voice of the Moving Image Arts
Instagram account, passes their links to Opus Clip to cut shorts, and holds
the results for human review before anything is scheduled.

The curatorial voice is derived from what has actually performed well on the
account, using Instagram retention and saves rather than likes.

## Layout

| Path | Contents |
|---|---|
| `.claude/skills/yt-sourcing/SKILL.md` | The pipeline. Loaded automatically when this repo is open in a Claude session. |
| `.claude/skills/yt-sourcing/CRITERIA.md` | The curatorial profile and what qualifies a video. Currently a scaffold with TODOs. |
| `queue/candidates.json` | Candidate state and dedup record. |
| `reference/decoder-clips-what-works.md` | Performance analysis of 55 reels. The evidence base for the criteria. |
| `reference/caption-voice-spec.json` | Caption voice spec, version 1.0. |
| `reference/spec-conflicts.md` | Where the voice spec and the analysis disagree. Unresolved. |

Voice, caption, and hashtag rules live in the separate account level
`miac-content` skill, not here.

## Why state lives in git

Claude sessions run in ephemeral containers that are reclaimed after a period
of inactivity. Anything not committed is lost when that happens. Keeping the
queue in the repository means a run can be picked up from any machine, and the
dedup record survives.

## Status

Scaffold. Outstanding before the pipeline can run:

1. **Spec conflicts.** Three unresolved disagreements between the voice spec
   and the performance analysis, catalogued in `reference/spec-conflicts.md`.
   One of them, whether `figure_overview` is a valid post type, changes what
   footage to look for.
2. **Discovery.** Sourcing is open search across YouTube, not a fixed
   channel list. There is no YouTube Data API key in the environment, so
   candidates currently come from supplied links or web search. Adding a key
   as `YOUTUBE_API_KEY` would allow filtering on duration and Creative
   Commons license at search time.
3. **Brand template.** Opus Clip has only the two stock presets, neither
   branded, and the default is landscape.
4. **YouTube Data API key.** Set `YOUTUBE_API_KEY` in the environment
   configuration, not a shell export, since session containers are
   disposable. Tested from inside a session: `youtube.com` is blocked by
   network policy but `googleapis.com` is reachable and returns a normal
   403 asking for a key, so the API works from here. It supplies the
   provenance check (`snippet.channelId`, confirming a video is an
   institution's own upload), source duration against the ten minute
   floor, licence, and real search. It does not supply video: no key lets
   an agent watch a clip, so judging framing stays a human step.
5. **Search terms.** Section 7 of `CRITERIA.md`. The analysis measured
   published posts, not how their sources were found, so this is the one part
   of the profile it cannot supply.
6. ~~**Rights.**~~ Resolved. Non-profit educational commentary use. Sourcing
   is not restricted to public domain. Section 6 now tracks platform detection
   exposure, which is a separate matter from the rights posture.
