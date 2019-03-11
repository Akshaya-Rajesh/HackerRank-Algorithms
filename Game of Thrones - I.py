#!/bin/python3

s=input()
s1=set(s)
flag=1
for i in s1:
    c=s.count(i)
    if(c%2==1):
        if(flag==0):
            print("NO")
            exit()
        flag=0
print("YES")
