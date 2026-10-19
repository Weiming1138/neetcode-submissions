class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        left = 0

        for right in range(len(prices)):
            
            if prices[right] > prices[left]:
                profit = max(profit, prices[right] - prices[left])
            else:
                left = right
            
        return profit

