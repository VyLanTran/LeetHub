class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        '''
        0 1
        3 1 1
        2 1 2
        1 1 3
        
        '''
        
        dp = [[None] * n for _ in range(m)]
        for i in range(m):
            dp[i][-1] = 1
        for j in range(n):
            dp[m - 1][j] = 1
            
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if not dp[i][j]:
                    dp[i][j] = dp[i][j + 1] + dp[i + 1][j]
        
        return dp[0][0]