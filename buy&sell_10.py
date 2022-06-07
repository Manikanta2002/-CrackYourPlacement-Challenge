class Solution(object):
    def maxProfit(self, prices):
        min_p=float('inf')
        max_profit=0
        for price in prices:
            min_p=min(min_p,price)
            profit=price-min_p
            max_profit=max(max_profit,profit)
        return max_profit
        