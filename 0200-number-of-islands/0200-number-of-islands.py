class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_islands = 0
        rows, cols = len(grid), len(grid[0])

        def dfs(i, j):
            if not (0 <= i < rows and 0 <= j < cols) or grid[i][j] != "1":
                return
            # mark as visited
            grid[i][j] = "#"
            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    dfs(i, j)
                    num_islands += 1
        return num_islands