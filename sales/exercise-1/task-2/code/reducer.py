#!/usr/bin/python

import sys

salesMax = 0
oldKey = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue

    thisKey, thisSale = data_mapped
    thisSale = float(thisSale)

    if oldKey and oldKey != thisKey:
        print oldKey, "\t", salesMax
        salesMax = 0

    oldKey = thisKey
    salesMax = max(salesMax, thisSale)

if oldKey is not None:
    print oldKey, "\t", salesMax
