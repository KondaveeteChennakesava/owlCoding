for _ in range(int(input())):
    n = int(input())
    temp = n
    for i in range(n-1,-1,-1):
        temp = temp & i
        if temp == 0:
            print(i)
            break