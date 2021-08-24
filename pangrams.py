#Pangram Checking
#https://practice.geeksforgeeks.org/problems/pangram-checking-1587115620/1/
#Given a string check if it is Pangram or not. A pangram is a sentence containing every letter in the English Alphabet.

s = input()
a = "abcdefghijklmnopqrstuvwxyz"
flag = 1
for i in a:
    if i not in s:
        print(0)
        flag = 0
        break
if(flag):
    print(1)