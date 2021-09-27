a = input()
c = '1'
count = 0
for i in range(len(a)):
    if (a[i] == c):
        count += 1
        c = chr(48 + (ord(c) + 1)%2)
        print(c)
print(count)