class Solution:
    def trap(self, height: List[int]) -> int:
        ltr,rtl = [],[]
        lm,rm = height[0],height[-1]
        for i in range(len(height)):
            lm = max(lm,height[i])
            ltr.append(lm)
        for i in range(len(height)-1,-1,-1):
            rm = max(rm,height[i])
            rtl.append(rm)
        rtl = rtl[::-1]
        ans = []
        for i in range(len(height)):
            lft = abs(height[i] - ltr[i])
            ryt = abs(height[i] - rtl[i])
            ans.append(min(lft,ryt))
        # print(ltr,rtl,ans)
        return sum(ans)