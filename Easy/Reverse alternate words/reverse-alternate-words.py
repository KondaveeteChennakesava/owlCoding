#User function Template for python3

class Solution:

    def reverseAlternate(self, Str):
        # code here
        l = Str.split(' ')
        for i in range(len(l)):
            if i%2:
                l[i] = l[i][::-1]
        # print(l)
        return ' '.join(l)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):

        Str = input()

        solObj = Solution()

        print(solObj.reverseAlternate(Str))

# } Driver Code Ends