class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
        [1, 2, 5]
        amount = 11
        
        amounts = 
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        [0, 1, 1, 2, 3, 1, _, 2, 3, _ , _ , _]
        '''
        if amount == 0:
            return 0
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(len(dp)):
            for coin in coins:
                if i + coin < amount + 1:
                    dp[i + coin] = min(dp[i + coin], 1 + dp[i])

        return dp[-1] if dp[-1] != float('inf') else -1