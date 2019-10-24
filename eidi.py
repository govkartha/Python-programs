t=int(input())
while(t):
    lst=list(map(int,input().split())
    i=lst[0]
    j=lst[3]
    flag1,flag2,flag3=0,0,0
    if(lst[i]>lst[i+1] and lst[j]>lst[j+1]):
        flag1=1
    if(lst[i]==lst[i+1] and lst[j]==lst[j+1]):
        flag2=1
    if(lst[i]<lst[i+1] and lst[j]<lst[j+1]):
        flag3=1
    if(flag1 and flag2 and flag3):
        print("FAIR")
    else:
        print("UNFAIR")
    t-=1