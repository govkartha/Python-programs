#Sum of two large numbers
#https://practice.geeksforgeeks.org/problems/sum-of-numbers-or-number1219/1
#Given two strings denoting non-negative numbers X and Y. Calculate the sum of X and Y.

from itertools import zip_longest

a = input()
b= input()
a = [int(x) for x in a]
b = [int(x) for x in b]
out,carry = [],0
for ca, cb in zip_longest(reversed(a), reversed(b), fillvalue=0):
    carry, digit = divmod(ca + cb + carry, 10)
    out.append(str(digit))
print("".join(reversed(out)).lstrip("0"))