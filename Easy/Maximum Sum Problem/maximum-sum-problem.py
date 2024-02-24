#User function Template for python3

class Solution:
    def maxSum(self, n): 
        # code here
        def help(n,d):
            if n <= 11:
                d[n] = n
                return d[n]
            if n in d:
                return d[n]
            else:
                first = (n // 2)
                second = (n // 3)
                third = (n // 4)
                if first > 11:
                    d[first] = help(first, d)
                    first = d[first]
                if second > 11:
                    d[second] = help(second, d)
                    second = d[second]
                if third > 11:
                    d[third] = help(third, d)
                    third = d[third]
                d[n] = first + second + third
                return d[n]
        return help(n,{})



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        ob = Solution()
        print(ob.maxSum(n))
# } Driver Code Ends