class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = [nums[i:i+3] for i in range(0,n,3)]
        for i in ans:
            if (i[2] - i[0] > k):
                return []
        return ans