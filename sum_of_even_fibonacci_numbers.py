n=int(input())
a, b = 1, 1
total = 0
while (a < n):
    if a % 2 == 0:
        total += a
    a, b = b, a+b  
print(total)