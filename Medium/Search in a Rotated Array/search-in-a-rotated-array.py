#User function Template for python3

class Solution:
    def search(self, A : list, l : int, h : int, key : int):
        A = A[l:h+1]
        if key in A:
            return A.index(key)
        return -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        A = [int(x) for x in input().split()]
        k = int(input())
        ob=Solution()
        print(ob.search(A, 0, n - 1, k))
# } Driver Code Ends