class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        '''
        Time: O(mn)
        Space: O(mn)
        '''

        minutes = -1
        fresh_count = 0
        queue = deque()
        rows, cols = len(grid), len(grid[0])
        direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh_count += 1
                elif grid[i][j] == 2:
                    queue.append((i, j))
                else:
                    pass

        if fresh_count == 0:
            return 0

        while queue:
            size = len(queue)
            for _ in range(size):
                i, j = queue.popleft()
                for di, dj in direction:
                    new_i = i + di
                    new_j = j + dj
                    if 0 <= new_i < rows and 0 <= new_j < cols and grid[new_i][new_j] == 1:
                        grid[new_i][new_j] = 2
                        fresh_count -= 1
                        queue.append((new_i, new_j))
            minutes += 1

        return minutes if fresh_count == 0 else -1

