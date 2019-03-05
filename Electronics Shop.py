#!/bin/python3

arr=list(map(int,input().split()))
keyboard=list(map(int,input().split()))
usb=list(map(int,input().split()))
sum=-1
keyboard.sort(reverse=True)
usb.sort()
for i in keyboard:
    for j in usb:
        if(i+j>arr[0]):
            break
        if(i+j>sum):
            sum=i+j
print(sum)
