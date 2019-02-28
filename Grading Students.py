#!/bin/python3

import sys

def solve(grades):
    for i in grades:
        rem=i%5
        if(i<38):
            print(i)
        elif(rem==2 or rem==1 or rem==0):
            print(i)
        else:
            print(i-rem+5)

n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
   grades_t = int(input().strip())
   grades.append(grades_t)
result = solve(grades)
print ("\n".join(map(str, result)))
