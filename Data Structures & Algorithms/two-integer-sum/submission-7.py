class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        maps = {}

        for i in range(len(nums)):
            difference = target - nums[i]
            if difference not in maps:
                maps[nums[i]] = i
            else:
                return [maps[difference], i]
    
    #-> 4: 0 