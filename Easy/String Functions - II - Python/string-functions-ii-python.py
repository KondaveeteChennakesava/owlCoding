#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

# Function to check if string 
# starts and ends with 'gfg'
def gfg(S):
    b = S.lower()
    if(b[:3] == b[-3:]):  
        print ("Yes")
    else:
        print ("No")

#{ 
 # Driver Code Starts.
# Driver Code
def main():
    # testcase input
    testcases = int(input())
    
    # looping through testcases
    while(testcases > 0):
        S = input()
        
        testcases -= 1
        
        gfg(S)

if __name__ == '__main__':
    main()
# } Driver Code Ends