#Set Matrix Zero
#Given a matrix, A of size M x N of 0's and 1's. 
# If an element is 0, set its entire row and column to 0.

n = int(input())
a = []
for _ in range(n):
    a.append(list(map(int, input().split()[:n])))

b = []
for i in range(n):
    if(0 in a[i]):
        b.append([0 for _ in range(n)])
    else:
        b.append([1 for _ in range(n)])

print("--------------------------")
for i in range(n):
    for j in range(n):
        print(b[i][j], end=" ")
    print()

