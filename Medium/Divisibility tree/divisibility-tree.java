//{ Driver Code Starts
import java.io.*;
import java.util.*;

class IntMatrix {
    public static int[][] input(BufferedReader br, int n, int m) throws IOException {
        int[][] mat = new int[n][];

        for (int i = 0; i < n; i++) {
            String[] s = br.readLine().trim().split(" ");
            mat[i] = new int[s.length];
            for (int j = 0; j < s.length; j++) mat[i][j] = Integer.parseInt(s[j]);
        }

        return mat;
    }

    public static void print(int[][] m) {
        for (var a : m) {
            for (int e : a) System.out.print(e + " ");
            System.out.println();
        }
    }

    public static void print(ArrayList<ArrayList<Integer>> m) {
        for (var a : m) {
            for (int e : a) System.out.print(e + " ");
            System.out.println();
        }
    }
}

class GFG {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t;
        t = Integer.parseInt(br.readLine());
        while (t-- > 0) {

            int n;
            n = Integer.parseInt(br.readLine());

            int[][] edges = IntMatrix.input(br, n - 1, 2);

            Solution obj = new Solution();
            int res = obj.minimumEdgeRemove(n, edges);

            System.out.println(res);
        }
    }
}

// } Driver Code Ends



class Solution {
       List<List<Integer>> adj ;
       int ans;
    public int minimumEdgeRemove(int n, int[][] edges) {
        // code here
      adj = new ArrayList<>();
           for (int i = 0; i <=n; i++) {
            adj.add(new ArrayList<>());
        }
        ans=0;
        boolean vis[] = new boolean[n+1];
         
        for(int x[] : edges){
            addEdge(x[0], x[1]);
        }
        
        dfs(1, vis);
        return ans;
        
    }
     void addEdge(int u, int v) {
        adj.get(u).add(v);
        adj.get(v).add(u);
    }
      int dfs(int node, boolean[] vis) {
      
      int cnt=0; vis[node] = true;
      
        int cntTillYet=0;
        
      for(int u : adj.get(node)){
          if(!vis[u]){
              cntTillYet = dfs(u, vis);
              if(cntTillYet%2==0){
                //   System.out.println(u+ " ");
              ans++;
              }
              else
              cnt+= cntTillYet;
          }
      }
      return cnt+1;
    }
}
