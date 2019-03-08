#!/bin/python3

t=int(input())
for i in range(0,t):
    count=0
    n=(input())
    for i in n:
        if(int(i)==0):
            continue
        if(int(n)%int(i)==0):
            count+=1
    print(count)
