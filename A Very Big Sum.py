#!/bin/python3

import sys

def aVeryBigSum(n,ar):
    sum=ar[0] 
    for i in range(1,n):
        sum+=ar[i]
    return(sum)

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = aVeryBigSum(n,ar)
print(result)
