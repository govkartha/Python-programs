#Maximum Absolute Difference - interviewbit
#https://www.interviewbit.com/problems/maximum-absolute-difference/
'''You are given an array of N integers, A1, A2 ,…, AN. 
Return maximum value of f(i, j) for all 1 ≤ i, j ≤ N.
f(i, j) is defined as |A[i] - A[j]| + |i - j|, 
where |x| denotes absolute value of x.'''

a = list(map(int, input().split()))

max1,max2,min1,min2 = float('-inf'),float('-inf'),float('inf'),float('inf')

for i in range(len(a)):
    max1 = max(max1, a[i]+i)
    min1 = min(min1, a[i]+i)

    max2 = max(max2, a[i]-i)
    min2 = min(min2, a[i]-i)

print(max((max1-min1), (max2-min2)))