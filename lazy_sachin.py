from itertools import permutations

l=[]
sp=[]
m=int(input())
x=input().split()
for i in range(m):
    l.append(x[i])
pt=permutations(l)
for i in pt:
    sp.append(int("".join(map(str,i))))
print(sum(sp))