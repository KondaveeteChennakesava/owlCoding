from typing import List
def missingInteger(self, nums: List[int]) -> int:
    pl = nums[0]
    for i in range(1,len(nums)):
        if nums[i] - 1 == nums[i-1]:
            pl += nums[i]
        else:
            break
    k = pl
    if k not in nums:
        return k
    while 1:
        if k not in nums:
            break
        else:
            k += 1
        
    return k