#WoodCutting Made Easy - interviewbit
#https://www.interviewbit.com/problems/woodcutting/

a = list(map(int,input().split()))
b = int(input())
a.sort()
l,r = 0,a[len(a)-1]
while(l<=r):
    mid = (l+r)//2
    s = 0
    for i in range(len(a)):
        if(a[i] > mid):
            s += a[i] - mid
    if(s==b):
        print(mid)
        break
    elif(s > b):
        l = mid+1
    else:
        r = mid-1
