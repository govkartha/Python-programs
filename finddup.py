#Find Duplicate in Array - interviewbit
'''Given an array of integers, find the first duplicate number for which the second occurrence has the minimal index.'''

from collections import Counter

a = list(map(int,input().split()))

print(max(set(a), key=a.count))

# d = {}
# flag = 0
# d = Counter(a)
# for key,value in d.items():
#     if(value>1):
#         print(key)
#         flag = 1
#         break
# if(flag==0): print("-1")  