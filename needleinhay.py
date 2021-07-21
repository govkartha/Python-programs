#Implement StrStr - interviewbit
#https://www.interviewbit.com/problems/strstr/

haystack = input()
needle = input()
flag = 0
for i in range(len(haystack)):
    if haystack[i] == needle[0]:
        if haystack[i:i+len(needle)] == needle:
            print(i)
            flag = 1
            break
if flag == 0:
    print("-1")
        