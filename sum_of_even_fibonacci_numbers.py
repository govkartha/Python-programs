n=int(input())
a, b = 1, 1
total = 0
while (a < n):
    if a % 2 == 0:
        total += a
    a, b = b, a+b  
print(total)

#alternate solution

a, b = 0, 1
total = 0

while a<n:
    total+=a
    a, b = a + 2*b, 2*a + 3*b
    
print(total)
