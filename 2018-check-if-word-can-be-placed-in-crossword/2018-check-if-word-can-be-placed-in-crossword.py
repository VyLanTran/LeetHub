class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        
        def isInBound(i, j):
            return i >= 0 and j >= 0 and i < rows and j < cols
        
        def dfs(i, j, k, dirI, dirJ):
            # if i == 0 and j == 1:
            #     print("here")
            # print(i, j, k, dirI, dirJ, startI, startJ)
            if k == len(word):
                # prevI, prevJ = startI - dirI, startJ - dirJ
                if not isInBound(i, j) or board[i][j] == "#":
                    # print("terminate:", startI, startJ, dirI, dirJ)
                    return True
                return False
            
            if not isInBound(i, j):
                return False
            val = board[i][j]
            if val != " " and val != word[k]:
                return False
            return dfs(i + dirI, j + dirJ, k + 1, dirI, dirJ)
        
        for i in range(rows):
            for j in range(cols):
                if (i - 1 < 0 or board[i - 1][j] == "#") and dfs(i, j, 0, 1, 0):
                    return True
                if (j - 1 < 0 or board[i][j - 1] == "#") and dfs(i, j, 0, 0, 1):
                    return True
                if (i + 1 >= rows or board[i + 1][j] == "#") and dfs(i, j, 0, -1, 0):
                    return True
                if (j + 1 >= cols or board[i][j + 1] == "#") and dfs(i, j, 0, 0, -1):
                    return True
               
                    
        return False