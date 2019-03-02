#!/bin/python3

n=int(input())
p=int(input())
first_pno=1
last_pno=(n//2+1)
target=(p//2+1)
print(min((target-first_pno),(last_pno-target)))
