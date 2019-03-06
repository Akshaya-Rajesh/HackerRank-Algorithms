#!/bin/python3

t=int(input())
for i in range(0,t):
    arr=list(map(int,input().split()))
    a=arr[0]
    b=arr[1]
    c=arr[2]
    if(abs(a-c)<abs(b-c)):
        print("Cat A")
    elif(abs(b-c)<abs(a-c)):
        print("Cat B")
    else:
        print("Mouse C")
