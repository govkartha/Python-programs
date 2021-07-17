#Perfect Peak of an Array - interviewbit
#https://www.interviewbit.com/problems/perfect-peak-of-array/
'''Given an integer array A of size N.
You need to check that whether there exist 
a element which is strictly greater than all the elements on left of it and strictly smaller than all the elements on right of it.
If it exists return 1 else return 0.'''

a = list(map(int, input().split()))

maxleft = [None]*len(a)
minright = float('inf')
maxleft[0] = float('-inf')
flag = 0

for i in range(1,len(a)):
    maxleft[i] = max(maxleft[i-1], a[i-1])

for i in range(len(a)-1, -1, -1):
    if(maxleft[i]<a[i] and minright>a[i]):
        print("1")
        flag = 1
    minright = min(minright,a[i])
if(flag==0):
    print("0")

