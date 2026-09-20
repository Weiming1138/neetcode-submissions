class MinStack:

    def __init__(self):
        self.minStack = []
        self.topStack = []
    def push(self, val: int) -> None:
        self.topStack.append(val)
        if len(self.minStack) == 0 or val <= self.minStack[-1]:
            self.minStack.append(val)
        pass
    def pop(self) -> None:
        popped = self.topStack.pop()
        if popped == self.minStack[-1]:
            self.minStack.pop()

    def top(self) -> int:
        return self.topStack[-1]
        pass
    def getMin(self) -> int:
        return self.minStack[-1]
        pass
        
