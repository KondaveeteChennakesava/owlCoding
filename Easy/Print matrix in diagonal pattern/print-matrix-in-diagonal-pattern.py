# Your task is to complete this function

class Solution:
    def matrixDiagonally(self,mat):
        # code here
        ans = []
        for i in range(len(mat)+len(mat)-1):
            ans.append([])
        for i in range(len(mat)):
            for j in range(len(mat)):
                ans[i+j].append(mat[i][j])
        for i in range(len(ans)):
            if i % 2 == 0:
                ans[i] = ans[i][::-1]
        fans = []
        for i in ans:
            fans.extend(i)
        return fans
#{ 
 # Driver Code Starts
# Driver Program
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        matrix = [[0 for i in range(n[0])]for j in range(n[0])]
        k=0
        for i in range(n[0]):
            for j in range(n[0]):
                matrix[i][j] = arr[k]
                k+=1
        a = Solution().matrixDiagonally(matrix)
        for x in a:
            print(x,end=' ')
        print('')
# Contributed by: Harshit Sidhwa
# } Driver Code Ends