#Wave Array - interviewbit
#https://www.interviewbit.com/problems/wave-array/
#Given an array of integers, sort the array into a wave like array and return it

a = list(map(int, input().split()))

# for i in range(0, len(a), 2):
#     if (a[i] < a[i-1]):
#         a[i],a[i-1] = a[i-1],a[i]
         
#     if(a[i] < a[i+1]):
#         a[i],a[i+1] = a[i+1],a[i]

a.sort()
for i in range(0, len(a)-1, 2):
    a[i],a[i+1] = a[i+1],a[i]

print(a)