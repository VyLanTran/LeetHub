class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols, n = len(board), len(board[0]), len(word)
        
        def rec(i, j, k):
            if k >= n:
                return True
            if i < 0 or i >= rows or j < 0 or j >= cols or board[i][j] != word[k]:
                return False
            board[i][j] = "*"
            res = rec(i - 1, j, k + 1) or rec(i + 1, j, k + 1) or rec(i, j - 1, k + 1) or rec(i, j + 1, k + 1)
            board[i][j] = word[k]
            return res
        
        for i in range(rows):
            for j in range(cols):
                if rec(i, j, 0):
                    return True
        return False
            
            