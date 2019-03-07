#!/bin/python3

nk=list(map(int,input().split()))
c=list(map(int,input().split()))
E=100
for i in range(0,nk[0],nk[1]):
    if(c[i]==1):
        E-=3
    else:
        E-=1
print(E)
