class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        l = []
        for i in strs:
            l.append(["".join(sorted(i)),i])
        d = {}
        for i,j in l:
            if i not in d:
                d[i] = []
                d[i].append(j)
            else:
                d[i].append(j)
        print(d)
        return list(d.values())