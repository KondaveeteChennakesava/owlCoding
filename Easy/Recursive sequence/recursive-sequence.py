#User function Template for python3

class Solution:
    def sequence(self, n):
        # code here
        s,a = 1,2
        mod = (10**9)+7
        for i in range(2,n+1):
            p,b = 1,a+i
            for j in range(a,b):
                p *= j
            s += p
            a = b
        return s % mod


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        
        ob = Solution()
        print(ob.sequence(N))
# } Driver Code Ends