class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map = {")":"(", "]":"[", "}":"{"}

        for i in s:
            if i in map:
                if not stack or stack[-1] != map[i]:
                    return False
                stack.pop()
            else:
                stack.append(i)
        return not stack

