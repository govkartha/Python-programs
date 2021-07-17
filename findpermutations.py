#Find Permutation - interviewbit
'''Given a positive integer n and a string s consisting only of letters D or I, 
you have to find any permutation of first n positive integer that satisfy the given input string.
D means the next number is smaller, while I means the next number is greater.'''

n = int(input())
s = input()
mn,mx = 1,n
l = []
for i in s:
    if(i=='D'):
        l.append(mx)
        mx -= 1
    if(i=='I'):
        l.append(mn)
        mn += 1
l.append(mn)
print(l)