#!/bin/python3

n=int(input())
arr=input()
count=1
valley=0
for i in arr:
    if i=='U':
        count+=1
    else:
        count-=1
    if(count==1 and i=='U'):
        valley+=1
print(valley)       
