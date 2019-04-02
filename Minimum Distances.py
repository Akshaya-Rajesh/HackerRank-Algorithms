#!/bin/python3

import math
import os
import random
import re
import sys

def minimumDistances(a):
    dict={}
    for i in range(0,len(a)):
        if(a[i] in dict):
            dict[a[i]].append(i)
        else:
            dict[a[i]]=[i]
    dist=len(a)
    for i in dict:
        if(len(dict[i])==1):
            continue
        else:
            for j in range(0,len(dict[i])-1):
                d=dict[i][j+1]-dict[i][j]
                if(d<dist):
                    dist=d
    if(dist==len(a)):
        return(-1)
    return dist

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
