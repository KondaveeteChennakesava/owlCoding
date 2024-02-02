#User function template for Python

class Solution:
    # your task is to complete this function
    # function should return an integer
    def atoi(self,s):
        # Code here
        flag = False
        for i in s:
            if ord(i) >= 97 and ord(i) <= 122:
                flag = True
                break
        if flag or ('-' in s and s[0] != '-'):
            return -1
        return int(s)


#{ 
 # Driver Code Starts
#Initial template for Python

if __name__=='__main__':
    t=int(input())
    for i in range(t):
        string = input().strip();
        ob=Solution()
        print(ob.atoi(string))
# } Driver Code Ends