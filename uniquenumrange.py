#Numbers having Unique (or Distinct) digits
#https://www.geeksforgeeks.org/numbers-unique-distinct-digits/
#Given a range, print all numbers having unique digits. 

b,l = input().split()
for i in range(int(b),int(l)+1):
    if(len(set(str(i))) == len(str(i))):
        print(i, end=" ")