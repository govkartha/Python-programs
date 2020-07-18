P = int(input())
Q = int(input())
R = int(input())
S = int(input())

    
def cadbury(l,b):

    c = 0
    while True:
        longbar,shortbar = max(l,b),min(l,b)
        c += 1
        diff = longbar - shortbar
        if diff==0:
            return c
        else :
            l = min(l,b)
            b = diff

count=0
for l in range(P,Q+1):
    for b in range(R,S+1):
        count += cadbury(l,b)

print(count)