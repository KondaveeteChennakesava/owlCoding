from typing import List
def minPairSum(nums: List[int]) -> int:
    nums.sort()
    a = nums[:len(nums)//2]
    b = nums[len(nums)//2:][::-1]
    l = []
    for i in range(len(nums)//2):
        l.append(a[i]+b[i])
    return max(l)
print(minPairSum([3,5,2,3]))