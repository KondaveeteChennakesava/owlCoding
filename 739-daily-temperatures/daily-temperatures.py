class Solution:
    def dailyTemperatures(self, arr: List[int]) -> List[int]:
        n = len(arr)
        ans = [0]*n
        stack = []
        for i in range(n):
            while stack and arr[i] > arr[stack[-1]]:
                k = stack.pop()
                ans[k] = i-k
            stack.append(i)
        return ans