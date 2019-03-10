#!/bin/python3

n=int(input())
st=input()
num=1
low=1
upp=1
spcl=1
numbers = "0123456789"
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_characters = "!@#$%^&*()-+"
for i in st:
    if(num==1):
        if(i in numbers):
            num=0
            continue
    if(low==1):
        if(i in lower_case):
            low=0
            continue
    if(upp==1):
        if(i in upper_case):
            upp=0
            continue
    if(spcl==1):
        if(i in special_characters):
            spcl=0
            continue
if(num+low+upp+spcl==0):
    if(n>=6):
        print(0)
    else:
        print(6-n)
else:
    if(n+num+low+upp+spcl>=6):
        print(num+low+upp+spcl)
    else:
        print(num+low+upp+spcl+(6-n-num-low-upp-spcl))
