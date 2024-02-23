#User function Template for python3
from itertools import permutations
class Solution:
    def find_permutation(self, S):
        ans = list(permutations(S))
        for i in range(len(ans)):
            ans[i] = list("".join(ans[i]))
        fans = []
        for i in ans:
            fans.append(''.join(i))
        return list(set(fans))

#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
	t=int(input())
	for i in range(t):
		S=input()
		ob = Solution()
		ans = ob.find_permutation(S)
		ans.sort()
		for i in ans:
			print(i,end=" ")
		print()
# } Driver Code Ends