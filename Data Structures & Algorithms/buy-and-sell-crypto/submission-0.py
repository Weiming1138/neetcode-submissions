class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_profit = prices[0]
        max_profit = 0

        for i in prices:
            min_profit = min(min_profit, i)

            current_profit = i - min_profit
            max_profit = max(max_profit, current_profit)
        
        return max_profit

