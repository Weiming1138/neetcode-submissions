class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0
        l, r = 0, len(heights) - 1

        while l < r:
            distance = r - l
            max_water = max(max_water, min(heights[l], heights[r]) * distance)

            if heights[r] > heights[l]:
                l += 1
            else:
                r -= 1
        
        return max_water
