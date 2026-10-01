#!/usr/bin/env python3
"""Caption register test for Moving Image Arts.

Published captions that performed well are 2-5 sentences, mean sentence
length 35-52 words, nothing under 15 words. Short punchy fragments are
off-voice. Run this on every caption before it is shown to the user.

Sentence splitting guards against false splits on initials ("William A.
Fraker", "John A. Alonzo") and on common abbreviations, which otherwise
register as 2-word sentences and fail a caption that is actually fine.
"""
import re
import sys

ABBREV = r'(?:[A-Z]|Mr|Mrs|Ms|Dr|Jr|Sr|St|ASC|BSC|vs|etc|No|Vol)'


def sentences(body):
    # Mask the period after an initial or known abbreviation so it is not
    # treated as a sentence end, split, then restore.
    masked = re.sub(r'\b(%s)\.(\s)' % ABBREV, lambda m: m.group(1) + '\x00' + m.group(2), body)
    parts = [p for p in re.split(r'(?<=[.!?])\s+', masked) if p.strip()]
    return [p.replace('\x00', '.') for p in parts]


def check(path):
    raw = open(path).read()
    if raw.lstrip().startswith('WITHDRAWN'):
        print('%-34s skipped (withdrawn)' % path.split('/')[-1])
        return True
    body = raw.split('\n\n#')[0].strip()
    sents = sentences(body)
    lengths = [len(s.split()) for s in sents]
    mean = sum(lengths) / len(lengths)
    ok = mean >= 35 and min(lengths) >= 15 and '—' not in body
    print('%-34s sent %d  words %3d  mean %4.1f  min %2d  %s%s' % (
        path.split('/')[-1], len(sents), sum(lengths), mean, min(lengths),
        'PASS' if ok else 'FAIL',
        '  EM-DASH' if '—' in body else ''))
    if not ok:
        for s, n in zip(sents, lengths):
            if n < 15:
                print('    short (%d): %s' % (n, s))
    return ok


if __name__ == '__main__':
    # Evaluate every file before deciding: all() short-circuits, which
    # silently hid every caption after the first failure.
    results = [check(p) for p in sys.argv[1:]]
    sys.exit(0 if all(results) else 1)
