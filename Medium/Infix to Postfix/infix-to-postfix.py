#User function Template for python3


class Solution:
    
    #Function to convert an infix expression to a postfix expression.
    def InfixtoPostfix(self, exp):
        #code here
        def getPriority(s):
            if s == '^':return 3
            elif s == '*' or s == '/':return 2
            elif s == '+' or s == '-':return 1
            return 0
        stack, answer = [], []
        for i in exp:
            if ('a' <= i <= 'z') or ('A' <= i <= 'Z') or ('0' <= i <= '9'):
                answer.append(i)
            elif i == '(':
                stack.append(i)
            elif i == ')':
                while stack and stack[-1] != '(':
                    answer.append(stack.pop())
                stack.pop()
            else:
                while stack and getPriority(i) <= getPriority(stack[-1]):
                    answer.append(stack.pop())
                stack.append(i)
        while stack:
            answer.append(stack.pop())
        return ''.join(answer)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

# This code is contributed by Nikhil Kumar Singh(nickzuck_007)


_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        exp = str(input())
        ob=Solution()
        print(ob.InfixtoPostfix(exp))
# } Driver Code Ends