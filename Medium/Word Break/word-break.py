#User function Template for python3

class Solution:
    def wordBreak(self, n, s, d):
        # Complete this function
        def moon(s):
            if (s=="") or s in d:
                return True
            for i in range(len(s)):
                s1=s[:i]
                s2=s[i:]
                if s1 in d and moon(s2):
                    return True
            return False
        return moon(s)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	test_case = int(input())

	for _ in range(test_case):
		n = int(input())
		dictionary = [word for word in input().strip().split()]
		s = input().strip()
		ob = Solution()
		res = ob.wordBreak(n, s, dictionary)
		if res:
			print(1)
		else:
			print(0)
# } Driver Code Ends