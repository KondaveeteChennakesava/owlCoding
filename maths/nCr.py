mod = (10**9)+7
def nCr(n,r):
    res = 1
    for i in range(n-r+1,n+1):
        res *= i
    for i in range(1,r+1):
        res //= i
    return res

def be(a,b):
    res = 1
    while b:
        if b&1:
            res = ((res%mod) * (a%mod)) % mod
        a = ((a % mod)*(a % mod)) % mod
        b = b >> 1
    return res

N = (10**5)+1
fact = [None] * N
invfact = [None] * N

def preFact():
    fact[0] = 1
    invfact[0] = 1
    for i in range(1,N):
        fact[i] = fact[i-1] * i
        fact[i] %= mod
        invfact[i] = be(fact[i],mod-2)
for _ in range(int(input())):
    n,r = map(int,input().split())
    # print(nCr(n,r))
    preFact()
    # ans = fact[n] // (fact[r] * fact[n-r])
    ans = ((fact[n]%mod)*(invfact[r]%mod)*(invfact[n-r]%mod)) % mod
    print(ans)