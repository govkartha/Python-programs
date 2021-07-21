#Minimum Parantheses - interviewbit
#https://www.interviewbit.com/problems/minimum-parantheses/
#Given a string S of '(' and ')' parentheses, 
#we add the minimum number of parentheses ( '(' or ')', and in any positions ) so that the resulting parentheses string is valid.

s = input()
c,p = 0,0
for i in s:
    if i == '(':
        c += 1
    else:
        c -= 1
        if c < 0:
            c = 0
            p += 1
print(p+c)

