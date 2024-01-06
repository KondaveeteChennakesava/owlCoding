n = int(input())
l = list(map(int,input().split()))

res = 0
for i in range(32):
    onesCount = 0
    for j in range(n):
        if l[j] & (1 << i):
            onesCount += 1
    if onesCount % 4 != 0:
        res = res | (1 << i)
print(res)