#!/bin/python3

import math
import os
import random
import re
import sys

def missingNumbers(arr, brr):
    dict={}
    ans=[]

    for i in arr:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1

    for i in brr:
        if i in dict:
            dict[i]-=1
        else:
            dict[i]=1

    for i in sorted(dict):
        if(dict[i]==0):
            continue
        else:
            ans.append(i)

    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    m = int(input())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
