#!/bin/python3

arr=list(map(int,input().split()))
n=arr[0]
k=arr[1]
h=list(map(int,input().split()))
print(max(0, max(h)-k))
