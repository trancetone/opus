---
name: "yt-sourcing"
description: "Finds YouTube videos matching the Moving Image Arts curatorial voice and runs them through Opus Clip to cut shorts for Instagram. Use when the user asks to pull YouTube candidates, find clips, run the sourcing pass, check the clip queue, or submit and review clips for Moving Image Arts. Derives the curatorial profile from what has performed well on Instagram, screens candidates before spending Opus credits, then previews finished clips in chat for approval. Never refer to the organization as MIAC."
---

# YouTube Sourcing Pipeline

Identifies a film-craft mechanism worth explaining, finds YouTube footage that
demonstrates it, passes the link to Opus Clip to cut shorts, and brings the
results back for human review before anything is scheduled.

**The order matters.** Research first, footage second. See Step 2.

The curatorial voice is not asserted from taste. It is derived from what has
actually performed well on the Instagram account, then applied as a search and
screening profile.

Voice, caption, and hashtag rules live in the `miac-content` skill and in
`reference/caption-voice-spec.json`. This skill covers sourcing and processing
only. Do not restate caption rules here.

Those two sources conflict with the performance analysis in three places. They
are catalogued in `reference/spec-conflicts.md` and are **unresolved**. Raise
the relevant one with the user rather than picking a side silently.

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

## Step 1: Establish the Curatorial Profile

Metricool is the performance record for the Instagram account. It is **not** a
source of YouTube links. Its job here is to say what has worked, so the search
in Step 2 knows what to look for.

```
getAnalyticsDataByMetrics(
  brandId: "6780970",
  from:    <ISO 8601, start of the look-back window>,
  to:      <ISO 8601, now>,
  metrics: ["IGRE01","IGRE03","IGRE06","IGRE27","IGRE28","IGRE24","IGRE12","IGRE21","IGRE23"]
)
```

Those fields are: date, caption text, reel URL, retention, view rate, average
watch time, saves, shares, views.

Rank by **three second hold rate (`IGRE28`) and saves (`IGRE12`)**, not by
likes. `IGRE28` is Metricool's `reelsViewRate`, the share of views held past
three seconds, which the analysis identifies as the leading indicator: it is
known within hours and predicts final reach better than anything else. **Below
45 percent, a post does not travel.** Saves say the clip was worth returning
to. Likes mostly measure reach, which reflects distribution more than curation.

**Exclude the last five days from the look-back window.** Posts accrue for
three to five days, so anything more recent has incomplete numbers and will
read as underperforming.

Read the captions of the top performers and name what they have in common:
subject, era, visual texture, pacing, whether there is speech. That description
is the curatorial profile. Carry it into Step 2 as concrete search terms and
into Step 3 as screening judgment.

`CRITERIA.md` holds the standing version of this profile. Update it only with
the user's agreement.

## Step 2: Find the Mechanism (not YouTube)

**Do not open YouTube yet.** Searching video first and then asking what can be
said about the results runs the pipeline backwards, and it reliably produces
surveys, because what a video search returns on a director's name is
retrospectives and career overviews. The evidence is in
`reference/what-search-found-them.md`.

The account's top posts were built mechanism first. Their captions cite
production histories, cinematographer interviews, and film scholarship, none of
which surfaces from a video search.

Search the literature for a technique worth explaining. Query shapes that match
the winners:

- `<cinematographer> <film> cinematography`
- `<named technique> <film or era>`
- `how <film> achieved <specific look>`
- `<film> production history <department>`

**Bias toward the technical collaborator over the director.** Willis, Zsigmond,
Unsworth, Thomson and Webb produced the top posts. Director names return career
surveys, which is the shape that fails.

**Favour mechanisms with a production constraint behind them.** The strongest
posts explain why a technique was adopted, not just that it exists. The
constraint is what makes the rule portable.

Output of this step is a specific claim: this film, this technique, this
collaborator, and the reason it was used.

## Step 2a: Check Source Availability Early

Before researching a mechanism in depth, check that a usable source could
exist. The preferred shape is a practitioner narrating over their own footage,
and that material exists abundantly for some subjects and not at all for
others.

`reference/source-registry.md` lists the known series. Check it first, and add
to it whenever a new one is found.

The test for any series: **does footage run under the voice, or is it a person
in a chair?** A talking head cannot demonstrate anything.

Practitioners who died before the video-interview era usually fail here however
good the mechanism is. Establish this before spending the research, not after.

Do not draw more than roughly one post in four from any single source. One
documentary means one grade, one interview setup, one rights holder, and a feed
that reads as a clip account rather than an editorial one.

## Step 2b: Find Footage That Proves It

Now YouTube, and only to satisfy the demonstrable requirement in `CRITERIA.md`
section 1.

- `<film title> <year> clip`
- `<film title> <the specific scene where the mechanism is visible>`
- `<film title> restoration trailer` for clean transfers

There is currently **no YouTube Data API key** in the environment. Use the
`WebSearch` tool, or work from links the user supplies. If a key is later added
as `YOUTUBE_API_KEY`, `search.list` filters on `videoDuration` and on
`videoLicense=creativeCommon`, which serves the credit cost and the rights
field in one call.

**If no footage demonstrates the mechanism on screen, the mechanism fails here**,
however good the research is. Sound mechanisms need audible proof, not visible.

**Screen the candidate before submitting.** With `YOUTUBE_API_KEY` set:

```
python3 tools/screen_source.py <url>
```

One quota unit. Reports duration against the ten minute floor, licence, and the
channel the video actually sits on, which is the provenance check. Exits
non-zero when a source fails.

Prefer `videos.list` over `search.list`: 1 unit against 100, so roughly 10,000
verifications a day but only 100 searches. Verification is effectively free and
search is the scarce resource.

Drop any URL already present in `queue/candidates.json` in any status. The
queue is the dedup record.

## Step 3: Screen Against Criteria

Read `CRITERIA.md` and apply it to every candidate.

Screening happens BEFORE submission because submission costs credits. Record
the specific reason each candidate passed or failed. A failed candidate goes
into the queue as `rejected` with its reason, so the same video is not
reconsidered next run.

Every candidate needs a `rights` value before it can be submitted. Open search
across YouTube surfaces mostly rights-reserved material, so this field carries
real weight rather than being a formality. If rights cannot be established, the
candidate is `rejected` with reason `rights-unclear`. Surface these to the user
rather than deciding the close calls unilaterally.

## Step 4: Submit Links to Opus Clip

Check headroom first with `opusclip_get_usage`. If the batch's total source
minutes exceed remaining monthly credits, submit the strongest candidates that
fit and leave the rest as `candidate`. Report what was deferred.

```
opusclip_submit_project(
  videoUrl:     <the YouTube watch URL, passed directly, no download>,
  aspectRatio:  "portrait",
  clipDurationsSec: [[60, 180]],
  title:        <source title>,
  rangeStart:   <seconds, when only part of a long source is relevant>,
  rangeEnd:     <seconds>,
  customPrompt: <steer curation using the curatorial profile>
)
```

Opus accepts YouTube URLs natively. Never download the video, and never use
yt-dlp or ffmpeg here.

`clipDurationsSec` must be set to `[[60, 180]]`. The target format is a one to
three minute clip. Leaving it unset produces fragments.

`aspectRatio` must be set explicitly on every call. The org default brand
template is landscape, so omitting it yields 16:9 output that is wrong for
Reels.

Use `rangeStart` and `rangeEnd` aggressively on long sources. They bound which
part of the video clips are drawn from, and they cut the credit cost.

Record the returned project ID in the queue and set status to `submitted`.

## Step 5: Poll, Then Review in Chat

Poll `opusclip_list_clips` until processing finishes. Concurrency limit is 10
in-flight projects.

When clips are ready, call `opusclip_preview_clips(projectId)` to render
playable ranked cards in chat. This is the review gate.

### Filter before showing anything

**`customPrompt` steers selection, not exclusion.** Tested twice. It pulls
curation toward the mechanism, but content it is explicitly told to avoid still
comes back: a sponsor read appeared at rank 7 of a project whose prompt ruled
out advertising in as many words.

Two reliable filters, neither of them the prompt:

| Signal | Rule | Limits |
|---|---|---|
| Sub-scores | Drop anything at or below 3 on hook and coherence. | **Catches advertising only.** An Oscar acceptance speech ranked first at score 99 with 10/10/10 in a project whose prompt excluded awards talk. Do not treat a high score as evidence a clip is on profile. |
| `connection_score` | Ignore it. | It reads 10 on nearly every clip in a project and discriminates nothing. |
| Duration | With `clipDurationsSec` set, anything outside the window is an artifact rather than a clip. | Weak on its own. |

**There is no mechanical filter for off-profile content.** Three projects now
show curation returning career summary, awards talk, biography and outright
noise at top rank, with scores indistinguishable from the good clips. The
screen is editorial: does this clip carry a visual mechanism with a turn.
Read every clip's title and content against the criteria. Automation ends at
the ad filter.

Also drop the `_bonus` duplicate, which repeats rank 1 with a second or two of
difference.

**Discard all Opus-generated metadata.** Titles, descriptions and hashtags are
hook copy in a register the voice rules ban, and the hashtags include tags from
the never-include list. Captions are written fresh every time.

Judge clips on whether a decoder caption can be written over them: is a
mechanism visible or audible here, in one work, provable on screen. Opus ranks
by its own engagement heuristics, which are not this account's criteria, so a
low ranked clip that demonstrates a mechanism beats a high ranked one that does
not.

**Stop here and wait.** Do not export, schedule, or post without explicit
approval on specific clips. Set status to `reviewed`.

### Editing a clip

`opusclip_edit_clip` can tidy a clip, but two cautions apply to the sources
this pipeline uses.

**Never run `remove_pauses` on a source that intercuts interview with film
clips.** The silences are the footage. That is where the demonstration plays
with no dialogue, and cutting it leaves a talking head describing something the
viewer can no longer see. This is the majority of preferred sources, so treat
the op as off by default.

**Always `dryRun` first.** It reports what would change, saves nothing and
renders nothing. It is also the only way to find out whether an intended fix
applies at all: a clip may not contain the passage you think it does, since the
clip's own span is not visible from the source transcript.

The editor deep link returned by every call opens the clip in the Opus editor,
which is the fastest way for the user to judge something the agent cannot
watch.

## Step 6: Export and Schedule Approved Clips

Only for clips the user approved by name or rank.

1. `opusclip_export_clip` on each approved clip
2. `opusclip_get_transcript` on the source, before writing anything that
   quotes or paraphrases speech in the clip. The voice spec requires factual
   claims to be verified rather than assumed, and names the transcript as the
   thing to ask for instead of guessing.
3. Write the caption using the `miac-content` skill's voice rules and
   `reference/caption-voice-spec.json`. The first sentence has to carry the
   mechanism. That is the single largest lever measured, at roughly 6.3x.
4. `getBestTimeToPostByNetwork(brandId: "6780970", socialNetwork: "instagram", timezone: "Europe/Madrid", ...)` to pick the slot
5. `opusclip_schedule_publish` to Instagram account `69b8b7924be415e37283b877`

Set status to `scheduled` and record the scheduled time.

## Step 7: Commit the Queue

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
  "duration_sec":  0,
  "discovered":    "ISO 8601 date this entered the queue",
  "found_via":     "user | websearch | youtube-api",
  "status":        "candidate | submitted | reviewed | scheduled | rejected",
  "rights":        "public-domain | cc-by | own-channel | licensed | commentary | unclear",
  "profile_match": "which part of the curatorial profile this answers",
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

## Closing the Loop

Once scheduled clips have run for a week or two, repeat Step 1 over the newer
window. The posts this pipeline produced are now part of the performance
record, so the profile sharpens each pass.

When a pattern is clear across several posts, propose a change to `CRITERIA.md`
and say what evidence supports it. Do not edit the criteria unilaterally.
