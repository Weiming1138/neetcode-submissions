class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):

            while stack and temperatures[stack[-1]] < temperatures[i]: #compares temp[index of current temp] to temp[index of previous temp in stack] so this checks if current temp is warmer than the one in stack
                stackI = stack.pop() #at that index, 

                res[stackI] = (i - stackI) #change the value to the distance from the current index subtracted by the index in the stack where we found warmer temp
            
            stack.append(i)
    
        return res
