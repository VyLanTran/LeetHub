class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        directions = [[-2, -1], [-1, -2], [1, -2], [2, -1], [-2, 1], [-1, 2], [1, 2], [2, 1]]
        queue = deque([(0, 0, 0)])
        visited = set([(0, 0)])

        while True:
            i, j, steps = queue.popleft()
            if i == x and j == y:
                return steps
            for di, dj in directions:
                new_i = i + di
                new_j = j + dj
                if (new_i, new_j) not in visited:
                    visited.add((new_i, new_j))
                    queue.append((new_i, new_j, steps + 1))
        return 0
