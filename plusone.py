#Add One to Number - interviewbit
#https://www.interviewbit.com/problems/add-one-to-number/
#Given a non-negative number represented as an array of digits, plus one to the number.

n = list(map(str, input().split()))

a = ("").join(n)
a = -(~(int(a)))

print(list(map(int,list(str(a)))))