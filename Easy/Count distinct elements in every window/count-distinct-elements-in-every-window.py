
class Solution:
    def countDistinct(self, A, N, K):
        # Code here
        d = {}
        for i in A[:k]:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        ans = [len(d)]
        for i in range(k,N):
            d[A[i-k]] -= 1
            if d[A[i-k]] == 0:
                del d[A[i - k]]
            if A[i] not in d:
                d[A[i]] = 1
            else:
                d[A[i]] += 1
            ans.append(len(d))
        return ans
#{ 
 # Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n,k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        res = Solution().countDistinct(arr, n, k)
        for i in res:
            print (i, end = " ")
        print ()
# } Driver Code Ends