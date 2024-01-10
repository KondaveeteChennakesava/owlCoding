def majorityElement(nums):
    d = {}
    for i in nums:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    m = 0
    k = -1
    for i,j in d.items():
        if j>=m:
            m = j
            k = i
    return k
print(majorityElement([2,2,1,1,1,2,2]))