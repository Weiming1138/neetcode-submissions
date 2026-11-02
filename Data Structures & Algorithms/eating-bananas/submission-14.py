class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        rate = r

        while l <= r:
            k = (l + r) // 2

            hours = 0
            for i in piles:
                hours += math.ceil(i/k)
            
            if hours <= h:
                rate = min(rate, k)
                r = k - 1
            else:
                l = k + 1
        
        return rate