class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_l, max_r = height[l], height[r]
        max_water = 0

        while l < r:
            if height[l] < height[r]:
                l += 1
                max_l = max(max_l, height[l])
                max_water += max_l - height[l]
            else:
                r -= 1
                max_r = max(max_r, height[r])
                max_water += max_r - height[r]

        return max_water


        