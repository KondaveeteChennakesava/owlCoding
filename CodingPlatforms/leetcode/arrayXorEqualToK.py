from typing import List
def minOperations(self, nums: List[int], k: int) -> int:
    res = 0
    for i in nums:
        res = res ^ i
    x = res ^ k
    cnt = 0
    while x:
        cnt += x & 1
        x = x >> 1
    return cnt