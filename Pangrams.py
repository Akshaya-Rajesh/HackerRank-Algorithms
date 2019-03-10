#!/bin/python3

string=input()
alphabet="abcdefghijklmnopqrstuvwxyz"
if(len(set(string.lower())-{' '})==26):
    print("pangram")
else:
    print("not pangram")
