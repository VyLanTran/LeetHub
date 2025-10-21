class Solution:
    def numSquares(self, n: int) -> int:
        '''
        f(n)
            if n is a perfect square:
                return 1
            try (sqrt(n))**2 to 1**2:
                1 + min(f(n - k**2))
        '''

        dp = {}

        def f(n):
            if int(sqrt(n)) ** 2 == n:
                return 1
            if n in dp:
                return dp[n]
            res = float('inf')
            for i in range(int(sqrt(n)), 0, -1):
                res = min(res, 1 + f(n - i**2))
            dp[n] = res
            return res

        return f(n)