class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = {}
        ans = []

        
        for i in strs:
            count = [0] * 26
            for char in i:
                count[ord(char) - ord('a')] += 1    
            key = tuple(count)

            if key in hash:
                hash[key].append(i)
            else:
                hash[key] = [i]
        return list(hash.values())
