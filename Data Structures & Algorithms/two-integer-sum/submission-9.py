class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = {}

        for i in range(len(nums)):
            difference = target - nums[i]

            if difference not in count:
                count[nums[i]] = i
            else:
                return [count[difference], i]
            
            