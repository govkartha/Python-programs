#Check if two strings are k-anagrams or not 
#https://practice.geeksforgeeks.org/problems/check-if-two-strings-are-k-anagrams-or-not/1
#Given two strings of lowercase alphabets and a value K, your task is to complete the given function which tells if  two strings are K-anagrams of each other or not.
# Two strings are called K-anagrams if both of the below conditions are true.
# 1. Both have same number of characters.
# 2. Two strings can become anagram by changing at most K characters in a string.

str1 = list(input())
str2 = list(input())
k = int(input())
c = 0
list(str1).sort()
list(str2).sort()
if(len(str1) != len(str2)):
    print(0)
else:
    print(sorted(str1))
    print(sorted(str2))
    for i in range(len(str1)):
        if(str1[i] != str2[i]):
            c += 1
    print(c)
    if(c<=k):
        print(1)
    else:
        print(0)