class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens:
            if i == "+":
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                stack.append(num1 + num2)
            elif i == "-":
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                stack.append(num2 - num1)
            elif i == "*":
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                stack.append(num1 * num2)
            elif i == "/":
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                stack.append(int(num2/num1))
            else:
                stack.append(i)

        return int(stack[0])
            


