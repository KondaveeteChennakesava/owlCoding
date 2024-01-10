def findPeakElement(nums):
    peak = float('-inf')
    k = -1
    for i in range(len(nums)-1,-1,-1):
        if peak < nums[i]:
            peak = nums[i]
            k = i
    return k
print(findPeakElement([1,2,1,3,5,6,4]))