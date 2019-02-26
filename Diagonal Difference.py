#!/bin/python3

import sys

def diagonalDifference(a,n):
    pd=a[0][0]
    ad=a[0][n-1]
    for i in range(1,n):
        pd+=a[i][i]
        ad+=a[i][n-i-1]
    return(abs(pd-ad))
if __name__ == "__main__":
    n = int(input().strip())
    a = []
    for a_i in range(n):
       a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
       a.append(a_t)
    result = diagonalDifference(a,n)
    print(result)
