#Kth smallest element 
#Given an array arr[] and a number K where K is smaller than size of array, the task is to find the Kth smallest element in the given array. It is given that all array elements are distinct.

a = list(map(int, input().split()))
k = int(input())
a.sort()
print(a[k-1])