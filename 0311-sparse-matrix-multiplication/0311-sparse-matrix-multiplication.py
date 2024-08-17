class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        m, k, n = len(mat1), len(mat1[0]), len(mat2[0])
        res = [[0 for _ in range(n)] for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                sum = 0
                for x in range(k):
                    sum += mat1[i][x] * mat2[x][j]
                res[i][j] = sum
        return res
        