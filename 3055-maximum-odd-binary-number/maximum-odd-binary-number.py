class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ones = s.count('1')
        zers = s.count('0')
        ans = ''
        ans += '1'* (ones-1)
        ans += '0'*zers
        ans += '1'
        return ans