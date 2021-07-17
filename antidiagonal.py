#Anti diagonals - interviewbit
'''Give a N*N square matrix, return an array of its anti-diagonals.'''

n = int(input())
a = []
for _ in range(n):
    a.append(list(map(int, input().split()[:n])))

ad = []
for _ in range(2*n-1):
    ad.append([])
for i in range(n):
    for j in range(n):
        ad[i+j].append(a[i][j])

for i in ad:
    print(i)



