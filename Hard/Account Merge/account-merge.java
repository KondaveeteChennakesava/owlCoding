//{ Driver Code Starts
//Initial Template for Java

import java.util.*;
import java.lang.*;
import java.math.*;
import java.io.*;

class GFG {
  public static void main(String[] args) throws IOException {
    Scanner sc = new Scanner(System.in);
    int T = sc.nextInt();
    while (T-- > 0) {
      int n = sc.nextInt();
      List<List<String>> accounts=new ArrayList<>();
      for (int i = 0; i < n; i++)
       {
        ArrayList<String> temp=new ArrayList<>();
        int x=sc.nextInt();
        for(int j = 0; j < x; j++)
           {
             String s1=sc.next();
             temp.add(s1);
           }
        accounts.add(temp);
       }
      Solution obj = new Solution();
      List<List<String>> res = obj.accountsMerge(accounts);
      Collections.sort(res, new Comparator<List<String>>() {
                @Override   public int compare(List<String> a,
                                              List<String> b) {
                    int al = a.size();
                    int bl = b.size();
                    int min = Math.min(al, bl);
                    for (int i = 0; i < min; i++) {
                        String xx=a.get(i);
                        String yy=b.get(i);
                        if (xx.compareTo(yy)<0)
                            return -1;
                        else if (xx.compareTo(yy)>0)
                            return 1;
                    }
                    if (al < bl)
                        return -1;
                    else if (al > bl)
                        return 1;
                    return -1;
                }
            });
      System.out.print("[");
      for (int i = 0; i < res.size(); ++i)
        {
          System.out.print("[");
          for (int j = 0; j < res.get(i).size(); j++)
             {
                if (j != res.get(i).size() - 1)
                     System.out.print(res.get(i).get(j)+", ");
                else
                     System.out.print(res.get(i).get(j));
             }
          if (i != res.size() - 1)
             System.out.println("], ");
          else
             System.out.print("]");
        }
       System.out.println("]");
    }
  }
}

// } Driver Code Ends


//User function Template for Java

class Solution {
    // Function to find the root of the set
    
    static int[] par;
    // Function to merge accounts
    static List<List<String>> accountsMerge(List<List<String>> a) {
        
        int n = a.size();
         par = new int[n];
        for (int i = 0; i < n; i++) {
            par[i] = i;
        }
       //s1
        Map<String,Integer> m1 = new HashMap<>();
      //itr for each email
        for (int i = 0; i < n; i++) {
            for (int j = 1; j < a.get(i).size(); j++) {
                String mail = a.get(i).get(j);
                if (m1.containsKey(mail)) {  //same person exisits , need to perform union
                    
                    int person = m1.get(mail);
                    union(i, person);
                } 
                else {
                    // If the email doesn't have an owner, set the current account as the owner
                    m1.put(mail, i);
                }
            }
        }
        //s2
       //map to store merger acc 
        Map<Integer, TreeSet<String>> map = new HashMap<>(); 
       
        for (int i = 0; i < n; i++) {
            //find the rep
            int root = find(i);
            List<String> al = a.get(i);
            
            //make a new tree set and if enc first time and put the list
            if (!map.containsKey(root)) //logn
                map.put(root, new TreeSet<String>());
            
            map.get(root).addAll(al.subList(1, al.size())); //emails start from 2nd
        }
        // print the ans
        List<List<String>> res = new ArrayList<List<String>>();
        
        for (int root : map.keySet()) {
            String name = a.get(root).get(0);
            ArrayList<String> curr = new ArrayList<>(map.get(root));
            curr.add(0,name);
           
            res.add(curr);
        }
        // Return the final merged accounts
        return res;
    }
    
    static int find(int idx) { //path compression
        
        if (idx == par[idx])
            return idx;
    
        return par[idx] = find(par[idx]);
    }
    static void union(int x, int y){
        int x_rep = find(x), y_rep=find(y);
        if(x_rep==y_rep) return;
        par[y_rep] = x_rep;
    }
}   