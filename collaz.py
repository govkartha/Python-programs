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


#alternate memoization soultion
memo = [-1]*1000000
memo[1] = 0

high = 0
num = -1
for i in range(1,1000000):    
    count = 0
    n=i
    while n > 1000000 or memo[n] == -1:
        count+=1
        if n%2 == 0:
            n/=2
        else:
            n=3*n+1
         
    memo[i] = memo[n]+ count
    if memo[i] >high:
        high=memo[i]
        num=i
print(num)
