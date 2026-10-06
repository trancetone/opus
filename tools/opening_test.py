#!/usr/bin/env python3
"""Clip opening test for Moving Image Arts.

Three-second hold is set by the first words a viewer hears, and nothing in
this repo tested them. The caption register test checks prose we write; this
checks the clip we did not write.

Grounded in the 16 posts measured to 2026-10-06. The worst hold on the
account (Coates, 43.7%) opens on a hedge and a conditional with no proper
noun: "Well we were in film in those days so I think sometimes wonder...".
The second best (Cardiff, 69.3%) opens on a concrete event with a named
place and film: "I went to Hollywood to play in Young Bess and the taxi
driver said...". Duration does not explain the gap, because both were
watched to about the same fraction of their length, 23.0% and 24.2%.

Run on a transcript before scheduling. A FAIL is a reason to pick another
clip, not to rewrite the caption: the caption cannot fix the first words.
"""
import re
import sys

WINDOW = 20          # words of transcript the test judges
HEDGE_ZONE = 5       # a hedge this early is disqualifying

HEDGES = {
    'well', 'so', 'um', 'uh', 'anyway', 'basically', 'actually', 'really',
    'and', 'but', 'because', 'which', 'then', 'also', 'now',
}
# Multi-word hedges and speculation, matched anywhere in the window.
SOFT = [
    r'\bi think\b', r'\bi mean\b', r'\byou know\b', r'\bsort of\b',
    r'\bkind of\b', r'\bi wonder\b', r'\bsometimes wonder\b', r'\bi guess\b',
    r'\bmaybe\b', r'\bperhaps\b', r'\bi suppose\b', r'\bor something\b',
]
# First-person action: a practitioner doing something, not musing.
ACTION = re.compile(
    r'\bi (went|shot|put|built|cut|lit|took|asked|wanted|had|made|used|'
    r'rigged|called|designed|removed|added)\b', re.I)

MARKERS = re.compile(r'__(?:silence|missing)__?|__silence|__missing')


def opening_words(transcript, n=WINDOW):
    text = MARKERS.sub(' ', transcript)
    text = re.sub(r'\s+', ' ', text).strip()
    return text.split()[:n], text


# Opus transcripts capitalise erratically mid-stream, so a capital letter
# alone does not mean a name. Without this stoplist the test passed a clip
# whose opening is film dialogue with nothing named in it, counting "You're"
# and "Then" as proper nouns.
NOT_NAMES = {
    'i', 'oh', 'the', 'a', 'an', 'this', 'that', 'these', 'those', 'there',
    'here', 'we', 'he', 'she', 'it', 'they', 'you', 'your', "you're", 'my',
    'and', 'but', 'so', 'then', 'now', 'well', 'what', 'when', 'where',
    'why', 'how', 'if', 'because', 'okay', 'no', 'yes', 'man', 'one', 'two',
    'first', 'about', 'in', 'on', 'at', 'to', 'of', 'for', 'with', 'as',
    'is', 'was', 'were', 'be', 'got', 'get', 'said', 'says', 'look', 'looks',
    'just', 'not', "don't", "it's", "that's", "what's", "there's",
}


def proper_nouns(words):
    """Capitalised tokens that are plausibly names of people, works or places."""
    found = []
    for w in words:
        bare = w.strip('\",.!?;:()')
        if not bare or not bare[0].isupper():
            continue
        if bare.lower() in NOT_NAMES:
            continue
        found.append(bare)
    return found


def check(transcript, label=''):
    words, flat = opening_words(transcript)
    if not words:
        return False, ['empty transcript'], ''
    window = ' '.join(words)
    low = window.lower()
    reasons = []

    first = words[0].strip('",.!?;:()').lower()
    if first in HEDGES:
        reasons.append('opens on the hedge "%s"' % words[0])
    for i, w in enumerate(words[:HEDGE_ZONE]):
        if w.strip('",.!?;:()').lower() in HEDGES and i:
            reasons.append('hedge "%s" inside the first %d words' % (w, HEDGE_ZONE))
            break
    for pat in SOFT:
        if re.search(pat, low):
            reasons.append('speculation: "%s"' % re.search(pat, low).group(0))
            break

    names = proper_nouns(words)
    has_action = bool(ACTION.search(window))
    if not names and not has_action:
        reasons.append('no named person, work or place, and no first-person action')
    elif not names:
        reasons.append('first-person action but nothing named in %d words' % WINDOW)

    ok = not reasons
    return ok, reasons, window


def main(paths):
    allok = True
    for p in paths:
        ok, reasons, window = check(open(p).read(), p)
        print('%-34s %s' % (p.split('/')[-1], 'PASS' if ok else 'FAIL'))
        print('    opening: %s' % window)
        for r in reasons:
            print('    - %s' % r)
        allok = allok and ok
    return 0 if allok else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
