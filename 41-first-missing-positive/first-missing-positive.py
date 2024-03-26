class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        if 1 not in nums:
            return 1
        for i in range(1,len(nums)):
            if nums[i] > 0 and nums[i-1] > 0 and nums[i] - nums[i-1] > 1:
                return nums[i-1] + 1
        return nums[-1] + 1
            