class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = {"+", "-", "*", "/"}

        stack = []

        for i in tokens:
            if i not in operations:
                stack.append(i)
            else:
                popped1 = int(stack.pop())
                popped2 = int(stack.pop())
                if i == "+":
                    num = popped1 + popped2
                    stack.append(num)
                elif i == "-":
                    num = popped2 - popped1
                    stack.append(num)
                elif i == "*":
                    num = popped1 * popped2
                    stack.append(num)
                elif i == "/":
                    num = popped2 / popped1
                    stack.append(int(num))
        
        return int(stack[0])

                
                    