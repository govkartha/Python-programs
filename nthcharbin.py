#Find the N-th character
#https://practice.geeksforgeeks.org/problems/find-the-n-th-character5925/1/
#Given a binary string S . Perform R iterations on string S, where in each iteration 0 becomes 01 and 1 becomes 10. Find the Nth character (considering 0 based indexing) of the string after performing these R iterations.

s = input()
r = int(input())
n = int(input())
d = {"0":"01", "1":"10"}
for _ in range(r):
    s = ''.join(d[i] for i in s)
print(s[n])