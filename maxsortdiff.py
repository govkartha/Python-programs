#Maximum Consecutive Gaps - interviewbit
#https://www.interviewbit.com/problems/maximum-consecutive-gap/
#Given an unsorted array, find the maximum difference between the successive elements in its sorted form.

a = list(map(int, input().split()))

mn,mx = min(a),max(a)
md = float("-inf")
for i in range(len(a)):
    if(a[i] in range(mn+1,mx)):
        md = mx - a[i]
        mn = a[i]
print(md)