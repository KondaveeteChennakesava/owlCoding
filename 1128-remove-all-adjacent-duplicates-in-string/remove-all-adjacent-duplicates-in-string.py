class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        i = 0
        while i < len(s):
            if len(stack) == 0 or stack[-1] != s[i]:
                stack.append(s[i])
            else:
                stack.pop()
            i += 1
        return ''.join(stack)