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

Voice, caption, and hashtag rules live in the separate account level
`miac-content` skill, not here.

## Why state lives in git

Claude sessions run in ephemeral containers that are reclaimed after a period
of inactivity. Anything not committed is lost when that happens. Keeping the
queue in the repository means a run can be picked up from any machine, and the
dedup record survives.

## Status

Scaffold. Three things are outstanding before the pipeline can run:

1. **Criteria.** The editorial sections of `CRITERIA.md` are TODO.
2. **Discovery.** Sourcing is open search across YouTube, not a fixed
   channel list. There is no YouTube Data API key in the environment, so
   candidates currently come from supplied links or web search. Adding a key
   as `YOUTUBE_API_KEY` would allow filtering on duration and Creative
   Commons license at search time.
3. **Brand template.** Opus Clip has only the two stock presets, neither
   branded, and the default is landscape.
