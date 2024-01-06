n,a,b = map(int,input().split())
c1,c2,d = 0,0,0
for i in range(32):
    if a&(1<<i):
        c1 += 1
    if b&(1<<i):
        c2 += 1
    if a&(1<<i) != b&(1<<i):
        d += 1
if c1%2 == c2%2:
    print(d//2)
else:
    print(-1)