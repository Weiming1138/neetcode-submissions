class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map_num = {}

        for i in nums:
            if i in map_num:
                return True
            map_num[i] = True
        return False