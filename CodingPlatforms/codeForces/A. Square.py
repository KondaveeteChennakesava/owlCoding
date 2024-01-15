for _ in range(int(input())):
    m = []
    for i in range(4):
        a,b = map(int,input().split())
        m.append([a,b])
    m.sort()
    s = abs(m[0][1] - m[1][1])
    print(s**2)