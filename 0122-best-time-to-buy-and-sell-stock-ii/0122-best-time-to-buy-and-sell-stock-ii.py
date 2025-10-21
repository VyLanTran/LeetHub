class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        Time: O(n)
        Space: O(1)
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