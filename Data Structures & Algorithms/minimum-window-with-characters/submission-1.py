class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s): #Base case
            return ""
        #Intialize maps, left pointer, answer, and formed (important)
        left = 0
        map_s = {}
        map_t = Counter(t)
        min_len = float("inf")
        formed = 0
        ans = ""

        for right in range(len(s)):
            #Keep intialize right character in s2 and add count to map
            char_right = s[right]
            map_s[char_right] = map_s.get(char_right, 0) + 1
            
            #Important: If we see that character we currently on is in map_t and have the same amount (To adjust to duplicates), we increase unique character tracker form by 1
            if char_right in map_t and map_s[char_right] == map_t[char_right]:
                formed += 1
            #(Important) When we have enough formed characters to match the amount of t characters
            while formed == len(map_t):
                #We track current length with classic r - l + 1 equation
                current_length = right - left + 1
                #And we update our min_len answer if the current_length is less than min_len every time we loop
                if current_length < min_len:
                    min_len = current_length
                    ans = s[left:right + 1] 
                #Keep track of left character so we can remove count from map ->
                char_left = s[left] 
                map_s[char_left] -= 1
                #If our changes to the left pointer caused window to move away from formed characters, we reduce the formed by 1 and stop the loop
                if char_left in map_t and map_s[char_left] < map_t[char_left]:
                    formed -= 1
                #-> and delete it off the map
                if map_s[char_left] == 0:
                    del map_s[char_left]

                left += 1 #Shrink window
        return ans
                


            
                

            
                

            
            

            
