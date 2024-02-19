#User function Template for python3
class Solution:
	def minJumps(self, arr, n):
	    if n == 1:return 0
	    pos,npos,cnt = 0,0,0
	    for i in range(len(arr)):
	        npos = max(npos,i+arr[i])
	        if i == pos:
	            pos = npos
	            cnt += 1
	            if pos >= len(arr)-1:
	                return cnt
        return -1
#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		Arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.minJumps(Arr,n)
		print(ans)
# } Driver Code Ends