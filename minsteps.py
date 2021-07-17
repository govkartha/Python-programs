#Minimum steps in infinite grid - interviewbit
'''Given a sequence of points and the order in which you need to cover the points.
Give the minimum number of steps in which you can achieve it.'''

a = list(map(int, input().split()))
b = list(map(int, input().split()))

s = 0
for i in range(len(a)-1):
    s += max(abs(a[i+1]-a[i]), abs(b[i+1]-b[i]))
print(s)