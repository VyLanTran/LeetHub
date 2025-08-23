class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        '''
        2 1 1 
        0 1 1 
        1 0 1

        - first, go through the matrix to
            - count number of fresh oranges
            - add the coordinate of all rotten oranges into a queue
        - bfs until queue becomes empty
            - decrement number of fresh oranges
            - increment number of minutes after each iteration
        - return -1 if fresh ornages still exist, else num_minutes
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
                    if new_i >= 0 and new_i < rows and new_j >= 0 and new_j < cols and grid[new_i][new_j] == 1:
                        grid[new_i][new_j] = 2
                        fresh_count -= 1
                        queue.append((new_i, new_j))
            minutes += 1

        return minutes if fresh_count == 0 else -1

