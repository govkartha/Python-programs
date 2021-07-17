from itertools import permutations

n = input()
l = []
p = sorted(permutations(n,len(n)))
for i in p:
    l.append("".join(i))
ind = l.index(n)
if(ind==len(l)-1):
    print(l[0])
else:
    print(l[ind+1])

