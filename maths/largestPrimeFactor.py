def largestPrimeFactor (N):
    k = isPrime(N)
    if k:
        return N
    l = []
    for i in range(2,int(N**0.5)+1):
        if N%i == 0:
            if isPrime(i):
                l.append(i)
            if isPrime(N//i):
                l.append(N//i)
    return l[-1]
        
def isPrime(n):
    if n < 2:
        return 0
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return 0
    return 1
print(largestPrimeFactor(69875))