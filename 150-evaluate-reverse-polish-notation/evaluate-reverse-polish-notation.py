import math as m
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        n = len(tokens)
        operands = '+-*/'
        for i in range(n):
            flag = False
            if '-' in tokens[i] and len(tokens[i]) > 1:
                k = int(tokens[i])*-1
                flag = True
            if flag:
                stack.append(-k)
            if len(stack) == 0 or (tokens[i]).isdigit():
                # print(int(tokens[i]))
                stack.append(int(tokens[i]))
            if tokens[i] in operands:
                # print(stack)
                first = stack.pop()
                sec = stack.pop()
                # if tokens[i] == "/":
                #     s = str(sec)+str(tokens[i])+"/"+str(first)
                # else:
                s = str(sec)+str(tokens[i])+str(first)
                # print(s)
                stack.append(int(eval(s)))
        # print(stack)
        return stack[0]