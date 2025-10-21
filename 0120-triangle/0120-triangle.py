class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        '''
        f(i) = result for triangle[0, i]
            if i == 0:
                return triangle[0][0]
            if on row i, we take number at index j, then the previous cell leading
            to this cell is either [i-1][j] or [i-1][j-1] if j-1 >= 0
            dp[i][0] = triangle[i][0] + dp[i-1][0]
            for j in range(1, end of cur row):
                dp[i][j] = min(dp[i][j], cur_row[j] + dp[i-1][j], cur_row[j] + dp[i-1][j-1])

        prev = [top value]

        for i in range(1, last_row + 1):
            cur_row
            cur = [cur_row[0] + prev[0]]
            for j in range(1, end of cur_row):
                cur.append(cur_row[j] + min(prev[j - 1], prev[j]))
            prev = cur_row
        '''

        num_rows = len(triangle)
        # if num_rows == 1:
        #     return triangle[0][0]

        prev = [triangle[0][0]]

        for i in range(1, num_rows):
            cur_row = triangle[i]
            cur = [cur_row[0] + prev[0]]
            for j in range(1, len(cur_row) - 1):
                cur.append(cur_row[j] + min(prev[j - 1], prev[j]))
            # the right most cell is only reachable from prev[j-1]
            cur.append(cur_row[-1] + prev[-1])
            prev = cur

        return min(prev)