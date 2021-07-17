#Power of two integers - interviewbit
#https://www.interviewbit.com/problems/power-of-two-integers/
#Given a positive integer which fits in a 32 bit signed integer, 
#find if it can be expressed as A^P where P > 1 and A > 0. A and P both should be integers.

import math   
n = int(input())
flag = 0
if n <= 0:
    print(False)
elif(n == 1):
    print(True)
else:
    for x in range(2,int(math.sqrt(n))+1):
        y = math.log10(n)/math.log10(x)
        if y == int(y):
            print(True)
            flag = 1
            break
    if flag == 0:
        print(False)