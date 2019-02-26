#!/bin/python3

def simpleArraySum(n,ar):
    sum=0
    for i in ar:
        sum+=i
    return(sum)

n = int(input())
ar = list(map(int, input().split(' ')))
result = simpleArraySum(n,ar)
print(result)
