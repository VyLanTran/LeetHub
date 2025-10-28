class Solution:
    def generate(self, numRows: int) -> List[List[int]]:


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

