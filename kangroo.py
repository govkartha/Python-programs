
v1=int(input())
v2=int(input())
x1=int(input())
x2=int(input())

flag=1
while(flag==1):
    if x1==x2 or v1==v2:
        flag=0
    elif v1-(v2+(x2-x1)) == 0:
        flag=0
    x1+=v1
    x2+=v2
    else:
        flag=0
if(flag==0):
    print("yes")
else:
    print("no")