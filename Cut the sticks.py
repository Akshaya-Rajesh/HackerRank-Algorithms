#!/bin/python3

import math
n=int(input())
arr=list(map(int,input().split()))
count=n
while(count>0):
    print(count)
    m=min(arr)
    while m in arr:
        arr.remove(m)
        count-=1
