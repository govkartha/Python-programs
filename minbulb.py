#Maximum Lights to Activate - interviewbit
#https://www.interviewbit.com/problems/minimum-lights-to-activate/

a = list(map(int,input().split()))
b = int(input())

c = 0
for i in range(len(a)):
    flag = 0
    for j in range((i+b-1),(i-b+2),-1):
        if(j<len(a) and j>=0): 
            if(a[j]==1):
                c += 1
                flag = 1
                i = j+b-1
                break
    if(flag==0):
        print("-1")
        break

    else: print(c)


 