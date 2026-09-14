class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        #encode it with length of string with delimiter and current letter
        for s in strs:
            res += str(len(s)) + "#" + s 
        return res
    def decode(self, s: str) -> List[str]:
        res, i = [], 0 #establish pointer to keep track of where we are so farand result

        while i < len(s): 
            j = i #to find delimiter, lets establish another pointer j
            while s[j] != "#":
                j += 1
            length = int(s[i:j]) #the length of the string will go from string at i to j not inclusive
            #length tells us how many characters we need to read after j

            res.append(s[j + 1 : j + 1 + length]) #starting from j + 1 because j is delimiter character, we go to end of string by doing j + 1 + length
            i = j + 1 + length #once it reads a word, update i into the new string character

        return res
