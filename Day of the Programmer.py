#!/bin/python3

leap=0
year=int(input())
if(1700<=year<=1917):
    if(year%4==0):
        leap=1
elif(year>1918):
    if((year%400==0)or((year%4==0)and(year%100!=0))):
        leap=1
if(year==1918):
        print("26.09.1918")
elif(leap==1):
    print("12.09."+str(year))
else:
    print("13.09."+str(year))
