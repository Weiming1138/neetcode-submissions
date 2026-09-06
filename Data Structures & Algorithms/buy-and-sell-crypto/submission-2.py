class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minProfit = prices[0]
        maxProfit = 0

        for i in prices:
            minProfit = min(minProfit, i)

            currentProfit = i - minProfit
            maxProfit = max(maxProfit, currentProfit)
        
        return maxProfit