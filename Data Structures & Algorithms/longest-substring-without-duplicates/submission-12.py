class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_s = {}
        length = 0

        for right in range(len(s)):
            char = s[right]

            if char in max_s:
                copy = max_s[char]

                while left <= copy:
                    del max_s[s[left]]
                    left += 1

            max_s[char] = right
            length = max(length, len(max_s))
        
        return length