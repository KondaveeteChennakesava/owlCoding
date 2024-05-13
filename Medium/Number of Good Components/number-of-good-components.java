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

            int e;
            e = Integer.parseInt(br.readLine());

            int v;
            v = Integer.parseInt(br.readLine());

            int[][] edges = IntMatrix.input(br, e, 2);

            Solution obj = new Solution();
            int res = obj.findNumberOfGoodComponent(e, v, edges);

            System.out.println(res);
        }
    }
}

// } Driver Code Ends



class Solution {
   static int v_count;
   static int e_count;
    static boolean vis[];
    public static int findNumberOfGoodComponent(int e, int V, int[][] edges) {
       ArrayList<ArrayList<Integer>> adj = new ArrayList<>();
        for (int i = 0; i <= V; i++) {
            adj.add(new ArrayList<>());
        }
        for (int[] edge : edges) {
            adj.get(edge[0]).add(edge[1]);
            adj.get(edge[1]).add(edge[0]); // if the graph is undirected
        }
         vis = new boolean[V+1];
        //dfs for all vertices
        int ans=0;
        for(int i=1; i<=V; i++)
        {
            if(!vis[i])
            {
                v_count=e_count=0;
                dfs(adj, i);
            
            if(e_count == (v_count *(v_count-1))) ans++;
            
            }
        }
        return ans;
        
    }
   static void dfs(ArrayList<ArrayList<Integer>> adj, int st)
    {
        vis[st]=true;
        v_count++; e_count += adj.get(st).size();
        //itr for nei
        for(int nei : adj.get(st) )
        {
            if(!vis[nei])
             dfs(adj, nei);
        }
    }
    
}
