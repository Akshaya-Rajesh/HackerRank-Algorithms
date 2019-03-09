#!/bin/python3

import sys

Q = int(input().strip())
for a0 in range(Q):
    n = int(input().strip())
    b = input().strip()
    dict1={}
    flag=0
    space=0
    if(len(b)==1):
        if(b=="_"):
            print("YES")
        else:
            print("NO")
    else:
        for i in b:
            if(i not in dict1):
                dict1[i]=1
            else:
                dict1[i]+=1
        if("_" in b):
            space=dict1['_']
            del dict1['_']
        if(space>0 and 1 not in dict1.values()):
            print("YES")
        elif(space>0 and 1 in dict1.values()):
            print("NO")
        elif(space==0):
            for k in range(1,len(b)-1):
                if(b[k]!=b[k-1] and b[k]!=b[k+1]):
                    flag=1
            if(b[0]!=b[1] or b[-1]!=b[-2]):
                  flag=1
            if(flag==0):
                print("YES")
            else:
                print("NO")
