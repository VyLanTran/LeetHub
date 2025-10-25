class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        1, 2, 3, 0, 2
        +, _, -, _, 

        0, 1, 2
        1, 2, 3
        
        dp[i] = res for prices[0-i]
        sell[i] = max profit if sell on day i

        dp: 
            to maximize profit, we never want to buy on last day (i)
            either sell or cool down (do nothing)

        4, 2, 1 = -> 0
        2, 4, 3 => 1


        0, 1, 2, 3, 4
        1, 2, 3, 0, 2
        sell[i]     = [0, _, _, _, _]
        cooldown[i] = [0, _, _, _, _]

        both starts with 0

        f(i, buy, prev_sell)
            if i >= n:
                return 0
            # can only buy if have no stock in
            if buy is None or (prev_sell is not None and buy < prev_sell and prev_sell + 1 < i):
                res1 =  -price + f(i + 1, i, prev_sell)
            # can only sell if having some stock in hand
            # if buy is not None and (prev_sell is None or prev_sell < buy):
            else:
                res1 = price - price[prev_sell] + f()
            

        f(i = 0, buy = None, prev_sell = None)
            # buy
            f(i = 1, buy = 0, prev_sell = None)
            
            # can't sell cuz buy = None

            # do nothing
            f(i = 1, buy, prev_sell)

        ---
        0, 1, 2, 3, 4
        1, 2, 3, 0, 2
        
        if can_sell = True then can only sell or do nothing (can't buy)
        if can_buy = True then can only buy or do nothing (can't sell cuz no stock in hand)

        f(i = 0, prof = 0, can_buy = T)
            # buy
            f(i = 1, prof = -1, False)
                # sell
                f(i = 3, prof = 1, T)
                    # buy
                    f(i = 4, prof = 1, F)
                        # sell
                        f(i = 6, prof = 3, T) = 0 (since out of bound)
                    # nothing
                    f(i = 4, prof = 1, T)
                # nothing
                f(i = 2, prof = -1, F)
            # nothing
            f(i = 1, prof = 0, T)

        f(i, can_buy = T)
            # buy
            res = -1 + f(1, F)
                # sell
                res = 2 + f(3, T)
                    # buy
                    res = 0 + f(4, F) = 2
                        # sell
                        res = 2 + f(6, T) = 2
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