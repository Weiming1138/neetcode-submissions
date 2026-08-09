class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        res = high

        while low <= high:
            mid = low + (high - low) // 2

            total_hours = 0
            
            for b in piles:
                hours = math.ceil(b / mid)
                total_hours += hours

            if total_hours <= h:
                res = min(res, mid)
                high = mid - 1
            elif total_hours >= h:
                low = mid + 1
        
        return res
        
        
            

        

            
            
        


            



