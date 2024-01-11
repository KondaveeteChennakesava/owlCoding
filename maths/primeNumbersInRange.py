def primeRange(m,n):
    l = [1 for i in range(n+1)]
    l[0],l[1] = 0,0
    for i in range(2,n+1):
        if l[i]:
            for j in range(i*i,n+1,i):
                l[j] = 0
    primes = []
    for i in range(len(l)):
        if l[i]:
            primes.append(i)
    k = []
    for i in primes:
        if i>=m:
            k.append(i)
    return k
print(primeRange(12,30))