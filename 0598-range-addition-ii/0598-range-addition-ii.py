class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        for row, col in ops:
            m = min(m, row)
            n = min(n, col)
        return m*n