class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        left = 0
        map_s = {}
        map_t = Counter(t)
        min_len = float("inf")
        formed = 0
        ans = ""
        
        if map_s == map_t:
            return t

        for right in range(len(s)):
            char_right = s[right]
            map_s[char_right] = map_s.get(char_right, 0) + 1
            

            if char_right in map_t and map_s[char_right] == map_t[char_right]:
                formed += 1

            while formed == len(map_t):
                current_length = right - left + 1
                if current_length < min_len:
                    min_len = current_length
                    ans = s[left:right + 1]

                char_left = s[left] 
                map_s[char_left] -= 1

                if char_left in map_t and map_s[char_left] < map_t[char_left]:
                    formed -= 1

                if map_s[char_left] == 0:
                    del map_s[char_left]

                left += 1
        return ans
                


            
                

            
                

            
            

            
