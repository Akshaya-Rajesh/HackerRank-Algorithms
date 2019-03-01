#!/bin/python3

import sys

def migratoryBirds(n, ar):
    dict1={1:0,2:0,3:0,4:0,5:0}
    for i in ar:
        dict1[i]+=1
    m=max(dict1.values())
    for i in range(1,6):
        if(dict1[i]==m):
            comm=i
    for i in range(1,6):
        if(dict1[i]==m and i<comm):
            comm=i
    return(comm)

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = migratoryBirds(n, ar)
print(result)
