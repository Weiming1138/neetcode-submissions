class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]: #Is stack empty and is current temp > top value of our stack
                stackT, stackI = stack.pop() #Pop to index and the temp from the stack
                result[stackI] = (i - stackI) #Find how long it took to find a greater temp
            stack.append([temp, i]) #Push into the stack the temperature and its index
        return result

        



        