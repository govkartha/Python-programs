#Group Anagrams - Leetcode
#https://leetcode.com/problems/group-anagrams/description/
'''Given an array of strings strs, group the anagrams together.'''

from collections import defaultdict

words = list(map(str, input().split()))

gd = defaultdict(list)
for word in words:
    gd["".join(sorted(word))].append(word)

for i in gd.values():
    print(i)