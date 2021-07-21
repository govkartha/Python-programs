#Longest Common Prefix - interviewbit
#https://www.interviewbit.com/problems/longest-common-prefix/
#Write a function to find the longest common prefix string amongst an array of strings.

s = list(map(str,input().split()))
if not s:
    print("")
elif len(s) == 1:
    print(s[0])
else:
    prefix = s[0]
    for i in range(1, len(s)):
        while not s[i].startswith(prefix):
            prefix = prefix[:-1]
            if prefix == "":
                break
    print(prefix)