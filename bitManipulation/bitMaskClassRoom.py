for _ in range(int(input())):
    n = int(input())
    for i in range(1,2**30):
        if (n&i > 0) and (n^i > 0):
            print(i)
            break