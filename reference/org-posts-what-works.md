# Organisational posts: what can be measured, and what it says so far

The clip record (`decoder-clips-what-works.md`) is about reels that explain a
mechanism. This file is about the other job: posts that exist to support
Moving Image Arts as an organisation, which so far means panels and events.
Opened 20 October 2026, after Tony asked for this thread and pointed at the
Sight + Sound + Soul announcement of 17 October.

Treat everything below as a starting baseline, not a finding. There are three
feed posts in the account's whole history.

## What each format can and cannot report

This is the most important thing in the file, because it decides what any of
this can ever be measured on.

| | Reels (`IGRE*`) | Feed posts (`IGPO*`) | Stories (`IGST*`) |
|---|---|---|---|
| Views | IGRE23 | IGPO28 | impressions only |
| Reach | IGRE11 | IGPO14 | IGST10 |
| Shares | IGRE21 | IGPO27 | none |
| Saves | IGRE12 | IGPO15 | none |
| **New followers from this post** | **none** | **IGPO29** | none |
| Average watch time | IGRE24 | n/a | n/a |
| Replies | n/a | comments IGPO08 | IGST11 |

**Reels cannot attribute a follower to a post.** `IGRE29` is reposts, not
follows. The account's main format is therefore blind on the one number an
organisation cares about, and feed posts are the only place follower
acquisition is visible per post. That asymmetry should drive format choice
whenever the goal is growth rather than reach.

Two other traps in that table: `IGRE26` video duration is marked paid data,
which is why retention still has to be computed as watch time over known clip
length, and `IGRE27` retention comes back null, as the clip record already
says.

## The baseline, normalised per 1,000 reach

Views are the wrong denominator for comparing formats, because reels get
pushed to non-followers and feed posts largely do not. Reach is the honest
basis.

| Post | Format | Reach | Interactions /1k | Shares /1k | Saves /1k | Follows |
|---|---|---|---|---|---|---|
| 19 Aug | feed image | 96 | 10.4 | n/a | 0 | 0 |
| 1 Sep | feed carousel | 838 | 37.0 | 4.8 | 2.4 | 1 |
| 12 Sep panel | reel | 893 | 52.6 | 2.2 | 9.0 | not reported |
| 15 Sep panel | reel | 534 | 37.5 | 1.9 | 3.7 | not reported |
| 17 Oct Sight + Sound + Soul | feed image | 305 | 72.1 | 29.5 | 0.0 | 1 |

## What the Sight + Sound + Soul post says

**The share rate is the story.** 29.5 shares per thousand reach, against 2.2
and 1.9 for the two panel reels and 4.8 for the carousel. It is also above
every decoder reel in the record: the Steadicam reel settled at 12.1 per
thousand views and Mary Poppins ran 13.9. An event announcement does not get
consumed, it gets forwarded to a specific person, which is exactly the
behaviour an event needs. n=1, but it is a large gap.

**Zero saves is the actionable half.** Not a low rate, zero, on a post whose
only instruction is that RSVP opens soon and the link is in bio. The post
asks the reader to do nothing and gives them nothing to keep. For an event
the natural save triggers are a date you must remember and a link you will
need later, and deferring the RSVP removes both at once.

**Reach is the weak point.** 305, against 534 and 893 for the panel reels and
anywhere from 650 to 54,700 for the decoder clips. A feed image does not
travel beyond the existing following. If the point of an event post is to
reach people who have not heard of the organisation, it cannot be the only
format used.

## Stories are not a usable channel as things stand

27 stories since 1 September. Reach runs 16 to 52, with a single outlier at
167 on 5 September. Replies across all 27: zero. The story that accompanied
the event announcement reached 43 people, with 15 exits against 19 taps
forward.

This is the one observation here with enough data points to lean on. Do not
build an RSVP push on stories at this reach. Either the channel needs
rebuilding first, or it is a reminder surface for people already coming, not
a recruitment surface.

## Measurement rules for this thread

- Judge these on **shares per 1,000 reach** and **follows**, never on views.
  Views is the decoder-clip metric and it answers a different question.
- Reach, not views, when comparing across formats.
- Log every organisational post here as it happens. The reason this file
  starts with n=3 is that nobody was keeping it.
- The follower denominator is missing. The last figure in the repo is 3,466
  from mid-September and it is stale; pull the current count before reading
  305 reach as good or bad.

## The denominators, 20 October 2026

| | |
|---|---|
| Followers | 5,044, gaining 51 to 102 a day, losing 3 to 5 |
| Avg reach per reel (`IGEV30`) | 1,233 |
| Avg reach per feed post (`IGEV19`) | 305 |
| Avg story reach | 16 to 52 |
| US share of followers | 50.9 percent |

So a feed post reaches about 6 percent of the following, a reel about 24
percent, a story about 1 percent. The event announcement's 305 reach was not
a failure, it was exactly the format average. A reel is worth roughly four
feed posts on reach.

**There is no city-level data for Instagram in Metricool.** The `country`
connector is all there is, and `cl` is Collabs, not cities. Half the
following is outside the US, the account is adding sixty to a hundred
followers a day from clips that pull a global cinephile audience, and the
events are one night in Los Angeles. Growth is diluting the local share
rather than concentrating it, and nothing in this tool can tell us by how
much. Ask Tony for the RSVP geography instead.

## Collabs are the only lever that changes who sees a post

Six collabs, all between 17 August and 5 September, none since:

| Date | Collaborator | Type | Views | Shares |
|---|---|---|---|---|
| 17 Aug | thisisbuzzfilm | reel | 1,970 | 10 |
| 28 Aug | thisisbuzzfilm | reel | 3,068 | 17 |
| 31 Aug | parsonsprojects | carousel | null | 5 |
| 1 Sep | thisisbuzzfilm | reel | 1,526 | 2 |
| 2 Sep | highwaysps | carousel | null | 7 |
| 5 Sep | aleistereaves | carousel | null | 3 |

The September event was promoted with collabs including the venue. The
Sight + Sound + Soul announcement was not one; the venue is only tagged.

**A collab appears to fall out of the account's own per-post analytics.** The
three collab carousels above show null views here, and none of them appear
among the three rows in the `IGPO` feed-post table, which holds only 19 Aug,
1 Sep and 17 Oct. This is inference from absence rather than a documented
behaviour, but it is consistent, and it means a collab costs the `IGPO29`
follows attribution.

That gives a clean split, and it is the answer to how to support an event:

- **Collab the reel.** Reels carry no follows metric anyway, so co-authoring
  costs nothing measurable and buys the venue's audience, which is local by
  definition. The best collab reel did 3,068 views against a 1,233 average.
- **Own the carousel.** Keep it off collab so `IGPO29` still reports. Seeing
  whether the event recruits anyone is the whole reason to post it.
- Put the link live in bio before the reveal posts. The 17 October post asked
  for nothing and got zero saves.
- Put the date in the image. A forwarded post arrives without its caption,
  and forwarding is what this audience does best.
- Do not displace the decoder clips. They are the growth engine.
