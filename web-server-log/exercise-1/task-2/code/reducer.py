#!/usr/bin/python

import sys

hits = 0
oldKey = None

for line in sys.stdin:
    thisKey = line.strip()

    if oldKey and oldKey != thisKey:
        print oldKey, " ", hits
        hits = 0

    oldKey = thisKey
    hits += 1

if oldKey is not None:
    print oldKey, " ", hits
