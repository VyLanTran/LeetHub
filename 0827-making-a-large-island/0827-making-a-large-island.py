class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        '''
        1 1 x x
        1 1 x x
        1 0 1 1
        x x 1 1
        '''
        rows, cols = len(grid), len(grid[0])
        island_area = defaultdict(int)
        key = 2
        max_area = 0
        dirs = [(0, -1), (0, 1), (1, 0), (-1, 0)]

        def dfs(i, j, key):
            if not (0 <= i < rows and 0 <= j < cols and grid[i][j] == 1):
                return
            grid[i][j] = key
            island_area[key] += 1
            dfs(i - 1, j, key)
            dfs(i + 1, j, key)
            dfs(i, j - 1, key)
            dfs(i, j + 1, key)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    dfs(i, j, key)
                    key += 1

        if len(island_area) == 0:
            return 1

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    unique_islands = set()
                    for di, dj in dirs:
                        new_i, new_j = i + di, j + dj
                        if 0 <= new_i < rows and 0 <= new_j < cols and grid[new_i][new_j] != 0:
                            unique_islands.add(grid[new_i][new_j])
                           
                    max_area = max(max_area, 1 + sum(island_area[key] for key in unique_islands))
    
    
        return rows * cols if max_area == 0 else max_area
