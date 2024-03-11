#User function Template for python3
class Solution:
	def countPairs(self, mat1, mat2, n, x):
		i,j,cnt = 0,n*n-1,0
		while i < (n * n) and j >= 0:
		    ele = mat1[i//n][i % n] + mat2[j // n][j % n]
		    if ele == x:
		        cnt += 1
		        i += 1
		        j -= 1
            elif ele > x:
                j -= 1
            else:
                i += 1
        return cnt
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n , x = input().split()
		n,x = int(n), int(x)
		mat1 = []
		for _ in range(n):
			a = [int(x) for x in input().split()]
			mat1.append(a)

		mat2 = []
		for _ in range(n):
			a = [int(x) for x in input().split()]
			mat2.append(a)

		ob = Solution()
		ans = ob.countPairs(mat1, mat2, n, x)
		print(ans)

# } Driver Code Ends