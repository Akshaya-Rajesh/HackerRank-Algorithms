#!/bin/python3

import math
import os
import random
import re
import sys

def superReducedString(s):
    if(len(s)==0):
        return 'Empty String'
    elif(len(s)==1):
        return s
    elif(len(s)==2):
        if(s[0]==s[1]):
            return 'Empty String'
        else:
            return s
    else:
        flag=0
        i=0
        last=1
        str=''
        while(i<len(s)-1):
            if(s[i]==s[i+1]):
                i+=2
                flag=1
                last=1
            else:
                str+=s[i]
                i+=1
                last=0
        if((last==1 and i==len(s)-1)or last==0):
            str+=s[len(s)-1]
        if(flag==0):
            return s
        else:
            return superReducedString(str)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
