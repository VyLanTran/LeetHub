class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        i: 0 -> n (n + 1)
        can_buy: 2 options

        Time: O(2n) = O(n)
        Space: O(n)
        '''

        n = len(prices)
        dp = {}

        def f(i, can_buy):
            if i >= n:
                return 0
            if (i, can_buy) in dp:
                return dp[(i, can_buy)]
            # do nothing
            res = f(i + 1, can_buy)

            if can_buy:
                res = max(res, -prices[i] + f(i + 1, not can_buy))
            else:
                res = max(res, prices[i] + f(i + 2, not can_buy))
            dp[(i, can_buy)] = res
            return res

        return f(0, True)