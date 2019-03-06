#!/bin/python3

h=list(map(int,input().split()))
s=input()
alph=list(map(chr,range(97,123)))
d={}
for i in range(0,26):
    d[alph[i]]=h[i]
s1=set(s)
max=0
for i in s1:
    if(d[i]>max):
        max=d[i]
print(len(s)*max)
