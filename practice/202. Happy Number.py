def isHappy(n):
    if n == 1:
        return 1
    s = 0
    while n:
        r = n%10
        n = n//10
        s += r ** 2
    if s == 7:
        return 1
    if s<10 and s!=1:
        return 0  
    return isHappy(s)
print(isHappy(100))