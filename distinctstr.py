#Distinct strings with odd and even changes allowed
#Given an array of lower case strings, the task is to find the number of strings that are distinct. Two strings are distinct if, on applying the following operations on one string, the second string cannot be formed.  
#A character on the odd index can be swapped with another character on the odd index only.
#A character on even index can be swapped with another character on even index only.

s = input().split()
c = 0
e,o = [],[]
for i in s:
    e.append(sorted(i[::2]))
    o.append(sorted(i[1::2]))

e = [list(x) for x in set(tuple(x) for x in e)]
o = [list(x) for x in set(tuple(x) for x in o)]

print(len(e))