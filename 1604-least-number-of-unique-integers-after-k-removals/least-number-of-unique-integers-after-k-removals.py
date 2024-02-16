class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freq,ans,secans = {},[],[]
        for i in arr:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1
        freq = sorted(freq.items(), key = lambda x:x[1])
        for i in freq:
            x = [i[0]]*i[1]
            ans += x
        # print(ans)
        # return 0
        return len(set(ans[k:]))