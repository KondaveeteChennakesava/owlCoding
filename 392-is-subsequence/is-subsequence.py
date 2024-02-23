class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == '':return True
        idx = 0
        key = s[idx]
        for i in range(len(t)):
            if t[i] == key:
                idx += 1
                if idx == len(s):return True
                key = s[idx]
        return False