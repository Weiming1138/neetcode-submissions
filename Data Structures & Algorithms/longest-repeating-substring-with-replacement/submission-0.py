class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        max_length = 0
        left = 0

        for right in range(len(s)):
            char = s[right]
            count[char] = count.get(char, 0) + 1

            window = right - left + 1
            max_freq = max(count.values())
           
            while (window - max_freq) > k:
                count[s[left]] -= 1
                left += 1

                window = right - left + 1

            max_length = max(max_length, window)
            
        return max_length


            
