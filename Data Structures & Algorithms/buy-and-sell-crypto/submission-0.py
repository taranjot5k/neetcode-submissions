class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        profit = 0
        maxProfit = 0

        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
            else:
                profit = prices[r] - prices[l]
            if maxProfit < profit:
                maxProfit = max(maxProfit, profit)
            r += 1
        return maxProfit


        