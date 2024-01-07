def countSetBits(n):
        if n == 0:
            return 0
        x = largestPowerOfTwo(n)
        if x <= 0:
            return 1
        s = x * (1 << (x - 1))
        z = n - (1 << x)
        return s + z + 1 + countSetBits(z)
        
def largestPowerOfTwo(n):
    res = 0
    while (1<<res) <= n:
        res += 1
    return res-1

print(countSetBits(4))