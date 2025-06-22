class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        m = 3
        n = 4
        i = 0, ..., 11

        0 to 3: row = i // n = 0
        0, 4, 8: col = 0
        1, 5, 9: col = 1 (i % n)
        '''

        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, rows * cols - 1

        while left <= right:
            mid = left + (right - left) // 2
            val = matrix[mid // cols][mid % cols]
            if val == target:
                return True
            elif val < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False