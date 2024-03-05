#User function Template for python3


class Solution:
    def firstElementKTime(self, n, k, a):
        # code here
        dic = {}
        for i in a:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
            if dic[i] == k:
                return i
        return -1



#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        n, k = sz[0], sz[1]
        a = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.firstElementKTime(n, k, a))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends