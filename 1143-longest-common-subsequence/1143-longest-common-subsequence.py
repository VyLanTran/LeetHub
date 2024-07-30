class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        '''
        01234
        abcde
        012
        ace
        
        f(i, j)
        = 1 + f(i + 1, j + 1) if same
        = max(f(i + 1, j), f(i, j + 1)) if not
        = 0 if i or j out of bound
        
        
        _ a b c d e
    _   0 0 0 0 0 0   
    a   0 1 1 1 1 1
    c   0 1 1 2 2 2
    e   0 1 1 2 2 3
        
        '''
        
        m, n = len(text1), len(text2)
        dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                c1, c2 = text1[j - 1], text2[i - 1]
                if c1 == c2:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[n][m]
                