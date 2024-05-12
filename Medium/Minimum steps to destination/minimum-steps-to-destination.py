#User function Template for python3

class Solution:
    def minSteps(self, d):
        # code here
        for i in range(1, 2 * d):
            if ((((i * (i + 1)) / 2) + d) % 2 == 0 and ((i * (i + 1)) / 2) >= d):
                return i
        return -1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        d = int(input())

        ob = Solution()
        print(ob.minSteps(d))

# } Driver Code Ends