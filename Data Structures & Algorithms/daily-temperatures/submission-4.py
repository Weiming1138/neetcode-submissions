class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):

            while stack and temp > stack[-1][0]:
                _, stackI = stack.pop()

                res[stackI] = (i - stackI)
            
            stack.append([temp, i])
    
        return res
