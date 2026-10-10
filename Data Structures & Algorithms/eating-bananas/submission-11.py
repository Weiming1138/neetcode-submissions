class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        min_rate = r
        while l <= r:
            rate = (l + r) // 2

            hours = 0
            for i in piles:
                hours += math.ceil(i/rate)

            if hours <= h:
                min_rate = min(min_rate, rate)
                r = rate - 1
            else:
                l = rate + 1

        return min_rate