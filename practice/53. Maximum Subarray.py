from typing import List
def maxSubArray(nums: List[int]) -> int:
        ma = float('-inf')
        cnt = 0
        for i in range(len(nums)):
            cnt += nums[i]
            if cnt > ma:
                ma = cnt
            if cnt < 0:
                cnt = 0
        return ma
print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))