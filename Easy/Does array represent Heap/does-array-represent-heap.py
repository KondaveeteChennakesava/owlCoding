
class Solution:
    def isMaxHeap(self,arr,n):
        # Your code goes here            
        d,idx = {},1
        for i in arr:
            if idx >= n:
                break
            d[i] = [arr[idx]]
            idx += 1
            if idx >= n:
                break
            d[i].append(arr[idx])
            idx += 1
        for i,j in d.items():
            if i < max(j):
                return 0
        return 1
#{ 
 # Driver Code Starts
if __name__ =='__main__':
    t= int(input())
    for tcs in range(t):
        n=int(input())
        arr=[int(x) for x in input().split()]
        ob=Solution()
        print(int(ob.isMaxHeap(arr,n)))
# } Driver Code Ends