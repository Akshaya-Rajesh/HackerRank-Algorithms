#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    last=s[0]
    array=[]
    count=1
    sum=0
    for i in range(1,len(s)):
        if(s[i]==last):
            count+=1
        else:
            array.append(count)
            count=1
            last=s[i]
    array.append(count)
    for i in array:
        sum+=(i-1)
    return(sum)    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()
