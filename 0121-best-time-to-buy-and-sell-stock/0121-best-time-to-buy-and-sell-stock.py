class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        3, 5, 1, 2, 6

        min = inf, 3, 1
        max profit = 0, 2
        '''

        min_price = float('inf')
        max_profit = 0

        for price in prices:
            max_profit = max(max_profit, price - min_price)
            min_price = min(min_price, price)
        return max_profit