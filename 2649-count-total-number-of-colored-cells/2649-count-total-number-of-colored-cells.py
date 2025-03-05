class Solution:
    def coloredCells(self, n: int) -> int:
        '''
        n = 1 => 1
        n = 2 => 5
        n = 3 => 13

          i
         ixi
        ixxxi
        xxxxx
         xxx
          x

        each of the cell on the edge can extend one more to the left/right
        each level has 2 cells on the edge (except the top and bottom row)
        the top and bottom level can extends 3 more cells
        n = 1 is a special case, return 1

        n = 2, return 5
        n = 3
            top -> 3
            bottom -> 3
            1 normal row -> 2
            5 + 8 = 13

        n = 4
            3 normal rows
            13 + (3 + 3 + 3 * 2) = 25

        '''

        if n == 1:
            return 1
        if n == 2:
            return 5

        res = 5
        normalRows = 1

        for _ in range(2, n):
            res += 6 + normalRows * 2
            normalRows += 2

        return res 