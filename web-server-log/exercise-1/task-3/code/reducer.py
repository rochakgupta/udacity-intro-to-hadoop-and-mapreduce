#!/usr/bin/python

import sys

maxHits = 0
maxKey = None
hits = 0
oldKey = None

for line in sys.stdin:
    thisKey = line.strip()

    if oldKey and oldKey != thisKey:
        if hits > maxHits:
            maxHits = hits
            maxKey = oldKey
        hits = 0

    oldKey = thisKey
    hits += 1

if hits > maxHits:
    maxHits = hits
    maxKey = oldKey

print maxKey, " ", maxHits
