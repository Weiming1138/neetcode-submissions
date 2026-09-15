class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        map_s = {}
        max_length = 0

        for right in range(len(s)):
            char = s[right]

            if char in map_s:
                duplicate = map_s[char] #find which position/number of places to get to the duplicate
            
                while duplicate >= left:
                    del map_s[s[left]]
                    left += 1
                
            map_s[char] = right
            max_length = max(max_length, len(map_s))
        
        return max_length
