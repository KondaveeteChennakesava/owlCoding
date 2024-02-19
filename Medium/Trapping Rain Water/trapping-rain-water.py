
class Solution:
    def trappingWater(self, arr,n):
        #Code here
        lef,rig,ans = [],[],[]
        lm,rm = arr[0],arr[-1]
        for i in range(n):
            lm = max(lm,arr[i])
            lef.append(lm)
        for i in range(n-1,-1,-1):
            rm = max(rm,arr[i])
            rig.append(rm)
        rig = rig[::-1]
        for i in range(n):
            ans.append(min(abs(arr[i] - lef[i]) , abs(arr[i] - rig[i])))
        # print(lef,rig,ans)
        return sum(ans)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math



def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            obj = Solution()
            print(obj.trappingWater(arr,n))
            
            
            T-=1


if __name__ == "__main__":
    main()



# } Driver Code Ends