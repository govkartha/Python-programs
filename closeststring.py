#Closest Strings
#https://practice.geeksforgeeks.org/problems/closest-strings0611/1/#
#Given a list of words followed by two words, the task to find the minimum distance between the given two words in the list of words

s = list(input().split())
word1 = input()
word2 = input()
print(abs(len(s)- list(reversed(s)).index(word1) - s.index(word2) - 1))