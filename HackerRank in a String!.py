#!/bin/python3

def hackerrankInString(s):
    i=0
    for j in 'hackerrank':
        if j in s[i:]:
            i=s.index(j,i)+1
        else:
            return 'NO'
    return 'YES'

q=int(input())
for i in range(q):
    s=input()
    print(hackerrankInString(s))
