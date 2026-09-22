class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map_s = {}
        left = 0
        length = 0

        for right in range(len(s)):
            char = s[right]

            if char in map_s:
                duplicate = map_s[char]

                while left <= duplicate:
                    del map_s[s[left]]
                    left += 1 
            map_s[char] = right
            length = max(length, len(map_s))
        
        return length