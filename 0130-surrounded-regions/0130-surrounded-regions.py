class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        rows, cols = len(board), len(board[0])
        
        def dfs(i, j):
            if i < 0 or j < 0 or i >= rows or j >= cols or board[i][j] != "O": 
                return 
            board[i][j] = "*"
            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)
        
        for i in range(rows):
            for j in range(cols):
                if (i == 0 or j == 0 or i == rows - 1 or j == cols - 1) and board[i][j] == "O":
                    dfs(i, j)
        
        for i in range(rows):
            for j in range(cols):
                board[i][j] = "O" if board[i][j] == "*" else "X"
                
        
        
            