class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        '''
        1 0 0
        1 1 0
        1 1 0

        if start or end is not 0:
            return -1
        
        BFS
        '''

        if grid[0][0] != 0 or grid[-1][-1] != 0:
            return -1
        n = len(grid)
        queue = deque([(0, 0)])
        steps = 1
        grid[0][0] = -1

        while len(queue) > 0:
            size = len(queue)
            for _ in range(size):
                i, j = queue.popleft()
                if i == n - 1 and j == n - 1:
                    return steps
                for di in range(-1, 2):
                    for dj in range(-1, 2):
                        if di == 0 and dj == 0:
                            continue
                        new_i, new_j = i + di, j + dj
                        if (0 <= new_i < n) and (0 <= new_j < n) and grid[new_i][new_j] == 0:
                            grid[new_i][new_j] = -1
                            queue.append((new_i, new_j))

            steps += 1

        return -1


            