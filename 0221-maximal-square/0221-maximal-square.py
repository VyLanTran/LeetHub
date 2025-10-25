class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        '''
        dp = matrix[0]
        max_side = max(dp)
        for i from 1 to rows - 1:
            prev = matrix[i][0]
            for j from 1 to cols - 1:
                count = 0
                if val == 1:
                    count = 1 + min(prev, dp[j - 1], dp[j])
                dp[j - 1] = prev
                prev = count
        keep track of max(dp[i][j])
        return max_side ** 2
        '''

        rows, cols = len(matrix), len(matrix[0])
        matrix = [[int(matrix[i][j]) for j in range(cols)] for i in range(rows)]
        dp = matrix[0]
        max_side = max(dp)

        for i in range(1, rows):
            prev = matrix[i][0]
            for j in range(1, cols):
                count = 0
                if matrix[i][j] == 1:
                    count = 1 + min(prev, dp[j - 1], dp[j])
                dp[j - 1] = prev
                prev = count
            dp[-1] = prev
            max_side = max(max_side, max(dp))

        return max_side ** 2
    