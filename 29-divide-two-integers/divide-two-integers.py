class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        ans = int(dividend / divisor)
        if ans > (2**31 - 1):
            return (2 ** 31 -1)
        if ans < (-2 ** 31):
            return (-2 ** 31)
        return ans