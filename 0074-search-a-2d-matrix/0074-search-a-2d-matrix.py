class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        left, right = 0, rows * cols - 1
        while left <= right:
            mid = left + (right - left) // 2
            pos = self.findRowCol(cols, mid)
            val = matrix[pos[0]][pos[1]]
            if val == target:
                return True
            elif val < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
    
    def findRowCol(self, cols, index):
        return (index // cols, index % cols)