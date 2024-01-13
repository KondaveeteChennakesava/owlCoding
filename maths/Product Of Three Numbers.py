for _ in range(int(input())):
    n = int(input())
    a,b,c = 1,1,1
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            a = i
            break
    n = n // a
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            if i != a:
                b = i
                break
            if (n//i != i) and (n//i != a):
                b = min(i,n//i)
    c = n // b
    if((a != b) and (b != c) and (c != 1)):
        print('YES')
        print(a,b,c)
    else:
        print('NO')