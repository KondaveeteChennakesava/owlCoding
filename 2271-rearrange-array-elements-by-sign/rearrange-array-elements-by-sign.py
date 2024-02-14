class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos,neg = [],[]
        for i in nums:
            if i > 0:
                pos.append(i)
            else:
                neg.append(i)
        nums[0:len(pos)*2:2] = pos
        nums[1:len(neg)*2:2] = neg
        return nums