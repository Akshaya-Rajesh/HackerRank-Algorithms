#!/bin/python3

def aVeryBigSum(n,ar):
    #initializing sum as the 1st element of the list
    sum=ar[0] 
    #adding each of the element to the variable sum
    for i in range(1,n):
        sum+=ar[i]
    return(sum)

n = int(input())
ar = list(map(int, input().split(' ')))
result = aVeryBigSum(n,ar)
print(result)
