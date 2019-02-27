#!/bin/python3

#consider a GP with a=3 and r=2 , sn=3*(2^n-1)
def strange_counter(t):
    n=1
    #to find the number possible to be the sum just greater than t
    while(t>3*(2**n-1)):
        n+=1
    return(3*(2**n-1)-t+1)

t=int(input())
print(strange_counter(t))
