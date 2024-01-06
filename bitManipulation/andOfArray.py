def andArray(l,r,arr):
    res = arr[l]
    for i in range(l+1,r+1):
        res = res & arr[i]
        if res == 0:
            return 0
    return res

arr = list(map(int,input().split()))
q = int(input())
while(q):
    l,r = map(int,input().split())
    print(andArray(l,r,arr))
    q -= 1