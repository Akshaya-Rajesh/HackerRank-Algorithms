#!/bin/python3

n=int(input())
arr=list(map(int,input().split()))
d={}
for i in arr:
    if(i not in d):
        d[i]=arr.count(i)
del arr
count=0
arr=d.values()
for i in arr:
    count+=i//2
print(count)
