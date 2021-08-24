#Encrypt the string - 2 
#https://practice.geeksforgeeks.org/problems/encrypt-the-string-21117/1/
#You are given a string S. Every sub-string of identical letters is replaced by a single instance of that letter followed by the hexadecimal representation of the number of occurrences of that letter. Then, the string thus obtained is further encrypted by reversing it

from collections import Counter

s = input()
d = dict(Counter(s))
x = ''
for i,j in d.items():
    x += (i + hex(j).lstrip("0x")).strip()

print(x[::-1])
    