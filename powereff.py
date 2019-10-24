MOD=1000000007
def exp(base,pow):
    result = 1
    while pow > 0:
        if pow % 2 == 1:
            result = (result * base) % MOD
        pow = pow // 2
        base = (base * base) %MOD
    return result

#print(exp(99999,(10**4)))
print(exp(2,1000))