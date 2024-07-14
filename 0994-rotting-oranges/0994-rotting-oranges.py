class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        totalOrange = 0
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        res = -1
        
        for i in range(rows):
            for j in range(cols):
                val = grid[i][j]
                if val == 2:
                    totalOrange += 1
                    queue.append((i, j))
                elif val == 1:
                    totalOrange += 1
                    
        # print(totalOrange)
        # print(queue)
        
        if totalOrange == 0:
            return 0
                    
        while queue:
            size = len(queue)
            res += 1
            
            for k in range(size):
                pos = queue.popleft()
                totalOrange -= 1
                i, j = pos[0], pos[1]

                if i - 1 >= 0 and grid[i - 1][j] == 1:
                    grid[i - 1][j] = 2
                    queue.append((i - 1, j))
                if i + 1 < rows and grid[i + 1][j] == 1:
                    grid[i + 1][j] = 2
                    queue.append((i + 1, j)) 
                if j - 1 >= 0 and grid[i][j - 1] == 1:
                    grid[i][j - 1] = 2
                    queue.append((i, j - 1) )
                if j + 1 < cols and grid[i][j + 1] == 1:
                    grid[i][j + 1] = 2
                    queue.append((i, j + 1) )
        
        
        return res if totalOrange == 0 else -1
        