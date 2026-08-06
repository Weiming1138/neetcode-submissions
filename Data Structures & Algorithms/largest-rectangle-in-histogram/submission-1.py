class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # (index, height)
        max_area = 0
        #track index and height of the array
        for i, h in enumerate(heights):
            start = i #we don't know if we can extend backwards, so initialize with i
            while stack and stack[-1][1] > h: #if not empty and if top value of stack and height is greater than height we reached, we pop the height and index, and check max area from that height, and extend current height backwards
                index, height = stack.pop() #retrieve index and height from stack
                max_area = max(max_area, height * (i - index)) #check if it could've been the max area with area formula, width: (i - index)
                start = index #now we know we can extend start index backwards
            stack.append((start, h)) #add start index we pushed back
        
        #for the ones we can extend, compute the height
        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))
            #same way we try to find the max area, except this time, we need to use the length of the histogram/heights subtracted by i start value in stack
        
        return max_area

            
            



                
                



