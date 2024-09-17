class Solution:
    
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        numRows, numCols = len(grid), len(grid[0])
        dp = [[[0, 0, 0, 0] for _ in range(numCols)] for _ in range(numRows)]
        
        def findCurrEnemies(neighborVal, neighborEnemies):
            return 0 if neighborVal == 'W' else (1 + neighborEnemies if neighborVal == 'E' else neighborEnemies)
        
        for i in range(numRows):
            for j in range(numCols):
                val = grid[i][j]
                if val == 'W':
                    continue
                if j - 1 >= 0:
                    dp[i][j][0] = findCurrEnemies(grid[i][j - 1], dp[i][j - 1][0]) 
                if i - 1 >= 0:
                    dp[i][j][2]  = findCurrEnemies(grid[i - 1][j], dp[i - 1][j][2]) 
        for i in range(numRows - 1, -1, -1):
            for j in range(numCols - 1, -1, -1):
                val = grid[i][j]
                if val == 'W':
                    continue
                if j + 1 < numCols:
                    dp[i][j][1] = findCurrEnemies(grid[i][j + 1], dp[i][j + 1][1])
                if i + 1 < numRows:
                    dp[i][j][3]  = findCurrEnemies(grid[i + 1][j], dp[i + 1][j][3])
                    
        # print(dp)
                    
        maxEnemies = 0
        for i in range(numRows):
            for j in range(numCols):
                if grid[i][j] == '0':
                    left, right, top, bottom = dp[i][j]
                    maxEnemies = max(maxEnemies, left + right + top + bottom)
            
        return maxEnemies
                
                
    
'''
["W","W","W","W","E"],
["W","E","E","E","E"],
["W","E","0","E","0"],
["W","E","E","E","E"],
["W","W","W","W","W"]
'''
                    
        