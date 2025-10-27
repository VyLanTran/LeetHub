class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        7, 3, 6, 1, 5, 4
        
        res = 0, (6-3), (5-1)
        min = inf, 7, 3, 1

        7, 1, 5, 3, 6, 4

        res = 0, (5-1), (6-1)
        min = inf, 7, 1, 
        '''

        res = 0
        min_price = float('inf')

        for price in prices:
            if price > min_price:
                res = max(res, price - min_price)
            else:
                min_price = min(min_price, price)
        
        return res