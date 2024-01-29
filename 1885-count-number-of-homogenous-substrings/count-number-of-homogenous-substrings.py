class Solution:
    def countHomogenous(self, s: str) -> int:
        ans,cnt = 0,0
        if len(s) == 1:
            ans += 1
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                cnt += 1
            else:
                cnt += 1
                k = (cnt*(cnt+1))//2
                ans += k
                cnt = 0
        if len(s)>=2 and s[-2] != s[-1] or cnt:
            cnt += 1
            ans += (cnt*(cnt+1))//2
        return ans%int(1e9+7)