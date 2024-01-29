#{ 
 # Driver Code Starts
#Initial Template for Python 3






import re

# } Driver Code Ends
#User function Template for python3

def validate(str):
    pat= '^[a-z]+[^\w]+[\d+]'
    match = re.search(pat, str)
    if(match):
        return True
    else:
        return False



#{ 
 # Driver Code Starts.

def main():
    testcases = int(input()) #testcases
    while(testcases > 0):
        str = input()
        print(validate(str))
        testcases -= 1
        


if __name__=='__main__':
    main()
# } Driver Code Ends