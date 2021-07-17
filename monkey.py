'''N monkeys are invited to a party where they start dancing. They dance in a circular formation, very similar to a Gujarati Garba or a Drum Circle. The dance requires the monkeys to constantly change positions after every 1 second.

The change of position is not random & you, in the audience, observe a pattern. Monkeys are very disciplined & follow a specific pattern while dancing.

Consider N = 6, and an array monkeys = {3,6,5,4,1,2}.

This array (1-indexed) is the dancing pattern. The value at monkeys[i], indicates the new of position of the monkey who is standing at the ith position.

Given N & the array monkeys[ ], find the time after which all monkeys are in the initial positions for the 1st time.'''

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
