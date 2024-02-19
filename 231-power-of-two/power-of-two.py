class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        b = bin(n)[2:]
        if b[0] == '1' and b[1:] == '0'*(len(b)-1):
            return 1
        return 0