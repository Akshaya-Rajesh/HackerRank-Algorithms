#!/bin/python3

import math
import os
import random
import re
import sys

def theLoveLetterMystery(s):
    n=len(s)
    sum=0
    for i in range(0,n//2):
        sum+=abs(ord(s[i])-ord(s[n-i-1]))
    return sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = theLoveLetterMystery(s)

        fptr.write(str(result) + '\n')

    fptr.close()
