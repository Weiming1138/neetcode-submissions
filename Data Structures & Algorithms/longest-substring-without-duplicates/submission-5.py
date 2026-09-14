class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map_s = {}
        max_length = 0
        left = 0

        for right in range(len(s)):
            if s[right] in map_s:
                duplicate = map_s[s[right]]
                
                while left <= duplicate:
                    del map_s[s[left]]
                    left += 1
            map_s[s[right]] = right
            max_length = max(max_length, len(map_s))
        
        return max_length
            

                


        