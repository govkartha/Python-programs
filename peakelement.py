#Peak element 
#A peak element in an array is the one that is not smaller than its neighbours
#https://practice.geeksforgeeks.org/problems/peak-element/1

a = list(map(int, input().split()))
b,l,flag = 0, len(a)-1, 0
while(b<=l):
    mid = (l+b)//2
    if(mid==0 or a[mid-1]<=a[mid] and mid==len(a)-1 or a[mid+1]<=a[mid] ):
        print(mid)
        flag = 1
        break
    elif(a[mid-1]>a[mid] and mid>0):
        l = mid-1
    else:
        b = mid+1
