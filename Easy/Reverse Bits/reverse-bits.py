#User function Template for python3

class Solution:
    def reversedBits(self, x):
        # code here 
        s = bin(x)[2:]
        ks = '0' * (32 - len(s)) + s
        ks = ks[::-1]
        # print(ks)
        return int(ks, 2)
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        X=int(input())
        
        ob = Solution()
        print(ob.reversedBits(X))
# } Driver Code Ends