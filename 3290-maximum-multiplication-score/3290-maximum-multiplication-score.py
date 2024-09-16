class Solution:
    def maxScore(self, a: List[int], b: List[int]) -> int:
        m, n = len(a), len(b)
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        
        for i in range(m, -1, -1):
            for j in range(n, -1, -1):
                if i == m:
                    dp[i][j] = 0
                    continue
                if j == n:
                    dp[i][j] = float('-inf')
                    continue
                dp[i][j] = max(dp[i][j + 1], a[i]*b[j] + dp[i + 1][j + 1])
        return dp[0][0]