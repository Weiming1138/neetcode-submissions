class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for i in range(len(nums)):
            difference = target - nums[i]

            if difference not in map:
                map[nums[i]] = i
            else:
                return [map[difference], i]
            
            

                
