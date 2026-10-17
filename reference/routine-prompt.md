# Daily clip pull: routine prompt

Paste the block below into the **Instructions** box at
[claude.ai/code/routines](https://claude.ai/code/routines) → **New routine**.

Set these alongside it in the form, because a routine created through the MCP
tool gets none of them and is both invisible in the UI and non-functional:

| Field | Value |
|---|---|
| Name | Moving Image Arts: daily clip pull |
| Model | Opus |
| Repositories | `trancetone/opus` |
| Environment | TR01 (the one holding `YOUTUBE_API_KEY`) |
| Trigger | Schedule, daily, 6:00am, local time |
| Connectors | **Opus** and **Metricool** only. Remove the rest: Claude can use every tool from an included connector, writes included, without asking. |

The form enters times in your local zone and converts them, so daylight saving
is handled. A cron expression set through the CLI is fixed UTC and drifts an
hour in November.

---

Daily Moving Image Arts sourcing run. Work in the trancetone/opus repo on branch `claude/funny-hawking-hizpek` (check it out first; it is not the default branch).

Read before doing anything:
  .claude/skills/yt-sourcing/SKILL.md
  .claude/skills/yt-sourcing/CRITERIA.md   (sections 10 and 11 are the newest and govern clip selection)
  queue/candidates.json                    (full history and the dedup record)

The YouTube Data API key reaches this environment as YOUTUBE_API_KEY, so `python3 tools/screen_source.py <url-or-id>` works. Use it on every candidate. It costs 1 quota unit.

This run has TWO halves. Do both, in this order.

## Part A: deliver two clips for review

Find work already past the source-confirmation gate: queue entries with status `submitted` or `reviewed`, or any source the user confirmed since the last run. Submit anything confirmed but not yet submitted (check `opusclip_get_usage` for headroom first; Opus bills roughly 1 credit per source minute).

Then select TWO clips and present them for review, each with:
  - the playable preview (`opusclip_preview_clips`)
  - the FIRST SENTENCE of the clip's own transcript, quoted
  - a caption drafted to the house voice: roughly 160 words, opens on named people and the work, no em dashes, no hook lines, 5-9 hashtags, majority proper nouns
  - which mechanism it demonstrates and why it passes CRITERIA

Hard selection rules, all of which have burned this account before:
  - Read EVERY clip's transcript. Opus sub-scores discriminate nothing; one project returned 10/10/10 on all thirteen clips, and top-ranked clips have been off-profile in five consecutive projects.
  - Check who is speaking, via the source transcript's `speaker` field AND by what only that person would say. A documentary about a cinematographer is not the cinematographer narrating. Diarization mixes film audio with interview audio. On the Storaro source, the passage that sounds like Storaro describing himself is Bertolucci describing Storaro.
  - Reject any clip whose opening sentence is a general claim rather than something that happened. This is CRITERIA section 11: a clip opening on an abstraction held 39.3 percent against 66.9 percent for one opening on a specific event.
  - Discard all Opus-generated titles, descriptions and hashtags. Captions are written fresh.
  - Drop the `_bonus` duplicate.

## Part B: propose tomorrow's source, then STOP

Run Step 1 and Step 2 of the skill: pull the Metricool performance window (brand 6780970, excluding the last five days), then search the LITERATURE for a mechanism, not YouTube. Bias toward the technical collaborator over the director. Then find footage, screen it with tools/screen_source.py, and check it against CRITERIA.

Present ONE OR TWO candidate URLs with the incident, the named collaborator, and why it fits. Then STOP and ask the user to confirm one thing: does the film play while the person talks, or is it a person in a chair. Do NOT submit to Opus without that confirmation. This gate exists because five consecutive sources failed on structure, which is invisible from here.

Note: the queue currently has NO live fallback source. The Harryhausen candidate was rejected at 54 seconds.

## Never do these

  - Never post or schedule anything. Present clips and captions, and stop. Scheduling happens only on the user's explicit approval of a named clip.
  - If the user does approve a schedule, hand over the Opus approval link EXACTLY ONCE. The screen creates a schedule on every visit, including visits that display an error; one link re-offered across three messages produced three identical schedules. Then verify with `opusclip_list_scheduled_posts` using a DATE WINDOW, never a project id.
  - Never run `remove_pauses` on a source that intercuts interview with film clips. The silences are the footage.
  - Always `dryRun` an edit first.
  - Never refer to the organisation as "MIAC". The name is Moving Image Arts.

## Finish

Commit queue/candidates.json and any caption drafts to `claude/funny-hawking-hizpek` and push, whatever happened. The container is ephemeral and an uncommitted queue loses the dedup record. A run that sourced nothing still commits.

Report in chat: the two clips with captions, the candidate URL(s) awaiting confirmation, and anything that failed.
