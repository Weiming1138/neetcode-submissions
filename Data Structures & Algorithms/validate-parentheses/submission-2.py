class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        map = {")":"(", "}":"{", "]":"["}

        for char in s:
            if char in map:
                top = stack.pop() if stack else ' '

                if map[char] != top:
                    return False
            else:
                stack.append(char)
        
        return not stack