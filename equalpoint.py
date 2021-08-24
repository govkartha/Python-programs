#Equal point in a string of brackets
#https://practice.geeksforgeeks.org/problems/find-equal-point-in-string-of-brackets2542/1/
#Given a string S of opening and closing brackets '(' and ')' only. The task is to find an equal point. An equal point is an index such that the number of closing brackets on right from that point must be equal to number of opening brackets before that point.

s = input()
o = [0] * (len(s)+1)
c = [0] * (len(s)+1)
o[-1],c[len(s)],index = 0,0,-1
for i in range(0,len(s)):
    if(s[i] == '('):
        o[i] = o[i-1] + 1
    else:
        o[i] = o[i-1]
for i in range(len(s)-1,-1,-1):
    if(s[i] == ')'):
        c[i] = c[i+1] + 1
    else:
        c[i] = c[i+1]
for i in range(0,len(s)):
    if(o[i]==c[i]):
        index = i
if(o[len(s)-1]==0):
    print(len(s))
elif(c[0]==0):
    print(0)
else:
    print(index)
