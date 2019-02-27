#!/bin/python3

def plusMinus(arr):
    z,p,n=0,0,0
    #z-count of zeros,p-count of +ve no.s,n-count of -ve no.s
    for i in arr:
        if(i>0):
            p+=1
        elif(i<0):
            n+=1
        else:
            z+=1
    print(p/(p+n+z))
    print(n/(p+n+z))
    print(z/(p+n+z))      

n = int(input())
arr = list(map(int, input().split(' ')))
plusMinus(arr)
