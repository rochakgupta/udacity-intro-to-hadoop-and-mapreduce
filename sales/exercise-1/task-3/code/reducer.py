#!/usr/bin/python

import sys

salesTotal = 0
salesCount = 0

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 1:
        continue

    sale = data_mapped[0]
    salesTotal += float(sale)
    salesCount += 1

print salesTotal, "\t", salesCount
