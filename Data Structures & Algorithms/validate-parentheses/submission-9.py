class Solution:
    def isValid(self, s: str) -> bool:
        hash = {"}":"{", ")":"(", "]":"["}
        stack = []

        for i in s:
            if i in hash:
                if not stack or stack[-1] != hash[i]:
                    return False               
                stack.pop()
            else:
                stack.append(i)
        
        return not stack

