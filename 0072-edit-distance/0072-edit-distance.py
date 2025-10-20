class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        '''
        f(i, j) = res for word1[0, i] and word2[0, j]
            if i < 0:
                if j < 0:
                    return 0
                return j + 1
            if j < 0:
                return i + 1
            char1, char2
            if char1 == char2:
                return f(i-1, j-1)
            # replace char1 with char2
            1 + f(i-1, j-1)
            # insert char2 into word1
            1 + f(i, j-1)
            # delete char1
            1 + f(i-1, j)
            dp[i, j] = min of three result above

        -1, m-1 = 0 to m => size m + 1
        dp: matrix size (m+1) x (n+1)
        dp[i][j] = res for word1[0, i-1] and word2[0, j-1]
        dp[0][j] = (checking index j-1) = j
        dp[i][0] = i
        '''

        m, n = len(word1), len(word2)
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for j in range(n + 1):
            dp[0][j] = j
        for i in range(m + 1):
            dp[i][0] = i

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                char1, char2 = word1[i - 1], word2[j - 1]
                if char1 == char2:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j])
        
        return dp[-1][-1]