class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        0,1,2,3,4,5
        7,1,5,3,6,4
        l r
        r r r 
        res = 0
        + (7-7) + (5-1)
        '''

        res = 0
        n = len(prices)
        l, r = 0, 0

        while r < n:
            while r + 1 < n and prices[r + 1] >= prices[r]:
                r += 1
            res += prices[r] - prices[l]
            l, r = r + 1, r + 1
        return res