class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        minRow, minCol = m, n
        for row, col in ops:
            minRow = min(minRow, row)
            minCol = min(minCol, col)
        return minRow*minCol