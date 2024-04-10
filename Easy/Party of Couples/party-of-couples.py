#User function Template for python3

class Solution:
    def findSingle(self, n, arr):
        # code here
        d = {}
        for i in arr:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        for i,j in d.items():
            if j % 2:
                return i
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        arr = input().split()
        for itr in range(N):
            arr[itr] = int(arr[itr])
        
        ob = Solution()
        print(ob.findSingle(N, arr))

# } Driver Code Ends