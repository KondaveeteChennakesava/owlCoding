for _ in range(int(input())):
    s = input()
    if s[0] == '0':
        print(0)
    else:
        ans = 1
        if s[0] == '?':
            ans *= 9
        for i in range(1,len(s)):
            if s[i] == '?':
                ans *= 10
        print(ans)