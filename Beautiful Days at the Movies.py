#!/bin/python3

i,j,k=map(int,input().split())
count=0
for item in range(i,j+1):
    if(((item-int(str(item)[::-1]))%k)==0):
        count+=1
print(count)
