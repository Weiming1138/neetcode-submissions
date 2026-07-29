class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        map_s1 = Counter(s1)
        map_s2 = {}
        left = 0

        for i in range(len(s1)): #Initialize the window
            char = s2[i]
            map_s2[char] = map_s2.get(char, 0) + 1 #Add frequency to map

        if map_s1 == map_s2: #Check beginning to see if its permutation
            return True

        for right in range(len(s1), len(s2)): #Looping length of s1 to length of s2 times
            #Keep intialize right character in s2 and add count to map
            char_right = s2[right] 
            map_s2[char_right] = map_s2.get(char_right, 0) + 1

            #Same with left except we remove left value from map to move window
            char_left = s2[left]
            map_s2[char_left] -= 1

            if map_s2[char_left] == 0:
                del map_s2[char_left] #Delete 0 values to map_s1 == map_s2 condition is accurate

            left += 1 #Move our left pointer

            if map_s1 == map_s2: #Final check after moving window
                return True
        return False
                

