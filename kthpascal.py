#Kth Row of Pascal's Triangle - interviewbit
#https://www.interviewbit.com/problems/kth-row-of-pascals-triangle/
#Given a row number, print the kth row of Pascal's triangle.


import math

k = int(input())
for i in range(k):
    print(math.comb(k,i), end=" ")