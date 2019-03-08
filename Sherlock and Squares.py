#!/bin/python3

import math
t=int(input())
for i in range(0,t):
    arr=list(map(int,input().split()))
    a=int(arr[0])
    b=int(arr[1])
    print(math.floor(math.sqrt(b))-math.ceil(math.sqrt(a))+1)
