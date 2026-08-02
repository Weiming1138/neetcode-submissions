class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []
    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minstack) == 0 or val <= self.minstack[-1]:
            self.minstack.append(val)   
        pass
    def pop(self) -> None:
        popped = self.stack.pop()
        if popped == self.minstack[-1]:
            self.minstack.pop()
        pass
    def top(self) -> int:
        return self.stack[-1]
        pass
    def getMin(self) -> int:
        return self.minstack[-1]
        pass
