class Solution:
    def divisorGame(self, n: int) -> bool:
        '''
        1 => False
        2 => True
        3 => False
        f(n) = can Alice win
        f(n)
            for x that is a valid divisor:
                if not f(n - x):
                    return True
        {
            1: F
            2: T
        }
        '''
        
        dp = [False] * (n + 1)
        if n <= 1:
            return dp[n]
        for i in range(2, n + 1):
            for j in range(1, i):
                if i % j == 0 and not dp[i - j]:
                    dp[i] = True
                    break
        return dp[-1]
