class Solution:
    def minimumLength(self, s: str) -> int:
        if len(s) == 1:return 1
        if len(set(s)) == 1:return 0
        def rec(s,i,j):
            # print(s[i:j+1])
            if s[i] != s[j] or i >= j:
                return len(s[i:j+1])
            for x in range(i,j+1):
                if s[x] != s[x+1]:
                    i = x + 1
                    break
            for x in range(j,-1,-1):
                if s[x] != s[x - 1]:
                    j = x - 1
                    break
            return rec(s,i,j)
        return rec(s,0,len(s)-1)