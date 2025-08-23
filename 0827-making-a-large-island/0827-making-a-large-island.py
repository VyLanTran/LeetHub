class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        '''
        1 1 1 0 0
        1 1 0 1 1
        0 0 1 0 1
        '''

        island_area = defaultdict(int)
        rows, cols = len(grid), len(grid[0])
        hash_value = 2
        max_area = 0

        direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        def dfs(i, j, hash_value):
            if not (0 <= i < rows and 0 <= j < cols) or grid[i][j] != 1:
                return
            nonlocal area
            area += 1
            grid[i][j] = hash_value
            dfs(i - 1, j, hash_value)
            dfs(i + 1, j, hash_value)
            dfs(i, j - 1, hash_value)
            dfs(i, j + 1, hash_value)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    area = 0
                    dfs(i, j, hash_value)
                    island_area[hash_value] = area
                    hash_value += 1
                    max_area = max(max_area, area)
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    visited_islands = set()
                    cur_area = 1
                    for di, dj in direction:
                        new_i = i + di
                        new_j = j + dj
                        if 0 <= new_i < rows and 0 <= new_j < cols and grid[new_i][new_j] not in visited_islands:
                            hash_value = grid[new_i][new_j]
                            visited_islands.add(hash_value)
                            cur_area += island_area[hash_value]
                    max_area = max(max_area, cur_area)

        return max_area
        


