#!/bin/python3

t=int(input())
for i in range(0,t):
    count=0
    s=[]
    nk=list(map(int,input().split()))
    s=list(map(int,input().split()))
    for j in s:
        if(j<=0):
            count+=1
    if(count>=nk[1]):
        print("NO")
    else:
        print("YES")
