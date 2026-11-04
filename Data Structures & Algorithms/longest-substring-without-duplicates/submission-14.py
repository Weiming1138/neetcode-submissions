class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        count_s = {}
        length = 0

        for right in range(len(s)):
            char = s[right]

            if char in count_s:
                dup = count_s[char]

                while left <= dup:
                    del count_s[s[left]]
                    left += 1
            count_s[char] = right
            length = max(length, len(count_s))
        
        return length