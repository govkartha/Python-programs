#Largest Number - interviewbit
#https://www.interviewbit.com/problems/largest-number/
#Given a list of non negative integers, arrange them such that they form the largest number.

from itertools import permutations

a = list(map(str, input().split()))
l = []
for i in permutations(a, len(a)):
    l.append("".join(i))
print(max(l)) 