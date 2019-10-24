n=int(input())
j=int(input())
res = [0 for x in range(n+1)]
res[0],res[1] = 1,1
for i in range(2,n+1): 
	k = 1
	while k<=j and k<=i: 
		res[i] = res[i] + res[i-k] 
		k += 1
print(res[n] )

 
