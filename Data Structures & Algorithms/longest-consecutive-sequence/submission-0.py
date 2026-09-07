class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        maxSequence = 0
            
        for i in nums:
            if (i - 1) not in nums:

                current_num = i
                current_sequence = 1

                while current_num + 1 in nums:
                    current_num += 1
                    current_sequence += 1
            
                maxSequence = max(maxSequence, current_sequence)
        
        return maxSequence





