class Solution:
    def trap(self, height: List[int]) -> int:
    #left and right pointer
    #- To determine our left and right movement, we disregard the first and last numbers 
    #of the array because its impossible that they are water blocks
    #- Run while left < right. If left height is less than right height, move left, vice versa
    #- The important condition: We need to check if Left and Right height are equal. 
    #Once they are, we run a while look to check the heights in between the left and right 
    #height to see if it has potential to contain water
    #- The condition also need to check every time is if the number its currently on is a water
    #block. Therefore, we need to check its left and right values every time, and the amount of
    #water stored will be the min(height[n - 1] and height[n + 1])
    #- Once we confirm there is a large container of water between left and right 
    #(ie. left and right height are the same, we again, use the while loop to check in between)
    #We know its a large portion because the heights between left and right are less than the heights of L and R
    #- To figure out how to calculate the large water container, we just need to subtract each
    #height value by the height of either left or right (since they're the same height) and do that
    #until you reach the left or right value (3-1, 3-0, 3-1, got to 3)
    
        if not height:
            return 0

        l, r = 0, len(height) - 1
        l_max, r_max = height[l], height[r]
        water_sum = 0

        while l < r:
            if height[l] < height[r]:
                l += 1
                l_max = max(l_max, height[l])
                water_sum += l_max - height[l]
            else:
                r -= 1
                r_max = max(r_max, height[r])
                water_sum += r_max - height[r]

        return water_sum



