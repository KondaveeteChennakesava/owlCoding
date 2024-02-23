#User function Template for python3

def isValid(s):
    #code here
    arr = s.split('.')
    for i in arr:
        if i == '':return 0
    if len(arr) != 4:
        return 0
    for i in arr:
        for num in i:
            if not num.isdigit():
                return 0
        if len(i) != len(str(int(i))):
            return 0
        if int(i) > 255 or int(i) < 0:
            return 0
    return 1



#{ 
 # Driver Code Starts
#Initial Template for Python 3

    
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s=input()
        if(isValid(s)):
            print(1)
        else:
            print(0)
    

# } Driver Code Ends