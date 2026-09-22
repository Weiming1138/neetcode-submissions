class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        length = 0
        max_f = 0
        count = {}

        for right in range(len(s)):
            char = s[right]
            
            count[char] = count.get(char, 0) + 1

            max_f = max(max_f, count[char])

            while (right - left + 1) - max_f > k:
                count[s[left]] -= 1
                left += 1
            length = max(length, right - left + 1)
        
        return length