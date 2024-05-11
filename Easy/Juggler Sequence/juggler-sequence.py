#User function Template for python3

class Solution:
    def jugglerSequence(self, n):
        # code here
        arr = []
        while True:
            arr.append(n)
            if n == 1:
                return arr
            if n % 2:
                n = int(n**(3/2))
            else:
                n = int(n**(1/2))

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())

        ob = Solution()
        arr = ob.jugglerSequence(n)
        for i in (arr):
            print(i, end=" ")
        print()

# } Driver Code Ends