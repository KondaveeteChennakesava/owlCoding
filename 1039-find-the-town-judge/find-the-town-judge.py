class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if trust == [] and n == 1:
            return 1
        dic = {}
        s = set()
        for ele in trust:
            s.add(ele[0])
            if ele[1] not in dic:
                dic[ele[1]] = 1
            else:
                dic[ele[1]] += 1
        # print(dic)
        if dic:
            for i,j in dic.items():
                if j == n-1 and i not in s:
                    return i
        return -1