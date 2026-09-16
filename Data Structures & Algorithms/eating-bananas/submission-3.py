class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1 #left right
        high = max(piles)
        res = high
        #think binary search from range of low -> high

        while low <= high:
            middle = (low + high) // 2 #middle rate

            #if middle meets h but not exact, decrease right, otherwise increase left
            hours = 0
            for i in piles: #to search through the piles
                hours += math.ceil(i/middle) #add your hours by dividing current piles with rate
            
            if hours <= h: #if your hours are less than or equal, its either too big of a rate or the correct min rate, so update res
                res = min(res, middle)
                high = middle - 1
            else: #otherwise, bring left pointer to middle + 1
                low = middle + 1 
        return res




            


        

