class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        '''
        Time: O(mn)
        Space: O(n)
        '''

        rows, cols = len(matrix), len(matrix[0])
        next_dp = matrix[-1]
        res = sum(next_dp)

        for i in range(rows - 2, -1, -1):
            cur_dp = [0] * (cols)
            cur_dp[-1] = matrix[i][-1]
            for j in range(cols - 2, -1, -1):
                if matrix[i][j] == 1:
                    cur_dp[j] = 1 + min(cur_dp[j + 1], next_dp[j], next_dp[j + 1])
            res += sum(cur_dp)
            next_dp = cur_dp
        
        return res

