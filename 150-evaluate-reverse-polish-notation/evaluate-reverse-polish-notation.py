class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {'+':1,'-':1,'*':2,'/':2}
        for i in tokens:
            if i in ops:
                op1 = int(stack.pop())
                op2= int(stack.pop())
                if i == "+":
                    stack.append(op1+op2)
                elif i == '-':
                    stack.append(op2-op1)
                elif i == '*':
                    stack.append(op2*op1)
                elif i == '/':
                    stack.append(int(op2/op1))
            else:
                stack.append(int(i))
        return stack[0]