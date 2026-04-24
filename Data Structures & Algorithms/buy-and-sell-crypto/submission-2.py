class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = 1000
        profit = 0

        for price in prices:
            min_price = min(min_price,price)
            curr_profit = price - min_price
            profit = max(profit,curr_profit)

        return profit
        