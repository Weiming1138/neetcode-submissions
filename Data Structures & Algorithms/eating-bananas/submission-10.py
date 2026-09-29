class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            mid_rate = (l + r) // 2

            hours = 0
            for i in piles:
                hours += math.ceil(i/mid_rate)
            
            if hours <= h:
                res = min(res, mid_rate)
                r = mid_rate - 1
            else:
                l = mid_rate + 1
        
        return res