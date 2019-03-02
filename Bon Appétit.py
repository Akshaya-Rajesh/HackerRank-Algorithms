#!/bin/python3

import sys

def bonAppetit(n, k, b, ar):
    sum=0
    for i in ar:
        sum+=i 
    s=sum-ar[k]
    s=int(s/2)
    if(s==b):
        return("Bon Appetit")
    else:
        return(b-s)

n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
ar = list(map(int, input().strip().split(' ')))
b = int(input().strip())
result = bonAppetit(n, k, b, ar)
print(result)
