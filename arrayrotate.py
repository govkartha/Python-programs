#Rotate Matrix - interviewbit
'''Given an image represented by an NxN matrix
write a method to rotate the image by 90 degrees.'''

n,a = int(input()),[]

for _ in range(n):
    a.append(list(map(int, input().split()[:n])))

for i in range(n):
    for j in range(n-1,-1,-1):
        print(a[j][i], end=" ")
    print()