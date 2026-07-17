class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {

        }
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference not in hash:
                hash[nums[i]] = i
            else:
                return [hash[difference], i]