#!/bin/python3

import sys

def birthdayCakeCandles(n, ar):
    m=max(ar)
    return(ar.count(m))

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = birthdayCakeCandles(n, ar)
print(result)
