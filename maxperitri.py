#Construct a triangle with max perimeter when a list of side lengths are given

from itertools import product,repeat
n = int(input())
r = (-1,-1,-1)
l = sorted(map(int, input().split()))
for a,b,c in product(*repeat(l,3)):
    if(a<b<c and (a+b)>c):
        r = max(r,(a,b,c))
if(r[0]==-1):
    print(-1)
else:
    print(r[0],r[1],r[2])