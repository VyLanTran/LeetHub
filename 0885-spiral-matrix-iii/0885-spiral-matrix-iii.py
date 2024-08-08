class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        left, right, top, bottom = cStart, cStart + 1, rStart, rStart + 1
        res = []
        while left >= 0 or right < cols or top >= 0 or bottom < rows:
            if top >= 0:
                for j in range(max(left, 0), min(right, cols)):
                    res.append([top, j])
            left -= 1
            if right < cols:
                for i in range(max(top, 0), min(bottom, rows)):
                    res.append([i, right])
            top -= 1
            if bottom < rows:
                for j in range(min(right, cols - 1), max(left, -1), -1):
                    res.append([bottom, j])
            right += 1
            if left >= 0:
                for i in range(min(bottom, rows - 1), max(top, -1), -1):
                    res.append([i, left])
            bottom += 1
        return res