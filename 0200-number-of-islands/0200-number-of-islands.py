class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def rec(i, j, grid):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != "1":
                return 
            grid[i][j] = "0"
            rec(i - 1, j, grid)
            rec(i + 1, j, grid)
            rec(i, j - 1, grid)
            rec(i, j + 1, grid)
            
        res = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    rec(i, j, grid)
                    res += 1
                    
        return res