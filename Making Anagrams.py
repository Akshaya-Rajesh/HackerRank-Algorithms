#!/bin/python3

from collections import Counter

counts = Counter(input())
counts.subtract(input())
print(sum(abs(x) for x in counts.values()))
