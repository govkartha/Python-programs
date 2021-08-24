#Subarray with given sum
#https://practice.geeksforgeeks.org/problems/subarray-with-given-sum-1587115621/1
#Given an unsorted array A of size N that contains only non-negative integers, find a continuous sub-array which adds to a given number S.

a = list(map(int, input().split()))
k = int(input())
s,b,l = 0,0,0
for i in range(len(a)):
    if(s == k):
        l = i
        break
    s += a[i]
    if(s > k):
        s -= a[b]
        b +=1
print(b+1,l)