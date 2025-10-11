class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        '''
        n = numRows
        the length of the n-th row is n

        Time: O(1 + 2 + 3 + .... + (n-1)) = O(n^2)
        Space: O(1)
        '''

        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]

        res = [[1], [1, 1]]

        for i in range(numRows - 2):
            prev_row = res[-1]
            cur_row = [1]
            for j in range(len(prev_row) - 1):
                cur_row.append(prev_row[j] + prev_row[j + 1])
            cur_row.append(1)
            res.append(cur_row)

        return res