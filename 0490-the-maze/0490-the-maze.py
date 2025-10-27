class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        rows, cols = len(maze), len(maze[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        start_i, start_j = start
        queue = deque([(start_i, start_j)])
        visited = set([(start_i, start_j)])

        while len(queue) > 0:
            i, j = queue.popleft()
            if i == destination[0] and j == destination[1]:
                return True
            for di, dj in directions:
                # roll in that direction as far as we can
                cur_i, cur_j = i, j
                while (0 <= cur_i < rows) and (0 <= cur_j < cols) and maze[cur_i][cur_j] == 0:
                    cur_i += di
                    cur_j += dj
                cur_i -= di
                cur_j -= dj
                if (cur_i, cur_j) not in visited:
                    visited.add((cur_i, cur_j))
                    queue.append((cur_i, cur_j))
        return False