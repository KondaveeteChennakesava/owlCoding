N = (10**5)
mod = (10**9)+7
fact = [None] * N
invFact = [None] * N
def be(a,b):
    ans = 1
    while b:
        if b & 1:
            ans = ((ans%mod)*(a%mod))%mod
        a = ((a%mod)*(a%mod))%mod
        b = b >> 1
    return ans  
def preFact():
    fact[0] = 1
    invFact[0] = 1
    for i in range(1,N):
        fact[i] = fact[i-1] * i
        fact[i] = fact[i] % mod
        invFact[i] = be(fact[i],mod-2)
preFact()
for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    ans = (((fact[10-n]%mod) * (invFact[2]%mod) * (invFact[10-n-2]%mod))%mod)* 6
    print(ans)