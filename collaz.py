high=0
for i in range(1,1000000):    
    count = 1
    n=i
    while n!=1 :
        count+=1
        if n%2 == 0:
            n/=2
        else:
            n=3*n+1
    if count>high:
        high=count
        num=i
print(num)
