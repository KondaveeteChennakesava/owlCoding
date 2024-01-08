def minOperations(n: int) -> int:
    cnt = 0
    l = []
    for i in range(n):
        l.append((2*i)+1)
    k = sum(l) // n
    for i in range(n//2):
        cnt += k-l[i]
    return cnt
print(minOperations(3))