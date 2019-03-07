#!/bin/python3

import math
n=int(input())
p=5
sum=0
for i in range(0,n):
    p=math.floor(p/2)
    sum+=p
    p=p*3
print(sum)
