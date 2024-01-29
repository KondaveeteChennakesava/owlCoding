class Solution:
    def countHomogenous(self, s: str) -> int:
        l = []
        cnt = 0
        for i in range(len(s)-1):
            # print(ans,cnt)
            if s[i] == s[i+1]:
                cnt += 1
            else:
                l.append(cnt+1)
                cnt = 0
        l.append(cnt+1)
        ss = 0
        for i in l:
            ss += (i*(i+1))//2
        return ss%int(1e9+7)