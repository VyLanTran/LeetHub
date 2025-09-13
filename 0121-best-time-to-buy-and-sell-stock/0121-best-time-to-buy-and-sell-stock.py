class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        Time: O(n)
        Space: O(1)
        '''

        min_price = float('inf')
        max_profit = 0

        for price in prices:
            max_profit = max(max_profit, price - min_price)
            min_price = min(min_price, price)

        return max_profit