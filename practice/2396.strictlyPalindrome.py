def isStrictlyPalindromic(n: int) -> bool:
    if isPal(str(n)) != 1:
        return 0
    for i in range(2,n-1):
        if isPal(base(n,i)) == 0:
            return 0
    return 1

def isPal(s):
    if s == s[::-1]:
        return 1
    return 0
def base(num,b):
    s = ''
    while num > b:
        if num%b == 0:
            s += '0'
        else:
            s += str(num%b)
        num //=b
    s += str(num)
    s = s[::-1]
    return s
print(isStrictlyPalindromic(12))