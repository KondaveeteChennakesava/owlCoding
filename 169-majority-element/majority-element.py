class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        me =  0 
        c = 0 
        for i in nums:
            if c  == 0 : 
                me = i 
            if me == i:
                c += 1 
            else:
                c -= 1 
        return me