class Solution:
    def trap(self, height: List[int]) -> int:
    #Core Idea: The water trapped above any bar is determined by:
    #min(tallest bar to its left, tallest bar to its right) - height[i]
    #Track the running max heights seen so far from both directions:
    #'left_max' and 'right_max'.

    #while l < r:
    #Compare height[l] and height[r] to process the shorter side first:  
        #1. If height[l] < height[r]:
            #Move left pointer inward (l += 1).
            #Update left_max = max(left_max, height[l]).
            #Add trapped water: left_max - height[l].
               
        #2. Else (height[l] >= height[r]):
            #Move right pointer inward (r -= 1).
            #Update right_max = max(right_max, height[r]).
            #Add trapped water: right_max - height[r].
    
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



