#!/bin/python3

n,k,q=map(int,input().split(" "))
arr=list(map(int,input().split(" ")))
k=k%n
for i in range(0,q):
    x=int(input())
    print(arr[(n+x-k)%n])
