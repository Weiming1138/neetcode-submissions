class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minStack) == 0 or val <= self.minStack[-1]:
            self.minStack.append(val)
        pass
    def pop(self) -> None:
        popped = self.stack.pop()
        if popped == self.minStack[-1]:
            self.minStack.pop()
        pass
    def top(self) -> int:
        return self.stack[-1]
        pass
    def getMin(self) -> int:
        return self.minStack[-1]
        pass