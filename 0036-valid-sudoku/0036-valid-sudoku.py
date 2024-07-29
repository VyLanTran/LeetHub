class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9
        rows = [set() for _ in range(n)]
        cols = [set() for _ in range(n)]
        squares = [set() for _ in range(n)]
        
        for i in range(n):
            for j in range(n):
                k = (i // 3) * 3 + (j // 3)
                val = board[i][j]
                if val == ".":
                    continue
                if val in rows[i] or val in cols[j] or val in squares[k]:
                    return False
                rows[i].add(val)
                cols[j].add(val)
                squares[k].add(val)
                
        return True