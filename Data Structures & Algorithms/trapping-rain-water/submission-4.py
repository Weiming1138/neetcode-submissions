class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_l, max_r = height[l], height[r]
        water_sum = 0

        while l < r:
            if height[l] < height[r]:
                l += 1
                max_l = max(max_l, height[l])
                water_sum += max_l - height[l]
            else:
                r -= 1
                max_r = max(max_r, height[r])
                water_sum += max_r - height[r]
        return water_sum
