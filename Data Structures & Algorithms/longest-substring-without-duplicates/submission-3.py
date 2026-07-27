class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #Hash and sliding window
        map_s = {} 
        max_length = 0
        left = 0

        for right in range(len(s)): #loop through s 
            char = s[right] #intialize current character as s[right]

            if char in map_s: #if that character is already in map, 
                duplicate = map_s[char] #Grab the index of that duplicate character
                while left <= duplicate: #starting from the left index to the duplicate index...
                    del map_s[s[left]] #remove all characters from the map up to duplicate index
                    left += 1

            map_s[char] = right #add new right value into map
            max_length = max(max_length, len(map_s)) #compare/update max_length with each map_s value

        return max_length