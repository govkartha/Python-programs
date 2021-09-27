#Teemo Attacking - Leetcode
#https://leetcode.com/problems/teemo-attacking/

timeSeries = list(map(int, input().split()))
duration = int(input())

r,cur = 0,0
for i,t in enumerate(timeSeries):
    if(i>0 and cur>=t):
        r -= (cur-t+1)
    r += duration
    cur = (t+duration-1)
print(r)