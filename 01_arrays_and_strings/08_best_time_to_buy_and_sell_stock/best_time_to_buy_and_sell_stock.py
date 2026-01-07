class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        min_price = prices[0]

        for i in range(0,len(prices)):
            profit = max(prices[i] - min_price, profit)
            min_price = min(prices[i], min_price)

        return profit