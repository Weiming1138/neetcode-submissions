class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        maxSequence = 0
        
        #Logic is that if i subtract one from current number in set, and if that number isnt in the set, that means it is a starter and i start counting sequence from there (while my current number + 1 sequence in the set)
        for i in nums:
            if (i - 1) not in nums:
                
                #Update your current number and sequence with each iteration
                current_num = i
                current_sequence = 1

                while current_num + 1 in nums:
                    current_num += 1
                    current_sequence += 1
            
                maxSequence = max(maxSequence, current_sequence)
        #then return the max sequence you found
        return maxSequence





