def seive(n):
    primes = [i for i in range(n+1)]
    primes[0],primes[1] = 0,0
    for i in range(2,int(n**0.5)+1):
        if primes[i]:
            for j in range(i*i,n+1,i):
                primes[j] = i
    return primes
n = 25
factors = seive(n)
print(factors)