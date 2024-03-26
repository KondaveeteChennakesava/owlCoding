#User function Template for python3

class Solution:
    
    #Function to find the smallest positive number missing from the array.
    def missingNumber(self,arr,n):
        #Your code here
        arr.sort()
        if 1 not in arr:
            return 1
        for i in range(1, len(arr)):
            if arr[i] > 0 and arr[i-1] > 0 and arr[i] - arr[i-1] > 1:
                return arr[i-1] + 1
        return arr[-1] + 1


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
            print(ob.missingNumber(arr,n))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends