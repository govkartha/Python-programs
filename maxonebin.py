#Flip - interviewbit
#https://www.interviewbit.com/problems/flip/
#Aim is to perform ATMOST one operation such that in final string number of 1s is maximised.

b = list(map(int, input().split()))

i,j = 0,1
while(i<len(b) and j<len(b)):
    if(b[i:j].count(0) > b[i:j].count(1)):
        b[i:j] = ~(b[i:j])
        break
