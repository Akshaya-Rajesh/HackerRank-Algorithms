#!/bin/python3

t=int(input())
arr=[]
for i in range(0,t):
    n=int(input())
    h=1
    while(n>0):
        h*=2
        n-=1
        if(n>0):
            h+=1
            n-=1
    arr.append(h)
for i in arr:
    print(i)
