class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
        4, 5

        8 = 4 + 4
        
        sort coin values first
        f(amount) = what is the fewest number of coins to make up this amount
            if amount < 0:
                return inf
            if amount == 0:
                return 0
            if amount in cache:
                return from cache

            min_count = inf
            for coin (from largest to smallest):
                num_coins = f(amount - value)
                min_count = min(min_count, 1 + num_coins)
            cache[amount] = min_count if min_count != inf


        f(11)
            f(6)
                f(1) = 1
                    f(-4) = inf
                    f(-1) = inf
                    f(0) = 0
        '''

        cache = {}
        coins.sort(reverse=True)

        def rec(amount):
            if amount < 0:
                return float('inf')
            if amount == 0:
                return 0
            if amount in cache:
                return cache[amount]
            res = float('inf')
            for coin in coins:
                res = min(res, 1 + rec(amount - coin))
            cache[amount] = res
            return res

        res = rec(amount)
        return res if res != float('inf') else -1