from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        dirs = [[-1,0],[1,0],[0,-1],[0,1]]
        
        def isValid(i, j):
            return i >= 0 and i < rows and j >= 0 and j < cols
        
        def initiateState():
            rotten_oranges = deque()
            fresh_oranges = 0
            for i in range(rows):
                for j in range(cols):
                    val = grid[i][j]
                    if val == 0:
                        continue
                    elif val == 2:
                        rotten_oranges.append((i, j)) 
                    else:
                        fresh_oranges += 1
            return fresh_oranges, rotten_oranges
        
        fresh_oranges, rotten_oranges = initiateState()
        if fresh_oranges == 0:
            return 0
        time = -1
        while rotten_oranges:
            time += 1
            size = len(rotten_oranges)
            for _ in range(size):
                i, j = rotten_oranges.popleft()
                for di, dj in dirs:
                    newI = i + di
                    newJ = j + dj
                    if isValid(newI, newJ) and grid[newI][newJ] == 1:
                        fresh_oranges -= 1
                        rotten_oranges.append((newI, newJ))
                        grid[newI][newJ] = 2
        return time if fresh_oranges == 0 else -1
    
    '''
    2 1 1
    0 1 1
    1 0 1
    '''