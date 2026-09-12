---
name: "yt-sourcing"
description: "Sources YouTube clips for Moving Image Arts Instagram and runs them through Opus Clip for review. Use when the user asks to pull YouTube candidates, find clips, run the sourcing pass, check the clip queue, or submit and review clips for Moving Image Arts. Screens candidates against CRITERIA.md before spending Opus credits, then previews finished clips in chat for approval. Never refer to the organization as MIAC."
---

# YouTube Sourcing Pipeline

Sources candidate YouTube videos, screens them against the criteria, runs the
survivors through Opus Clip, and brings finished clips back for human review
before anything is scheduled.

Voice, caption, and hashtag rules live in the `miac-content` skill. This skill
covers sourcing and processing only. Do not restate caption rules here.

**Naming rule: never use "MIAC". The name is Moving Image Arts.**

## Account Constants

| Thing | Value |
|---|---|
| Metricool brand ID | `6780970` |
| Metricool timezone | `Europe/Madrid` |
| Instagram post account ID | `69b8b7924be415e37283b877` |
| Facebook Page post account ID | `6a8dc0b745a6d7099fbf3b3a` |
| Opus Clip plan | PRO, API access enabled |
| Opus monthly credits | 900, resets the 1st |

Opus bills roughly **1 credit per minute of SOURCE video**, not per clip. A
90 minute lecture costs 90 credits whether it yields one clip or ten. This is
why screening happens before submission, and why long sources get a range.

## Step 1: Discover Candidates

Pull tracked-channel videos from Metricool:

```
getAnalyticsDataByMetrics(
  brandId: "6780970",
  from:    <ISO 8601, start of window>,
  to:      <ISO 8601, now>,
  metrics: ["YTCV01","YTCV03","YTCV04","YTCV06","YTCV07","YTCV08","YTCV09"]
)
```

Those fields are, in order: published date, channel name, watch URL, title,
views, comments, likes.

Requires YouTube connected on the brand in Metricool with the source channels
added as tracked competitors. If the call returns nothing for YouTube, say so
plainly rather than silently falling back. The user can also hand over URLs
directly, which skip to Step 2.

Drop any URL already present in `queue/candidates.json` in any status. The
queue is the dedup record.

## Step 2: Screen Against Criteria

Read `CRITERIA.md` in this directory and apply it to every candidate.

Screening happens BEFORE submission because submission costs credits. For each
candidate, record the specific reason it passed or failed. A candidate that
fails goes into the queue as `rejected` with its reason, so the same video is
not reconsidered next run.

Every candidate needs a `rights` value before it can be submitted. Reposting
third party footage is the real exposure in this pipeline. If rights cannot be
established, the candidate is `rejected` with reason `rights-unclear`.

## Step 3: Submit to Opus Clip

Check headroom first with `opusclip_get_usage`. If the batch's total source
minutes exceed the remaining monthly credits, submit the highest ranked
candidates that fit and leave the rest as `candidate`. Report what was deferred.

```
opusclip_submit_project(
  videoUrl:     <the YouTube watch URL, passed directly, no download>,
  aspectRatio:  "portrait",
  title:        <source title>,
  rangeStart:   <seconds, when only part of a long source is relevant>,
  rangeEnd:     <seconds>,
  customPrompt: <steer curation using the criteria's editorial angle>
)
```

Opus accepts YouTube URLs natively. Never download the video, and never use
yt-dlp or ffmpeg here.

Use `rangeStart` and `rangeEnd` aggressively on long sources. They bound which
part of the video clips are drawn from, and they cut the credit cost.

Record the returned project ID in the queue and set status to `submitted`.

## Step 4: Poll, Then Review in Chat

Poll `opusclip_list_clips` until processing finishes. Concurrency limit is 10
in-flight projects.

When clips are ready, call `opusclip_preview_clips(projectId)` to render
playable ranked cards in chat. This is the review gate.

**Stop here and wait.** Do not export, schedule, or post without explicit
approval on specific clips. Set status to `reviewed`.

## Step 5: Export and Schedule Approved Clips

Only for clips the user approved by name or rank.

1. `opusclip_export_clip` on each approved clip
2. Write the caption using the `miac-content` skill's voice rules
3. `getBestTimeToPostByNetwork(brandId: "6780970", socialNetwork: "instagram", timezone: "Europe/Madrid", ...)` to pick the slot
4. `opusclip_schedule_publish` to Instagram account `69b8b7924be415e37283b877`

Set status to `scheduled` and record the scheduled time.

## Step 6: Commit the Queue

The container running this is ephemeral. State that is not committed is lost.

Commit `queue/candidates.json` at the end of every run, whatever happened. A
run that sourced nothing still commits, so the dedup record stays accurate.

## Queue Record Schema

`queue/candidates.json` is a JSON array. One record per candidate:

```json
{
  "id":            "yt-<video id>",
  "url":           "https://www.youtube.com/watch?v=...",
  "title":         "source video title",
  "channel":       "channel name",
  "published":     "ISO 8601 date",
  "source_views":  0,
  "discovered":    "ISO 8601 date this entered the queue",
  "status":        "candidate | submitted | reviewed | scheduled | rejected",
  "rights":        "public-domain | cc-by | own-channel | licensed | commentary | unclear",
  "screen_notes":  "the specific reason this passed or failed",
  "range":         { "start_sec": null, "end_sec": null },
  "opus_project":  null,
  "approved_clips": [],
  "scheduled_at":  null
}
```

Status meanings:

- `candidate` passed screening, not yet submitted, may be waiting on credits
- `submitted` in Opus, processing or awaiting review
- `reviewed` clips previewed, awaiting or partially given approval
- `scheduled` approved clips are queued to post
- `rejected` failed screening, kept so it is not reconsidered

## Tuning the Criteria

Instagram reel performance is the feedback signal. Useful fields on the
`instagram / reels` connector:

| Field | Metric |
|---|---|
| `IGRE27` | retention, average percent of video viewed |
| `IGRE28` | reel view rate, watched past three seconds |
| `IGRE12` | saves |
| `IGRE21` | shares |
| `IGRE24` | average watch time |

Retention and saves say more about whether a sourcing rule is working than
likes do. When a pattern is clear across several posts, propose a criteria
change to the user. Do not edit `CRITERIA.md` unilaterally.
