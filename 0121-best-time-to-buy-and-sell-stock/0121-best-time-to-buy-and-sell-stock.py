class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minSoFar = float('inf')
        maxProfit = 0
        for price in prices:
            minSoFar = min(minSoFar, price)
            maxProfit = max(maxProfit, price - minSoFar)
        return maxProfit
