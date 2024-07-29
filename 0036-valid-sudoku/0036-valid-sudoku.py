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
                # print(val)
                # if val == "8":
                #     print(val, rows[i], cols[j], squares[k])
                #     continue
                if val == ".":
                    # print(i, j)
                    continue
                if val in rows[i] or val in cols[j] or val in squares[k]:
                    return False
                rows[i].add(val)
                cols[j].add(val)
                squares[k].add(val)
                # print("here")
                
        return True
    
    '''
["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]
    '''