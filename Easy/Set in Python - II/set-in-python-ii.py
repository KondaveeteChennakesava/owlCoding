#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

# Function to find common elements in sets
# should return the intersection of sets
def common_in_set(a, b):
    # Your code here
    return a.intersection(b)
    

# Function to find difference in sets
# Should return the difference in sets
def diff(a, b):
    # Your code here
    return a.difference(b)



# Function to find union of sets
# Should return the union of sets
def all_in_set(a, b):
    # Your code here
    return a.union(b)
    

#{ 
 # Driver Code Starts.

# Driver code
def main():
    testcase = int(input())
    
    # looping through all testcases
    while testcase > 0:
        
        # taking input of set
        a = {int(x) for x in input().split()}
        b = {int(x) for x in input().split()}
        
        for x in all_in_set(a, b):
            print (x, end = ' ')
            
        print ()
        
        for x in common_in_set(a, b):
            print (x, end = ' ')
            
        print ()
        
        for x in diff(a, b):
            print (x, end = ' ')
        
        print ()
        
        testcase -= 1

if __name__ == '__main__':
    main()
# } Driver Code Ends