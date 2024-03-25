#User function Template for python3
class Solution:
	def NBitBinary(self, n):
		# code here
		cnt_0, cnt_1 = 0,0
		ans = []
		string = ''
		self.helper(cnt_1, cnt_0, ans, string, n)
        return ans
        

    def helper(self, cnt_1, cnt_0, ans, string, n):
        if n == 0:
            ans.append(string)
            return
        self.helper(cnt_1 + 1, cnt_0, ans, string + '1', n-1)
        if cnt_1 > cnt_0:
            self.helper(cnt_1, cnt_0 + 1, ans, string + '0', n-1)
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution()	
		answer = ob.NBitBinary(n)
		for value in answer:
			print(value,end=" ")
		print()


# } Driver Code Ends