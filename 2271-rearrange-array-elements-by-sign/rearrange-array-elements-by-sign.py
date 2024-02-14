class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos,neg = [],[]
        for num in nums:
            if num >= 0:
                pos.append(num)
            else:
                neg.append(num)
        nums[0:len(pos)*2:2] = pos
        nums[1:len(neg)*2:2] = neg
        return nums