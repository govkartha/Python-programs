#Sort an array of 0s, 1s and 2s
#https://practice.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s4231/1
#Given an array of size N containing only 0s, 1s, and 2s; sort the array in ascending order.

from collections import Counter

a = list(map(int, input().split()))
d = dict(Counter(a))
for _ in range(d[0]):
    print('0',end=" ")
for _ in range(d[1]):
    print('1',end=" ")
for _ in range(d[2]):
    print('2',end=" ")