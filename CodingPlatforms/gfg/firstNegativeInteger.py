def printFirstNegativeInteger( a, n ,k):
    # code here
    l = []
    for i in range(n-k+1):
        cnt = 0
        for j in range(i,i+k):
            cnt += 1
            if a[j] < 0:
                l.append(a[j])
                break
            if cnt == k:
                l.append(0)
    return l
print(printFirstNegativeInteger([-8, 2, 3, -6, 10],5,2))