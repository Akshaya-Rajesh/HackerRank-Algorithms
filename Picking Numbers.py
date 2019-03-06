#!/bin/python3

n=int(input())
arr=list(map(int,input().split()))
s=set(arr)
s1=[]
set1=0
s=list(s)
s.sort()
for i in s:
    s1.append(arr.count(i))
set=s1[0]   
for i in range(0,len(s)-1):
    num=s[i]
    set2=s1[i]
    if(s[i+1]==num+1):
        set1=s1[i]+s1[i+1]
    set1=max(set1,set2)
    if(set1>set):
            set=set1
print(set)
