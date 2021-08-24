#Isomorphic Strings 
#https://practice.geeksforgeeks.org/problems/isomorphic-strings-1587115620/1/
#Two strings str1 and str2 are called isomorphic if there is a one to one mapping possible for every character of str1 to every character of str2 while preserving the order.

from collections import Counter

str1 = input()
str2 = input()
if(len(str1) != len(str2)):
    print(0)
elif(list(dict(Counter(str1)).values()) == list(dict(Counter(str2)).values())):
    print(1)
else:
    print(0)