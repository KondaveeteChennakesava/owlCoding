#User function Template for python3

class Solution:
    #Complete this function
    # Function to find the maximum index difference.
    def maxIndexDiff(self,a, n): 
        ##Your code here
        if n == 1:return 0
        ans = float('-inf')
        for i in range(n):
            j = n - 1
            while i <= j :
                if a[i] <= a[j]:
                    ans = max(ans, j - i)
                    break
                j -= 1
        return ans
#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            ob=Solution()
            print(ob.maxIndexDiff(arr,n))
            
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends