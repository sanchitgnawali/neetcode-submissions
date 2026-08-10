class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        maxProfit = 0
        
        for i in range(len(prices)):
            sell = prices[i]
            buy = min(buy, prices[i])

            maxProfit = max(maxProfit, sell - buy)
        
        return maxProfit