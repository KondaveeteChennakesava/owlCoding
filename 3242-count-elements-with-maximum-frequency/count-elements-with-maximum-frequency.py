class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        dic = {}
        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        ans = list(dic.values())
        return max(ans) * ans.count(max(ans))