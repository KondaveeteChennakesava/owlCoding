class Solution:
    def pivotInteger(self, n: int) -> int:
        if n == 1:return 1
        temp = n - 1
        while temp:
            ryt = sum(range(temp, n + 1))
            lft = sum(range(1,temp + 1))
            # print(lft,ryt)
            if ryt == lft:
                return temp
            temp -= 1
        return -1