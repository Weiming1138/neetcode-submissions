class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_left, max_right = height[l], height[r]
        max_water = 0

        while l < r:
            if height[l] < height[r]:
                l += 1
                max_left = max(max_left, height[l])
                max_water += max_left - height[l]
            else:
                r -= 1
                max_right = max(max_right, height[r])
                max_water += max_right - height[r]
        
        return max_water