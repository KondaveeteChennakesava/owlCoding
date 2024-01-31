import sys
sys.setrecursionlimit(10**9)
class Solution:
    def lastRemaining(self, n: int) -> int:
        if n == 0:return 0
        if n == 1:return 1
        return 2*(1+n//2-self.lastRemaining(n//2))