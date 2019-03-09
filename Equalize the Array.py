#!/bin/python3

num=int(input())
n=list(map(int,input().split()))
num=set(n)
max=0
for i in num:
    if(n.count(i)>max):
        max=n.count(i)
print(len(n)-max)
