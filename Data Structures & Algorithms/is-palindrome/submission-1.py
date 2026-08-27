import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        change_s = re.sub(r'[^a-zA-Z0-9]', '', "".join(s).lower())

        l, r = 0, len(change_s) - 1

        while l < r:
            if change_s[l] != change_s[r]:
                return False
            l += 1
            r -= 1
        
        return True
        