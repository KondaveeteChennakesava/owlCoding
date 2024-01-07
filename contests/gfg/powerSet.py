def AllPossibleStrings(s):
    # Code here
    n = len(s)
    l = []
    for i in range(1,(1<<n)):
        k = ''
        for j in range(n):
            if (i>>j)&1:
                k += s[j]
        l.append(k)
    l.sort()
    return l
print(AllPossibleStrings('abc'))