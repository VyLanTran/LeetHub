class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        '''
        -9, -1, -7
        -8, 9, -2
        -3, -4, -6

        n = 3
        i = 6 -> (2, 0)
        i = num - 1
        i // n = row
        i % n = col

        (1, 1) -> 1 * n + 1 = 4 -> real number is 4 + 1 = 5
        '''

        res = [0, 0]
        n = len(grid)

        for i in range(n):
            for j in range(n):
                index = abs(grid[i][j]) - 1
                row, col = index // n, index % n
                if grid[row][col] < 0:
                    res[0] = index + 1
                grid[row][col] = -abs(grid[row][col])

        for i in range(n):
            for j in range(n):
                if grid[i][j] > 0:
                    res[1] = i * n + j + 1
                    return res


        return res