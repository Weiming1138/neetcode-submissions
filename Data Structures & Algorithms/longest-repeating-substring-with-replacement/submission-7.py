class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        freq = 0
        count = {}
        length = 0

        for right in range(len(s)):
            char = s[right]

            count[char] = count.get(char, 0) + 1

            freq = max(freq, count[char])

            while (right - left + 1) - freq > k:
                count[s[left]] -= 1
                left += 1
            
            length = max(length, right - left + 1)
        
        return length