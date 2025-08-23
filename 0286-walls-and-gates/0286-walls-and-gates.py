class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        INF = 2147483647
        rows, cols = len(rooms), len(rooms[0])
        queue = deque([])
        direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        for i in range(rows):
            for j in range(cols):
                if rooms[i][j] == 0:
                    queue.append((i, j, 0))

        while queue:
            i, j, dist = queue.popleft()
            for di, dj in direction:
                new_i = i + di
                new_j = j + dj
                if new_i >= 0 and new_i < rows and new_j >= 0 and new_j < cols and rooms[new_i][new_j] == INF:
                    rooms[new_i][new_j] = dist + 1
                    queue.append((new_i, new_j, dist + 1))

        