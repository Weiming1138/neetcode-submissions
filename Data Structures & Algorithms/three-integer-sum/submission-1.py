class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue #dont use duplicate

            l, r = i + 1, len(nums) - 1 #start from after beginning

            while l < r: #perform two pointer and check to see if the three values == 0 
                tsum = a + nums[l] + nums[r] 
                if tsum > 0:
                    r -= 1
                elif tsum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    #to avoid same set, move your left and keep moving left pointer while checking the current left equal to previous and left is still less than right
                    l += 1 
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                    
        return res



        