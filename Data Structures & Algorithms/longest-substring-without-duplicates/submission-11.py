class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        map_s = {}
        length = 0

        for right in range(len(s)):
            char = s[right]

            if char in map_s:
                replace = map_s[char]

                while left <= replace:
                    del map_s[s[left]]
                    left += 1
            
            map_s[char] = right
            length = max(length, len(map_s))
        
        return length