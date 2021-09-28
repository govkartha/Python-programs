#Shortest Distance to a Character
#https://leetcode.com/problems/shortest-distance-to-a-character/
#Given a string s and a character c that occurs in s, return an array of integers answer where answer.length == s.length and answer[i] is the distance from index i to the closest occurrence of character c in s

s = input()
c = input()
a = []
for i in range(len(s)):
    q = min((s[i:].find(c)),(s[i::-1]).find(c))
    print(q if q!=-1 else s[i:].find(c), end = " ")