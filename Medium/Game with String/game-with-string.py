#User function Template for python3

class Solution:
    def minValue(self, s, k):
        # code here
        d = {}
        for i in s:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        ans = list(d.values())
        ans.sort()
        while k:
            ans[-1] -= 1
            k -= 1
            ans.sort()
        cnt = 0
        for i in ans:
            cnt += (i**2)
        return cnt


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        k = int(input())
        
        ob = Solution()
        print(ob.minValue(s, k))
# } Driver Code Ends