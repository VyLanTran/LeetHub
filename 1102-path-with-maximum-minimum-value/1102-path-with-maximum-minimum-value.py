class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        max_heap = [(-grid[0][0], 0, 0)]
        score = grid[0][0]
        grid[0][0] = -1
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while max_heap:
            neg_val, i, j = heappop(max_heap)
            score = min(score, -neg_val)
            if i == m - 1 and j == n -1 :
                return score
            for di, dj in dirs:
                new_i, new_j = i + di, j + dj
                if 0 <= new_i < m and 0 <= new_j < n and grid[new_i][new_j] != -1:
                    heappush(max_heap, (-grid[new_i][new_j], new_i, new_j))
                    grid[new_i][new_j] = -1
        
        return score

