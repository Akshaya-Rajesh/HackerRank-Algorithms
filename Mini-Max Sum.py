#!/bin/python3

import sys
import math

def miniMaxSum(arr):
    minimum=min(arr)
    maximum=max(arr)
    sum=arr[0]
    for i in range(1,5):
        sum+=arr[i]
    print(str(sum-maximum)+" "+str(sum-minimum))

if __name__ == "__main__":
    arr = list(map(int, input().strip().split(' ')))
    miniMaxSum(arr)
