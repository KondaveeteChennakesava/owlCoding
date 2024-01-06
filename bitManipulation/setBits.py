n = int(input())
for i in range(1,n+1):
    if (i and ((i & (i - 1)) == 0)):
        print('-----------------------')
    l = bin(i)[2:]
    print(l,l.count('1'))