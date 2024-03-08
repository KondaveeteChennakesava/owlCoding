#User function Template for python3
class Solution:
    def sameFreq(self, s):
        # code here
        dic = {}
        for i in s:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        arr = list(dic.values())
        if len(set(arr)) == 1:
            return 1
        for i in range(len(arr)):
            arr[i] -= 1
            if len(set(arr)) == 1 or (len(set(arr)) == 2 and 0 in set(arr)):
                return 1
            arr[i] += 1
        return 0
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
	T=int(input())

	for _ in range(T):
		s = input()
		ob = Solution()
		answer = ob.sameFreq(s)
		if answer:
			print(1)
		else:
			print(0)

# } Driver Code Ends