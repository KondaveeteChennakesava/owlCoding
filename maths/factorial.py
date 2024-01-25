def fact(n):
    mod = 1000000007
    if n == 1:
        return 1
    return n * fact((n-1)%mod)
print(fact(400))