class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break   
            
        fast2 = 0
        while fast2 != slow:
            fast2 = nums[fast2]
            slow = nums[slow]
        
        return slow

        