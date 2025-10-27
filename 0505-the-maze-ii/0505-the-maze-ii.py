class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        '''
        Time: O(m * n * max(m, n))
        Space: O(m * n)
        '''
        rows, cols = len(maze), len(maze[0])
        start_i, start_j = start
        dest_i, dest_j = destination
        queue = deque([(start_i, start_j, 0)])
        visited_dist = {
            (start_i, start_j): 0
        }
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        res = float('inf')

        while len(queue) > 0:
            i, j, dist = queue.popleft()
            if i == dest_i and j == dest_j:
                res = min(res, dist)
            else:
                for di, dj in directions:
                    cur_i, cur_j = i, j
                    while (0 <= cur_i < rows) and (0 <= cur_j < cols) and maze[cur_i][cur_j] == 0:
                        cur_i += di
                        cur_j += dj
                    cur_i -= di
                    cur_j -= dj
                    cur_dist = abs(cur_i - i) + abs(cur_j - j) + dist
                    if (cur_i, cur_j) not in visited_dist or visited_dist[(cur_i, cur_j)] > cur_dist:
                        visited_dist[(cur_i, cur_j)] = cur_dist
                        queue.append((cur_i, cur_j, cur_dist))
        return -1 if res == float('inf') else res
