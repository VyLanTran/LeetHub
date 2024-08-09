class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        def isMagic(top, left):
            vals = set()
            if top + 2 >= rows or left + 2 >= cols:
                return False
            sum = grid[top][left] + grid[top][left + 1] + grid[top][left + 2]
            rowSum = dict()
            colSum = dict()
            diag1, diag2 = 0, 0
            for i in range(top, top + 3):
                for j in range(left, left + 3):
                    val = grid[i][j]
                    if val == 0 or val > 9 or val in vals:
                        return False
                    vals.add(val)
                    rowSum[i] = rowSum.get(i, 0) + val
                    colSum[j] = colSum.get(j, 0) + val
                    if i - j == top - left:
                        diag1 += val
                    if i + j == top + left + 2:
                        diag2 += val
                    if j == left + 2 and rowSum[i] != sum:
                        return False
                    if i == top + 2 and colSum[j] != sum:
                        return False
                    if i == top + 2 and j == left and diag2 != sum:
                        return False
                    if i == top + 2 and j == left + 2 and diag1 != sum:
                        return False
            return True
        
        res = 0
        for i in range(rows):
            for j in range(cols):
                if isMagic(i, j):
                    res += 1
        return res
            