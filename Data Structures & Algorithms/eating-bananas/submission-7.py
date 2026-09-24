class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2

            hour = 0
            for i in piles:
                hour += math.ceil(i/k)

            if hour <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
        
        return res