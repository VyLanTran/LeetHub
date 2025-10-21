class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        '''
        f(i, j) = res if right corner is at (i, j)
            if i == 0 and j == 0:
                return 1
            if i < 0 or j < 0: 
                return 0
            # reach from top cell (if applicable)
            f(i - 1, j)
            # reach from left cell 
            f(i, j - 1)
            return sum of the 2 results above

        dp[0][_] = 1
        dp[_][0] = 1
        only need 2 rows: prev, cur

        1 1 1 1 1 1 1
        1 2 3 4 5 6 7
        1 3 6  _ _ _
                0 1 2 3 4 5 6
        prev = [1 3 6 4 5 6 7]
        cur. = [1 1 1 1 1 1 1]

        i = 1
        '''

        prev = [1] * n

        for i in range(1, m):
            for j in range(1, n):
                prev[j] += prev[j - 1]
        return prev[-1]

