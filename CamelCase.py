#!/bin/python3

import sys

def camelcase(s):
    count=0
    for i in s:
        if(i.isupper()==True):
            count+=1
    return(count+1)

if __name__ == "__main__":
    s = input().strip()
    result = camelcase(s)
    print(result)
