#Look and Say Pattern 
#https://practice.geeksforgeeks.org/problems/decode-the-pattern1138/1
#Given an integer n. Return the nth row of the look-and-say pattern.

from itertools import groupby

n = int(input())
x = "1"
if(n==1):
    print(1)
elif(n==2):
    print(11)
else:
    for _ in range(n-1):
        x = ''.join( str(len(list(g))) + k for k,g in groupby(x))
    print(x)