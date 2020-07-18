def groove(m):
    temp = m   
    x = [0]*len(m)  
    count=0
    while(x != m):
        count += 1
        x = [0]*len(m)    
        for i in range(len(m)):
            x[m[i]-1] = temp[i]
        temp = x

    return(count)
 
t = int(input())    
for _ in range(t):
    n = int(input())
    monkeys = list(map(int,input().split()))  
    result = groove(monkeys)

    print(result)