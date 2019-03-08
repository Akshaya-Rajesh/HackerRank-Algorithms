#!/bin/python3

s=input()
n=int(input())
num_a=s.count('a')
num_a=int((n/len(s)))*num_a
num_a+=s.count('a',0,(n%len(s)))
print(num_a)
