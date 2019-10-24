seq = 1
n= 2
while(1):
    count=0
    for div in range(1,int(seq**0.5)):
        if seq%div==0:
            count+=2
    if count>500:
        print(seq)
        break

    seq+=n
    n+=1

    
    

    

