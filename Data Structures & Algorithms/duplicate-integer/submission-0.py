class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map = {}

        for i in nums:
            if i in map:
                return True
            map[i] = True
        return False