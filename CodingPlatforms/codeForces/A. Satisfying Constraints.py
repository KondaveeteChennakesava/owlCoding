for _ in range(int(input())):
    start,end,skip = 0,float('inf'),[]
    for q in range(int(input())):
        k,x = map(int,input().split())
        if k == 1:
            start = max(start,x)
        elif k == 2:
            end = min(end,x)
        else:
            skip.append(x)
    if end < start:
        print(0)
    else:
        cnt = 0
        for i in skip:
            if i>=start and i <= end:
                cnt += 1
        print(end-start-cnt+1)