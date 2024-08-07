class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        rows, cols = len(land), len(land[0])
        res = []
        
        def dfs(i, j):
            nonlocal bottomRight
            
            if i < 0 or j < 0 or i >= rows or j >= cols or land[i][j] != 1:
                return
            land[i][j] = -1
            if i >= bottomRight[0] and j >= bottomRight[1]:
                bottomRight = (i, j)
            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)
            
        
        for i in range(rows):
            for j in range(cols):
                if land[i][j] != 1:
                    continue
                bottomRight = (i, j)
                dfs(i, j)
                res.append([i, j, bottomRight[0], bottomRight[1]])
        return res
                