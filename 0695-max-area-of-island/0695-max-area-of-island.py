class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        cur_area = 0
        max_area= 0
        
        def dfs(i, j):
            nonlocal cur_area
            if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] != 1:
                return
            cur_area += 1
            grid[i][j] = 0
            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)
            
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    cur_area = 0
                    dfs(i, j)
                    max_area= max(max_area, cur_area)
                    
        return max_area