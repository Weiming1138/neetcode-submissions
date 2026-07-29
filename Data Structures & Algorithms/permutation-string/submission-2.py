class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        map_s1 = Counter(s1)
        map_s2 = {}
        left = 0

        for i in range(len(s1)):
            char = s2[i]
            map_s2[char] = map_s2.get(char, 0) + 1

        if map_s1 == map_s2:
            return True

        for right in range(len(s1), len(s2)):
            char_right = s2[right]
            map_s2[char_right] = map_s2.get(char_right, 0) + 1

            char_left = s2[left]
            map_s2[char_left] -= 1

            if map_s2[char_left] == 0:
                del map_s2[char_left]

            left += 1

            if map_s1 == map_s2:
                return True
        return False
                

