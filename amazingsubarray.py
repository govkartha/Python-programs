#Amazing Subarray - interviewbit
#https://www.interviewbit.com/problems/amazing-subarrays/
#Given a string S, and you have to find all the amazing substrings of S.
#Amazing Substring is one that starts with a vowel 

s = input()
count = 0
for idx, char in enumerate(s):
    if char in "aeiouAEIOU":
       count += len(s) - idx

print(count%10003)