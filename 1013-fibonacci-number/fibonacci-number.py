class Solution:
    def fib(self, n: int) -> int:
        ans = [0,1]
        for i in range(1,n):
            ans.append(ans[i]+ans[i-1])
        return ans[n]