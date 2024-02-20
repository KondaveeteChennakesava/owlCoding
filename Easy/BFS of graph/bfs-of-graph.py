#User function Template for python3

from typing import List
from queue import Queue
class Solution:
    #Function to return Breadth First Traversal of given graph.
    
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        # code here
        v=[False for i in range(V)]
        qu=[]
        qu.append(0)
        r=[0]
        v[0]=True
        while(len(qu)!=0):
            a=qu.pop(0)
            for i in adj[a]:
                if v[i]==False:
                    qu.append(i)
                    r.append(i)
                    v[i]=True
        return r
                
                

#{ 
 # Driver Code Starts


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
		ob = Solution()
		ans = ob.bfsOfGraph(V, adj)
		for i in range(len(ans)):
		    print(ans[i], end = " ")
		print()
        

# } Driver Code Ends