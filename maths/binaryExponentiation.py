def binaryExpo(a,b):
    res = 1
    while b:
        if b&1:
            b -= 1
            res *= a
        else:
            b //= 2
            a = a * a
    return res

def inverse(a):
    mod = 10**9 + 7
    return binaryExpo(a,mod-2)


print(binaryExpo(2,9))