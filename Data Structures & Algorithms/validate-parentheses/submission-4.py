class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        map = {")":"(", "}":"{", "]":"["}

        for char in s:
            if char in map: #checks only closing characters

                if not stack or stack[-1] != map[char]: #If stack is empty or doesnt match any of the symbols in the map, false
                    return False
                stack.pop()
            else:
                stack.append(char) #append all opening characters
        
        return not stack