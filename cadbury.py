'''You are a teacher in reputed school. During Celebration Day you were assigned a task to distribute Cadbury such that maximum children get the chocolate. You have a box full of Cadbury with different width and height. You can only distribute largest square shape Cadbury. So if you have a Cadbury of length 10 and width 5, then you need to break Cadbury in 5X5 square and distribute to first child and then remaining 5X5 to next in queue


Constraints

0<P<Q<1501
0<R<S<1501

Input Format

First line contains an integer P that denotes minimum length of Cadbury in the box

Second line contains an integer Q that denotes maximum length of Cadbury in the box

Third line contains an integer R that denotes minimum width of Cadbury in the box

Fourth line contains an integer S that denotes maximum width of Cadbury in the box

Output

Print total number of children who will get chocolate.'''

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
