class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        map = {")":"(", "}":"{", "]":"["}

        for char in s:
            if char in map:

                if not stack or stack[-1] != map[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)
        
        return not stack