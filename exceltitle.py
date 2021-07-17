#Excel Column Title - interviewbit
'''Given a positive integer A, 
return its corresponding column title as appear in an Excel sheet.'''

s = input()

r = 0
for i,v in enumerate(reversed(s)):
    r += (ord(v)-ord('A')+1)*(26**i)
print(r)