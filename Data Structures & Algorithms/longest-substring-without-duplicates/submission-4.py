class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        left = 0
        hash = {}

        for right in range(len(s)):
            char = s[right]

            if char in hash:
                duplicate = hash[char]

                while left <= duplicate: 
                    del hash[s[left]]
                    left += 1
            
            hash[char] = right
            max_length = max(max_length, len(hash))
        
        return max_length