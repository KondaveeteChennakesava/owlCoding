class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        nums = '123456789'
        ans = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)+1):
                if low <= int(nums[i:j]) <= high:
                    ans.append(int(nums[i:j]))
        ans.sort()
        return ans