#Triplets with Sum between given range
#https://www.interviewbit.com/problems/triplets-with-sum-between-given-range/
#Given an array of real numbers greater than zero,
# Find if there exists a triplet (a,b,c) such that 1 < a+b+c < 2 .

l = list(map(float, input().split()))

a,b,c = l[0],l[1],l[2]
for i in range(3,len(l)):
    if((a+b+c)>1 and (a+b+c)<2):
        print("1")
        break
    elif((a+b+c)<1):
        if(a<b and a<c):
            a = l[i]
        elif(b<a and b<c):
            b = l[i]
        else:
            c = l[i]
    else:
        if(a>b and a>c):
            a = l[i]
        elif(b>a and b>c):
            b = l[i]
        else:
            c = l[i]
if((a+b+c)>1 and (a+b+c)<2):
    print("1")
else:
    print("0")