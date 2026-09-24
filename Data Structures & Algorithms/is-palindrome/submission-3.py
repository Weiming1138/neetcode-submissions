import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        change = re.sub(r'[^a-zA-Z0-9]', '', "".join(s).lower())

        l, r = 0, len(change) - 1

        while l < r:
            if change[l] != change[r]:
                return False
            
            l += 1
            r -= 1
        
        return True