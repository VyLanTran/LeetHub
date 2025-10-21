class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        '''
        01234
        abcde

        012
        ace

        f(i, j) = answer for text1[0, i], text2[0, j]
            if i < 0 or j < 0:
                return 0
            if char1 == char2:
                return 1 + f(i - 1, j - 1)
            return max(f(i - 1, j), f(i, j - 1))

        i: 0 to m - 1 => m
        j: 0 to n - 1 => n
        i = 0 but actual index is i - 1
        '''

        m, n = len(text1), len(text2)
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                char1, char2 = text1[i - 1], text2[j - 1]
                if char1 == char2:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]