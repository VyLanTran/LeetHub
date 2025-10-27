class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        rows, cols = len(maze), len(maze[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        def is_in_bound(i, j):
            return (0 <= i < rows) and (0 <= j < cols)

        def roll(i, j, di, dj):
            while True:
                new_i, new_j = i + di, j + dj
                if is_in_bound(new_i, new_j):
                    if maze[new_i][new_j] == 1:
                        return i, j
                    i, j = new_i, new_j
                else:
                    return i, j

        visited = set()
        visited.add((start[0], start[1]))
        queue = deque([(start[0], start[1])])

        while len(queue) > 0:
            i, j = queue.popleft()
            # print(f'cur: {i, j}')
            if i == destination[0] and j == destination[1]:
                return True
            for di, dj in directions:
                new_i, new_j = roll(i, j, di, dj)
                if (new_i, new_j) not in visited:
                    # print(f'new end: {new_i, new_j, di, dj}')
                    visited.add((new_i, new_j))
                    queue.append((new_i, new_j))
        return False

        '''
           0,1,2,3,4
        0 [0,e,0,0,0],
        1 [1,1,0,0,1],
        2 [0,0,0,0,0],
        3 [0,1,0,0,1],
        4 [0,1,0,s,0]
        '''


            
            

