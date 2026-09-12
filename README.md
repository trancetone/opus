# opus

Sourcing pipeline for Moving Image Arts Instagram.

Pulls candidate videos from tracked YouTube channels, screens them against
editorial criteria, runs the survivors through Opus Clip, and holds finished
clips for human review before anything is scheduled.

## Layout

| Path | Contents |
|---|---|
| `.claude/skills/yt-sourcing/SKILL.md` | The pipeline. Loaded automatically when this repo is open in a Claude session. |
| `.claude/skills/yt-sourcing/CRITERIA.md` | What qualifies a video. Currently a scaffold with TODOs. |
| `queue/candidates.json` | Candidate state and dedup record. |

Voice, caption, and hashtag rules live in the separate account level
`miac-content` skill, not here.

## Why state lives in git

Claude sessions run in ephemeral containers that are reclaimed after a period
of inactivity. Anything not committed is lost when that happens. Keeping the
queue in the repository means a run can be picked up from any machine, and the
dedup record survives.

## Status

Scaffold. Two things are outstanding before the pipeline can run:

1. **Criteria.** The editorial sections of `CRITERIA.md` are TODO.
2. **Discovery.** Metricool brand `6780970` has Instagram and Facebook
   connected but not YouTube. Discovery depends on connecting YouTube on that
   brand and adding the source channels as tracked competitors, which exposes
   their videos through the `youtube / competitor videos` connector. Until
   then, candidate URLs have to be supplied by hand.
