class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        k = 1

        while l < r:
            if nums[l] == nums[l + 1]:
                del nums[l]
                r -= 1
            else:
                l += 1
                        
        k = len(nums)
        return k