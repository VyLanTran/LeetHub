class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        '''
        if numRows <= 2:
            special case
        
        res = [[1], [1, 1]]
        for i from 2 to numRows: (i elements: 0, 1, ..., i - 1)
            cur_row = [1]
            for j from 1 to i - 2:
                val = prev_row[j - 1] + prev_row[j]
            cur_row.append(1)

        dp as prev

        '''

        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        prev = [1, 1]
        res = [[1], [1, 1]]

        for i in range(2, numRows):
            cur = [1]
            for j in range(1, i):
                cur.append(prev[j- 1] + prev[j]) 
            cur.append(1)
            res.append(cur)
            prev = cur
        return res

