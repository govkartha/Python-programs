#Check if string is rotated by two places 
#https://practice.geeksforgeeks.org/problems/check-if-string-is-rotated-by-two-places-1587115620/1
#Given two strings a and b. The task is to find if the string 'b' can be obtained by rotating another string 'a' by exactly 2 places

str1 = input()
str2 = input()
s1 = str1
flag = 0
for _ in range(2):
    s1 = s1[1:] + s1[0]
if(s1 == str2):
    print(1)
    flag = 1
else:
    print(0)
    flag = 1

if(flag==0):
    s1 = str1
    for _ in range(2):
        s1 = s1[0] + s1[1:]
    if(s1 == str2):
        print(1)
    else:
        print(0)
