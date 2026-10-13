class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                tempI = stack.pop()

                temp[tempI] = (i - tempI)
            stack.append(i)
        return temp